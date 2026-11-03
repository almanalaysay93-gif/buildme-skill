#!/usr/bin/env python3
"""Install pinned Agent Desktop locally; never request OS permissions or read apps."""

import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys


VERSION = "1.1.0"
PACKAGE = f"agent-desktop@{VERSION}"


def run(argv, **kwargs):
    result = subprocess.run(argv, capture_output=True, text=True, check=False, **kwargs)
    if result.returncode:
        raise RuntimeError(f"{Path(str(argv[0])).name} command failed; inspect the local package-manager output")
    return result.stdout.strip()


def npm_command():
    npm = shutil.which("npm")
    node = shutil.which("node")
    if not npm or not node:
        raise RuntimeError("Node.js 18+ and npm are required for Agent Desktop")
    resolved = Path(npm).resolve()
    candidates = [resolved, Path(node).parent / "node_modules/npm/bin/npm-cli.js",
                  Path(node).parent.parent / "lib/node_modules/npm/bin/npm-cli.js"]
    for path in candidates:
        if path.name == "npm-cli.js" and path.is_file():
            return [node, str(path)], node
    if os.name != "nt":
        return [npm], node
    raise RuntimeError("Cannot locate npm-cli.js; repair the Node/npm installation")


def install(directory):
    directory = Path(directory).expanduser().resolve()
    receipt = directory / "buildme-desktop.json"
    if directory.exists() and any(directory.iterdir()):
        try:
            old = json.loads(receipt.read_text())
        except (ValueError, OSError) as error:
            raise RuntimeError("Desktop tool directory contains unmanaged files; choose an empty directory") from error
        if not isinstance(old, dict) or old.get("package") != PACKAGE:
            raise RuntimeError("Desktop tool directory is not managed by this installer version")
    npm, node = npm_command()
    directory.mkdir(parents=True, exist_ok=True)
    receipt.write_text(json.dumps({"package": PACKAGE, "status": "installing"}) + "\n")
    run([*npm, "install", "--prefix", str(directory), "--save-exact", "--no-audit", "--no-fund", PACKAGE])
    package = directory / "node_modules/agent-desktop"
    # Resolve the bundled native executable through the package's own platform table.
    query = "const p=require(process.argv[1]);const e=p.resolve(process.platform,process.arch);console.log(JSON.stringify({entry:e,helpers:e?p.helperNames(e):[]}));"
    resolved = json.loads(run([node, "-e", query, str(package / "lib/platform.js")]))
    entry = resolved.get("entry")
    if not isinstance(entry, dict) or not entry.get("released"):
        raise RuntimeError("No released Agent Desktop binary for this platform")
    binary = package / "bin" / entry["binaryName"]
    if not binary.resolve().is_relative_to(package.resolve()) or not binary.is_file():
        raise RuntimeError("Agent Desktop native binary is missing")
    env = dict(os.environ)
    helper = None
    if os.name != "nt" and sys.platform == "darwin":
        helpers = resolved.get("helpers") or []
        if not helpers:
            raise RuntimeError("Agent Desktop did not identify its macOS helper")
        helper = package / "bin" / helpers[0]
        if not helper.is_file():
            raise RuntimeError("Agent Desktop macOS helper is missing; allow its npm install script and retry")
        env["AGENT_DESKTOP_MACOS_HELPER_PATH"] = str(helper)
    version = json.loads(run([str(binary), "version"], env=env))
    if version.get("ok") is not True or version.get("data", {}).get("version") != VERSION:
        raise RuntimeError("Agent Desktop version verification failed")
    docs = directory / "skills"
    docs.mkdir(exist_ok=True)
    for name in ("desktop", "platform"):
        result = json.loads(run([str(binary), "skills", "get", name], env=env))
        content = result.get("data", {}).get("content")
        if result.get("ok") is not True or not isinstance(content, str) or not content.strip():
            raise RuntimeError("Agent Desktop did not provide its version-matched skills")
        (docs / f"{name}.md").write_text(content)
    receipt.write_text(json.dumps({"package": PACKAGE, "binary": str(binary), "helper": str(helper) if helper else None,
                                   "status": "installed", "desktop_tested": False}, indent=2) + "\n")
    print(f"Agent Desktop {VERSION} and its version-matched skills installed at {directory}.")
    print("No apps were read or controlled. OS permissions/graphical-session readiness still need checking.")
    return binary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--directory", type=Path, default=Path.home() / ".agents/tools/agent-desktop")
    args = parser.parse_args()
    try:
        install(args.directory)
    except (OSError, RuntimeError, ValueError, KeyError, TypeError) as error:
        print(f"Agent Desktop installation incomplete: {error}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
