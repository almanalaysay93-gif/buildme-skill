#!/usr/bin/env python3
"""Opt-in JEV journey worker. Default execution makes no browser or model calls."""

import argparse
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import re
import sys
import time
from urllib.parse import urlparse


REF = "8251e272398011cdef648965204d1c20cd838333"
SOURCE = f"https://github.com/browser-use/jev-ultrafast/archive/{REF}.zip"
LIMITATIONS = [
    "JEV uses TypeSafe; typing also uses the configured text-model API. Calls may be billed.",
    "Decision/action budgets are not dollar caps; upstream request retries can add API calls.",
    "Use only synthetic data and disposable test environments with a dedicated test Chrome profile.",
    "Origin checks detect navigation changes; they are not a network or side-effect sandbox.",
    "Frames, shadow DOM, canvas, uploads, pop-up tabs, nested scrolling and arbitrary keyboard widgets are outside this JEV MVP.",
    "JEV's desktop journey result does not replace free Playwright mobile/accessibility/performance/SEO gates.",
]


def origin(url):
    if not isinstance(url, str):
        raise ValueError("Test URLs must be strings")
    parsed = urlparse(url)
    try:
        port = parsed.port or (443 if parsed.scheme == "https" else 80)
    except ValueError as error:
        raise ValueError("Invalid test URL") from error
    if parsed.scheme not in ("http", "https") or not parsed.hostname or parsed.username or parsed.password:
        raise ValueError("Use an HTTP(S) test URL without embedded credentials")
    return parsed.scheme, parsed.hostname.lower(), port


def validate(scenario):
    if not isinstance(scenario, dict):
        raise ValueError("Scenario must be an object")
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]{0,63}", scenario.get("id", "")):
        raise ValueError("Scenario id must be a short identifier")
    if not isinstance(scenario.get("goal"), str) or not 1 <= len(scenario["goal"].strip()) <= 2000:
        raise ValueError("Provide a bounded, nonempty test goal")
    start = origin(scenario.get("url", ""))
    if scenario.get("test_environment") is not True or scenario.get("dedicated_test_profile") is not True:
        raise ValueError("Declare a disposable test environment and dedicated test profile; never use a production account")
    allowed = scenario.get("allowed_origins", [scenario["url"]])
    if not isinstance(allowed, list) or not 1 <= len(allowed) <= 5 or start not in [origin(x) for x in allowed]:
        raise ValueError("Initial test URL must match the bounded allowed-origin list")
    decisions = scenario.get("max_decisions", 12)
    actions = scenario.get("max_actions", 8)
    if type(decisions) is not int or type(actions) is not int or not 1 <= actions <= decisions <= 40:
        raise ValueError("Use 1 <= max_actions <= max_decisions <= 40")
    if type(scenario.get("allow_typing", False)) is not bool:
        raise ValueError("allow_typing must be boolean")
    if scenario.get("requires", []) != []:
        raise ValueError("Use the normal browser worker for features outside the JEV MVP")
    checks = scenario.get("checks")
    if not isinstance(checks, list) or not 1 <= len(checks) <= 20:
        raise ValueError("Provide 1–20 independent outcome checks")
    for check in checks:
        if not isinstance(check, dict) or check.get("type") not in ("text", "url_path", "exists", "field_value"):
            raise ValueError("Unsupported outcome check")
        keys = {"type", "selector", "value"} if check["type"] == "field_value" else {"type", "selector"} if check["type"] == "exists" else {"type", "value"}
        if set(check) != keys or any(not isinstance(check[k], str) or not check[k] or len(check[k]) > 2000 for k in keys - {"type"}):
            raise ValueError("Outcome checks require exact, bounded string fields")
    return allowed, decisions, actions


def doctor():
    result = {"python_ready": sys.version_info >= (3, 12), "expected_ref": REF,
              "package_ready": False, "pinned_source": False,
              "browser_tested": False, "model_calls_made": False}
    try:
        distribution = importlib.metadata.distribution("jev-ultrafast")
        result["version"] = distribution.version
        result["package_ready"] = True
        direct = json.loads(distribution.read_text("direct_url.json") or "{}")
        result["pinned_source"] = direct.get("url") == SOURCE
    except (importlib.metadata.PackageNotFoundError, ValueError, TypeError):
        pass
    result["status"] = "READY_FOR_CONFIG" if all(result[k] for k in ("python_ready", "package_ready", "pinned_source")) else "NEED_SETUP"
    return result


def load_agent():
    if doctor()["status"] != "READY_FOR_CONFIG":
        raise RuntimeError("Use the optional pinned Python 3.12+ JEV environment")
    from jev_ultrafast import Agent
    return Agent


def verify(browser, checks):
    results = []
    for index, check in enumerate(checks):
        kind = check["type"]
        if kind == "text":
            expression = "document.body.innerText.includes(" + json.dumps(check["value"]) + ")"
        elif kind == "url_path":
            expression = "location.pathname === " + json.dumps(check["value"])
        elif kind == "exists":
            expression = "document.querySelector(" + json.dumps(check["selector"]) + ") !== null"
        else:
            expression = "document.querySelector(" + json.dumps(check["selector"]) + ")?.value === " + json.dumps(check["value"])
        # Expressions are code-owned; scenario strings are JSON data, never code.
        results.append({"check": index + 1, "type": kind, "passed": browser.evaluate(expression) is True})
    return results


