from google.adk.agents import LlmAgent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.workflow import Workflow, START


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

root_agent = Workflow(name="brief_pipeline", edges=[(START, researcher), (researcher, writer)])

runner = Runner(
    app_name="brief_app",
    agent=root_agent,
    session_service=InMemorySessionService(),
    auto_create_session=True,
)
print("constructed:", root_agent.name, "runner:", runner.app_name)
