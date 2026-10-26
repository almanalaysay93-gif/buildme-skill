"""Template for agent/agent.py: a two-step ADK Workflow (research, then write).

Runs on a free local model through Ollama. No API key, account or paid service.

Copy to `agent/agent.py` and add `agent/__init__.py` containing `from . import agent`.
`adk run`, `adk web` and `adk test` import this module and read `root_agent`, so keep
module-level code free of side effects. Run this file directly for an offline
construction check (no model call).

Requires: google-adk, litellm, and Ollama running locally with the model pulled:
  ollama pull qwen2.5:1.5b
Override the model with the BUILDME_LOCAL_MODEL environment variable.
"""

import os

from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm
from google.adk.workflow import START, Workflow

LOCAL_MODEL = LiteLlm(model="ollama_chat/" + os.environ.get("BUILDME_LOCAL_MODEL", "qwen2.5:1.5b"))


def lookup_brief(topic: str) -> dict:
  """Return a short fact sheet for a topic from the project's own content."""
  return {"topic": topic, "facts": []}


researcher = LlmAgent(
    name="researcher",
    model=LOCAL_MODEL,
    instruction="Gather facts for the user's topic using lookup_brief.",
    tools=[lookup_brief],
    output_key="facts",
)

writer = LlmAgent(
    name="writer",
    model=LOCAL_MODEL,
    instruction="Write a short answer from {facts}. Say so when facts are empty.",
    output_key="answer",
)

root_agent = Workflow(
    name="brief_pipeline",
    edges=[(START, researcher), (researcher, writer)],
)


if __name__ == "__main__":
  from google.adk.agents.run_config import RunConfig
  from google.adk.runners import Runner
  from google.adk.sessions import InMemorySessionService

  runner = Runner(
      app_name="brief_app",
      agent=root_agent,
      session_service=InMemorySessionService(),
      auto_create_session=True,
  )
  run_config = RunConfig(max_llm_calls=20)  # pass to runner.run_async(run_config=...)
  print("constructed:", root_agent.name, "| model:", LOCAL_MODEL.model,
        "| max_llm_calls:", run_config.max_llm_calls)
