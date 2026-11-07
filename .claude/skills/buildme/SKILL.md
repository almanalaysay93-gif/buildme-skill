---
name: buildme
description: "Activates when the user types /Buildme, /buildme, or asks to build a web app using the multi-agent build ensemble. Runs reference analysis, Grill Me discovery, coordinates specialized subagents (orchestration, references, design, taste, a11y, motion, copy, llms.txt, anti-slop, bug hunting, perf/a11y, token snapshots, planning author/reviewer, observability, security, architecture, state/data, caching/offline) plus Design Arena, conditional ADK building (Agent 14) and competitor/repository discovery (Agent 15) for in-product AI agents, to build high-craft, AI-discoverable, bug-free UIs. Free local workflow using Agent Desktop and specialized web audits. Not for a standalone one-screen design bake-off (use design-arena) or for adding an AI agent to an existing product on its own (use adk-agent-builder)."
metadata:
  triggers: /Buildme, /buildme, buildme, 5 agent build, build with design ensemble, 10 agent build, 13 agent build
  slash_command: /Buildme
---

# 🚀 BuildMe: Design & Development Orchestrator (Agents 0–22) (v5)

The **BuildMe** skill orchestrates a high-craft frontend development workflow powered by **23 numbered roles (Agents 0–22) plus optional Design Arena**.

Before any code is generated, BuildMe runs a **Grill Me** discovery interview to understand your vision, aesthetic preferences, tech stack, and specs. It then dispatches the ensemble across 6 phases — preflight analysis, design, build, synthesis, quality gates, and AI discoverability — with a Master Orchestrator coordinating every dispatch, versioned design snapshots, and an optional Design Arena mode when direction is uncertain.

---

## 📋 Workflow Execution Phasing

```
[Phase 0: Orchestration Setup] ➔ [Phase 1: Preflight (Reference Analysis)] ➔ [Phase 2: Grill Me Discovery]
➔ [Phase 2.5: Markdown Planning Gate] ➔ [Phase 3: Agent Dispatch] ➔ [Phase 4: Integration & Craft Synthesis]
➔ [Phase 5: Final Gate Revalidation] ➔ [Phase 6: SEO/Discoverability Revalidation]
➔ [Post-Deploy: Live Monitoring]
```

> **Full dispatch rule (every invocation)**: dispatch every agent (0–13, 15–22) and every phase this file defines, in the order and waves it specifies, through the Agent tool. Do not decide on your own that an agent, workflow phase, or quality gate is unnecessary, redundant, or already covered. Each one must end with its output file or result, or with a BLOCKED entry naming the missing dependency and its fix. Agent 14 and Design Arena run only when their stated trigger is met by the confirmed brief, and that decision is recorded with the brief's wording. Skips are allowed only for user-declined optional companions, recorded with the user's answer. Concurrency limits mean waves, not dropped agents.

> **Zero-cost default**: BuildMe uses local Agent Desktop for UI control and specialized web audits, without additional API keys, paid services or accounts. Every agent uses the free tools listed in [the zero-cost policy](references/zero-cost.md); a task that would need a paid service is marked "not run" and given a free alternative.

> **Optional branch**: between Phases 2 and 3, run the **Design Arena** (bake-off mode) when the visual direction is uncertain — see `design-arena/SKILL.md`.

---

## Prerequisites: companion skills

Agents 1–5 need these skills installed next to `buildme`: `impeccable-director`, `frontend-architect`, `taste-specialist`, `ui-ux-auditor` and `motion-specialist`. They ship in this repo. Install them with `bash scripts/install.sh` from a clone of the repo. Before Phase 3, confirm each one is present (its `SKILL.md` exists in the shared skills folder). If one is missing, stop, name the missing skill and ask the user to install it. Do not dispatch Agents 1–5 without them.

**Optional richer companions** (read by Agents 2–5 when present; `scripts/install.sh` reports which are found): `frontend-design`, `taste-skill`, `ui-ux-pro-max`, `impeccable`, `emil-design-eng`, and motion/animation skills `motion-design-lottie` and `gsap-*`. Missing optional companions never block the build; the agent notes that it worked from the bundled skill.

