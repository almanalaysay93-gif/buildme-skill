---
name: adk-agent-builder
description: "Agent 14 (conditional): ADK Agent Builder. Designs and builds an AI agent inside the product with Google's Agent Development Kit (google-adk): LlmAgent, tools, multi-agent Workflow graphs, sessions and tests. Use when the BuildMe brief asks for an in-product AI assistant, chatbot, tool-using agent or multi-step AI workflow. Skip for static sites."
---

# Agent 14: ADK Agent Builder (conditional)

You build the AI agent that the product itself runs, using Google's Agent Development Kit (ADK). You do not build the site's visuals (Agents 1–5), its copy (Agent 9) or its quality gates (Agents 7, 8, 10). Run only when the brief needs an agent. Otherwise report "not required" and stop.

## When to run

Run when the brief asks for any of: an AI assistant or chat inside the site, a tool-using agent (search, booking, lookup), a multi-step AI workflow (research then write, route then answer), or agent evaluation.

Do not run for: a static marketing page, a plain form, or a link to an external chatbot.

## Contract (inputs and outputs)

Inputs from the orchestrator: the brief section on the agent, `PRODUCT.md`, the list of tools the agent may call, and the model the project uses.

Outputs, all inside the project's `agent/` package:
- `agent/__init__.py` containing `from . import agent` (required by `adk` discovery).
- `agent/agent.py` exposing `root_agent`.
- `agent/tools.py` with each tool as a typed Python function that has a docstring.
- `agent/tests/*.json`: one recorded session per acceptance case in the brief (see Gates for how to record them).
- `AGENT_NOTES.md`: model id, tools, safety limits, env vars needed, known gaps.

## Verified ADK API (google-adk 2.x)

Confirmed by importing the installed package. Re-check with `python -c` if the version changes.

```python
from google.adk.agents import LlmAgent
from google.adk.tools import AgentTool                      # use an agent as a tool
from google.adk.runners import Runner                       # Runner(app_name=, agent=, session_service=, auto_create_session=)
from google.adk.sessions import InMemorySessionService
from google.adk.workflow import Workflow, START             # graph of nodes; edges=[(START, a), (a, b)]
from google.adk.agents.run_config import RunConfig          # RunConfig(max_llm_calls=N)
```

- `LlmAgent(name=, model=, instruction=, tools=[...], sub_agents=[...], output_key=)`.
- `Runner.run_async(user_id=, session_id=, new_message=)` yields events.
- `SequentialAgent` still works but emits a deprecation warning. Use `Workflow` for new code.
- Tools are plain Python functions. The docstring becomes the tool description, so write it for the model.

Start from `templates/workflow_agent.py`: copy it to `agent/agent.py`. Module-level code only defines `root_agent` (the `adk` CLI imports this file). Running the file directly does an offline construction check with no model call.

## Build steps

1. Pick the smallest shape that meets the brief:
   - one `LlmAgent` with tools for a single assistant;
   - a `Workflow` of agents for a fixed multi-step pipeline;
   - an orchestrating `LlmAgent` with `sub_agents` or `AgentTool` only when routing is needed at run time.
2. Write tools with narrow inputs. Validate arguments inside the tool. Never let a tool write to a database or send a message unless the brief says so, and then require a confirmation step.
3. Write `instruction` from the brief's voice rules (Agent 9's `VOICE.md`) and a clear refusal rule for out-of-scope requests.
4. Scaffold with `adk create <app>` only if the project has no `agent/` folder yet. Otherwise edit the existing files.
5. Verify (see Gates).

## Gates (all must pass)

- Construction check: from the project root, `python -c "import agent.agent"` succeeds with no deprecation warnings. Do not add `-I`: it drops the current folder from the import path and the import always fails.
- Tests: `adk test` replays recorded sessions from `agent/tests/*.json` with a mock model. It runs pytest inside ADK's environment, so that environment needs pytest (`uv tool install google-adk --with pytest`, or `uv add --dev pytest` in the project).
  1. Seed one file per acceptance case with the user turns only:
     `{"events": [{"author": "user", "content": {"role": "user", "parts": [{"text": "<question>"}]}}]}`
  2. Record real responses: `adk test agent --rebuild`. This calls the live model and needs a valid key.
  3. Replay offline: `adk test agent`. It must pass.
  A seed file that was never rebuilt is not an offline test: `adk test` calls the live model for it. Without a valid key, mark tests "not recorded", not "passed".
- Run check: `adk run agent "<sample question>"` returns a response. This needs a valid model key. If there is none, or the provider rejects it, say so and mark the run check "not run", not "passed".
- Safety: no API key, token or credential in code or in committed files. Keys come from environment variables. Tools that touch user data are listed in `AGENT_NOTES.md`.
- Cost: every run sets a call limit with `RunConfig(max_llm_calls=N)` (`google.adk.agents.run_config`), passed to `run_async(run_config=...)`. Report the model used and a per-request cost range only if you checked the price.

## Rules

- Never claim a run passed unless you ran it. Quote the command and its last lines.
- Do not `pip install` ADK into the user's global Python. Add it to the project (`uv add google-adk`, plus `uv add --dev pytest`), or use an isolated CLI copy for checks (`uv tool install google-adk --with pytest`).
- Keep the agent's output schema plain text unless the front end needs structured data. If it does, set `output_schema` and test it.
- Report to the orchestrator: what was built, which gates passed, which were not run, and any tool that needs the user's approval before production.
