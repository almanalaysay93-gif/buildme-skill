---
name: buildme
description: "Activates when the user types /Buildme, /buildme, or asks to build a web app using the multi-agent build ensemble. Runs reference analysis, Grill Me discovery, coordinates specialized subagents (orchestration, references, design, taste, a11y, motion, copy, llms.txt, anti-slop, bug hunting, perf/a11y, token snapshots, planning author/reviewer, observability, security, architecture, state/data, caching/offline) plus Design Arena, conditional ADK building (Agent 14) and competitor/repository discovery (Agent 15) for in-product AI agents, to build high-craft, AI-discoverable, bug-free UIs. Free local workflow using Agent Desktop and specialized web audits. Not for a standalone one-screen design bake-off (use design-arena) or for adding an AI agent to an existing product on its own (use adk-agent-builder)."
metadata:
  triggers: /Buildme, /buildme, buildme, 5 agent build, build with design ensemble, 10 agent build, 13 agent build
  slash_command: /Buildme
---

# Buildme compatibility entry

Read [the canonical Buildme workflow](skills/buildme/SKILL.md) and follow it in full.
It defines expanded Grill Me, Agents 0–22, research-tool routing, activation matrix,
Superlite execution and mandatory UX laws. Install companions as described in
[README.md](README.md). Do not use an older interview or dispatch sequence.

## Phase 3 dispatch order

Grill Me -> Reference Analysis -> planning-agent -> planning-reviewer -> frontend-architect (with rendering decision) -> architecture-agent -> state-data-agent -> caching-offline-agent -> motion-specialist (delegate to /designme if premium) -> security-agent -> bug-hunter -> perf-a11y-auditor -> observability-agent -> token-snapshotter -> llm-txt-skill -> content-voice -> anti-slop-enforcer

The canonical workflow defines supporting dispatches for all existing roles,
repair/revalidation order and mandatory shipping gates. New contracts are in
[agents/](agents/); the existing [frontend architect update](agents/frontend-architect.md)
requires rendering-decision.md before code.

## Required files after Grill Me

Before implementation, create/update project_context.md, constitution.md, spec.md,
plan.md and tasks.md using the [Markdown planning contract](skills/buildme/references/markdown-planning.md).
They are the build's governing documents; every worker receives their canonical
paths/revisions and assigned task IDs. No application code or speckit implement
before Phase 2.5 is READY. Existing agents and the Phase 3 sequence remain intact.


Agent 21 [planning-agent](agents/planning-agent.md) writes the five files; Agent 22
[planning-reviewer](agents/planning-reviewer.md) reviews them independently into
planning-review.md. Findings return to Agent 21 until verified or the two-round
cap is reached. A current independent PASS is required before Agent 0 records
READY; unresolved failures block implementation.
