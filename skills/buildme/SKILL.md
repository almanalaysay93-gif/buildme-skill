---
name: buildme
description: "Activates when the user types /Buildme, /buildme, or asks to build a web app using the multi-agent build ensemble. Runs reference analysis, Grill Me discovery, coordinates specialized subagents (orchestration, references, design, taste, a11y, motion, copy, llms.txt, anti-slop, bug hunting, perf/a11y, token snapshots, post-launch monitoring) plus Design Arena, conditional ADK building (Agent 14) and competitor/repository discovery (Agent 15) for in-product AI agents, to build high-craft, AI-discoverable, bug-free UIs. Free to run: no API keys or paid services. Not for a standalone one-screen design bake-off (use design-arena) or for adding an AI agent to an existing product on its own (use adk-agent-builder)."
metadata:
  triggers: /Buildme, /buildme, buildme, 5 agent build, build with design ensemble, 10 agent build, 13 agent build
  slash_command: /Buildme
---

# 🚀 BuildMe: Design & Development Orchestrator (Agents 0–15) (v4)

The **BuildMe** skill orchestrates a high-craft frontend development workflow powered by **16 numbered roles (Agents 0–15) plus optional Design Arena**.

Before any code is generated, BuildMe runs a **Grill Me** discovery interview to understand your vision, aesthetic preferences, tech stack, and specs. It then dispatches the ensemble across 6 phases — preflight analysis, design, build, synthesis, quality gates, and AI discoverability — with a Master Orchestrator coordinating every dispatch, versioned design snapshots, and an optional Design Arena mode when direction is uncertain.

---

## 📋 Workflow Execution Phasing

```
[Phase 0: Orchestration Setup] ➔ [Phase 1: Preflight (Reference Analysis)] ➔ [Phase 2: Grill Me Discovery]
➔ [Phase 3: Agent Dispatch] ➔ [Phase 4: Integration & Craft Synthesis]
➔ [Phase 5: Quality Gates (Anti-Slop + Bug Hunt + Perf/A11y)] ➔ [Phase 6: AI Discoverability (llms.txt)]
➔ [Post-Deploy: Live Monitoring]
```

> **Zero-cost rule**: BuildMe is free to run. No API keys, no paid services, no accounts. Every agent uses the free tools listed in [the zero-cost policy](references/zero-cost.md); a task that would need a paid service is marked "not run" and given a free alternative.

> **Optional branch**: between Phases 2 and 3, run the **Design Arena** (bake-off mode) when the visual direction is uncertain — see `design-arena/SKILL.md`.

---

## Prerequisites: companion skills

Agents 1–5 need these skills installed next to `buildme`: `impeccable-director`, `frontend-architect`, `taste-specialist`, `ui-ux-auditor` and `motion-specialist`. They ship in this repo. Install them with `bash scripts/install.sh` from a clone of the repo. Before Phase 3, confirm each one is present (its `SKILL.md` exists in the shared skills folder). If one is missing, stop, name the missing skill and ask the user to install it. Do not dispatch Agents 1–5 without them.

## Phase 0: Orchestration Setup

Run **Agent 0 (Master Orchestrator)** per `master-orchestrator/SKILL.md` *before anything else*:

1. Decompose the brief into non-overlapping work units with single owners and explicit contracts.
2. Write the first checkpoint to `ORCHESTRATOR.md` (phase, decisions, files, next dispatches).
3. Set per-agent token budgets (≤ 20% of session each) and max 2 revision rounds per agent.
4. Define the tiebreaker hierarchy for conflicts: user brief → anti-slop rule → cited principle → ask user.

---

## Phase 1: Seed brief and research preflight

Ask the seed questions in [the full-build question bank](references/discovery-questions.md):
product/job, audience, platform, category/region and constraints. Reuse known answers.
Initialize [BUILD_BRIEF.md](templates/BUILD_BRIEF.md).

