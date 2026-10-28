# Zero-cost policy: no API keys, no paid services

BuildMe must run end to end at no cost. Every agent follows this file.

## The rule

- **No API keys.** Never ask the user for a key, never read one from the environment for BuildMe work, and never write one into code or config.
- **No paid services or credits.** No paid APIs, no trial sign-ups, no tools that bill per request.
- **No accounts.** Never create an account, log in or sign up on the user's behalf.
- **Free means free to use without registration**: open-source tools that run locally, the host agent's own built-in tools, and public web pages that need no login.

If a task can only be done with a paid or keyed service, stop that task, mark it **"not run (needs a paid service)"**, offer the closest free alternative below, and continue with the rest of the build. Never mark it "passed".

## Free tool for each job

| Job | Use (free) | Never use |
|---|---|---|
| Lighthouse / Web Vitals (Agents 10, 13) | Lighthouse CLI run locally (`npx lighthouse <url> --output=json --chrome-flags="--headless"`), or the Chrome DevTools MCP `lighthouse_audit` tool | PageSpeed Insights API with a key, paid monitoring (SpeedCurve, Calibre and similar) |
| Accessibility checks (Agents 4, 8, 10) | Lighthouse a11y category, Chrome DevTools MCP snapshots, manual keyboard and screen-reader passes | Paid scanners |
| Screenshots (Agents 8, 12, design arena) | Chrome DevTools MCP `take_screenshot`, or a local headless browser (Playwright, Puppeteer) | Hosted screenshot APIs |
| Reference and competitor research (Agents 15, 11) | The host agent's built-in web search and page fetch, on public pages only | SERP APIs, Ahrefs, Semrush, Similarweb or any SEO tool that needs a key |
| AI discoverability (Agents 6, 13) | `llms.txt` checks with `curl`; the host agent's own web search for brand/category queries | Paid AI-visibility trackers; logging in to ChatGPT, Perplexity or others |
| Icons | Bundled Material Symbols in `assets/icons/` (Apache 2.0) | Paid icon packs |
| Fonts | System fonts, self-hosted open-licence fonts, or the Google Fonts CDN (no key) | Paid font services that need an account |
| Images | User-supplied assets, CSS/SVG artwork, open-licence images the user approves (keep attribution) | Paid image-generation or stock APIs |
| In-product AI agent (Agent 14) | Google ADK on a local Ollama model (`qwen2.5:1.5b` by default) | Gemini, OpenAI, Anthropic, Groq or any hosted model API |
| Deploy (post-launch) | Whatever free hosting the user already uses, or a local preview | Signing the user up for hosting |

## Reporting

In `ORCHESTRATOR.md`, keep a **Cost** line: `Cost: $0 — no API keys or paid services used.` If any task was skipped because it needed a paid service, list it there with the free alternative offered.

## Research-provider compatibility

See [tool routing](research-tools.md). Agent-Reach uses only keyless public channels
without importing authenticated sessions. BrowserAct's documented API requires a
key; OpenComputer's documented cloud route requires login. Both are disabled by
default. Use only actual configured capabilities after explicit user authorization
to override this policy for the named provider. Record exceptions accurately
instead of emitting an unverified Cost: $0 claim. Host public search/fetch and a
local browser remain the default fallback.
