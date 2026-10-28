# Free SEO integration decision

Source review: AgriciDaniel/claude-seo at
6be93f45064ffbadced572b5d5c95f55fd263af0 (MIT), inspected 2026-10-28.
Reviewed: README, requirements, technical/visual/performance/schema agent docs,
parse_html.py, sitemap_discovery.py and schema_ecommerce_validate.py.

| Approach | Fit | Limitations | Decision |
| --- | --- | --- | --- |
| Entire upstream plugin and runtime | Broad audit coverage | Claude-specific model routing, large runtime plus Google API/report dependencies, redundant orchestration and optional paid routes | Not activated |
| Existing Buildme Lighthouse and llms.txt checks alone | Local and compatible | Lacks an explicit technical SEO/schema scope and report/repair contract | Retain and extend |
| Selected pinned MIT checklists + Product validator + bounded local artifact runner | Ships in existing install, works without keys/new dependencies, fits Agents 6/10 | Static artifacts cannot prove runtime/indexing or field metrics; browser review remains mandatory | Selected |

The existing orchestrator owns dispatch. No new numbered role or model provider
is introduced. Four upstream audit reference files, its Product validator, MIT
license and provenance are bundled. All other checks use the current host model,
Python stdlib, local browser and local Lighthouse. Existing Agent-Reach remains
for public research, not a new SEO-service dependency.

Scope excludes paid extensions, provider API clients, Google account setup, ranking
promises, automatic submissions and unknown-license assets. All upstream claims
about current Google features require current official-source confirmation.
Validation lives in tests/test_free_seo_audit.py and the generated-product audit
contract; package tests are not evidence a particular site passed SEO.