**Browser QA runner (free):** Agents 8, 10 and 12 use the bundled `scripts/browser-qa.mjs` (Playwright + local Chromium) for screenshots, console/network errors, overflow and keyboard focus. Setup: [browser QA runner](references/browser-qa.md).

Agent-Reach and its upstream skill are also required research dependencies.
`bash scripts/install.sh` installs both the ensemble and Agent-Reach. Confirm
`agent-reach version`, `agent-reach skill` and `agent-reach channels` succeed before
claiming research readiness. Skill-only installation does not run this bootstrap.
See [research tools](references/research-tools.md) for public/keyless operation.

## Phase 0: Orchestration Setup

Run **Agent 0 (Master Orchestrator)** per `master-orchestrator/SKILL.md` *before anything else*:

1. Apply **Rule 1**: for every unfamiliar feature, delegate GitHub discovery to Agent 15 and approach comparison to Agent 11, then record the decision before implementation. Follow [the research-first protocol](references/research-first.md).
2. Dispatch Agent 21 for the initial repository scan and provisional project_context.md; Agent 0 records paths and evidence. Final document authoring/review follows Grill Me in Phase 2.5.
3. Write the first checkpoint to `ORCHESTRATOR.md` (phase, decisions, files, next dispatches).
4. Set per-agent token budgets (≤ 20% of session each) and max 2 revision rounds per agent.
5. Apply the project authority chain: constitution.md -> spec.md -> plan.md -> tasks.md, subject to host instructions and explicit user-authorized amendments. Resolve conflicts before affected implementation.

---

## Phase 1: Seed brief and research preflight

Start with 10 unanswered questions from [the full-build question bank](references/discovery-questions.md),
including the seed product/job, audience, platform, category/region and constraints.
Wait for answers before research or the next round. Use fewer only if fewer than
10 unanswered, relevant questions remain. Reuse known answers.
Initialize [BUILD_BRIEF.md](templates/BUILD_BRIEF.md).

Run Agent 15 per [competitor-researcher/SKILL.md](../competitor-researcher/SKILL.md) to
discover competitors, websites and public repos using [available research tools](references/research-tools.md).
Agent 15 qualifies sources; Agent 11 then deep-analyzes the best three references
and writes REFERENCES.md. Never duplicate discovery or fabricate observations.
If optional competitor research is declined, record both roles' dispositions and
use known material. Rule 1 still applies to unfamiliar implementation features.

Agent 0 coordinates this preflight. Research and document-only planning dispatch are allowed before final artifact
review; no application implementation starts before the Phase 2.5 gate is READY.

---

## Phase 2: Full-build Grill Me and activation review

Read [all 41 questions in 12 groups](references/discovery-questions.md). Ask exactly
10 unanswered, relevant questions per round and wait for answers before the next
round; use fewer only when fewer than 10 remain. Cover product/platform, market, users/journeys,
visuals/content, data/backend/auth, integrations/payments, AI, mobile/native/offline,
motion, accessibility/performance, discoverability/privacy, testing and delivery.
Reuse supplied answers and research. Give conditional topics a not-applicable
reason instead of forcing unnecessary features.

Write BUILD_BRIEF.md using [the template](templates/BUILD_BRIEF.md). Include screens,
flows, stack/platform, scope, data/API contracts, implementation owners, acceptance
evidence and an activation matrix assessing every Agent 0–22. Dispatch every core
role under the full dispatch rule; observability setup runs before launch, live monitoring waits for deployment,
and Agent 14 runs only when in-product AI is needed.
Record Design Arena selection and blocked/not-applicable roles with reasons.
Do not invent AI, public SEO or animation solely to fill the roster.

Backend/native/offline needs require named host implementation owners, toolchains
and platform-specific validation. Frontend specialty roles alone do not implement
those capabilities. Identify gaps and agree scope before promising completion.

Use the answers to complete the Markdown planning gate below. Present the Design
Read, brief, activation matrix and completed planning artifacts together before
Phase 3 implementation. Existing explicit approval for the same scope counts;
do not restart the interview or add repetitive confirmation rounds.

---

## Phase 2.5: Markdown Planning Gate

After Grill Me, follow [the Markdown planning contract](references/markdown-planning.md).
Create/update these five files from the repository audit, answers and references:

