---
name: buildme
description: "Activates when the user types /Buildme, /buildme, or asks to build a web app using the 13-agent design ensemble. Runs reference analysis, Grill Me discovery, dispatches 13 specialized subagents (orchestration, references, design, taste, a11y, motion, copy, llms.txt, anti-slop, bug hunting, perf/a11y, token snapshots, post-launch monitoring) plus the optional Design Arena bake-off, to build high-craft, AI-discoverable, bug-free UIs."
metadata:
  triggers: /Buildme, /buildme, buildme, 13 agent build, build with design ensemble
  slash_command: /Buildme
---

# 🚀 BuildMe: 13-Agent Design & Development Orchestrator (v4)

The **BuildMe** skill orchestrates a high-craft frontend development workflow powered by **13 specialized subagents plus one optional feature mode**.

This file is the orchestrator. Agents 1–5 live in **external** skill repos. Agents 0 and 6–13 live under `skills/buildme/`. A single download of this repo will not register 13 separate CLI agents.

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

## Phase 2: Interactive Alignment ("Grill Me")

> **CRITICAL RULE**: Do NOT start building or spawning subagents until Grill Me is complete and requirements are confirmed.

1. **Conduct the Discovery Interview**:
   Ask the user 3 to 5 targeted questions covering:
   * **Product & Goal**
   * **Tech Stack**
   * **Visual Vibe & Aesthetic**
   * **Motion & Animation Level**
   * **Core Scope & Priority**

2. **Formulate the Design Read**:
   > *"Reading this as: [Page/App Type] for [Audience] in a [Visual Vibe] language using [Tech Stack]."*

3. **Confirm & Proceed** before launching dispatch.

---

## Phase 1: Preflight — Reference Analysis

Run **Agent 11** per `reference-analyzer/SKILL.md` when the user names reference sites or a market category. Skip if none.

---

## Phase 3: 13-Agent Dispatch

Launch subagents per their dependency contracts using `invoke_subagent`.

**Dependency order:**
- **Preflight**: Agent 11 before Grill Me.
- **Early**: Agent 9 and Agents 1–3 feed the build.
- **Build**: Agent 2 + Agent 5 (parallel).
- **Late gates**: Agents 7, 8, 10 (slop → bugs → perf/a11y).
- **Final**: Agent 6 on the passing build.
- **Snapshots / monitor**: Agents 12 and 13 at their triggers.

If an external skill (Agents 1–5) is missing, tell the user to run the install commands in the README instead of silently dropping to a 5-agent subset.

---

## Phase 4: Integration & Craft Synthesis

Combine design system tokens, layout, anti-slop rules, UX states, and animation primitives into production-ready code. Verify no console errors, responsive layout, interaction states, contrast, and animation performance.

---

## Phase 5: Quality Gates

Run **Agents 7, 8, 10** in order. All three must pass before Phase 6.

---

## Phase 6: AI Discoverability (`llms.txt`)

Run **Agent 6**. Generate `public/llms.txt` from `PRODUCT.md` and final site content.

---

## 🏟️ Optional: Design Arena Mode

When direction is uncertain, run `design-arena/SKILL.md` between Phases 2 and 3. Warn about token cost first.

---

## 🛠️ The 13-Agent Skill Ensemble Reference

| Agent | Assigned Skill | Location | Key Function |
|---|---|---|---|
| **Agent 0** | **Master Orchestrator** | `skills/buildme/master-orchestrator/SKILL.md` | Plan decomposition, contracts, budgets, checkpoints |
| **Agent 1** | **Impeccable** | external: `impeccable/SKILL.md` | PRODUCT.md / DESIGN.md, 59 anti-pattern rules |
| **Agent 2** | **Frontend Design** | external: `frontend-design/SKILL.md` | Tokens, type, color, grid |
| **Agent 3** | **Taste Skill** | external: `taste-skill/SKILL.md` | Anti-default styling |
| **Agent 4** | **UI UX Pro Max** | external: `ui-ux-pro-max/SKILL.md` | States, a11y, friction |
| **Agent 5** | **Emil's Skills** | external: `emil-design-eng/SKILL.md` | Motion, springs, micro-interactions |
| **Agent 6** | **AI Discoverability** | `skills/buildme/llm-txt-skill/SKILL.md` | llms.txt generation |
| **Agent 7** | **Anti-Slop Enforcer** | `skills/buildme/anti-slop-enforcer/SKILL.md` | 13 slop detectors + veto |
| **Agent 8** | **Bug Hunter & Fixer** | `skills/buildme/bug-hunter/SKILL.md` | Reproduce → fix → verify |
| **Agent 9** | **Content & Copy Voice** | `skills/buildme/content-voice/SKILL.md` | VOICE.md + site copy |
| **Agent 10** | **Perf & A11y Auditor** | `skills/buildme/perf-a11y-auditor/SKILL.md` | Web Vitals + WCAG 2.2 AA |
| **Agent 11** | **Reference Analyzer** | `skills/buildme/reference-analyzer/SKILL.md` | Steal / Beat / Avoid brief |
| **Agent 12** | **Token Snapshotter** | `skills/buildme/token-snapshotter/SKILL.md` | Versioned token snapshots |
| **Agent 13** | **Post-Launch Monitor** | `skills/buildme/post-launch-monitor/SKILL.md` | Live deploy + Lighthouse |
| **Feature** | **Design Arena** | `skills/buildme/design-arena/SKILL.md` | Design bake-off |

---

## 📦 Upstream Skill Dependencies

| Skill | Canonical Repo |
|---|---|
| impeccable | `github.com/pbakaus/impeccable` |
| frontend-design | `github.com/anthropics/skills` |
| taste-skill | `github.com/Leonxlnx/taste-skill` |
| ui-ux-pro-max | `github.com/nextlevelbuilder/ui-ux-pro-max-skill` |
| emil-design-eng (+ apple-design, review-animations, animation-vocabulary) | `github.com/emilkowalski/skills` |
