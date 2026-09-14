# 🚀 BuildMe Skill (`/Buildme`) — v4

> **13-Agent Design & Development Orchestrator for AI Coding Agents**

BuildMe (`/Buildme`) is an advanced multi-agent orchestrator skill designed for AI coding assistants (Antigravity, Claude Code, Gemini CLI, Cursor, Codex).

Before writing code, BuildMe runs an interactive **Grill Me** interview, then dispatches **13 specialized subagents** across six phases — orchestration, preflight reference analysis, design, synthesis, quality gates, and AI discoverability — plus versioned design snapshots, post-launch monitoring, and an optional **Design Arena** bake-off mode when the visual direction is uncertain.

---

## Important: why `npx skills add` only shows ~5 agents

This repo installs as **one orchestrator skill** (`buildme`).

Agents **1–5 are external skills**. They are **not** inside this repo. A single `npx skills add` of this URL will not create 13 separate agent skills.

| Source | Agents |
|---|---|
| This repo | Agent 0, 6–13 + Design Arena (subfolders under `skills/buildme/`) |
| External installs (required) | Agents 1–5 |

If your CLI only registered 5 items, install the five upstream skills below, then re-add this repo.

Also change the GitHub repo **About** description from “5-Agent…” to “13-Agent…” (Settings → General → Description). That field is not in git.

---

## 🛠️ The 13-Agent Ensemble

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
| **Agent 11** | **Reference Analyzer** | Pre-Grill Me tear-down of 2–3 reference/competitor sites → Steal / Beat / Avoid brief |
| **Agent 12** | **Token Snapshotter** | Versioned, diffable design-system snapshots at every phase trigger + drift guard |
| **Agent 13** | **Post-Launch Monitor** | Live deploy verification, llms.txt checksum, live Lighthouse, AI-discoverability baseline |
| **Feature** | **Design Arena** | Informed vs blind design bake-off — multiple agents redesign one screen, user judges, winner ships |

---

## 📦 Full install (13-agent ensemble)

Run **all** of these:

```bash
# Agents 1–5 — external (required)
npx skills add https://github.com/pbakaus/impeccable
npx skills add https://github.com/anthropics/skills --skill frontend-design
npx skills add https://github.com/Leonxlnx/taste-skill
npx skills add https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
npx skills add https://github.com/emilkowalski/skills

# Agents 0, 6–13 + Design Arena — this repo
npx skills add https://github.com/almanalaysay93-gif/buildme-skill
```

### Manual Installation

Copy `SKILL.md` **and every folder** under `skills/buildme/` into your agent's skills directory so each sub-skill has its own `SKILL.md`:

- **Global**: `~/.gemini/config/skills/buildme/`
- **Project**: `.agents/skills/buildme/` or `.gemini/skills/buildme/`

Bundled sub-skills: `master-orchestrator`, `llm-txt-skill`, `anti-slop-enforcer`, `bug-hunter`, `content-voice`, `perf-a11y-auditor`, `reference-analyzer`, `token-snapshotter`, `post-launch-monitor`, `design-arena`.

---

## ⚡ Usage

```bash
/Buildme
```

1. **Grill Me Phase**: Answer 3–5 targeted questions to specify your app's goal, tech stack, visual vibe, and motion preferences.
2. **Preflight (optional)**: Agent 11 tears down your reference/competitor sites before the interview.
3. **Orchestration Setup**: Agent 0 decomposes the brief into work units, contracts, and token budgets.
4. **Parallel Dispatch**: The ensemble spawns specialized subagents (plus optional Design Arena).
5. **Craft Synthesis**: Design, UX, layout, motion, and copy integrate into production-ready code — snapshot after each major change (Agent 12).
6. **Quality Gates**: Agents 7 → 8 → 10 must all pass before the build advances.
7. **AI Discoverability**: Agent 6 generates `public/llms.txt`.
8. **Post-Launch**: Agent 13 verifies the live site.

**Optional**: between steps 1 and 3, ask for a **Design Arena** when the direction is uncertain.

---

## 🔄 Keeping the Ensemble Up to Date

Re-run the full install commands monthly. Upstream repos change often.

---

## 📄 License
[Apache 2.0](LICENSE) © [AL Manalaysay](https://github.com/almanalaysay93-gif)
