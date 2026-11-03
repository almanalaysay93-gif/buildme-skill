#!/usr/bin/env python3
"""Scoped Agent Desktop observe/act/verify adapter; no external model or API keys."""

import argparse
import json
import os
from pathlib import Path
import re
import shutil
import subprocess


class DesktopError(RuntimeError):
    def __init__(self, code, delivery="unknown", retry="unknown"):
        super().__init__(code)
        self.code, self.delivery, self.retry = code, delivery, retry


def command():
    receipt = Path.home() / ".agents/tools/agent-desktop/buildme-desktop.json"
    if receipt.is_file():
        try:
            data = json.loads(receipt.read_text())
            binary = Path(data["binary"])
            if data.get("status") == "installed" and binary.is_file():
                env = dict(os.environ)
                if data.get("helper"):
                    env["AGENT_DESKTOP_MACOS_HELPER_PATH"] = data["helper"]
                return [str(binary)], env
        except (ValueError, KeyError, TypeError, OSError):
            pass
    binary = shutil.which("agent-desktop")
    if binary and not binary.lower().endswith((".cmd", ".bat")):
        return [binary], dict(os.environ)
    raise DesktopError("NEED_SETUP")


def invoke(args):
    argv, env = command()
    try:
        result = subprocess.run([*argv, *args], capture_output=True, text=True, timeout=45, env=env)
    except subprocess.TimeoutExpired as error:
        raise DesktopError("TIMEOUT") from error
    except OSError as error:
        raise DesktopError("NEED_SETUP") from error
    try:
        payload = json.loads(result.stdout)
    except ValueError as error:
        raise DesktopError("INVALID_OUTPUT") from error
    if not isinstance(payload, dict):
        raise DesktopError("INVALID_OUTPUT")
    if result.returncode or payload.get("ok") is not True:
        failure = payload.get("error") or {}
        disposition = failure.get("disposition") or {}
        code = failure.get("code", "COMMAND_FAILED")
        raise DesktopError(code if re.fullmatch(r"[A-Z_]+", str(code)) else "COMMAND_FAILED",
                           disposition.get("delivery", "unknown"), disposition.get("retry", "unknown"))
    return payload


