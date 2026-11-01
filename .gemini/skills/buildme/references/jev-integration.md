# Optional JEV Ultrafast journey worker

Upstream: https://github.com/browser-use/jev-ultrafast (MIT)
Pinned ref: 8251e272398011cdef648965204d1c20cd838333, inspected 2026-11-01.
Reviewed README, pyproject.toml, agent.py, browser.py, model.py and check_guards.py.

## Choice and cost boundary

| Approach | Fit | Decision |
| --- | --- | --- |
| Existing Playwright browser QA | Free/keyless screenshots, console/network, overflow, keyboard and viewport checks | Keep as default and required QA evidence |
| JEV Ultrafast | Goal-driven choice of observed controls, freshness/occlusion guards and bounded desktop journeys | Optional Agent 8 helper, never a replacement for deterministic QA |
| Browser Harness alone | Local browser transport used by JEV, without its TypeSafe goal policy | Not a substitute for the requested goal-driven agent |

The source code is open source, but live JEV decisions call TypeSafe. TYPE_TEXT also
calls a configured text-model API. These calls may be billed and transmit observed
page content. This is NOT part of Buildme's free/keyless default. No OpenRouter,
OpenAI or other text provider is silently selected by Buildme; configure the desired
JEV-compatible text provider outside chat if typing is authorized.

The operator must explicitly authorize each paid scenario via `--allow-paid`.
Installing JEV or selecting it in the brief does not authorize API consumption.
The regular installer does not install JEV; no keys, accounts, credits or provider
calls are created by the optional install. The default workflow remains keyless.

## Optional installation

From a Buildme checkout:

```bash
bash scripts/install.sh --with-jev
```

This retains normal Agent-Reach/skill installation and additionally creates a
managed Python 3.12 venv at `~/.agents/tools/jev-ultrafast/venv`, installing the
pinned upstream archive and its dependencies. uv can download Python 3.12 when
needed. It does not start Chrome, run demos or make model calls. An unmanaged
existing target is preserved and reported as an error.

Offline readiness check (macOS/Linux):

```bash
~/.agents/tools/jev-ultrafast/venv/bin/python   ~/.agents/skills/buildme/scripts/jev_qa.py --doctor
```

On Windows, use the venv's `Scripts/python.exe`. The doctor reads dependency/source
metadata only; it does not read keys, connect to a browser or call a model. Read
upstream Browser Harness connection documentation and use its doctor in a dedicated
test Chrome profile. The library creates a tab in the connected existing profile;
Buildme cannot independently prove that the profile is isolated.

## Scenario and execution contract

Copy [the scenario template](../templates/jev-scenario.json). Agent 0 and Agent 8
freeze its goal, disposable test URL, permitted origins, synthetic data, supported
features, action/decision budgets and independent outcome checks before running.
Use [the local fixture](../templates/jev-fixture.html) for a harmless first scenario.
Confirm the dedicated test profile in the scenario only after actually configuring it.

The scenario must declare test_environment and dedicated_test_profile true. Those
are operator assertions, not verified isolation. Use only disposable local/staging
apps and synthetic data. Do not use a production Chrome profile or tasks that buy,
book, send messages, delete real data or affect third parties. Origin checks detect
unexpected navigation; they are not a browser/network side-effect sandbox.

Configure TYPESAFE_API_KEY outside chat. If allow_typing is true, also configure
TEXT_MODEL_API_KEY, TEXT_MODEL_BASE_URL and TEXT_MODEL explicitly. The adapter
requires a named provider endpoint/model instead of silently using upstream defaults;
use HTTPS except for a local loopback model endpoint.
Buildme reads credentials only after --allow-paid, never prints or persists them,
and never provisions a provider account. Do not put secrets in scenario JSON.

```bash
~/.agents/tools/jev-ultrafast/venv/bin/python   ~/.agents/skills/buildme/scripts/jev_qa.py   --scenario .buildme/qa/jev/scenario.json   --output .buildme/qa/jev/report.json --allow-paid
```

Without --allow-paid, it returns BLOCKED before dependency import, browser actions
or key reads. It persists a scenario hash, counters, check results and sanitized failure stages,
not raw DOM snapshots, provider requests, generated text, screenshots or traces.
A decision/action budget is not a dollar limit: upstream retries/text calls can
increase request counts. Raw upstream traces should never be committed.

## Agent handoff and independent verification

Agent 8 owns scenario execution and JEV journey findings; Agent 0 schedules it only
when explicitly selected and permitted. Agent 15 discovers relevant APIs/examples;
Agent 11 compares approaches under research-first Rule 1 when a feature is unfamiliar.
Agent 4 provides journey criteria. Agents 10/12 retain the normal free browser
checks, accessibility, mobile matrix and screenshots. No new numbered agent is added.

The JEV choice DONE is not PASS. The adapter evaluates separate, code-owned checks
against the actual page (text, URL path, selector existence and field values), with
scenario values serialized as data, never executable code. A wrong outcome is FAIL;
missing setup, exhausted budgets, unsupported behavior or execution errors are
BLOCKED. A journey PASS still leaves overall_qa_status BLOCKED: the orchestrator
must combine it with required normal QA evidence before marking the build complete.

Send reproduction steps and failed checks to the responsible implementation worker,
then rerun the same scenario/checks after its fix. Existing two-round limits apply;
unresolved mandatory failures stay FAIL/BLOCKED. Missing paid authorization is not
a failure of the free workflow: use deterministic Playwright for the required journey.

## Known limits and fallbacks

The pinned MVP handles common HTML/ARIA controls, not the full accessible-name spec.
Shadow roots, frames, canvas, uploads, pop-up tabs, nested scrolling and arbitrary
keyboard widgets are unsupported. JEV's browser defaults to desktop 1120×780; its
scroll coordinates are desktop-specific. Do not count it as mobile coverage.
Use the existing browser worker for unsupported controls and mobile/viewports.
Do not transfer upstream's single-task timing claims to Buildme or promise speed,
cost savings, general reliability, accessibility or performance from a JEV run.
