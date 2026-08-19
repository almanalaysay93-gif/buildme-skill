---
name: buildme
description: "Activates when the user types /Buildme, /buildme, or asks to build a web app using the 6-agent design ensemble. First runs an interactive Grill Me discovery to align on requirements, then launches 6 subagents (Impeccable, Frontend Design, Taste Skill, UI UX Pro Max, Emil's Design Engineering, and AI Discoverability/llms.txt) to build high-craft, AI-discoverable UIs."
metadata:
  triggers: /Buildme, /buildme, buildme, 5 agent build, build with design ensemble
  slash_command: /Buildme
---

# 🚀 BuildMe: 6-Agent Design & Development Orchestrator

The **BuildMe** skill orchestrates a high-craft frontend development workflow powered by **6 specialized design & engineering subagents**.

Before any code is generated, BuildMe runs a **Grill Me** discovery interview to understand your vision, aesthetic preferences, tech stack, and specs. It then dispatches 6 concurrent subagents—each enforcing a world-class design skill—to shape, build, audit, and polish your web application, and finally make it discoverable by AI assistants via `llms.txt`.

---

## 📋 Workflow Execution Phasing

```
[Phase 1: Grill Me Discovery] ➔ [Phase 2: 6-Agent Parallel Dispatch] ➔ [Phase 3: Integration & Craft Synthesis] ➔ [Phase 4: AI Discoverability (llms.txt)]
```

---

## Phase 1: Interactive Alignment ("Grill Me")

> **CRITICAL RULE**: Do NOT start building or spawning subagents until Phase 1 is complete and requirements are confirmed.

1. **Conduct the Discovery Interview**:
   Ask the user 3 to 5 targeted questions (using bullet points or concise text) covering:
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

## Phase 2: 6-Agent Parallel Dispatch

Launch **6 subagents concurrently** using `invoke_subagent`. Each subagent is assigned a specific design domain and reads its authoritative skill instruction file:

```json
[
  {
    "TypeName": "self",
    "Role": "Agent 1: Impeccable Design Director",
    "Prompt": "You are Agent 1 (Impeccable Design Director). Read the skill instruction file at `C:\\Users\\Admin\\.gemini\\config\\skills\\impeccable\\SKILL.md`. Initialize design context (`PRODUCT.md` and `DESIGN.md`), run anti-pattern scans against the 59 deterministic detector rules, enforce craft floor standards, and audit visual hierarchy and identity."
  },
  {
    "TypeName": "self",
    "Role": "Agent 2: Lead Frontend Architect",
    "Prompt": "You are Agent 2 (Lead Frontend Architect). Read the skill instruction file at `C:\\Users\\Admin\\.gemini\\config\\skills\\frontend-design\\SKILL.md`. Establish the core CSS design system, typography scale, custom OKLCH/HSL color palette, grid layout architecture, responsive container rules, and base UI component structure."
  },
  {
    "TypeName": "self",
    "Role": "Agent 3: Anti-Slop Taste Specialist",
    "Prompt": "You are Agent 3 (Anti-Slop Taste Specialist). Read the skill instruction file at `C:\\Users\\Admin\\.gemini\\config\\skills\\taste-skill\\SKILL.md`. Enforce anti-default discipline (eliminating generic AI purple gradients, slate card grids, and cookie-cutter layouts). Apply contextual vibe alignment and high-taste visual decisions based on the project brief."
  },
  {
    "TypeName": "self",
    "Role": "Agent 4: UI/UX & A11y Auditor",
    "Prompt": "You are Agent 4 (UI/UX & A11y Auditor). Read the skill instruction file at `C:\\Users\\Admin\\.gemini\\config\\skills\\ui-ux-pro-max\\SKILL.md`. Audit component interaction states (hover, active, focus, disabled, loading, empty, error), touch target sizing, contrast ratios, keyboard navigation, cognitive load reduction, and user flow friction points."
  },
  {
    "TypeName": "self",
    "Role": "Agent 5: Emil's Motion & Animation Specialist",
    "Prompt": "You are Agent 5 (Emil's Motion & Animation Specialist). Read the skill instruction file at `C:\\Users\\Admin\\.gemini\\config\\skills\\emil-design-eng\\SKILL.md` (and reference skills `apple-design`, `review-animations`, `animation-vocabulary`). Implement buttery-smooth CSS/Framer motion transitions, fluid spring physics, gesture affordances, and micro-interaction polish."
  },
  {
    "TypeName": "self",
    "Role": "Agent 6: AI Discoverability & llms.txt Specialist",
    "Prompt": "You are Agent 6 (AI Discoverability & llms.txt Specialist). Read the skill instruction file at `C:\\Users\\Admin\\.gemini\\config\\skills\\buildme\\llm-txt-skill\\SKILL.md`. Run after Phase 3 synthesis: generate a spec-compliant llms.txt (and llms-full.txt if needed) at public/llms.txt so AI assistants (ChatGPT, Claude, Perplexity) can correctly understand and recommend the business/product. Derive all content from PRODUCT.md and the final site content; self-verify against the checklist."
  }
]
```

