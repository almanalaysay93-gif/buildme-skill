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
   checks in the task contract. Assign Agent 15 the relevant feature research slice.
   If no subagents are available, execute the same roles sequentially.
2. Use Agent-Reach's public GitHub routes (or host public GitHub search/fetch when
   unavailable). Search by actual feature, stack/platform and constraints. Record
   exact queries, access date and source links in research/FEATURE_APPROACHES.md.
3. Inspect up to three relevant open-source candidates per feature. Compare at
   least two approaches when available; do not fabricate a second candidate if
   search finds only one or none. Record the search coverage and its limits.
4. Compare implementation mechanism, requirement fit, license compatibility and
   attribution, maintenance/version evidence, dependencies, security implications,
   accessibility/performance considerations and cost of adapting it to this repo.
   A GitHub repo without an applicable license is not reusable open-source code.
   Stars and recent commits are signals, not proof of fitness or security.
5. The coordinator and implementation owner choose reuse, adapt or implement
   independently, with reasons tied to the brief. Reuse existing architecture
   where possible. Do not add a large framework for a small feature just because
   it appeared in search. Independent implementation still needs the comparison
   explaining why no existing approach fits.
6. Put the decision, source refs and required notices into the worker contract.
   Run the chosen approach's actual acceptance checks after integration. Research
   evidence is not evidence that implementation works.

## Evidence and ownership

Agent 15 owns research/FEATURE_APPROACHES.md with its other research files and
records the coordinator/worker decision supplied at handoff. The coordinator owns
the dispatch status and decision summary in ORCHESTRATOR.md. Workers consume the
record and do not edit the researcher's files concurrently.

Use this block per feature:

```text
Feature / task ID / implementation owner:
Unfamiliar aspect / existing code inspected:
Requirements and acceptance checks:
GitHub queries / access date / tool / search limitations:
Candidate URLs and inspected refs:
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
