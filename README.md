# 🚀 BuildMe Skill (`/Buildme`) — v3

> **10-Agent Design & Development Orchestrator for AI Coding Agents**

BuildMe (`/Buildme`) is an advanced multi-agent orchestrator skill designed for AI coding assistants (Antigravity, Claude Code, Gemini CLI, Cursor, Codex).

Before writing code, BuildMe runs an interactive **Grill Me** interview, then dispatches **10 parallel subagents** across five phases — orchestration, design, synthesis, quality gates, and AI discoverability — plus an optional **Design Arena** bake-off mode when the visual direction is uncertain.

---

## 🛠️ The 10-Agent Ensemble

| Agent | Assigned Skill | Core Responsibility |
|---|---|---|
| **Agent 0** | **Master Orchestrator** | Plan decomposition, dispatch contracts, token budgets, conflict resolution, session checkpointing (`ORCHESTRATOR.md`) |
| **Agent 1** | **Impeccable** | `PRODUCT.md` / `DESIGN.md` setup, 59 anti-pattern rules, craft floor & polish |
| **Agent 2** | **Frontend Design** | Color palettes, typography scale, CSS tokens & grid architecture |
| **Agent 3** | **Taste Skill** | Brief inference, anti-slop discipline, anti-default styling |
| **Agent 4** | **UI UX Pro Max** | Component state audit, accessibility (a11y), UX friction & touch targets |
| **Agent 5** | **Emil's Skills** | Fluid animations, spring physics, motion vocabulary & micro-interactions |
| **Agent 6** | **AI Discoverability (llms.txt)** | `llms.txt` generation so AI assistants (ChatGPT, Claude, Perplexity) can read and recommend the business |
| **Agent 7** | **Anti-Slop Enforcer** | 13 deterministic slop detectors (visual, copy, motion) with a veto gate before shipping |
| **Agent 8** | **Bug Hunter & Fixer** | Reproduce → fix → verified-fix loop, responsive/a11y/state checks, regression guards, before/after evidence |
| **Agent 9** | **Content & Copy Voice** | `VOICE.md`, distinctive brand copy and SEO meta, zero banned buzzwords |
| **Agent 10** | **Perf & A11y Auditor** | Web Vitals budgets (LCP < 2.5s, CLS < 0.1), WCAG 2.2 AA, keyboard/screen-reader passes, Rams honesty audit |
| **Feature** | **Design Arena** | Informed vs blind design bake-off — multiple agents redesign one screen, user judges, winner ships |

---

## 📦 Quick Start / Installation

### Install globally via GitHub:
```bash
npx skills add https://github.com/almanalaysay93-gif/buildme-skill
```

### Manual Installation:
Copy `SKILL.md` (and the `buildme/` skill folders) to your agent's skills folder:
- **Global**: `~/.gemini/config/skills/buildme/`
- **Project**: `.agents/skills/buildme/` or `.gemini/skills/buildme/`

---

## ⚡ Usage

Simply type `/Buildme` or `/buildme` in your AI coding agent chat:

```bash
/Buildme
```

1. **Grill Me Phase**: Answer 3–5 targeted questions to specify your app's goal, tech stack, visual vibe, and motion preferences.
2. **Orchestration Setup**: Agent 0 decomposes the brief into work units, contracts, and token budgets.
3. **Parallel Dispatch**: The ensemble spawns specialized subagents working simultaneously (plus the optional Design Arena bake-off).
4. **Craft Synthesis**: All design, UX, layout, motion, and copy work integrates into production-ready code.
5. **Quality Gates**: Agents 7 → 8 → 10 (anti-slop → bug hunt → perf/a11y) must all pass before the build advances.
6. **AI Discoverability**: Agent 6 generates a spec-compliant `llms.txt` at `public/llms.txt`.

**Optional**: between steps 1 and 2, ask for a **Design Arena** when the direction is uncertain — several agents each take a full swing at one screen, you judge the gallery, and the winner ships.

---

## 🔄 Keeping the Ensemble Up to Date

The ensemble agents consume externally installed skills. To pull the latest versions at any time, run:

```bash
# Agent 1 — Impeccable
npx skills add https://github.com/pbakaus/impeccable

# Agent 2 — Frontend Design (official Anthropic skill)
npx skills add https://github.com/anthropics/skills --skill frontend-design

# Agent 3 — Taste Skill
npx skills add https://github.com/Leonxlnx/taste-skill

# Agent 4 — UI UX Pro Max
npx skills add https://github.com/nextlevelbuilder/ui-ux-pro-max-skill

# Agent 5 — Emil Kowalski's official skills
# (emil-design-eng + apple-design, review-animations, animation-vocabulary)
npx skills add https://github.com/emilkowalski/skills

# Agents 6–10 + Design Arena + Orchestrator — this repo itself
npx skills add https://github.com/almanalaysay93-gif/buildme-skill
```

> **Tip:** Re-run these commands periodically (monthly is a good cadence) — all upstream repos are actively maintained and receive anti-slop rules and design improvements frequently.

---

## 📄 License
[Apache 2.0](LICENSE) © [AL Manalaysay](https://github.com/almanalaysay93-gif)