def run_scenario(scenario, allow_paid=False, agent_factory=None):
    allowed, max_decisions, max_actions = validate(scenario)
    report = {"scenario_id": scenario["id"], "scenario_sha256": hashlib.sha256(
                  json.dumps(scenario, sort_keys=True, separators=(",", ":")).encode()).hexdigest(),
              "source_ref": REF, "journey_status": "BLOCKED",
              "overall_qa_status": "BLOCKED", "decisions_attempted": 0, "actions_executed": 0,
              "checks": [], "limitations": LIMITATIONS,
              "profile_isolation": "declared by scenario; not independently verified"}
    if not allow_paid:
        report["reason"] = "DISABLED_BY_DEFAULT: a live run requires explicit --allow-paid and configured providers"
        return report
    needed = ["TYPESAFE_API_KEY"] + (["TEXT_MODEL_API_KEY", "TEXT_MODEL_BASE_URL", "TEXT_MODEL"]
                                    if scenario.get("allow_typing", False) else [])
    if any(not os.environ.get(name) for name in needed):
        report["reason"] = "NEED_SETUP: configure required provider credentials outside chat; none were printed"
        return report
    if scenario.get("allow_typing", False):
        endpoint = urlparse(os.environ["TEXT_MODEL_BASE_URL"])
        local = endpoint.hostname in ("localhost", "127.0.0.1", "::1")
        if (not endpoint.hostname or endpoint.username or endpoint.password or endpoint.query or endpoint.fragment
                or (endpoint.scheme != "https" and not (endpoint.scheme == "http" and local))):
            report["reason"] = "NEED_SETUP: use an explicit HTTPS text-model endpoint, or HTTP on local loopback"
            return report
    start = time.monotonic()
    phase = "dependency setup"
    agent = None
    try:
        factory = agent_factory or load_agent()
        allowed_origins = {origin(x) for x in allowed}
        phase = "browser setup"
        # No inspector, raw screenshots, state traces or generated field values are persisted.
        with factory(scenario["url"], scenario["goal"], screenshots=False) as agent:
            def check_origin():
                return origin(agent.browser.evaluate("location.href")) in allowed_origins

            phase = "journey execution"
            for _ in range(max_decisions):
                if not check_origin():
                    report["reason"] = "Navigation left the approved test origin"
                    break
                report["decisions_attempted"] += 1
                agent.command("predict")
                if not check_origin():
                    report["reason"] = "Navigation changed before execution"
                    break
                decision = agent.state["decision"]["choice"]
                if decision not in ("DONE", "BLOCKED"):
                    action = next(x for x in agent.state["page"]["actions"] if x["id"] == decision)
                    if action["kind"] not in ("click", "fill", "select", "scroll", "wait"):
                        report["reason"] = "Unsupported action requires the normal browser worker"
                        break
                    if action["kind"] == "fill" and not scenario.get("allow_typing", False):
                        report["reason"] = "Typing is outside the approved scenario"
                        break
                    if report["actions_executed"] >= max_actions:
                        report["reason"] = "Action budget exhausted"
                        break
                agent.command("act", {"fingerprint": agent.state["page"]["fingerprint"]})
                report["actions_executed"] = len(agent.state["history"])
                if not check_origin():
                    report["reason"] = "Navigation left the approved test origin"
                    break
                if agent.state["status"] == "done":
                    phase = "independent outcome verification"
                    report["checks"] = verify(agent.browser, scenario["checks"])
                    report["journey_status"] = "PASS" if all(c["passed"] for c in report["checks"]) else "FAIL"
                    report["reason"] = "Independent outcome checks completed; normal browser QA gates still required"
                    break
                if agent.state["status"] == "blocked":
                    report["reason"] = "JEV reported BLOCKED"
                    break
            else:
                report["reason"] = "Decision budget exhausted"
    except Exception as error:
        if agent is not None:
            report["actions_executed"] = len(agent.state.get("history", []))
        # Provider exceptions may contain requests or page data; persist only the class and stage.
        report["reason"] = f"{phase} failed ({type(error).__name__}); inspect locally without sharing secrets"
    report["elapsed_ms"] = round((time.monotonic() - start) * 1000)
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--doctor", action="store_true", help="Offline dependency check; no key reads or browser/model calls")
    parser.add_argument("--scenario", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--allow-paid", action="store_true", help="Explicit authorization for this scenario's provider calls")
    args = parser.parse_args()
    if args.doctor:
        print(json.dumps(doctor(), indent=2))
        return 0
    if not args.scenario or not args.output:
        parser.error("Provide --scenario and --output, or use --doctor")
    try:
        if args.scenario.stat().st_size > 64 * 1024:
            raise ValueError("Scenario exceeds 64 KiB")
        report = run_scenario(json.loads(args.scenario.read_text()), args.allow_paid)
    except (ValueError, OSError, TypeError) as error:
        parser.error(str(error))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n")
    print(f"JEV journey: {report['journey_status']}; overall QA: BLOCKED. Report: {args.output}")
    return 0 if report["journey_status"] == "PASS" else 1 if report["journey_status"] == "FAIL" else 2


if __name__ == "__main__":
    raise SystemExit(main())