Run Agent 15 per [competitor-researcher/SKILL.md](competitor-researcher/SKILL.md) to
discover competitors, websites and public repos using [available research tools](references/research-tools.md).
Agent 15 qualifies sources; Agent 11 then deep-analyzes the best three references
and writes REFERENCES.md. Never duplicate discovery or fabricate observations.
If research is declined, record both roles' dispositions and use known material.

Agent 0 coordinates this preflight. Only research dispatch is allowed before
brief approval; implementation agents wait for Phase 2 confirmation.

---

## Phase 2: Full-build Grill Me and activation review

Read [all 41 questions in 12 groups](references/discovery-questions.md). Ask rounds
of 3–6 related questions covering product/platform, market, users/journeys,
visuals/content, data/backend/auth, integrations/payments, AI, mobile/native/offline,
motion, accessibility/performance, discoverability/privacy, testing and delivery.
Reuse supplied answers and research. Give conditional topics a not-applicable
reason instead of forcing unnecessary features.

Write BUILD_BRIEF.md using [the template](templates/BUILD_BRIEF.md). Include screens,
flows, stack/platform, scope, data/API contracts, implementation owners, acceptance
evidence and an activation matrix assessing every Agent 0–15. Activate applicable
roles; defer monitoring until deployment and Agent 14 unless in-product AI is needed.
Record Design Arena selection and blocked/not-applicable roles with reasons.
Do not invent AI, public SEO or animation solely to fill the roster.

Backend/native/offline needs require named host implementation owners, toolchains
and platform-specific validation. Frontend specialty roles alone do not implement
those capabilities. Identify gaps and agree scope before promising completion.

Present the Design Read, brief, activation matrix, unresolved choices and acceptance
plan. Obtain confirmation before Phase 3 implementation. Existing explicit approval
for that same scope counts; do not restart the interview.

---

## Phase 3: Agent Dispatch

Use the host's actual delegation tools, or execute roles sequentially if unavailable.
The prompts below are contract examples, not literal API arguments. Run only
independent work concurrently and follow the approved activation matrix:

