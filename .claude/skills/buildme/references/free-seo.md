# Free SEO quality integration

Uses a [pinned Claude SEO subset](../vendor/claude-seo/NOTICE.md) under its MIT
license. Read [the integration decision](seo-integration-decision.md) for scope.
No extra numbered agents, accounts, API keys, credits or paid services are added.
Do not activate upstream model choices or blindly run upstream install commands.

## Scope and owners

Agent 0 records SEO scope in BUILD_BRIEF.md: public indexable routes, private or
native-only scope, canonical origin, sitemap strategy, applicable schema, language
variants and expected runtime evidence. Mixed apps audit only the approved public
routes; private/account pages must not be exposed to satisfy SEO checks.

- Agent 6 owns SEO_SCOPE.md, SEO_AUDIT.md and reports/seo-static.json. It audits
  technical SEO, final content metadata, crawl controls, sitemaps, schema and
  grounded llms.txt after Phase 5. It does not promise rankings or AI citations.
- Agent 10 owns PERF_A11Y_AUDIT.md and browser/Lighthouse artifacts. Reuse its
  mobile, desktop, keyboard, accessibility and performance evidence; do not start
  a duplicate performance ensemble. Agent 12 supplies matched screenshots.
- The coordinator assigns fixes to existing owners: Agent 2 for HTML/routing,
  Agent 9 for copy, Agent 5 for motion, and the explicitly named backend owner for
  server headers/redirects. Reviewers return findings; the responsible worker fixes.

For private dashboards/native-only apps, record NOT_APPLICABLE with rationale for
search indexing checks. Functional, mobile and accessibility gates still apply.

## Runnable local checks (no network or extra dependencies)

The normal Buildme installer copies this runner and the upstream Product validator
with the buildme skill. It requires Python 3.10+ already used by the installer.
Use the project's actual build output, not an assumed dist directory:

```bash
python3 <buildme-skill-directory>/scripts/free_seo_audit.py   --site-dir <actual-build-output> --base-url https://approved-site.example   --output reports/seo-static.json
```

Repeat `--page relative/page.html` to restrict the approved public scope. Use
`--require-schema` only where applicable schema is an agreed requirement. Use
`--product-schema` only on the selected Product pages; this runs the bundled
Claude SEO Product validator. Review contextual recommendations against current
[Google Product documentation](https://developers.google.com/search/docs/appearance/structured-data/product).

The runner checks HTML titles, descriptions, viewport, accidental noindex/robots
blocks, canonical declarations, image signals, JSON-LD syntax and local sitemap
XML. Missing recommended metadata produces warnings, not invented ranking rules.
It bounds local reads, refuses out-of-scope file traversal and never fetches URLs.
CLI exit zero means artifact checks completed without static failures, NOT full
SEO approval. `overall_status` remains BLOCKED until required runtime reviews are
recorded in SEO_AUDIT.md. Page caps and every uninspected route remain explicit.

## Runtime checks and truthful evidence

Agent 6 uses approved local/staging pages and the host/local browser to verify:
served status and redirects, response headers, intended robots rules, actual
sitemap declarations/indexes and served XML, canonical destinations, metadata and
rendered JSON-LD matching visible content. SSR/CSR/SPAs need real rendered-page
review; an empty source shell or successful compilation cannot pass this gate.
No URL submissions, IndexNow notifications, account logins or provider APIs run.

Agent 10 checks matched desktop/tablet/mobile views, navigation, visible primary
content/CTA where appropriate, no overflow, content/schema parity, keyboard/focus,
44px Buildme touch targets and 14 UX laws. Use local Lighthouse/Chrome DevTools and
an available local browser, not paid scanners or hosted screenshot services.

Record two comparable local Lighthouse runs and the worse diagnostic result,
commands, tool versions, device/viewport and artifacts. Lighthouse lab results do
not establish field INP or real-user CWV. Interaction traces are local measurements,
not a p75 field verdict. If field data is unavailable, report it as unavailable;
never provision Google credentials or infer ranking/traffic/AI-citation gains.

## Mandatory finding → worker → recheck loop

Use [the SEO report template](../templates/SEO_AUDIT.md). Findings require a stable
ID, affected route/file, severity, observed/expected behavior, source/evidence,
assigned worker, exact fix, and retest evidence. Agent 0 dispatches fixes to that
worker, and Agent 6/10 rerun affected checks. Code changes in Phase 6 require the
relevant Phase 5 gates to run again. Do not edit concurrently with the worker.

Keep the existing two-revision limit per agent. At the cap, unresolved mandatory
failures remain FAIL; missing required evidence remains BLOCKED. Report the exact
remaining work. Neither a caveat, a missing paid tool nor a static PASS waives an
applicable requirement. Advisory warnings may be accepted with documented reasons.
Overall public-site SEO PASS requires all agreed static and runtime checks to
pass, with no mandatory FAIL/BLOCKED findings. Do not mark a site complete first
and offer the required audit afterwards.