| Artifact | Required purpose | Bundled starting template |
| --- | --- | --- |
| project_context.md | Observed app identity, stack, libraries and current architecture | [project_context.md](templates/planning/project_context.md) |
| constitution.md | Non-negotiable project principles, authority and amendment rules | [constitution.md](templates/planning/constitution.md) |
| spec.md | Functional requirements, stories, acceptance and scope | [spec.md](templates/planning/spec.md) |
| plan.md | Technical strategy, schema fields/types, architecture, tools and compliance | [plan.md](templates/planning/plan.md) |
| tasks.md | Sequential T001-style owned tasks, dependencies and verification | [tasks.md](templates/planning/tasks.md) |

Agent 21 owns and writes the artifact set; Agent 22 independently reviews it.
Agent 0 coordinates them and owns the final readiness checkpoint. Reuse an
existing Spec Kit installation's actual canonical paths and map them in ORCHESTRATOR.md; otherwise use project-root files.
Run constitution -> specify -> plan -> tasks using real installed agent commands,
or the explicitly labeled bundled-template adapter. Never invent a speckit shell
command or claim native Spec Kit ran when it did not.

Planning-only specialist consultations produce rendering/architecture/data/cache/
security/operations contracts before the final plan/tasks. They do not authorize
application code, schema migrations or deployments. The existing Phase 3 order
remains unchanged for implementation and review dispatches.

**Author -> review -> repair:** dispatch [Agent 21: Markdown Planner](agents/planning-agent.md)
to build all five files, then [Agent 22: Planning Reviewer](agents/planning-reviewer.md)
to write [planning-review.md](templates/planning-review.md) against their actual
contents and repository evidence. Reviewer findings return through Agent 0 to
Agent 21 for fixes and Agent 22 for re-review. Neither self-approval nor reviewer
edits to source documents are allowed. Separate contexts are required when the
host supports delegation; disclose limited independence if roles run sequentially.

**Gate:** no implementation, including speckit implement, until Agent 22 has a
current PASS for the reviewed paths/revisions/fingerprints and all five substantive
artifacts are consistent, material unknowns resolved, constitution checks satisfied,
requirements traced to owned tasks and acceptance checks, and existing scope
approval recorded. Mark READY/BLOCKED with paths/revisions/evidence in
ORCHESTRATOR.md. Missing/stale review, FAIL or BLOCKED prevents implementation.
Material changes invalidate PASS and require renewed independent review; the
planning contract defines the narrow verified progress-only exception. Existing
two-round repair cap applies; unresolved failures remain blocked. Templates and
missing/unverified capabilities are not a pass.

---

## Phase 3: Agent Dispatch

Before each implementation dispatch, require Phase 2.5 READY backed by a current
Agent 22 PASS (or verified progress-only update recorded under the contract).
Attach the resolved five Markdown paths/revisions, constitution IDs, requirement/story IDs, plan
sections and Txxx task IDs; workers read these before editing. Also require the
Rule 1 search/comparison decision
for unfamiliar work in `research/FEATURE_APPROACHES.md`. Include Agent 15's discovery and Agent 11's independent comparison from
`research/FEATURE_REVIEWS.md` in the worker handoff. If unfamiliar details appear
mid-task, pause that portion and send it through both research agents before continuing.

Use the host's actual delegation tools (sequential role execution only if the host
has no delegation capability). Full dispatch applies to every existing core role
and all added specialist and planning roles. The following dependency sequence
is authoritative over legacy early-copy or slop-before-bug instructions in companion skills:

```text
Grill Me -> Reference Analysis -> planning-agent -> planning-reviewer -> frontend-architect (with rendering decision) -> architecture-agent -> state-data-agent -> caching-offline-agent -> motion-specialist (delegate to /designme if premium) -> security-agent -> bug-hunter -> perf-a11y-auditor -> observability-agent -> token-snapshotter -> llm-txt-skill -> content-voice -> anti-slop-enforcer
```

The seed-reference preflight may still happen in Phase 1, but after the full
Grill Me confirmation Agent 11 reconciles REFERENCES.md with the confirmed brief
before frontend-architect begins. Reuse evidence; do not duplicate web research.