```json
[
  {
    "TypeName": "self",
    "Role": "Agent 1: Impeccable Design Director",
    "Prompt": "You are Agent 1 (Impeccable Design Director). Read `.../skills/impeccable-director/SKILL.md` (bundled; if the optional upstream `impeccable` skill is installed, also read `.../skills/impeccable/SKILL.md`). Initialize design context (PRODUCT.md and DESIGN.md), run anti-pattern scans against the 59 deterministic detector rules, enforce craft floor standards, and audit visual hierarchy and identity."
  },
  {
    "TypeName": "self",
    "Role": "Agent 2: Lead Frontend Architect",
    "Prompt": "You are Agent 2 (Lead Frontend Architect). Read `.../skills/frontend-architect/SKILL.md` (bundled; if the optional upstream `frontend-design` skill is installed, also read `.../skills/frontend-design/SKILL.md`). Establish the core CSS design system, typography scale, custom OKLCH/HSL color palette, grid layout architecture, responsive container rules, and base UI component structure. Source all icons from the bundled Material Symbols set in `.../skills/buildme/assets/icons/` (see `.../skills/buildme/references/icons.md`)."
  },
  {
    "TypeName": "self",
    "Role": "Agent 3: Anti-Slop Taste Specialist",
    "Prompt": "You are Agent 3 (Anti-Slop Taste Specialist). Read `.../skills/taste-specialist/SKILL.md` (bundled; if the optional upstream `taste-skill` is installed, also read `.../skills/taste-skill/SKILL.md`). Enforce anti-default discipline (eliminating generic AI purple gradients, slate card grids, and cookie-cutter layouts). Apply contextual vibe alignment and high-taste visual decisions based on the project brief."
  },
  {
    "TypeName": "self",
    "Role": "Agent 4: UI/UX & A11y Auditor",
    "Prompt": "You are Agent 4 (UI/UX & A11y Auditor). Read `.../skills/ui-ux-auditor/SKILL.md` (bundled; if the optional upstream `ui-ux-pro-max` is installed, also read `.../skills/ui-ux-pro-max/SKILL.md`). Audit component interaction states (hover, active, focus, disabled, loading, empty, error), touch target sizing, contrast ratios, keyboard navigation, cognitive load reduction, and user flow friction points."
  },
  {
    "TypeName": "self",
    "Role": "Agent 5: Emil's Motion & Animation Specialist",
    "Prompt": "You are Agent 5 (Emil's Motion & Animation Specialist). Read `.../skills/motion-specialist/SKILL.md` (bundled; if the optional upstream `emil-design-eng` skill is installed, also read `.../skills/emil-design-eng/SKILL.md` and its references `apple-design`, `review-animations`, `animation-vocabulary` from `emilkowalski/skills`). Implement buttery-smooth CSS/Framer motion transitions, fluid spring physics, gesture affordances, and micro-interaction polish."
  },
  {
    "TypeName": "self",
    "Role": "Agent 12: Design Token Snapshotter",
    "Prompt": "You are Agent 12 (Design Token Snapshotter). Read `.../skills/buildme/token-snapshotter/SKILL.md`. Take versioned snapshots at each trigger: after the design system lands (snap-001), after arena-winner application, after every quality-gate fix round, after copy lands, and pre-deploy (snap-final). Each snapshot: diffable design.md tokens, component token bindings, consistent-viewport screenshots (1440 + 390), and a delta.md vs the previous snapshot. Run drift guard checks and provide diffs on demand."
  },
  {
    "TypeName": "self",
    "Role": "Agent 13: Post-Launch Monitor",
    "Prompt": "You are Agent 13 (Post-Launch Monitor). Read `.../skills/buildme/post-launch-monitor/SKILL.md`. After deployment: verify deploy integrity (live URL, no 404s, llms.txt serving byte-identical to repo, robots.txt, sitemap), run live Lighthouse against budgets, baseline AI discoverability exposure (record observed facts vs a saved baseline), and write monitor/MONITOR.md. Report observations only — never promise rankings."
  },
  {
    "TypeName": "self",
    "Role": "Agent 6: AI Discoverability & llms.txt Specialist",
    "Prompt": "You are Agent 6 (AI Discoverability & llms.txt Specialist). Read `.../skills/buildme/llm-txt-skill/SKILL.md`. In Phase 6, after the Phase 5 quality gates pass: generate a spec-compliant llms.txt (and llms-full.txt if needed) at public/llms.txt so AI assistants (ChatGPT, Claude, Perplexity) can correctly understand and recommend the business/product. Derive all content from PRODUCT.md and final site content; self-verify against the checklist."
  },
  {
    "TypeName": "self",
    "Role": "Agent 7: Anti-Slop Enforcer",
    "Prompt": "You are Agent 7 (Anti-Slop Enforcer). Read `.../skills/buildme/anti-slop-enforcer/SKILL.md`. After Phase 3: run all 13 deterministic slop detectors (V1-V6 visual, C1-C4 copy, M1-M3 motion) on the built output, prescribe a concrete replacement for every violation, and gate the build: zero block-severity violations to pass. Report status per detector with evidence."
  },
  {
    "TypeName": "self",
    "Role": "Agent 8: Bug Hunter & Fixer",
    "Prompt": "You are Agent 8 (Bug Hunter & Fixer). Read `.../skills/buildme/bug-hunter/SKILL.md`. After Phase 3: run the full hunt checklist (console/build errors, responsive 320-1440px, keyboard-only walkthrough, contrast, state edge cases), reproduce every bug before fixing, fix root causes with regression guards, re-run the repro to verify, and attach before/after evidence. Gate: zero block + zero major bugs."
  },
  {
    "TypeName": "self",
    "Role": "Agent 9: Content & Copy Voice Specialist",
    "Prompt": "You are Agent 9 (Content & Copy Voice Specialist). Read `.../skills/buildme/content-voice/SKILL.md`. Run early (after Grill Me): write VOICE.md (voice rails, banned words, proof-point inventory), then write all site copy — headlines, CTAs, microcopy, error states, alt text, SEO meta — concrete, proof-backed, zero banned buzzwords. Grep-verify zero banned words before delivery."
  },
  {
    "TypeName": "self",
    "Role": "Agent 10: Performance & Accessibility Auditor",
    "Prompt": "You are Agent 10 (Performance & Accessibility Auditor). Read `.../skills/buildme/perf-a11y-auditor/SKILL.md`. After Phase 3: run Lighthouse (2 runs, worst wins) and the keyboard/screen-reader/honesty passes against the fixed budgets (LCP<2.5s, CLS<0.1, INP<200ms, bundle<250KB gz, contrast 4.5:1, touch 44px). Every finding cites its source (WCAG 2.2, Web Vitals, Rams). Gate: zero block findings."
  },
  {
    "TypeName": "self",
    "Role": "Agent 14: ADK Agent Builder (conditional)",
    "Prompt": "You are Agent 14 (ADK Agent Builder). Dispatch ONLY when the brief needs an AI agent inside the product (assistant, chat, tool-using agent, multi-step AI workflow); otherwise report 'not required'. Read `.../skills/buildme/adk-agent-builder/SKILL.md`. Build the agent in `agent/` with google-adk (LlmAgent, tools, Workflow) on a free local Ollama model via LiteLlm (no API key, no hosted model), write `AGENT_NOTES.md`, and pass that skill's gates: offline construction check, offline tool tests (`python -m pytest -q agent/tests`), acceptance runs on the local model (`adk run agent ...`), and a no-keys check. If Ollama is not installed, mark the acceptance runs 'not run', never 'passed', and never fall back to a hosted model. Set a call limit with RunConfig(max_llm_calls=N)."
  }
]
```

