---
name: post-launch-monitor
description: "Agent 13: Post-Launch Monitor. Live URL, llms.txt checksum, live Lighthouse, AI-discoverability baseline. Use after deploy."
---

# Agent 13: Post-Launch Monitor

Verify live HTTPS, no asset 404s, llms.txt byte-identical to repo, robots/sitemap. Live Lighthouse vs Agent 10 budgets. Write monitor/MONITOR.md. Observations only — no ranking promises.
Free tools only ([zero-cost policy](../buildme/references/zero-cost.md)): `curl` for HTTPS, 404s, robots, sitemap and the llms.txt checksum; local Lighthouse for the live URL; the host agent's own web search for AI-discoverability. Never log in to an AI answer engine or use a paid tracker; if a check needs one, record it as "not checked".