| Order | Dispatch and contract | Required output / acceptance |
| --- | --- | --- |
| 1 | Grill Me (Agent 0) | Confirmed BUILD_BRIEF.md; 10 unanswered relevant questions per round; full activation matrix |
| 2 | Reference Analysis (Agents 15 then 11) | Cited research shortlist, REFERENCES.md and unfamiliar-feature decisions |
| 3 | [planning-agent](agents/planning-agent.md) (Agent 21; Phase 2.5) | Five substantive governing Markdown documents; sole author, no self-approval |
| 4 | [planning-reviewer](agents/planning-reviewer.md) (Agent 22; Phase 2.5) | planning-review.md; independent current PASS or repair/block |
| 5 | [frontend-architect](../frontend-architect/SKILL.md) (Agent 2; [update](agents/frontend-architect.md)) | rendering-decision.md first: route -> strategy -> why; no code before rendering and architecture decisions |
| 6 | [architecture-agent](agents/architecture-agent.md) (Agent 20) | architecture.md, architecture-rules.json; folder tree, boundaries, tokens; then Agent 2 implements tokens/base components within these rules |
| 7 | [state-data-agent](agents/state-data-agent.md) (Agent 17) | state-architecture.md and data layer; every fetch has loading/empty/error/retry and cancellation |
| 8 | [caching-offline-agent](agents/caching-offline-agent.md) (Agent 18) | caching-strategy.md, service-worker.js, precache manifest, offline fallback UI, sync queue |
| 9 | [motion-specialist](../motion-specialist/SKILL.md) (Agent 5) | Token-bound motion, reduced-motion fallback and measured checks; delegate premium visual/motion work to /designme when the brief requests premium craft |
| 10 | [security-agent](agents/security-agent.md) (Agent 16) | security-audit.md; all 20 checks, risk, exact patches and retests; FAIL blocks ship |
| 11 | [bug-hunter](../bug-hunter/SKILL.md) (Agent 8) | Reproduction -> owner fix -> independent retest; zero block/major bugs |
| 12 | [perf-a11y-auditor](../perf-a11y-auditor/SKILL.md) (Agent 10) | Mobile/browser, keyboard/screen-reader and measured performance evidence; no block findings |
| 13 | [observability-agent](agents/observability-agent.md) (Agent 19) | observability-setup.md, Sentry config, logging wrapper, dashboards.md, rollback-plan.md; verified ingestion, alerts and source maps |
| 14 | [token-snapshotter](../token-snapshotter/SKILL.md) (Agent 12) | Versioned tokens, bindings, screenshots at 1440/390 and drift delta |
| 15 | [llm-txt-skill](../llm-txt-skill/SKILL.md) (Agent 6) | SEO_AUDIT.md and truthful public llms.txt; private/native indexing exclusions require reasons |
| 16 | [content-voice](../content-voice/SKILL.md) (Agent 9) | VOICE.md, final proof-backed copy and metadata; reconcile Agent 6 artifacts after copy changes |
| 17 | [anti-slop-enforcer](../anti-slop-enforcer/SKILL.md) (Agent 7) | All 13 detectors plus architecture-rules.json checks; zero block violations |

**Preserve all existing roles:** Agent 0 coordinates throughout. The Phase 2.5
author/review dispatches above are reused when current; do not run a second
planning workflow merely because Phase 3 repeats their positions. Dispatch Agent 1
(Impeccable Director) to initialize PRODUCT.md / DESIGN.md after references and
before Agent 2; Agent 3 (Taste Specialist) reviews architecture/design decisions;
Agent 4 (UI/UX Auditor) reviews journeys/states during the data/offline/motion
handoffs before security. These are supporting checkpoints, not replacements for
any stage above. Their existing skill contracts still apply.

Agent 13 (Post-Launch Monitor) remains installed and is dispatched by Agent 19
as a compatibility child work unit for its existing live-integrity checklist and
monitor/MONITOR.md. Agent 19 replaces its top-level dispatch and owns monitoring
setup before ship. Before deployment, Agent 13 records BLOCKED awaiting authorized
live URL; this defers only live evidence, never pre-ship observability setup.
Agent 14 remains conditional for in-product AI, with sole ownership of agent/;
complete its local-model/no-keys gates before the security review. Design Arena
retains its confirmed-brief trigger. Never drop a core role due to concurrency
limits: queue non-overlapping work in waves.

