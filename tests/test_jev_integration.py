"""Offline JEV adapter and opt-in installer contract tests. No API/browser calls."""

import importlib.util
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import Mock, patch
from contextlib import redirect_stdout


ROOT = Path(__file__).resolve().parents[1]


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    with patch.object(sys, "path", [str(ROOT / "scripts"), *sys.path]):
        spec.loader.exec_module(result)
    return result


jev = module("buildme_jev", ROOT / "skills/buildme/scripts/jev_qa.py")
installer = module("buildme_jev_installer", ROOT / "scripts/install_jev.py")


def scenario():
    return {"id": "test-journey", "url": "http://127.0.0.1:3000/", "goal": "Show the test result",
            "test_environment": True, "dedicated_test_profile": True,
            "max_actions": 2, "max_decisions": 4,
            "checks": [{"type": "text", "value": "Ready"}]}


class FakeBrowser:
    def __init__(self, valid=True):
        self.url = "http://127.0.0.1:3000/"
        self.valid = valid
        self.expressions = []

    def evaluate(self, expression):
        self.expressions.append(expression)
        return self.url if expression == "location.href" else self.valid


class FakeAgent:
    def __init__(self, choices, valid=True, leave_origin=False, error=False):
        self.browser = FakeBrowser(valid)
        self.choices = iter(choices)
        self.leave_origin = leave_origin
        self.error = error
        self.closed = False
        self.state = {"page": {"fingerprint": "observed", "actions": [
            {"id": "click", "kind": "click"}, {"id": "fill", "kind": "fill"}]},
            "history": [], "status": "ready", "decision": None}

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.closed = True

    def command(self, name, body=None):
        if name == "predict":
            if self.error:
                raise RuntimeError("SECRET_PROVIDER_REQUEST_AND_PAGE_TEXT")
            self.state["decision"] = {"choice": next(self.choices, "click")}
        elif name == "act":
            choice = self.state["decision"]["choice"]
            if choice in ("DONE", "BLOCKED"):
                self.state["status"] = choice.lower()
            else:
                self.state["history"].append({"kind": choice})
                if self.leave_origin:
                    self.browser.url = "https://outside.test/"


