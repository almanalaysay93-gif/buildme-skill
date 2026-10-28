"""Exercise installer success and partial/failure states without changing user tools."""

import contextlib
import importlib.util
import io
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("install_agent_reach", ROOT / "scripts/install_agent_reach.py")
installer = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(installer)


def response(result):
    return {"ok": True, "result": result}


class InstallerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="buildme-install-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.bin = self.root / "tools with spaces"
        self.bin.mkdir()
        self.exe = self.bin / ("agent-reach.exe" if os.name == "nt" else "agent-reach")
        self.exe.touch()
        self.calls = []
        self.failure = None
        self.data = {
            "version": response({"version": "1.6.0"}),
            "setup": response({"default_channels": [{"channel": "web", "ok": True},
                                                       {"channel": "github", "ok": True}],
                               "installation_report": {"markdown": "# Upstream report\n\nKeep this exact.\n"},
                               "user_actions": ["Refresh skill discovery."]}),
            "skill": response({"installed": True}),
            "channels": {"ok": True, "channels": [{"name": "web"}, {"name": "github"}]},
        }
        self.addCleanup(patch.stopall)
        patch.object(installer.shutil, "which", return_value="/existing/uv").start()
        patch.object(installer.subprocess, "run", side_effect=self.fake_run).start()

    def fake_run(self, argv, **kwargs):
        self.calls.append((argv, kwargs))
        if self.failure and self.failure in argv:
            return subprocess.CompletedProcess(argv, 1, "", "simulated install failure")
        if argv[1:] == ["tool", "dir", "--bin"]:
            output = str(self.bin)
        elif argv[1:3] == ["tool", "install"]:
            output = "installed"
        else:
            output = json.dumps(self.data[argv[1]])
        return subprocess.CompletedProcess(argv, 0, output, "")

    def install(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            installer.install([self.root / "shared skills"])
        return output.getvalue()

    def test_official_install_setup_skill_link_and_inventory(self):
        output = self.install()
        args = [call[0] for call in self.calls]
        self.assertEqual(args[0], ["/existing/uv", "tool", "install", "--force", installer.SOURCE])
        self.assertIn([str(self.exe), "setup"], args)
        self.assertIn([str(self.exe), "skill", "link", str(self.root / "shared skills")], args)
        self.assertIn("# Upstream report\n\nKeep this exact.\n", output)
        self.assertIn("Refresh skill discovery.", output)
        self.assertIn("Live research has not been tested", output)
        for command in args:
            self.assertNotIn("login", command)
            self.assertNotIn("configure", command)
            self.assertNotIn("add", command)

    def test_partial_setup_fails_even_with_ok_envelope(self):
        self.data["setup"]["result"]["default_channels"][1]["ok"] = False
        with self.assertRaisesRegex(RuntimeError, "setup is incomplete"):
            self.install()
        self.assertNotIn("channels", [call[0][1] for call in self.calls])

    def test_missing_skill_is_not_success(self):
        self.data["skill"] = response({"installed": False})
        with self.assertRaisesRegex(RuntimeError, "skill is not installed"):
            self.install()

    def test_missing_github_channel_is_not_success(self):
        self.data["channels"]["channels"] = [{"name": "web"}]
        with self.assertRaisesRegex(RuntimeError, "web and GitHub"):
            self.install()

    def test_failed_package_install_stops_before_setup(self):
        self.failure = "install"
        with self.assertRaisesRegex(RuntimeError, "simulated install failure"):
            self.install()
        self.assertEqual(len(self.calls), 1)

    def test_missing_executable_fails_without_path_guess(self):
        self.exe.unlink()
        with self.assertRaisesRegex(RuntimeError, "executable is missing"):
            self.install()

    def test_old_or_nonofficial_version_schema_is_rejected(self):
        self.data["version"] = response({"version": "1.5.0"})
        with self.assertRaisesRegex(RuntimeError, "1.6"):
            self.install()

    def test_invalid_json_and_error_hint_are_actionable(self):
        with self.assertRaisesRegex(RuntimeError, "valid Agent-Reach JSON"):
            installer.envelope("Agent Reach v1.5", "version")
        with self.assertRaisesRegex(RuntimeError, "repair setup"):
            installer.envelope(json.dumps({"ok": False, "error": {"hint": "repair setup"}}), "setup")


class BootstrapTests(unittest.TestCase):
    @unittest.skipIf(os.name == "nt", "POSIX shell failure propagation")
    def test_full_installer_stops_before_registering_skills_when_dependency_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            fake_python = Path(directory) / "python3"
            fake_python.write_text("#!/bin/sh\nexit 27\n")
            fake_python.chmod(0o755)
            # No HOME override and no installer writes: the failed dependency
            # must stop install.sh before its skill-copy loop can run.
            env = dict(os.environ, PATH=directory + os.pathsep + os.environ["PATH"])
            result = subprocess.run(["bash", str(ROOT / "scripts/install.sh")],
                                    env=env, capture_output=True, text=True)
            self.assertEqual(result.returncode, 27)
            self.assertNotIn("are installed", result.stdout)

    def test_missing_uv_uses_official_astral_installer_without_shell_profile_changes(self):
        with tempfile.TemporaryDirectory() as directory:
            user_dir = Path(directory)
            uv = user_dir / ".local/bin" / ("uv.exe" if os.name == "nt" else "uv")

            def bootstrap(argv, **kwargs):
                uv.parent.mkdir(parents=True)
                uv.touch()
                self.assertEqual(kwargs["env"]["UV_NO_MODIFY_PATH"], "1")
                self.assertEqual(kwargs["env"].get("HOME"), os.environ.get("HOME"))
                return ""

            with patch.object(installer.shutil, "which", return_value=None), \
                    patch.object(installer.Path, "home", return_value=user_dir), \
                    patch.object(installer.urllib.request, "urlretrieve") as download, \
                    patch.object(installer, "run", side_effect=bootstrap):
                self.assertEqual(installer.ensure_uv(), str(uv))
            self.assertTrue(download.call_args.args[0].startswith("https://astral.sh/uv/install."))


if __name__ == "__main__":
    unittest.main()
