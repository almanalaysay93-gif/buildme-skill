---
name: buildme
description: "Activates when the user types /Buildme, /buildme, or asks to build a web app using the 13-agent design ensemble. Runs reference analysis, Grill Me discovery, dispatches 13 specialized subagents (orchestration, references, design, taste, a11y, motion, copy, llms.txt, anti-slop, bug hunting, perf/a11y, token snapshots, post-launch monitoring) plus the optional Design Arena bake-off, to build high-craft, AI-discoverable, bug-free UIs."
metadata:
  triggers: /Buildme, /buildme, buildme, 5 agent build, build with design ensemble, 10 agent build, 13 agent build
  slash_command: /Buildme
---

# 🚀 BuildMe: 13-Agent Design & Development Orchestrator (v4)

The **BuildMe** skill orchestrates a high-craft frontend development workflow powered by **13 specialized subagents plus one optional feature mode**.

Before any code is generated, BuildMe runs a **Grill Me** discovery interview to understand your vision, aesthetic preferences, tech stack, and specs. It then dispatches the ensemble across 6 phases — preflight analysis, design, build, synthesis, quality gates, and AI discoverability — with a Master Orchestrator coordinating every dispatch, versioned design snapshots, and an optional Design Arena mode when direction is uncertain.

---

## 📋 Workflow Execution Phasing

```
[Phase 0: Orchestration Setup] ➔ [Phase 1: Preflight (Reference Analysis)] ➔ [Phase 2: Grill Me Discovery]
➔ [Phase 3: 13-Agent Dispatch] ➔ [Phase 4: Integration & Craft Synthesis]
➔ [Phase 5: Quality Gates (Anti-Slop + Bug Hunt + Perf/A11y)] ➔ [Phase 6: AI Discoverability (llms.txt)]
➔ [Post-Deploy: Live Monitoring]
```

> **Optional branch**: between Phases 2 and 3, run the **Design Arena** (bake-off mode) when the visual direction is uncertain — see `design-arena/SKILL.md`.

---

## Phase 0: Orchestration Setup

Run **Agent 0 (Master Orchestrator)** per `master-orchestrator/SKILL.md` *before anything else*:

1. Decompose the brief into non-overlapping work units with single owners and explicit contracts.
2. Write the first checkpoint to `ORCHESTRATOR.md` (phase, decisions, files, next dispatches).
3. Set per-agent token budgets (≤ 20% of session each) and max 2 revision rounds per agent.
4. Define the tiebreaker hierarchy for conflicts: user brief → anti-slop rule → cited principle → ask user.

---

## Phase 1: Interactive Alignment ("Grill Me")

> **CRITICAL RULE**: Do NOT start building or spawning subagents until Phase 1 is complete and requirements are confirmed.

1. **Conduct the Discovery Interview**:
   Ask the user 3 to 5 targeted questions (bullet points or concise text) covering:
   * **Product & Goal**: What specific application/feature are you building, and who is the primary target audience?
   * **Tech Stack**: What framework and styling tools do you prefer? (e.g. Vanilla HTML/CSS/JS, Vite + React, Next.js, Tailwind, etc.)
   * **Visual Vibe & Aesthetic**: What design language fits best? (e.g. *Linear-clean, Apple-fluid, Editorial/Minimalist, Neo-Brutalist, Soft/Tactile, High-energy Dark Tech, etc.*)
   * **Motion & Animation Level**: What level of motion do you want? (e.g. *Subtle micro-interactions, Fluid Apple-style spring physics, High-octane kinetic motion, or Calm/Static*)
   * **Core Scope & Priority**: What are the top 1-3 screens or components that must wow the user immediately?

2. **Formulate the Design Read**:
   Synthesize the user's answers into a single-line **Design Read**:
   > *"Reading this as: [Page/App Type] for [Audience] in a [Visual Vibe] language using [Tech Stack]."*

3. **Confirm & Proceed**:
   Obtain the user's confirmation before launching Phase 2.

---

## Phase 1: Preflight — Reference Analysis

Run **Agent 11 (Reference & Competitor Analyzer)** per `reference-analyzer/SKILL.md` when the user names reference sites or a market category:

