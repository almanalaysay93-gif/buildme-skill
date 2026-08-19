---
name: design-arena
description: "Feature: Design Arena — a design bake-off mode where 2-4 subagents each redesign one screen (informed and/or blind), the user judges a gallery, and the winner gets applied. Use when the direction is uncertain or the current design feels stuck."
metadata:
  mode: optional
  triggers: design arena, bake-off, redesign contest, blind design
---

# 🏟️ Feature: Design Arena (Design Bake-Off)

Run a **design competition** when the single-agent direction is uncertain, or when the current design is a local maximum and no amount of polish escapes it. Multiple agents each take a full swing at **one screen** — the user judges, the winner ships.

> **Golden rule**: one screen per arena, never the whole app. Twelve takes on "everything" is incomparable mush.

---

## 🎭 The Two Tracks

| Track | What the agent sees | Job |
|---|---|---|
| 🟢 **Informed** | Screenshots, source CSS, design tokens, brand notes | Keep what works, fix what's cheap, raise the ceiling |
| 🔵 **Blind** | Functional spec only (copy, actions, hierarchy). NO colors, fonts, layouts, or screenshots | Invent the strongest direction from nothing |

The blind track is only meaningful if airtight: blind agents are barred from opening source/tokens/screenshots, and the orchestrator greps each blind brief for leaked hex codes and font names before dispatch.

## 🏁 Arena Protocol

1. **Scope**: user picks exactly ONE screen/section. Write the arena brief (`arena/context.md`) containing the functional spec + track assignments.
2. **Roster**: pick 2–4 agents/skills for distinct lineages (e.g., taste-skill, frontend-design, emil-design-eng, devor). Six forks of one upstream measure one taste six times — keep lineages distinct.
3. **Dispatch**: each agent produces exactly two files:
   - `arena/{track}/{agent}/mockup.html` — a self-contained, standalone HTML mockup of the screen
   - `arena/{track}/{agent}/apply-plan.md` — direction, token set, which real files change, assets, motion notes, risks. Executable without having watched the agent work.
4. **Gallery**: build `arena/competition-brief.html` — every mockup framed identically, side by side, judgeable in one sitting. Serve via a local static server (`file://` won't frame).
5. **Judge**: user picks the winner (or "merge these two"). Losers are thanked and discarded — no sunk-cost attachment.
6. **Apply & verify**: execute the winner's apply-plan against the real codebase, then screenshot-verify the real screen renders it. Applied means verified.

## 💰 Cost Warning

Every agent costs real tokens. Tell the user the estimated cost before spawning and offer the small-arena variant (2 skills × 1 track). Default to 2 agents unless the user asks for more.

## ⚡ Anti-Patterns (Never)

- Running the arena on the whole app
- Letting blind agents see tokens or screenshots (then it isn't blind)
- Applying the winner without verifying the real screen renders it
- Keeping losing designs "just in case" — it pollutes the design context