class JourneyTests(unittest.TestCase):
    def run_case(self, agent, config=None):
        factory = Mock(return_value=agent)
        with patch.dict(os.environ, {"TYPESAFE_API_KEY": "test-placeholder", "TEXT_MODEL_API_KEY": ""}):
            result = jev.run_scenario(config or scenario(), allow_paid=True, agent_factory=factory)
        return result, factory

    def test_disabled_before_key_read_dependency_import_or_browser(self):
        factory = Mock(side_effect=AssertionError("must not open browser"))
        class ForbiddenEnvironment:
            def get(self, key):
                raise AssertionError("must not read credentials")
        with patch.object(jev.os, "environ", ForbiddenEnvironment()):
            result = jev.run_scenario(scenario(), agent_factory=factory)
        self.assertEqual(result["journey_status"], "BLOCKED")
        factory.assert_not_called()

    def test_missing_key_stops_before_agent_creation(self):
        factory = Mock()
        with patch.dict(os.environ, {"TYPESAFE_API_KEY": ""}):
            result = jev.run_scenario(scenario(), allow_paid=True, agent_factory=factory)
        self.assertIn("NEED_SETUP", result["reason"])
        factory.assert_not_called()

    def test_done_requires_independent_outcomes(self):
        agent = FakeAgent(["DONE"], valid=False)
        result, _ = self.run_case(agent)
        self.assertEqual(result["journey_status"], "FAIL")
        self.assertFalse(result["checks"][0]["passed"])
        self.assertTrue(agent.closed)

    def test_verified_journey_never_implies_overall_qa_pass(self):
        result, factory = self.run_case(FakeAgent(["click", "DONE"]))
        self.assertEqual(result["journey_status"], "PASS")
        self.assertEqual(result["overall_qa_status"], "BLOCKED")
        self.assertEqual(result["actions_executed"], 1)
        self.assertFalse(factory.call_args.kwargs["screenshots"])
        self.assertNotIn("goal", result)

    def test_action_budget_prevents_next_mutation(self):
        config = scenario()
        config["max_actions"] = 1
        agent = FakeAgent(["click", "click", "DONE"])
        result, _ = self.run_case(agent, config)
        self.assertEqual(result["reason"], "Action budget exhausted")
        self.assertEqual(len(agent.state["history"]), 1)
        self.assertTrue(agent.closed)

    def test_decision_budget_is_bounded(self):
        config = scenario()
        config.update(max_actions=2, max_decisions=2)
        result, _ = self.run_case(FakeAgent(["click", "click", "DONE"]), config)
        self.assertEqual(result["reason"], "Decision budget exhausted")
        self.assertEqual(result["decisions_attempted"], 2)

    def test_typing_is_not_silently_enabled(self):
        agent = FakeAgent(["fill"])
        result, _ = self.run_case(agent)
        self.assertIn("Typing is outside", result["reason"])
        self.assertEqual(len(agent.state["history"]), 0)
        config = scenario()
        config["allow_typing"] = True
        result, factory = self.run_case(FakeAgent(["fill"]), config)
        self.assertIn("NEED_SETUP", result["reason"])
        factory.assert_not_called()

    def test_origin_change_blocks_and_closes_tab(self):
        agent = FakeAgent(["click"], leave_origin=True)
        result, _ = self.run_case(agent)
        self.assertEqual(result["journey_status"], "BLOCKED")
        self.assertIn("left the approved", result["reason"])
        self.assertTrue(agent.closed)

    def test_errors_are_sanitized(self):
        agent = FakeAgent(["DONE"], error=True)
        result, _ = self.run_case(agent)
        self.assertNotIn("SECRET_PROVIDER", json.dumps(result))
        self.assertEqual(result["journey_status"], "BLOCKED")
        self.assertTrue(agent.closed)

    def test_unsupported_or_undeclared_test_environment_is_refused(self):
        for change in ({"requires": ["iframe"]}, {"test_environment": False},
                       {"dedicated_test_profile": False}, {"max_decisions": 100}):
            config = dict(scenario(), **change)
            with self.subTest(change=change), self.assertRaises(ValueError):
                jev.validate(config)

    def test_checks_are_bounded_declarative_data(self):
        config = scenario()
        config["checks"] = [{"type": "javascript", "value": "alert(1)"}]
        with self.assertRaises(ValueError):
            jev.validate(config)
        self.assertEqual(jev.origin("https://example.test:443/"), jev.origin("https://example.test/other"))
        with self.assertRaises(ValueError):
            jev.origin("https://user:secret@example.test")

    def test_cli_without_paid_flag_writes_blocked_report(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / "scenario.json"
            path.write_text(json.dumps(scenario()))
            result = subprocess.run([sys.executable, str(ROOT / "skills/buildme/scripts/jev_qa.py"),
                                     "--scenario", str(path), "--output", str(root / "report.json")],
                                    capture_output=True, text=True)
            self.assertEqual(result.returncode, 2, result.stderr)
            self.assertIn("DISABLED_BY_DEFAULT", (root / "report.json").read_text())

    def test_doctor_checks_metadata_without_importing_agent(self):
        distribution = Mock(version="0.1.0")
        distribution.read_text.return_value = json.dumps({"url": jev.SOURCE})
        with patch.object(jev.importlib.metadata, "distribution", return_value=distribution):
            self.assertTrue(jev.doctor()["pinned_source"])
        distribution.read_text.return_value = json.dumps({"url": "https://other.test/not-jev.zip"})
        with patch.object(jev.importlib.metadata, "distribution", return_value=distribution):
            self.assertFalse(jev.doctor()["pinned_source"])


class OptionalInstallerTests(unittest.TestCase):
    def test_installs_pinned_library_without_live_calls(self):
        calls = []
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "jev"
            def command(argv):
                calls.append(argv)
                return "0.1.0" if argv[1] == "-c" else ""
            with patch.object(installer, "ensure_uv", return_value="/fake/uv"), \
                    patch.object(installer, "run", side_effect=command), redirect_stdout(io.StringIO()):
                installer.install(target)
            self.assertIn(["/fake/uv", "venv", "--python", "3.12", str(target / "venv")], calls)
            self.assertTrue(any(argv[-1] == jev.SOURCE for argv in calls))
            self.assertEqual(json.loads((target / "buildme-jev.json").read_text())["status"], "installed")
            self.assertFalse(any("setup" in argv or "jev" in argv or "login" in argv for argv in calls))

    def test_unmanaged_target_is_preserved(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory)
            (target / "user-file").write_text("preserve")
            with self.assertRaisesRegex(RuntimeError, "unmanaged files"):
                installer.install(target)
            self.assertEqual((target / "user-file").read_text(), "preserve")

    def test_failed_dependency_install_is_not_marked_ready(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "jev"
            with patch.object(installer, "ensure_uv", return_value="/fake/uv"), \
                    patch.object(installer, "run", side_effect=RuntimeError("dependency install failed")), \
                    self.assertRaises(RuntimeError):
                installer.install(target)
            self.assertEqual(json.loads((target / "buildme-jev.json").read_text())["status"], "installing")


if __name__ == "__main__":
    unittest.main()
