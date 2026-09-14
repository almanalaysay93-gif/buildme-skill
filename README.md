# 🚀 BuildMe Skill (`/Buildme`) — v4

> **13-Agent Design & Development Orchestrator for AI Coding Agents**

One command installs the orchestrator **and every agent skill** as sibling folders under `skills/`.

```bash
npx skills add https://github.com/almanalaysay93-gif/buildme-skill
```

That registers these skills together:

`buildme`, `master-orchestrator`, `impeccable-director`, `frontend-architect`, `taste-specialist`, `ui-ux-auditor`, `motion-specialist`, `llm-txt-skill`, `anti-slop-enforcer`, `bug-hunter`, `content-voice`, `perf-a11y-auditor`, `reference-analyzer`, `token-snapshotter`, `post-launch-monitor`, `design-arena`

Re-run the same command after pulling. Do not install only the repo root — the CLI needs the flat `skills/<name>/SKILL.md` layout (nested files under `skills/buildme/` are shadowed and ignored).

Then type `/Buildme`. The orchestrator dispatches all agents in-session; they do not appear as 13 separate chat bots, they appear as 15 installed skills.

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
| Feature | design-arena |

## License
[Apache 2.0](LICENSE) © [AL Manalaysay](https://github.com/almanalaysay93-gif)
