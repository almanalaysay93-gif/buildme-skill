#!/usr/bin/env python3
"""Optional pinned JEV library install; makes no browser or model calls."""

import argparse
import json
import os
from pathlib import Path

from install_agent_reach import ensure_uv, run


REF = "8251e272398011cdef648965204d1c20cd838333"
SOURCE = f"https://github.com/browser-use/jev-ultrafast/archive/{REF}.zip"


def install(directory):
    directory = Path(directory).expanduser().resolve()
    receipt = directory / "buildme-jev.json"
    if directory.exists() and any(directory.iterdir()):
        try:
            previous = json.loads(receipt.read_text())
        except (OSError, ValueError) as error:
            raise RuntimeError("JEV target contains unmanaged files; choose an empty directory") from error
        if previous.get("source") != SOURCE:
            raise RuntimeError("JEV target does not match this pinned integration")
    directory.mkdir(parents=True, exist_ok=True)
    receipt.write_text(json.dumps({"source": SOURCE, "status": "installing"}) + "\n")
    uv = ensure_uv()
    venv = directory / "venv"
    python = venv / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
    if not python.is_file():
        run([uv, "venv", "--python", "3.12", str(venv)])
    run([uv, "pip", "install", "--python", str(python), SOURCE])
    version = run([str(python), "-c", "import sys, importlib.metadata as m; assert sys.version_info >= (3,12); print(m.version('jev-ultrafast'))"])
    receipt.write_text(json.dumps({"source": SOURCE, "version": version, "status": "installed"}) + "\n")
    print(f"Optional JEV library installed at {python}.")
    print("No API keys configured; no browser or model calls made. Live runs remain disabled by default.")
    return python


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--directory", type=Path, default=Path.home() / ".agents/tools/jev-ultrafast")
    args = parser.parse_args()
    try:
        install(args.directory)
    except (RuntimeError, OSError, ValueError) as error:
        print(f"Optional JEV installation incomplete: {error}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
