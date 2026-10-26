"""Template for agent/agent.py: a two-step ADK Workflow (research, then write).

Copy to `agent/agent.py` and add `agent/__init__.py` containing `from . import agent`.
`adk run`, `adk web` and `adk test` import this module and read `root_agent`, so keep
module-level code free of side effects. Run this file directly for an offline
construction check (no model call, no API key needed).
"""

from google.adk.agents import LlmAgent
from google.adk.workflow import START, Workflow


def lookup_brief(topic: str) -> dict:
  """Return a short fact sheet for a topic from the project's own content."""
  return {"topic": topic, "facts": []}


researcher = LlmAgent(
    name="researcher",
    model="gemini-2.5-flash",
    instruction="Gather facts for the user's topic using lookup_brief.",
    tools=[lookup_brief],
    output_key="facts",
)

writer = LlmAgent(
    name="writer",
    model="gemini-2.5-flash",
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
  print("constructed:", root_agent.name, "| runner:", runner.app_name,
        "| max_llm_calls:", run_config.max_llm_calls)