def save(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd = os.open(path, os.O_CREAT | os.O_TRUNC | os.O_WRONLY, 0o600)
    with os.fdopen(fd, "w", encoding="utf-8") as stream:
        if os.name != "nt":
            os.fchmod(stream.fileno(), 0o600)
        json.dump(data, stream, indent=2)
        stream.write("\n")


def nodes(node):
    if isinstance(node, dict):
        yield node
        for child in node.get("children", []):
            yield from nodes(child)


def complete(payload):
    data = payload.get("data") or {}
    if not isinstance(data, dict):
        return False
    return (payload.get("ok") is True and data.get("complete") is True
            and not data.get("truncated") and not data.get("identity_unproven")
            and isinstance(data.get("tree"), dict)
            and not any(x.get("subtree_truncated") for x in nodes(data["tree"])))


def snapshot(app, window_id=None):
    if not isinstance(app, str) or not app.strip() or app.startswith("-"):
        raise ValueError("Name the specific approved app")
    args = ["snapshot", f"--app={app}"]
    if window_id:
        args.append(f"--window-id={window_id}")
    return invoke(args)


def observe(app, window_id=None):
    payload = snapshot(app, window_id)
    return {"status": "OBSERVED" if complete(payload) else "BLOCKED", "observation": payload,
            "reason": "Complete scoped tree" if complete(payload) else "Incomplete/unproven tree; do not act or claim absent elements"}


def act(observation, action, ref, value=None):
    if not complete(observation):
        raise DesktopError("INCOMPLETE_OBSERVATION", "not_delivered", "safe")
    data = observation["data"]
    expected = "@" + str(data.get("snapshot_id", "")) + ":"
    if not re.fullmatch(r"@[A-Za-z0-9_-]+:e[0-9]+", ref) or not ref.startswith(expected):
        raise ValueError("Use a qualified ref from this complete snapshot")
    if not any(node.get("ref_id") == ref for node in nodes(data["tree"])):
        raise ValueError("Ref was not observed in this snapshot")
    allowed = {"click", "set-value", "type", "clear", "select", "check", "uncheck", "expand", "collapse", "scroll-to"}
    if action not in allowed:
        raise ValueError("Only scoped semantic ref actions are supported; no headed/physical fallback")
    needs_value = action in ("set-value", "type", "select")
    if needs_value != (value is not None) or value is not None and (not isinstance(value, str) or len(value) > 2000):
        raise ValueError("Supply bounded text only for text/selection actions")
    args = [action, ref]
    if value is not None:
        # Prevent data beginning with '-' from becoming a CLI flag.
        if value.startswith("-"):
            raise ValueError("Leading-dash values require direct CLI syntax review")
        args.append(value)
    result = invoke(args)  # Never automatically repeat or substitute a mutation.
    disposition = result.get("data", {}).get("disposition") or {}
    return {"status": "BLOCKED", "delivery": disposition.get("delivery", "unknown"),
            "retry": disposition.get("retry", "unknown"),
            "reason": "Action returned; fresh independent application-state verification is still required"}


def verify(app, window_id, checks):
    if not isinstance(checks, list) or not 1 <= len(checks) <= 20:
        raise ValueError("Provide 1–20 approved accessibility-state assertions")
    for check in checks:
        if (not isinstance(check, dict) or not check.get("role")
                or not set(check).issubset({"role", "name", "value", "states"}) or len(check) < 2):
            raise ValueError("Checks require role plus exact name/value/states; no scripts")
        if (not isinstance(check["role"], str) or any(not isinstance(check[k], str) or not check[k]
                for k in ("name", "value") if k in check)
                or "states" in check and (not isinstance(check["states"], list) or not check["states"]
                    or any(not isinstance(state, str) or not state for state in check["states"]))):
            raise ValueError("Assertions need concrete names/values or a nonempty state list")
    observation = snapshot(app, window_id)
    if not complete(observation):
        return {"assertion_status": "BLOCKED", "overall_qa_status": "BLOCKED", "checks": [],
                "reason": "Partial tree is not absence or completion evidence"}
    observed = list(nodes(observation["data"]["tree"]))
    results = []
    for index, check in enumerate(checks):
        matches = [node for node in observed if str(node.get("role", "")).lower() == str(check["role"]).lower()
                   and all(node.get(field) == check[field] for field in ("name", "value") if field in check)
                   and all(state in node.get("states", []) for state in check.get("states", []))]
        results.append({"check": index + 1, "passed": len(matches) == 1, "matches": len(matches)})
    return {"assertion_status": "PASS" if all(x["passed"] for x in results) else "FAIL",
            "overall_qa_status": "BLOCKED", "checks": results,
            "reason": "Accessibility-state assertions only; persistence and all required web/mobile/quality gates still apply"}


def doctor():
    result = {"status": "BLOCKED", "desktop_tested": False, "api_keys_required": False}
    try:
        version = invoke(["version"])
        result["version"] = version.get("data", {}).get("version")
        status = invoke(["status"])
        result["status"] = "STATUS_AVAILABLE" if status.get("ok") is True else "BLOCKED"
        result["reason"] = "Platform status available; this does not prove any app/task passed"
    except DesktopError as error:
        result["reason"] = error.code
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("operation", choices=("doctor", "observe", "act", "verify"))
    parser.add_argument("--app")
    parser.add_argument("--window-id")
    parser.add_argument("--observation", type=Path)
    parser.add_argument("--checks", type=Path)
    parser.add_argument("--action")
    parser.add_argument("--ref")
    parser.add_argument("--value")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        if args.operation == "doctor":
            result = doctor()
        elif args.operation == "observe":
            result = observe(args.app, args.window_id)
        elif args.operation == "act":
            if not args.observation or not args.action or not args.ref:
                parser.error("act requires --observation, --action and --ref")
            result = act(json.loads(args.observation.read_text())["observation"], args.action, args.ref, args.value)
        else:
            if not args.checks:
                parser.error("verify requires --checks")
            result = verify(args.app, args.window_id, json.loads(args.checks.read_text()))
    except DesktopError as error:
        result = {"status": "BLOCKED", "reason": error.code, "delivery": error.delivery, "retry": error.retry}
    except (ValueError, OSError, KeyError, TypeError):
        result = {"status": "BLOCKED", "reason": "INVALID_INPUT"}
    if args.output:
        save(args.output, result)
    # Raw accessibility trees may contain private content. Persist locally only.
    summary = {key: value for key, value in result.items() if key != "observation"}
    print(json.dumps(summary, indent=2))
    return 0 if result.get("status") in ("OBSERVED", "STATUS_AVAILABLE") or result.get("assertion_status") == "PASS" else 1 if result.get("assertion_status") == "FAIL" else 2


if __name__ == "__main__":
    raise SystemExit(main())