For premium motion, /designme means premium craft, not a paid service. Delegate
through the installed designme skill, keep Agent 5 accountable for outputs, and
retain local/free tools. If the required skill is missing, mark that handoff
BLOCKED with the install remedy rather than silently skipping it.

All specialty and planning agents are bundled under agents/ and also registered as companion
skills by the installer. Their complete checklists and gates are mandatory.
Non-applicable individual capabilities need cited scope reasons; they do not
permit skipping an agent. Missing required tooling/evidence is BLOCKED.

**Implementation handoff:** reuse the Phase 2.5 rendering and architecture plans,
rechecking their current revisions before implementation; Agent 2 and named feature workers implement within them
before downstream QA. Single owners serialize shared files. Content lands in its
listed final stage; use approved brief text during implementation, then have
Agent 9 finalize it before ship. Token snapshots still run at existing intermediate triggers and
again after final copy/repair changes; the listed snapshot is the main checkpoint.

**Repair loop:** security -> bugs -> performance/a11y -> observability are evaluated
in this order; final anti-slop follows discoverability and content. Any FAIL or
BLOCKED mandatory check prevents ship. Agent 0 sends findings to the original
worker; the reviewer independently rechecks. Re-run security, bugs, perf/a11y,
observability, snapshots and SEO for affected code/content after later patches.
Reviewers also verify constitution/spec/plan/task compliance. New scope or material
discoveries update the five artifacts before further affected code. After the
existing two-round cap, leave unresolved gates FAIL/BLOCKED and escalate.

---

## Phase 4: Integration & Craft Synthesis

1. **Synthesize Subagent Outputs**:
   Combine the design system tokens, layout structure, anti-slop rules, UX state handoffs, and animation primitives into clean, production-ready code.
2. **Verify Execution**:
   - Ensure zero console errors or broken styling.
   - Verify layout responsiveness across desktop, tablet, and mobile viewports.
   - Test interaction states, contrast, and animation performance.
3. **Deliver Walkthrough & Summary**:
   Provide a clear summary of what was built, clickable file links, and key features.

---

## Phase 5: Final Gate Revalidation

Phase 3 establishes the authoritative dispatch order. After Phase 4 integration,
verify all artifacts still match the integrated build. Reuse unchanged evidence;
rerun affected reviews in their Phase 3 relative order (security, bug hunter,
perf/a11y, observability, token snapshot, llms.txt, content, final anti-slop).
Agent 7 checks architecture-rules.json against real source and built output,
including dependency boundaries and token use, as well as all 13 slop detectors.

Start primary GUI journeys with the Agent Desktop observe–act–verify contract.
For web artifacts also run `node ~/.agents/skills/buildme/scripts/browser-qa.mjs <url> .buildme/qa/<gate>`
for shared mobile/viewport screenshots, console/network and keyboard evidence.
NEED_SETUP or unavailable session/permissions means BLOCKED, never passed.
Performance reports distinguish lab checks from unmeasured field INP.

All required new-agent gates and existing bug, UX-law, security, accessibility,
architecture and craft gates must pass before ship. Monitoring setup is mandatory
before launch; live deployment checks wait for an authorized deployment.

---

## Phase 6: Free SEO and AI Discoverability Revalidation

Agent 6 first runs in the Phase 3 position above; this phase revalidates its
[free SEO protocol](references/free-seo.md) and SEO_AUDIT.md against final copy
and integrated artifacts. Do not use this phase to move the initial dispatch
after content or bypass the final anti-slop review. Check final canonical/sitemap,
rendered content, schema, llms.txt and exposure of private content; reuse Agent 10's
mobile evidence. Public content changes from Agent 9 must refresh Agent 6 outputs.
Private/native scope gets reasoned indexing exclusions while retaining other QA.

Agent 0 routes repairs to the original worker, then the reviewer rechecks affected
gates in Phase 3 order and Agent 7 signs off last. Missing required evidence and
unresolved mandatory failures block completion at the two-round revision cap.

---

## 🏟️ Optional: Design Arena Mode

When the visual direction is uncertain or the current design is a local maximum, run the **Design Arena** between Phases 2 and 3: 2–4 agents each redesign **one screen** on informed and/or blind tracks; the user judges a gallery; the winner's apply-plan ships. Full protocol: `design-arena/SKILL.md`. Warn the user of token cost before spawning.

