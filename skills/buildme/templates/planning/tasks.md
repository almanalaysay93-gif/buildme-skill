# Implementation tasks

Status: DRAFT — replace the example structure with actionable tasks.
Feature / revision / canonical path / plan revision / spec revision:

## Execution rules
Use unique sequential T001, T002, ... IDs. Every task maps to US/FR/NFR and C
principle IDs, a plan section, one agent/owner, allowed files, explicit dependency
IDs, outputs, acceptance commands/evidence and status. Dependencies must refer to
existing earlier tasks; no cycles, duplicates, orphan requirements or implicit work.
Execute sequentially by default in Phase 3 order. Parallel work requires an
explicit [P] marker, satisfied dependencies and disjoint ownership; never infer it.

## Ordered work
For each real task use this structure (do not ship this example as a task):

### T001 — action and observable outcome
- Story / requirements / principles / plan section:
- Owner / allowed files / inputs / outputs:
- Depends on: none (or explicit earlier task IDs).
- Acceptance commands and expected results / evidence paths:
- Status: TODO (then IN_PROGRESS, BLOCKED, REVIEW, DONE).
- Actual results / reviewer / repair round:

Include implementation, data/schema migration where needed, security, bug,
mobile/performance/a11y, observability, snapshots, discoverability/content,
architecture/anti-slop and final review tasks. Retain all existing role dispatches;
record live-only waiting separately from pre-ship blockers.

## Coverage and verification
Map every in-scope requirement/story and constitution principle to tasks and tests.
A task is DONE only after outputs exist and its checks are reviewed with actual
evidence. A checkbox, tool success envelope or source scan alone is not full QA.

## Change record
Revision, new/superseded tasks, affected requirement/plan versions, reason and
verification invalidated by the change. Preserve completed evidence and task IDs.