**Dependency order (orchestrator enforces):**
- **Preflight**: Agent 15 discovers from seed answers; Agent 11 deep-analyzes the shortlist. Both feed Grill Me before implementation.
- **Early (before build)**: Agent 9 (copy) and Agents 1–3 (design system) feed the build.
- **Build**: Agent 2 + Agent 5 (parallel, token vs motion work units).
- **Conditional (in-product AI agent only)**: Agent 14 (ADK) runs in parallel with Agent 2 after Agents 1–3 and 9 are done. It owns only `agent/`, so it does not overlap the frontend work units. Its gates run before Agent 7.
- **Late gates (after build)**: Agents 7, 8, 10 (run in this order — slop → bugs → perf/a11y).
- **Final**: Agent 6 (llms.txt) on the verified, passing build.

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

## Phase 5: Quality Gates (Anti-Slop + Bug Hunt + Perf/A11y)

Run **Agents 7, 8, 10** as sequential gates after the build:

1. **Agent 7** — all detectors pass (zero blocks); exemptions only as `exempt-by-brief` with reasons.
2. **Agent 8** — zero block + major bugs; each fix verified by its own reproduction re-run.
3. **Agent 10** — all metric budgets hit; keyboard + screen-reader + honesty passes complete.

Only after all three gates pass does the build advance to Phase 6.

---

## Phase 6: AI Discoverability (`llms.txt`)

Run **Agent 6** as the final gate, after the site passes all quality gates:

1. **Generate `public/llms.txt`** per `llm-txt-skill/SKILL.md`, grounded strictly in `PRODUCT.md` and final site content.
2. **Verify** the file builds into the deploy output (`dist/llms.txt`) and the self-verify checklist passes.
3. **Confirm discoverability keywords** are present (product category + location + intent), so AI assistants can recommend the business for free.

---

## 🏟️ Optional: Design Arena Mode

When the visual direction is uncertain or the current design is a local maximum, run the **Design Arena** between Phases 2 and 3: 2–4 agents each redesign **one screen** on informed and/or blind tracks; the user judges a gallery; the winner's apply-plan ships. Full protocol: `design-arena/SKILL.md`. Warn the user of token cost before spawning.

---

## 🛠️ Skill Ensemble Reference (Agents 0–15)

