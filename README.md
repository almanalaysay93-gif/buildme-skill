# 🚀 BuildMe Skill (`/Buildme`) — v4

> **13-Agent Design & Development Orchestrator for AI Coding Agents**

One command installs the orchestrator **and every agent skill** as sibling folders under `skills/`.

```bash
npx skills add https://github.com/almanalaysay93-gif/buildme-skill
```

That registers these skills together:

`buildme`, `master-orchestrator`, `impeccable-director`, `frontend-architect`, `taste-specialist`, `ui-ux-auditor`, `motion-specialist`, `llm-txt-skill`, `anti-slop-enforcer`, `bug-hunter`, `content-voice`, `perf-a11y-auditor`, `reference-analyzer`, `token-snapshotter`, `post-launch-monitor`, `design-arena`, `adk-agent-builder`

### Install BuildMe and its companion skills (required)

BuildMe needs five companion skills to run Agents 1–5. They ship in this repo and are installed with it. Install them every time you use BuildMe:

```bash
git clone https://github.com/almanalaysay93-gif/buildme-skill
cd buildme-skill
bash scripts/install.sh
```

The script installs BuildMe and these companions, `impeccable-director`, `frontend-architect`, `taste-specialist`, `ui-ux-auditor` and `motion-specialist`, for Claude Code, Codex, Grok and Antigravity on this machine. It only replaces skills with the same names. If a companion is missing, BuildMe stops before Phase 3 and tells you which one to install.

Re-run the same command after pulling. Do not install only the repo root — the CLI needs the flat `skills/<name>/SKILL.md` layout (nested files under `skills/buildme/` are shadowed and ignored).

Then type `/Buildme`. The orchestrator dispatches all agents in-session; they do not appear as separate chat bots, they appear as 17 installed skills.

Optional upstream upgrades (richer than the bundled role skills):

```bash
npx skills add https://github.com/pbakaus/impeccable
npx skills add https://github.com/anthropics/skills --skill frontend-design
npx skills add https://github.com/Leonxlnx/taste-skill
npx skills add https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
npx skills add https://github.com/emilkowalski/skills
```

## Ensemble

| Agent | Skill folder |
|---|---|
| 0 | master-orchestrator |
| 1 | impeccable-director |
| 2 | frontend-architect |
| 3 | taste-specialist |
| 4 | ui-ux-auditor |
| 5 | motion-specialist |
| 6 | llm-txt-skill |
| 7 | anti-slop-enforcer |
| 8 | bug-hunter |
| 9 | content-voice |
| 10 | perf-a11y-auditor |
| 11 | reference-analyzer |
| 12 | token-snapshotter |
| 13 | post-launch-monitor |
| 14 (conditional) | adk-agent-builder |
| Feature | design-arena |

## License
[Apache 2.0](LICENSE) © [AL Manalaysay](https://github.com/almanalaysay93-gif)

## Superlite execution

This skill now uses a bundled [Superlite execution adapter](skills/master-orchestrator/references/superlite-integration.md) for
dependency-aware tasks, single-owner file contracts, targeted repairs and fresh
final review. Its specialty workflow and quality gates remain in charge. No native
plugin or model service is required. The reference includes optional native-plugin
setup and host limitations. Never enable Superlite alongside Superpowers.

## Free to run: no API keys

BuildMe needs no API keys, paid services or accounts. Every agent uses free tools: local
Lighthouse or the Chrome DevTools MCP for audits and screenshots, the host agent's own web
search for research, bundled Material Symbols icons, and a local Ollama model for in-product AI
agents. A task that would need a paid service is skipped with a free alternative and never
reported as passed. See [the zero-cost policy](skills/buildme/references/zero-cost.md).

Optional free setup for Agent 14 and audits: [Node.js](https://nodejs.org) (for `npx lighthouse`),
[Ollama](https://ollama.com) with `ollama pull qwen2.5:1.5b`, and `uv` for the Python packages.

## Mandatory UX laws

The bundled [14-law UX reference](skills/buildme/references/ux-laws.md) now applies to planning,
implementation and post-build review. Plans map the laws to actual flows; every
build or significant change produces `UX_LAWS_AUDIT.md` with evidence, fixes and
re-audit results. Completion requires no violations and documented reasons for
any justified Partial results. See [the audit workflow](skills/buildme/references/ux-laws-workflow.md).

## Icons

BuildMe bundles 58 common Material Symbols icons (Outlined, 24px, Apache 2.0) in
[`skills/buildme/assets/icons/`](skills/buildme/assets/icons/), so builds use one icon
family without a network call. See [the icon reference](skills/buildme/references/icons.md)
for usage, accessibility rules and how to add more icons. The icons' `LICENSE` and
`NOTICE.md` must stay with them.

## In-product AI agents (Agent 14)

Agent 14 (`skills/buildme/adk-agent-builder/`) builds an AI agent that the product itself runs, using
[Google's Agent Development Kit](https://github.com/google/adk-python) (`google-adk`) on a free
local model through [Ollama](https://ollama.com) (default `qwen2.5:1.5b`). No API key or hosted
model is used. The orchestrator dispatches it only when the brief asks for an assistant, a
tool-using agent or a multi-step AI workflow. It writes the agent in `agent/`, adds offline tool
tests, runs the acceptance questions on the local model, and sets a call limit on every run.
