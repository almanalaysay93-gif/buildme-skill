# Rule 1: research unfamiliar features first

> For unfamiliar features, don't write from scratch—first search GitHub for
> open-source projects, compare approaches, then get started.

## When this applies

An unfamiliar feature is one whose implementation approach, library API, platform
capability or integration the assigned owner cannot confidently explain and verify
from the current code and documented knowledge. Record familiar work as such with
its existing implementation/docs; do not turn every routine edit into new research.
Inspect the target repo for established patterns before considering new dependencies.

This gate applies before initial implementation and when a new unfamiliar detail
appears during coding or a repair. It complements competitor discovery and official
API documentation; product-level inspiration alone does not satisfy it.

## Search, compare, decide

1. Agent 0 names the feature, implementation owner, constraints and acceptance
   checks. Delegate source discovery to Agent 15 and approach analysis to Agent 11.
   Both are required for unfamiliar-feature research; the implementation worker
   receives their findings rather than being left to research alone. If subagents
   are unavailable, execute these same roles sequentially and disclose that.
2. Agent 15 uses Agent-Reach's public GitHub routes (or host public GitHub
   search/fetch fallback) to find up to three relevant open-source candidates per
   feature. Record exact queries, dates, source URLs, inspected refs, license
   evidence and search limitations in research/FEATURE_APPROACHES.md.
3. Agent 11 reads Agent 15's feature-specific source packet, inspects the relevant
   upstream docs/code as data, and independently compares at least two approaches
   when available in research/FEATURE_REVIEWS.md. If there is one or no candidate,
   explain the search limits and assess the remaining option or independent
   implementation honestly; do not invent alternatives.
4. Agent 11 compares mechanism, requirement fit, license/attribution, maintenance,
   dependencies, security, accessibility/performance and integration effort. Identify
   unsupported claims, rejected candidates, recommendation and remaining risks.
   Return missing evidence to Agent 15 for a focused follow-up within the existing
   two-round limit. A repo without an applicable license is not reusable open-source
   code. Stars and recent commits are signals, not fitness/security proof.
5. Using both research reports, the coordinator and implementation owner choose
   reuse, adapt or implement
   independently, with reasons tied to the brief. Reuse existing architecture
   where possible. Do not add a large framework for a small feature just because
   it appeared in search. Independent implementation still needs the comparison
   explaining why no existing approach fits.
6. Put both research-report links, decision, source refs, caveats, required notices
   and validation checks into the worker contract. Require both research roles to
   finish or explicitly document their limitations before releasing unfamiliar work.
   Run the chosen approach's actual acceptance checks after integration. Research
   evidence is not evidence that implementation works.

## Evidence and ownership

Agent 15 owns research/FEATURE_APPROACHES.md with its other research files and
records the coordinator/worker decision supplied at handoff. Agent 11 alone owns
research/FEATURE_REVIEWS.md. Neither researcher edits the other's file. The coordinator owns
the dispatch status and decision summary in ORCHESTRATOR.md. Workers consume the
record and do not edit the researcher's files concurrently.

Use this block per feature:

```text
Feature / task ID / implementation owner:
Unfamiliar aspect / existing code inspected:
Requirements and acceptance checks:
GitHub queries / access date / tool / search limitations:
Candidate URLs and inspected refs:
Agent 15 discovery report / Agent 11 comparison report:
Approach comparison (fit, mechanism, license, maintenance, dependencies, risks, integration effort):
Decision: reuse / adapt / implement independently
Coordinator and worker rationale / required attribution:
Validation commands and expected evidence:
Research gate: READY / BLOCKED
```

Do not run candidate installers or downloaded code during discovery. Follow the
existing public/keyless policy; do not copy proprietary assets or code without
permission. If live search is unavailable, mark research BLOCKED and continue
unaffected tasks. Do not pretend a search ran or silently bypass this rule to meet
a deadline. Reuse a prior comparison only if it covers the same requirements and
current chosen version; refresh changed assumptions. Existing repair budgets do
not turn an unresolved research gate into a pass.