| Agent | Assigned Skill | Location | Key Function |
|---|---|---|---|
| **Agent 0** | **Master Orchestrator** | [`master-orchestrator/SKILL.md`](master-orchestrator/SKILL.md) | Plan decomposition, dispatch contracts, token budgets, conflict resolution, session checkpointing |
| **Agent 1** | **Impeccable** | [`impeccable/SKILL.md`](https://github.com/pbakaus/impeccable) | `PRODUCT.md` / `DESIGN.md` setup, 59 anti-pattern rules, craft floor & polish |
| **Agent 2** | **Frontend Design** | [`frontend-design/SKILL.md`](https://github.com/anthropics/skills) | Color palettes, typography scale, CSS tokens & grid architecture |
| **Agent 3** | **Taste Skill** | [`taste-skill/SKILL.md`](https://github.com/Leonxlnx/taste-skill) | Brief inference, anti-slop discipline, anti-default styling |
| **Agent 4** | **UI UX Pro Max** | [`ui-ux-pro-max/SKILL.md`](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | Component state audit, accessibility (a11y), UX friction & touch targets |
| **Agent 5** | **Emil's Skills** | [`emil-design-eng/SKILL.md`](https://github.com/emilkowalski/skills) | Fluid animations, spring physics, motion vocabulary & micro-interactions |
| **Agent 6** | **AI Discoverability (llms.txt)** | [`llm-txt-skill/SKILL.md`](llm-txt-skill/SKILL.md) | `llms.txt` / `llms-full.txt` generation so AI assistants can read and recommend the site |
| **Agent 7** | **Anti-Slop Enforcer** | [`anti-slop-enforcer/SKILL.md`](anti-slop-enforcer/SKILL.md) | 13 deterministic slop detectors (visual, copy, motion) with veto gate |
| **Agent 8** | **Bug Hunter & Fixer** | [`bug-hunter/SKILL.md`](bug-hunter/SKILL.md) | Reproduce → fix → verified-fix loop; responsive, a11y, state edge cases; regression guards |
| **Agent 9** | **Content & Copy Voice** | [`content-voice/SKILL.md`](content-voice/SKILL.md) | VOICE.md, distinctive brand copy, SEO meta, zero banned buzzwords |
| **Agent 10** | **Perf & A11y Auditor** | [`perf-a11y-auditor/SKILL.md`](perf-a11y-auditor/SKILL.md) | Web Vitals budgets, WCAG 2.2 AA, keyboard/screen-reader passes, Rams honesty audit |
| **Agent 11** | **Reference Analyzer** | [`reference-analyzer/SKILL.md`](reference-analyzer/SKILL.md) | Pre-Grill Me tear-down of 2–3 reference/competitor sites → Steal/Beat/Avoid brief |
| **Agent 12** | **Token Snapshotter** | [`token-snapshotter/SKILL.md`](token-snapshotter/SKILL.md) | Versioned, diffable design-system snapshots at every phase trigger + drift guard |
| **Agent 13** | **Post-Launch Monitor** | [`post-launch-monitor/SKILL.md`](post-launch-monitor/SKILL.md) | Live deploy verification, llms.txt checksum, live Lighthouse, AI-discoverability baseline |
| **Agent 14** (conditional) | **ADK Agent Builder** | [`adk-agent-builder/SKILL.md`](adk-agent-builder/SKILL.md) | In-product AI agent with Google ADK (LlmAgent, tools, Workflow graphs), tests and run gates; runs only when the brief needs an agent |
| **Agent 15** | **Competitor & Repository Researcher** | [`competitor-researcher/SKILL.md`](competitor-researcher/SKILL.md) | Discovers competitors, websites and repos; routes available Agent-Reach/OpenComputer/BrowserAct and supplies Agent 11 a cited shortlist |
| **Feature** | **Design Arena** | [`design-arena/SKILL.md`](design-arena/SKILL.md) | Informed vs blind design bake-off; user judges, winner ships |

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
