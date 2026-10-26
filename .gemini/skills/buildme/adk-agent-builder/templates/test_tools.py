"""Template for agent/tests/test_tools.py: offline, deterministic tool tests.

Run from the project root: python -m pytest -q agent/tests
No model call, no Ollama and no API key needed.
"""

from agent.agent import lookup_brief


def test_lookup_brief_returns_topic_and_facts():
  result = lookup_brief("vehicle wraps")
  assert result["topic"] == "vehicle wraps"
  assert isinstance(result["facts"], list)


def test_lookup_brief_handles_empty_topic():
  result = lookup_brief("")
  assert result["topic"] == ""
  assert result["facts"] == []
