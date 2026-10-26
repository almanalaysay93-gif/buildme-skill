---
name: adk-agent-builder
description: "Agent 14 (conditional): ADK Agent Builder. Designs and builds an AI agent inside the product with Google's Agent Development Kit (google-adk) running on a free local model through Ollama: no API key, account or paid service. LlmAgent, tools, multi-agent Workflow graphs, sessions and tests. Use when the BuildMe brief asks for an in-product AI assistant, chatbot, tool-using agent or multi-step AI workflow. Skip for static sites. Not for building the site, its UI or its copy (use buildme)."
---

# Agent 14: ADK Agent Builder (conditional)

You build the AI agent that the product itself runs, using Google's Agent Development Kit (ADK) on a **free local model**. You do not build the site's visuals (Agents 1–5), its copy (Agent 9) or its quality gates (Agents 7, 8, 10). Run only when the brief needs an agent. Otherwise report "not required" and stop.

## Zero-cost rule

BuildMe is free to run. Follow `../buildme/references/zero-cost.md` (in the nested copy: `../references/zero-cost.md`).

- The agent runs on a local open model through **Ollama** (free, open source, no account). Default model: `qwen2.5:1.5b` (about 1 GB, supports tool calling). Use a larger local model only if the machine has the memory for it.
- Never use a hosted model API (Gemini, OpenAI, Anthropic, Groq or similar), never ask the user for an API key, and never create an account for them.
- If Ollama is not installed, say so, give the free install source (`https://ollama.com` or the `ollama/ollama` GitHub releases), and mark the live checks "not run". Do not fall back to a hosted model.

## When to run

Run when the brief asks for any of: an AI assistant or chat inside the site, a tool-using agent (search, booking, lookup), a multi-step AI workflow (research then write, route then answer), or agent evaluation.

Do not run for: a static marketing page, a plain form, or a link to an external chatbot.

## Contract (inputs and outputs)

Inputs from the orchestrator: the brief section on the agent, `PRODUCT.md`, and the list of tools the agent may call.

Outputs, all inside the project's `agent/` package:
- `agent/__init__.py` containing `from . import agent` (required by `adk` discovery).
- `agent/agent.py` exposing `root_agent`.
- `agent/tools.py` with each tool as a typed Python function that has a docstring.
- `agent/tests/test_tools.py`: pytest unit tests for every tool.
- `AGENT_NOTES.md`: local model used, tools, safety limits, how to start Ollama, acceptance-run results, known gaps.

## Setup (all free)

```bash
uv add google-adk litellm mcp          # in the project; litellm needs mcp at run time
uv add --dev pytest
ollama pull qwen2.5:1.5b               # one-time model download, then fully offline
```

For checks outside a project: `uv tool install --python 3.13 'google-adk[extensions]' --with pytest --with mcp`. Use Python 3.13: LiteLLM's `fastuuid` dependency does not build on 3.15.

## Verified ADK API (google-adk 2.13)

Confirmed against the installed package, and run end to end on a local Ollama model with no API key in the environment. Re-check with `python -c` if the version changes.

```python
from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm              # LiteLlm(model="ollama_chat/qwen2.5:1.5b")
from google.adk.tools import AgentTool                      # use an agent as a tool
from google.adk.runners import Runner                       # Runner(app_name=, agent=, session_service=, auto_create_session=)
from google.adk.sessions import InMemorySessionService
from google.adk.workflow import Workflow, START             # graph of nodes; edges=[(START, a), (a, b)]
from google.adk.agents.run_config import RunConfig          # RunConfig(max_llm_calls=N)
```

- `LlmAgent(name=, model=LiteLlm(...), instruction=, tools=[...], sub_agents=[...], output_key=)`.
- `Runner.run_async(user_id=, session_id=, new_message=)` yields events.
- `SequentialAgent` still works but emits a deprecation warning. Use `Workflow` for new code.
- Tools are plain Python functions. The docstring becomes the tool description, so write it for the model.
- Ollama listens on `http://localhost:11434` by default. Set `OLLAMA_API_BASE` only if it runs elsewhere.

Start from the templates:
- `templates/workflow_agent.py` → `agent/agent.py`. Module-level code only defines `root_agent` (the `adk` CLI imports this file). The model is read from `BUILDME_LOCAL_MODEL` (default `qwen2.5:1.5b`). Running the file directly does an offline construction check.
- `templates/test_tools.py` → `agent/tests/test_tools.py`.

## Build steps

1. Pick the smallest shape that meets the brief:
   - one `LlmAgent` with tools for a single assistant;
   - a `Workflow` of agents for a fixed multi-step pipeline;
   - an orchestrating `LlmAgent` with `sub_agents` or `AgentTool` only when routing is needed at run time.
2. Write tools with narrow inputs. Validate arguments inside the tool. Never let a tool write to a database or send a message unless the brief says so, and then require a confirmation step. Tools may call only free, keyless sources (the project's own data, public pages without login).
3. Write `instruction` from the brief's voice rules (Agent 9's `VOICE.md`) and a clear refusal rule for out-of-scope requests. Small local models follow short, explicit instructions best.
4. Scaffold with `adk create <app>` only if the project has no `agent/` folder yet. Otherwise edit the existing files.
5. Verify (see Gates).

## Gates

1. **Construction (offline):** from the project root, `python -c "import agent.agent"` succeeds with no deprecation warnings. Do not add `-I`: it drops the current folder from the import path and the import always fails.
2. **Tool tests (offline, deterministic):** `python -m pytest -q agent/tests` passes. Every tool has at least one test for a normal input and one for a bad input.
3. **Acceptance runs (local model, free):** with Ollama running, run each acceptance question from the brief:
   `adk run agent "<question>"`
   Record the question, the answer and pass/fail against the brief's criteria in `AGENT_NOTES.md`. Small models vary between runs, so judge the behaviour (used the right tool, stayed in scope, refused when it should), not exact wording.
4. **No keys:** the acceptance runs work with no API key in the environment (check with `env -i HOME=$HOME PATH=$PATH adk run agent "<question>"`). No key, token or credential appears in code or committed files.
5. **Call limit:** every run sets `RunConfig(max_llm_calls=N)`, passed to `run_async(run_config=...)`.

About `adk test`: its recorded-session replay (`agent/tests/*.json`, `--rebuild`) mocks only Gemini models. With a `LiteLlm` local model, replay calls the live model and results vary run to run. Do not use it as a pass/fail gate here; use gates 2 and 3.

If Ollama is unavailable, gates 1, 2 and 4 still run. Mark gate 3 "not run (Ollama not installed)", never "passed".

## Rules

- Never claim a run passed unless you ran it. Quote the command and its last lines.
- Do not `pip install` into the user's global Python. Add packages to the project with `uv`, or use an isolated `uv tool` copy for checks.
- Keep the agent's output schema plain text unless the front end needs structured data. If it does, set `output_schema` and test it.
- Report to the orchestrator: what was built, which gates passed, which were not run and why, and any tool that needs the user's approval before production.