1. Tear down 2–3 reference/competitor sites into per-site reference files (`references/`).
2. Synthesize one-page `REFERENCES.md`: **Steal / Beat / Avoid / sharper Grill Me questions**.
3. Pass the brief into Grill Me and every agent's context slice.

> Skip gracefully if the user has no references and declines SERP research.

---

## Phase 3: 13-Agent Dispatch

Launch subagents per their dependency contracts using `invoke_subagent`. Agents marked **(parallel)** can run concurrently; others are serialized by the orchestrator:

```json
[
  {
    "TypeName": "self",
    "Role": "Agent 1: Impeccable Design Director",
    "Prompt": "You are Agent 1 (Impeccable Design Director). Read `.../skills/impeccable/SKILL.md`. Initialize design context (PRODUCT.md and DESIGN.md), run anti-pattern scans against the 59 deterministic detector rules, enforce craft floor standards, and audit visual hierarchy and identity."
  },
  {
    "TypeName": "self",
    "Role": "Agent 2: Lead Frontend Architect",
    "Prompt": "You are Agent 2 (Lead Frontend Architect). Read `.../skills/frontend-design/SKILL.md`. Establish the core CSS design system, typography scale, custom OKLCH/HSL color palette, grid layout architecture, responsive container rules, and base UI component structure."
  },
  {
    "TypeName": "self",
    "Role": "Agent 3: Anti-Slop Taste Specialist",
    "Prompt": "You are Agent 3 (Anti-Slop Taste Specialist). Read `.../skills/taste-skill/SKILL.md`. Enforce anti-default discipline (eliminating generic AI purple gradients, slate card grids, and cookie-cutter layouts). Apply contextual vibe alignment and high-taste visual decisions based on the project brief."
  },
  {
    "TypeName": "self",
    "Role": "Agent 4: UI/UX & A11y Auditor",
    "Prompt": "You are Agent 4 (UI/UX & A11y Auditor). Read `.../skills/ui-ux-pro-max/SKILL.md`. Audit component interaction states (hover, active, focus, disabled, loading, empty, error), touch target sizing, contrast ratios, keyboard navigation, cognitive load reduction, and user flow friction points."
  },
  {
    "TypeName": "self",
    "Role": "Agent 5: Emil's Motion & Animation Specialist",
    "Prompt": "You are Agent 5 (Emil's Motion & Animation Specialist). Read `.../skills/emil-design-eng/SKILL.md` (and reference skills `apple-design`, `review-animations`, `animation-vocabulary` from `emilkowalski/skills`). Implement buttery-smooth CSS/Framer motion transitions, fluid spring physics, gesture affordances, and micro-interaction polish."
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
    "Prompt": "You are Agent 6 (AI Discoverability & llms.txt Specialist). Read `.../skills/buildme/llm-txt-skill/SKILL.md`. After Phase 3 synthesis: generate a spec-compliant llms.txt (and llms-full.txt if needed) at public/llms.txt so AI assistants (ChatGPT, Claude, Perplexity) can correctly understand and recommend the business/product. Derive all content from PRODUCT.md and final site content; self-verify against the checklist."
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
  }
]
```

**Dependency order (orchestrator enforces):**
- **Preflight**: Agent 11 (references) before Grill Me; its brief feeds every agent.
- **Early (before build)**: Agent 9 (copy) and Agents 1–3 (design system) feed the build.
- **Build**: Agent 2 + Agent 5 (parallel, token vs motion work units).
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

## 🛠️ The 10-Agent Skill Ensemble Reference

