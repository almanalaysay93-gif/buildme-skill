#!/usr/bin/env python3
"""Install official Agent-Reach, its skill and default channels for Buildme."""

import argparse
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.request


SOURCE = "https://github.com/Panniantong/Agent-Reach/releases/latest/download/agent-reach.zip"


def run(argv, **kwargs):
    result = subprocess.run(argv, capture_output=True, text=True, check=False, **kwargs)
    if result.returncode:
        raise RuntimeError(f"{Path(str(argv[0])).name} {argv[1]} failed: "
                           f"{result.stderr.strip() or result.stdout.strip()}")
    return result.stdout.strip()


def envelope(text, operation):
    try:
        data = json.loads(text)
    except ValueError as error:
        raise RuntimeError(f"{operation} did not return valid Agent-Reach JSON") from error
    if not isinstance(data, dict) or data.get("ok") is not True:
        error = data.get("error") if isinstance(data, dict) else None
        hint = error.get("hint") or error.get("message") if isinstance(error, dict) else ""
        raise RuntimeError(f"{operation} was not successful. {hint}")
    return data


def ensure_uv():
    existing = shutil.which("uv")
    if existing:
        return existing
    print("Installing uv from Astral's official installer (no admin access).")
    install_dir = Path.home() / ".local" / "bin"
    windows = os.name == "nt"
    suffix = "ps1" if windows else "sh"
    with tempfile.TemporaryDirectory(prefix="buildme-uv-") as directory:
        script = Path(directory) / f"install.{suffix}"
        urllib.request.urlretrieve(f"https://astral.sh/uv/install.{suffix}", script)
        env = dict(os.environ, UV_INSTALL_DIR=str(install_dir), UV_NO_MODIFY_PATH="1")
        argv = (["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", str(script)]
                if windows else ["sh", str(script)])
        run(argv, env=env)
    uv = install_dir / ("uv.exe" if windows else "uv")
    if not uv.is_file():
        raise RuntimeError("uv installation failed; see https://docs.astral.sh/uv/getting-started/installation/")
    return str(uv)


def install(skills_dirs):
    uv = ensure_uv()
    # Use the upstream URL, never the unrelated package on PyPI. Reinstalling the
    # named CLI refreshes its source without deleting Agent-Reach's user settings.
    print("Installing Agent-Reach from its official GitHub release.")
    run([uv, "tool", "install", "--force", SOURCE])
    directory = run([uv, "tool", "dir", "--bin"])
    if not directory or not Path(directory).is_absolute():
        raise RuntimeError("uv did not return an absolute tool-bin directory")
    executable = Path(directory) / ("agent-reach.exe" if os.name == "nt" else "agent-reach")
    if not executable.is_file():
        raise RuntimeError(f"Agent-Reach executable is missing from {directory}")
    command = str(executable)
    version = envelope(run([command, "version"]), "version").get("result") or {}
    match = re.match(r"^(\d+)\.(\d+)", str(version.get("version", "")))
    if not match or tuple(map(int, match.groups())) < (1, 6):
        raise RuntimeError("Agent-Reach 1.6+ is required for JSON setup and channel verification")
    setup = envelope(run([command, "setup"]), "setup").get("result") or {}
    report = setup.get("installation_report") or {}
    markdown = report.get("markdown")
    if not isinstance(markdown, str) or not markdown.strip():
        raise RuntimeError("Agent-Reach setup did not provide its installation report")
    # Display the upstream report unchanged, including its limitations.
    sys.stdout.write(markdown)
    if not markdown.endswith("\n"):
        sys.stdout.write("\n")
    for action in setup.get("user_actions") or []:
        print(action)
    defaults = setup.get("default_channels")
    if (not isinstance(defaults, list) or not defaults
            or any(not isinstance(row, dict) or row.get("ok") is not True for row in defaults)):
        raise RuntimeError("Agent-Reach default-channel setup is incomplete; resolve the report and rerun the installer")
    for directory in skills_dirs:
        envelope(run([command, "skill", "link", str(directory)]), "skill link")
    skill = envelope(run([command, "skill"]), "skill").get("result") or {}
    if skill.get("installed") is not True:
        raise RuntimeError("Agent-Reach's upstream skill is not installed")
    channels = envelope(run([command, "channels"]), "channels").get("channels")
    if not isinstance(channels, list) or not {"web", "github"}.issubset(
            {row.get("name") for row in channels if isinstance(row, dict)}):
        raise RuntimeError("Agent-Reach did not expose the web and GitHub research channels")
    print(f"Agent-Reach {version['version']}, upstream skill and channel inventory verified.")
    print("Live research has not been tested. Buildme uses public/keyless routes only.")
    if str(executable.parent) not in os.environ.get("PATH", "").split(os.pathsep):
        print(f"Add {executable.parent} to PATH in your agent's shell, then refresh skill discovery.")


def main():
    if sys.version_info < (3, 10):
        print("Python 3.10+ is required for Agent-Reach.", file=sys.stderr)
        return 1
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skills-dir", action="append", type=Path, default=[])
    args = parser.parse_args()
    try:
        install(args.skills_dir)
    except (RuntimeError, OSError, subprocess.SubprocessError) as error:
        print(f"Agent-Reach installation incomplete: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
