---
name: buildme
description: "Activates when the user types /Buildme, /buildme, or asks to build a web app using the multi-agent build ensemble. Runs reference analysis, Grill Me discovery, coordinates specialized subagents (orchestration, references, design, taste, a11y, motion, copy, llms.txt, anti-slop, bug hunting, perf/a11y, token snapshots, post-launch monitoring) plus Design Arena, conditional ADK building (Agent 14) and competitor/repository discovery (Agent 15) for in-product AI agents, to build high-craft, AI-discoverable, bug-free UIs. Free to run: no API keys or paid services. Not for a standalone one-screen design bake-off (use design-arena) or for adding an AI agent to an existing product on its own (use adk-agent-builder)."
metadata:
  triggers: /Buildme, /buildme, buildme, 5 agent build, build with design ensemble, 10 agent build, 13 agent build
  slash_command: /Buildme
---

# Buildme compatibility entry

Read [the canonical Buildme workflow](skills/buildme/SKILL.md) and follow it in full.
It defines expanded Grill Me, Agents 0–15, research-tool routing, activation matrix,
Superlite execution and mandatory UX laws. Install companions as described in
[README.md](README.md). Do not use an older interview or dispatch sequence.