| Agent | Assigned Skill | Location | Key Function |
|---|---|---|---|
| **Agent 0** | **Master Orchestrator** | [`master-orchestrator/SKILL.md`](file:///C:/Users/Admin/.gemini/config/skills/buildme/master-orchestrator/SKILL.md) | Plan decomposition, dispatch contracts, token budgets, conflict resolution, session checkpointing |
| **Agent 1** | **Impeccable** | [`impeccable/SKILL.md`](file:///C:/Users/Admin/.gemini/config/skills/impeccable/SKILL.md) | `PRODUCT.md` / `DESIGN.md` setup, 59 anti-pattern rules, craft floor & polish |
| **Agent 2** | **Frontend Design** | [`frontend-design/SKILL.md`](file:///C:/Users/Admin/.gemini/config/skills/frontend-design/SKILL.md) | Color palettes, typography scale, CSS tokens & grid architecture |
| **Agent 3** | **Taste Skill** | [`taste-skill/SKILL.md`](file:///C:/Users/Admin/.gemini/config/skills/taste-skill/SKILL.md) | Brief inference, anti-slop discipline, anti-default styling |
| **Agent 4** | **UI UX Pro Max** | [`ui-ux-pro-max/SKILL.md`](file:///C:/Users/Admin/.gemini/config/skills/ui-ux-pro-max/SKILL.md) | Component state audit, accessibility (a11y), UX friction & touch targets |
| **Agent 5** | **Emil's Skills** | [`emil-design-eng/SKILL.md`](file:///C:/Users/Admin/.gemini/config/skills/emil-design-eng/SKILL.md) | Fluid animations, spring physics, motion vocabulary & micro-interactions |
| **Agent 6** | **AI Discoverability (llms.txt)** | [`llm-txt-skill/SKILL.md`](file:///C:/Users/Admin/.gemini/config/skills/buildme/llm-txt-skill/SKILL.md) | `llms.txt` / `llms-full.txt` generation so AI assistants can read and recommend the site |
| **Agent 7** | **Anti-Slop Enforcer** | [`anti-slop-enforcer/SKILL.md`](file:///C:/Users/Admin/.gemini/config/skills/buildme/anti-slop-enforcer/SKILL.md) | 13 deterministic slop detectors (visual, copy, motion) with veto gate |
| **Agent 8** | **Bug Hunter & Fixer** | [`bug-hunter/SKILL.md`](file:///C:/Users/Admin/.gemini/config/skills/buildme/bug-hunter/SKILL.md) | Reproduce → fix → verified-fix loop; responsive, a11y, state edge cases; regression guards |
| **Agent 9** | **Content & Copy Voice** | [`content-voice/SKILL.md`](file:///C:/Users/Admin/.gemini/config/skills/buildme/content-voice/SKILL.md) | VOICE.md, distinctive brand copy, SEO meta, zero banned buzzwords |
| **Agent 10** | **Perf & A11y Auditor** | [`perf-a11y-auditor/SKILL.md`](file:///C:/Users/Admin/.gemini/config/skills/buildme/perf-a11y-auditor/SKILL.md) | Web Vitals budgets, WCAG 2.2 AA, keyboard/screen-reader passes, Rams honesty audit |
| **Agent 11** | **Reference Analyzer** | [`reference-analyzer/SKILL.md`](file:///C:/Users/Admin/.gemini/config/skills/buildme/reference-analyzer/SKILL.md) | Pre-Grill Me tear-down of 2–3 reference/competitor sites → Steal/Beat/Avoid brief |
| **Agent 12** | **Token Snapshotter** | [`token-snapshotter/SKILL.md`](file:///C:/Users/Admin/.gemini/config/skills/buildme/token-snapshotter/SKILL.md) | Versioned, diffable design-system snapshots at every phase trigger + drift guard |
| **Agent 13** | **Post-Launch Monitor** | [`post-launch-monitor/SKILL.md`](file:///C:/Users/Admin/.gemini/config/skills/buildme/post-launch-monitor/SKILL.md) | Live deploy verification, llms.txt checksum, live Lighthouse, AI-discoverability baseline |
| **Feature** | **Design Arena** | [`design-arena/SKILL.md`](file:///C:/Users/Admin/.gemini/config/skills/buildme/design-arena/SKILL.md) | Informed vs blind design bake-off; user judges, winner ships |

---

## 📦 Upstream Skill Dependencies

The ensemble agents 1–5 consume externally installed skills. Keep them current per the README's "Keeping the Ensemble Up to Date" section. Canonical sources:

| Skill | Canonical Repo |
|---|---|
| impeccable | `github.com/pbakaus/impeccable` |
| frontend-design | `github.com/anthropics/skills` |
| taste-skill | `github.com/Leonxlnx/taste-skill` |
| ui-ux-pro-max | `github.com/nextlevelbuilder/ui-ux-pro-max-skill` |
| emil-design-eng (+ apple-design, review-animations, animation-vocabulary) | `github.com/emilkowalski/skills` |
