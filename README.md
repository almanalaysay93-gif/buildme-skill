# 🚀 BuildMe Skill (`/Buildme`)

> **6-Agent Design & Development Orchestrator for AI Coding Agents**

BuildMe (`/Buildme`) is an advanced multi-agent orchestrator skill designed for AI coding assistants (Antigravity, Claude Code, Gemini CLI, Cursor, Codex).

Before writing code, BuildMe runs an interactive **Grill Me** interview to understand requirements and design intent. It then dispatches **6 parallel subagents**, each enforcing a specialized world-class design skill (Impeccable, Frontend Design, Taste Skill, UI UX Pro Max, Emil's Design Engineering, and AI Discoverability/llms.txt), then makes the finished site discoverable by AI assistants.

---

## 🛠️ The 6-Agent Ensemble

| Agent | Assigned Skill | Core Responsibility |
|---|---|---|
| **Agent 1** | **Impeccable** | `PRODUCT.md` / `DESIGN.md` setup, 59 anti-pattern rules, craft floor & polish |
| **Agent 2** | **Frontend Design** | Color palettes, typography scale, CSS tokens & grid architecture |
| **Agent 3** | **Taste Skill** | Brief inference, anti-slop discipline, anti-default styling |
| **Agent 4** | **UI UX Pro Max** | Component state audit, accessibility (a11y), UX friction & touch targets |
| **Agent 5** | **Emil's Skills** | Fluid animations, spring physics, motion vocabulary & micro-interactions |
| **Agent 6** | **AI Discoverability (llms.txt)** | `llms.txt` / `llms-full.txt` generation so AI assistants (ChatGPT, Claude, Perplexity) can read and recommend the business |

---

## 📦 Quick Start / Installation

### Install globally via GitHub:
```bash
npx skills add https://github.com/almanalaysay93-gif/buildme-skill
```

### Manual Installation:
Copy `SKILL.md` to your agent's skills folder:
- **Global**: `~/.gemini/config/skills/buildme/SKILL.md`
- **Project**: `.agents/skills/buildme/SKILL.md` or `.gemini/skills/buildme/SKILL.md`

---

## ⚡ Usage

Simply type `/Buildme` or `/buildme` in your AI coding agent chat:

```bash
/Buildme
```

1. **Grill Me Phase**: Answer 3–5 targeted questions to specify your app's goal, tech stack, visual vibe, and motion preferences.
2. **Parallel Dispatch**: The agent automatically spawns 6 specialized subagents working simultaneously.
3. **Craft Synthesis**: The agent integrates all design, UX, layout, and motion rules into production-ready code.
4. **AI Discoverability**: Agent 6 generates a spec-compliant `llms.txt` at `public/llms.txt` so the finished site can be correctly understood and recommended by AI assistants — no ads, no SEO agency.

---

## 📄 License
[Apache 2.0](LICENSE) © [AL Manalaysay](https://github.com/almanalaysay93-gif)
