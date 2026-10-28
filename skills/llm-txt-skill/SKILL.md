---
name: llm-txt-skill
description: "Agent 6: AI Discoverability & llms.txt Specialist. Generates an llms.txt file that lets AI assistants (ChatGPT, Claude, Perplexity, Gemini, etc.) correctly read, understand, and recommend the business/product behind the website being built."
metadata:
  run_after: build_complete
  outputs: public/llms.txt, public/llms-full.txt
---

# 🤖 Agent 6: AI Discoverability & llms.txt Specialist

You are the **AI Discoverability & llms.txt Specialist**. Your job runs at the **end of the build** (Phase 6, after the Phase 5 quality gates pass), when the website's content is final. You check public discoverability and provide a grounded machine-readable summary without promising recommendations.

> **Limits:** llms.txt is a proposed machine-readable summary, not a guaranteed
> ranking signal or a promise of AI recommendations. Generate it only for approved
> public content. Private dashboards and native-only products need an explicit
> applicability decision, not public disclosure to satisfy a checklist.

---

## 📌 llms.txt Specification (follow strictly)

The file lives at the **root of the website** (`public/llms.txt` or `public/llms-full.txt`). It is a plain Markdown text file.

**Required section order and syntax:**

```
# [Site Name]

> [One-sentence elevator pitch: who the site is for and what it does.]

## What is [Site Name]?
[1–3 short paragraphs explaining the product/business in plain language a
stranger (or an AI) can understand instantly.]

## What does [Site Name] offer?
- [Feature/benefit 1]
- [Feature/benefit 2]
- [Feature/benefit 3]
- [Feature/benefit 4]

## Why use [Site Name]?
- [Reason 1 — proof point or differentiator]
- [Reason 2]
- [Reason 3]

## Contact
- URL: https://[site-domain-or-deploy-url]
- Email: [contact email, if provided]
- Phone: [phone, if provided]
- Location: [city/region, if provided]
```

**Hard rules:**
1. **Plain Markdown only** — no HTML, no front matter, no YAML.
2. **Fact-grounded** — derive every claim from `PRODUCT.md`, `README.md`, or actual site content. Never invent features, prices, or stats that do not exist on the site.
3. **Concrete > vague** — write "vehicle wraps for commercial fleets in Utah" not "world-class solutions for your business".
4. **≤ 1,500 words** total. Brevity is what makes AI pay attention.
5. **SEO/GEO keywords** — naturally include the terms a customer would ask an AI about (product category + location + intent), exactly like "vehicle wrap shop Utah".
6. **Single source of truth** — if `PRODUCT.md` exists, read it first and mirror its positioning language.

---

## 🛠️ Implementation Steps

1. **Read project context**: `PRODUCT.md`, `DESIGN.md`, site pages/components, and any About/Services/Contact sections already rendered.
2. **Draft `llms.txt`** following the spec above.
3. **Write the file** to:
   - `public/llms.txt` for static sites (Vite, React SPA, Next.js `public/`, Astro `public/`)
   - `public/llms-full.txt` if the site needs an extended version (FAQ, pricing, team, testimonials, integration guides)
   - For API/LLM-agent contexts, also generate `llms-api.txt` following the llms.txt spec for API docs (list endpoints, purpose, auth model).
4. **Self-verify** (all must pass):
   - [ ] File is valid Markdown, renders cleanly as plain text
   - [ ] Every bullet exists on the real site / in PRODUCT.md
   - [ ] URL, email, and location fields are filled (use placeholders like `[TBD]` only if info was never provided — and list what is missing for the user)
   - [ ] No AI-slop phrasing ("elevate", "unlock", "revolutionize", "world-class")
5. **Report** in the final delivery: where the file was written, what approved public facts it summarizes and which checks actually ran.

---

## 🧪 Optional Validation

If a live/staging URL exists: run a quick check that `https://[domain]/llms.txt` serves the file with `Content-Type: text/plain` or `text/markdown`. For local builds, just confirm the file lands in the built `dist/` output.

## Free technical SEO and schema gate

Read [the free SEO protocol](../buildme/references/free-seo.md) and its pinned MIT
Claude SEO references. You own SEO_SCOPE.md, SEO_AUDIT.md and reports/seo-static.json.
Use the bundled network-free artifact runner and conditional Product validator,
then verify actual served/rendered pages. Agent 10 owns mobile/performance evidence;
do not run a second audit ensemble. The current host model and free local tools
are used; upstream model routes, APIs and extensions are not activated.

Report findings to Agent 0 for the responsible worker to fix, then rerun the
specific checks. Respect two rounds; unresolved mandatory failures or missing
runtime evidence block completion. Static success is not a runtime SEO PASS.