---

## 🛠️ Skill Ensemble Reference (Agents 0–22)

| Agent | Assigned Skill | Location | Key Function |
|---|---|---|---|
| **Agent 0** | **Master Orchestrator** | [`master-orchestrator/SKILL.md`](../master-orchestrator/SKILL.md) | Plan decomposition, dispatch contracts, token budgets, conflict resolution, session checkpointing |
| **Agent 1** | **Impeccable** | [`impeccable/SKILL.md`](https://github.com/pbakaus/impeccable) | `PRODUCT.md` / `DESIGN.md` setup, 59 anti-pattern rules, craft floor & polish |
| **Agent 2** | **Frontend Design** | [`frontend-design/SKILL.md`](https://github.com/anthropics/skills) | Color palettes, typography scale, CSS tokens & grid architecture |
| **Agent 3** | **Taste Skill** | [`taste-skill/SKILL.md`](https://github.com/Leonxlnx/taste-skill) | Brief inference, anti-slop discipline, anti-default styling |
| **Agent 4** | **UI UX Pro Max** | [`ui-ux-pro-max/SKILL.md`](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | Component state audit, accessibility (a11y), UX friction & touch targets |
| **Agent 5** | **Emil's Skills** (+ `motion-design-lottie`, `gsap-*` when installed) | [`emil-design-eng/SKILL.md`](https://github.com/emilkowalski/skills) | Fluid animations, spring physics, motion vocabulary & micro-interactions; timing rules and GSAP tweens/timelines/ScrollTrigger |
| **Agent 6** | **AI Discoverability (llms.txt)** | [`llm-txt-skill/SKILL.md`](../llm-txt-skill/SKILL.md) | `llms.txt` / `llms-full.txt` generation so AI assistants can read and recommend the site |
| **Agent 7** | **Anti-Slop Enforcer** | [`anti-slop-enforcer/SKILL.md`](../anti-slop-enforcer/SKILL.md) | 13 deterministic slop detectors (visual, copy, motion) with veto gate |
| **Agent 8** | **Bug Hunter & Fixer** | [`bug-hunter/SKILL.md`](../bug-hunter/SKILL.md) | Reproduce → fix → verified-fix loop; responsive, a11y, state edge cases; regression guards |
| **Agent 9** | **Content & Copy Voice** | [`content-voice/SKILL.md`](../content-voice/SKILL.md) | VOICE.md, distinctive brand copy, SEO meta, zero banned buzzwords |
| **Agent 10** | **Perf & A11y Auditor** | [`perf-a11y-auditor/SKILL.md`](../perf-a11y-auditor/SKILL.md) | Web Vitals budgets, WCAG 2.2 AA, keyboard/screen-reader passes, Rams honesty audit |
| **Agent 11** | **Reference Analyzer** | [`reference-analyzer/SKILL.md`](../reference-analyzer/SKILL.md) | Pre-Grill Me tear-down of 2–3 reference/competitor sites → Steal/Beat/Avoid brief |
| **Agent 12** | **Token Snapshotter** | [`token-snapshotter/SKILL.md`](../token-snapshotter/SKILL.md) | Versioned, diffable design-system snapshots at every phase trigger + drift guard |
| **Agent 13** | **Post-Launch Monitor (compatibility child of Agent 19)** | [`post-launch-monitor/SKILL.md`](../post-launch-monitor/SKILL.md) | Live deploy verification, llms.txt checksum, live Lighthouse, AI-discoverability baseline |
| **Agent 14** (conditional) | **ADK Agent Builder** | [`adk-agent-builder/SKILL.md`](../adk-agent-builder/SKILL.md) | In-product AI agent with Google ADK (LlmAgent, tools, Workflow graphs), tests and run gates; runs only when the brief needs an agent |
| **Agent 15** | **Competitor & Repository Researcher** | [`competitor-researcher/SKILL.md`](../competitor-researcher/SKILL.md) | Discovers competitors, websites and repos; uses Agent-Reach and local-browser fallback and supplies Agent 11 a cited shortlist |
| **Agent 16** | **Security Gate** | [agents/security-agent.md](agents/security-agent.md) | 20 checks, exact patches, mandatory ship gate |
| **Agent 17** | **State + Data** | [agents/state-data-agent.md](agents/state-data-agent.md) | State ownership, fetch contracts, retry/cancellation |
| **Agent 18** | **Caching + Offline** | [agents/caching-offline-agent.md](agents/caching-offline-agent.md) | Versioned caches, offline fallback and safe sync |
| **Agent 19** | **Observability** | [agents/observability-agent.md](agents/observability-agent.md) | Sentry, alerting, source maps, tests, rollback; owns Agent 13 live work |
| **Agent 20** | **Architecture** | [agents/architecture-agent.md](agents/architecture-agent.md) | Modules, boundaries, tokens and machine-readable enforcement |
| **Agent 21** | **Markdown Planner / Author** | [agents/planning-agent.md](agents/planning-agent.md) | Writes and repairs the five governing files |
| **Agent 22** | **Independent Planning Reviewer** | [agents/planning-reviewer.md](agents/planning-reviewer.md) | Read-only source review; PASS/FAIL/BLOCKED gates implementation |
| **Feature** | **Design Arena** | [`design-arena/SKILL.md`](../design-arena/SKILL.md) | Informed vs blind design bake-off; user judges, winner ships |

---

## 📦 Upstream Skill Dependencies

Agents 1–5 run on the bundled skills (`impeccable-director`, `frontend-architect`, `taste-specialist`, `ui-ux-auditor`, `motion-specialist`), which work on a fresh install. The upstream skills below are optional richer versions; when installed, the agent reads them too. Canonical sources:

| Skill | Canonical Repo |
|---|---|
| impeccable | `github.com/pbakaus/impeccable` |
| frontend-design | `github.com/anthropics/skills` |
| taste-skill | `github.com/Leonxlnx/taste-skill` |
| ui-ux-pro-max | `github.com/nextlevelbuilder/ui-ux-pro-max-skill` |
| emil-design-eng (+ apple-design, review-animations, animation-vocabulary) | `github.com/emilkowalski/skills` |
| motion-design-lottie (LottieFiles motion-design skill; installed under this name so it does not collide with the Remotion `motion-design` skill) | `github.com/LottieFiles/motion-design-skill` |
| gsap-* (official GSAP skills) | installed in the shared folder; source not recorded in this repo |

## Superlite execution

Read the [Superlite execution adapter](references/superlite-integration.md) before
planning dispatch. It supplies request sizing, dependency tasks, ownership contracts,
targeted repairs and a fresh final review. The Master Orchestrator remains the sole
coordinator. Use the host's actual delegation tools (sequential roles if unavailable),
not a hard-coded `invoke_subagent` API. Existing discovery and quality gates apply.

## Mandatory UX laws

Before planning or building, read the complete [UX laws reference](references/ux-laws.md)
and [its workflow](references/ux-laws-workflow.md). Map all 14 laws in the plan and
include the relevant checks in every specialist handoff. After every build or
significant change, complete `UX_LAWS_AUDIT.md`, fix findings and re-audit before
completion. The audit is mandatory even when optional UX tools are skipped.
Unresolved violations or missing evidence block completion; existing repair caps apply.

## Icons

BuildMe bundles 58 Material Symbols icons (Outlined, 24px, Apache 2.0) in `assets/icons/`.
Read [the icon reference](references/icons.md) before adding any icon. Use the bundled
icons first, keep one icon style per product, make decorative icons hidden from assistive
technology, give icon-only controls an accessible name, and keep `LICENSE` and `NOTICE.md`
with the icons. Do not use third-party brand logos from the icon set.


## Primary UI tool: Agent Desktop

Use [Agent Desktop](references/agent-desktop.md) for the orchestration's browser/native
GUI control, with the host agent running observe–act–verify. The full installer
provisions the pinned CLI and its embedded skills without API keys or permission
prompts. Agent 0 freezes app/window scope and outcomes; Agent 8 executes and routes
failures back to the implementation owner. A missing graphical session/permission
blocks the GUI check. Independent outcome evidence is required; success envelopes
alone are insufficient. Existing Playwright/Lighthouse runners are specialized web
measurement tools, not the default GUI-control policy or proof of native app QA.
