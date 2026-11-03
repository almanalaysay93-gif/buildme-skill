"""Offline native-CLI contract tests; never inspect or control the real desktop."""

import importlib.util
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import Mock, patch
from contextlib import redirect_stdout
import io


ROOT = Path(__file__).resolve().parents[1]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


desktop = load("desktop_qa", ROOT / "skills/buildme/scripts/desktop_qa.py")
installer = load("install_desktop", ROOT / "scripts/install_agent_desktop.py")


def observation():
    return {"version": "2.6", "ok": True, "command": "snapshot", "data": {
        "app": "Owned test app", "window": {"id": "w-1"}, "snapshot_id": "s123", "complete": True,
        "tree": {"role": "window", "children": [
            {"role": "button", "name": "Show details", "ref_id": "@s123:e1", "states": ["enabled"]},
            {"role": "statictext", "name": "Ready"}]}}}


class DesktopTests(unittest.TestCase):
    def test_observation_is_scoped_and_not_sent_to_a_model(self):
        with patch.object(desktop, "invoke", return_value=observation()) as call:
            result = desktop.observe("Owned test app", "w-1")
        self.assertEqual(result["status"], "OBSERVED")
        call.assert_called_once_with(["snapshot", "--app=Owned test app", "--window-id=w-1"])

    def test_partial_or_identity_unproven_tree_blocks_mutation(self):
        for change in ({"complete": False}, {"identity_unproven": True}, {"truncated": True}):
            data = observation()
            data["data"].update(change)
            with self.subTest(change=change), patch.object(desktop, "invoke") as call:
                with self.assertRaises(desktop.DesktopError):
                    desktop.act(data, "click", "@s123:e1")
                call.assert_not_called()

    def test_subtree_truncation_is_not_ignored(self):
        data = observation()
        data["data"]["tree"]["children"][0]["subtree_truncated"] = True
        self.assertFalse(desktop.complete(data))

    def test_bare_foreign_and_unobserved_refs_are_rejected(self):
        for ref in ("@e1", "@other:e1", "@s123:e99"):
            with self.subTest(ref=ref), patch.object(desktop, "invoke") as call:
                with self.assertRaises(ValueError):
                    desktop.act(observation(), "click", ref)
                call.assert_not_called()

    def test_delivered_action_does_not_pass_the_task(self):
        result = {"ok": True, "data": {"disposition": {"delivery": "delivered_verified", "retry": "unsafe"}}}
        with patch.object(desktop, "invoke", return_value=result) as call:
            report = desktop.act(observation(), "click", "@s123:e1")
        self.assertEqual(report["status"], "BLOCKED")
        self.assertEqual(report["retry"], "unsafe")
        call.assert_called_once_with(["click", "@s123:e1"])

    def test_uncertain_delivery_is_never_automatically_retried(self):
        error = desktop.DesktopError("TIMEOUT", "delivery_uncertain", "unsafe")
        with patch.object(desktop, "invoke", side_effect=error) as call:
            with self.assertRaises(desktop.DesktopError) as caught:
                desktop.act(observation(), "click", "@s123:e1")
            self.assertEqual(caught.exception.retry, "unsafe")
            self.assertEqual(call.call_count, 1)

    def test_no_automatic_headed_coordinate_or_keyboard_fallback(self):
        for action in ("--headed", "mouse-click", "press", "clipboard-set"):
            with self.subTest(action=action), self.assertRaises(ValueError):
                desktop.act(observation(), action, "@s123:e1")

    def test_text_is_an_argv_value_not_a_shell_command(self):
        result = {"ok": True, "data": {"disposition": {"delivery": "delivered_unverified", "retry": "unsafe"}}}
        text = "synthetic & $(not-a-command)"
        with patch.object(desktop, "invoke", return_value=result) as call:
            desktop.act(observation(), "set-value", "@s123:e1", text)
        call.assert_called_once_with(["set-value", "@s123:e1", text])
        with self.assertRaises(ValueError):
            desktop.act(observation(), "set-value", "@s123:e1", "--headed")

    def test_fresh_assertions_are_separate_from_overall_qa(self):
        checks = [{"role": "statictext", "name": "Ready"}]
        with patch.object(desktop, "invoke", return_value=observation()) as call:
            result = desktop.verify("Owned test app", "w-1", checks)
        self.assertEqual(result["assertion_status"], "PASS")
        self.assertEqual(result["overall_qa_status"], "BLOCKED")
        self.assertEqual(call.call_count, 1)

    def test_wrong_duplicate_and_partial_outcomes_cannot_pass(self):
        checks = [{"role": "statictext", "name": "Ready"}]
        for mode in ("wrong", "duplicate", "partial"):
            data = observation()
            if mode == "wrong":
                data["data"]["tree"]["children"][1]["name"] = "Still loading"
            elif mode == "duplicate":
                data["data"]["tree"]["children"].append({"role": "statictext", "name": "Ready"})
            else:
                data["data"]["complete"] = False
            with self.subTest(mode=mode), patch.object(desktop, "invoke", return_value=data):
                result = desktop.verify("Owned test app", "w-1", checks)
            self.assertEqual(result["assertion_status"], "BLOCKED" if mode == "partial" else "FAIL")

    def test_invalid_assertion_shape_is_refused_before_desktop_read(self):
        for checks in ([], [{"script": "anything"}], [{"role": "button", "states": []}]):
            with self.subTest(checks=checks), patch.object(desktop, "invoke") as call:
                with self.assertRaises(ValueError):
                    desktop.verify("Owned test app", "w-1", checks)
                call.assert_not_called()

    def test_native_error_disposition_is_preserved_without_private_text(self):
        payload = {"ok": False, "error": {"code": "STALE_REF", "message": "PRIVATE_SCREEN_TEXT",
                   "disposition": {"delivery": "not_delivered", "retry": "safe"}}}
        with patch.object(desktop, "command", return_value=(["/fake/native"], {})), \
                patch.object(desktop.subprocess, "run", return_value=subprocess.CompletedProcess([], 1, json.dumps(payload), "")) as run:
            with self.assertRaises(desktop.DesktopError) as caught:
                desktop.invoke(["click", "@s123:e1"])
        self.assertEqual(caught.exception.retry, "safe")
        self.assertNotIn("PRIVATE_SCREEN_TEXT", str(caught.exception))
        self.assertNotIn("shell", run.call_args.kwargs)

    def test_malformed_output_and_process_timeout_do_not_claim_non_delivery(self):
        with patch.object(desktop, "command", return_value=(["/fake/native"], {})):
            with patch.object(desktop.subprocess, "run", side_effect=subprocess.TimeoutExpired([], 45)):
                with self.assertRaises(desktop.DesktopError) as caught:
                    desktop.invoke(["click", "@s123:e1"])
                self.assertEqual(caught.exception.retry, "unknown")
            with patch.object(desktop.subprocess, "run", return_value=subprocess.CompletedProcess([], 0, "not JSON", "")):
                with self.assertRaises(desktop.DesktopError):
                    desktop.invoke(["snapshot", "--app=Owned test app"])

    def test_missing_session_is_blocked_by_doctor(self):
        with patch.object(desktop, "invoke", side_effect=desktop.DesktopError("PERM_DENIED")):
            result = desktop.doctor()
        self.assertEqual(result["status"], "BLOCKED")
        self.assertFalse(result["desktop_tested"])

    def test_raw_snapshots_are_saved_locally_with_private_posix_mode(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "snapshot.json"
            desktop.save(path, observation())
            self.assertEqual(json.loads(path.read_text())["data"]["snapshot_id"], "s123")
            if os.name != "nt":
                self.assertEqual(path.stat().st_mode & 0o777, 0o600)


class InstallTests(unittest.TestCase):
    def test_pinned_install_loads_builtin_skills_without_reading_apps(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "tool"
            calls = []
            def fake_run(argv, **kwargs):
                calls.append(argv)
                if "install" in argv:
                    path = root / "node_modules/agent-desktop/bin/native-test"
                    path.parent.mkdir(parents=True)
                    path.touch()
                    return ""
                if "-e" in argv:
                    return json.dumps({"entry": {"released": True, "binaryName": "native-test"}, "helpers": []})
                if argv[-1] == "version":
                    return json.dumps({"ok": True, "data": {"version": installer.VERSION}})
                return json.dumps({"ok": True, "data": {"content": "version-matched skill"}})
            with patch.object(installer, "npm_command", return_value=(["/fake/npm"], "/fake/node")), \
                    patch.object(installer, "run", side_effect=fake_run), redirect_stdout(io.StringIO()):
                installer.install(root)
            self.assertIn(installer.PACKAGE, calls[0])
            self.assertEqual(json.loads((root / "buildme-desktop.json").read_text())["desktop_tested"], False)
            self.assertTrue((root / "skills/desktop.md").is_file())
            self.assertFalse(any("status" in argv or "snapshot" in argv or "permissions" in argv for argv in calls))

    def test_unmanaged_directory_is_not_overwritten(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "user-file").write_text("preserve")
            with self.assertRaisesRegex(RuntimeError, "unmanaged"):
                installer.install(root)
            self.assertEqual((root / "user-file").read_text(), "preserve")

    def test_failed_dependency_install_is_not_marked_ready(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "tool"
            with patch.object(installer, "npm_command", return_value=(["/fake/npm"], "/fake/node")), \
                    patch.object(installer, "run", side_effect=RuntimeError("failed")), self.assertRaises(RuntimeError):
                installer.install(root)
            self.assertEqual(json.loads((root / "buildme-desktop.json").read_text())["status"], "installing")


if __name__ == "__main__":
    unittest.main()