---

## Phase 3: Integration & Craft Synthesis

1. **Synthesize Subagent Outputs**:
   Combine the design system tokens, layout structure, anti-slop rules, UX state handoffs, and animation primitives into clean, production-ready code.

2. **Verify Execution**:
   - Ensure zero console errors or broken styling.
   - Verify layout responsiveness across desktop, tablet, and mobile viewports.
   - Test interaction states, contrast, and animation performance.

3. **Deliver Walkthrough & Summary**:
   Provide a clear summary of what was built, clickable file links, and key features.

---

## Phase 4: AI Discoverability (`llms.txt`)

Run **Agent 6 (AI Discoverability & llms.txt Specialist)** as the final gate, after the site builds successfully:

1. **Generate `public/llms.txt`** per `llm-txt-skill/SKILL.md`, grounded strictly in `PRODUCT.md` and final site content.
2. **Verify** the file builds into the deploy output (`dist/llms.txt`) and self-verify checklist passes.
3. **Confirm discoverability keywords** are present (product category + location + intent), so AI assistants can recommend the business for free.

---

## 🛠️ The 6-Agent Skill Ensemble Reference

| Agent | Assigned Skill | Location | Key Function |
|---|---|---|---|
| **Agent 1** | **Impeccable** | [`impeccable/SKILL.md`](file:///C:/Users/Admin/.gemini/config/skills/impeccable/SKILL.md) | `PRODUCT.md` / `DESIGN.md` setup, 59 anti-pattern rules, craft floor & polish |
| **Agent 2** | **Frontend Design** | [`frontend-design/SKILL.md`](file:///C:/Users/Admin/.gemini/config/skills/frontend-design/SKILL.md) | Color palettes, typography scale, CSS tokens & grid architecture |
| **Agent 3** | **Taste Skill** | [`taste-skill/SKILL.md`](file:///C:/Users/Admin/.gemini/config/skills/taste-skill/SKILL.md) | Brief inference, anti-slop discipline, anti-default styling |
| **Agent 4** | **UI UX Pro Max** | [`ui-ux-pro-max/SKILL.md`](file:///C:/Users/Admin/.gemini/config/skills/ui-ux-pro-max/SKILL.md) | Component state audit, accessibility (a11y), UX friction & touch targets |
| **Agent 5** | **Emil's Skills** | [`emil-design-eng/SKILL.md`](file:///C:/Users/Admin/.gemini/config/skills/emil-design-eng/SKILL.md) | Fluid animations, spring physics, motion vocabulary & micro-interactions |
| **Agent 6** | **AI Discoverability (llms.txt)** | [`llm-txt-skill/SKILL.md`](file:///C:/Users/Admin/.gemini/config/skills/buildme/llm-txt-skill/SKILL.md) | `llms.txt` / `llms-full.txt` generation so AI assistants can read and recommend the site |
