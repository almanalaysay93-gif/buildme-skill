# Technical execution plan

Status: DRAFT — complete before tasks are authorized.
Feature / revision / canonical path / spec revision / constitution version:

## Technical strategy and repository impact
Chosen stack and versions, reuse/adapt decisions with Agent 15/11 research,
architecture updates, folder tree, feature modules, dependencies, owners,
server/client boundaries and existing behavior to preserve. Link project_context.md.

## Rendering and architecture annexes
Link rendering-decision.md (per-route strategy, why, client exclusions or CSR
SEO/LCP mitigation), architecture.md and architecture-rules.json. Planning-only
Agent 2 and Agent 20 prepare these before code. Tokens, theming, flags, config
and dependency rules must agree with this plan and the constitution.

## Data schema and API contracts
List exact entity/table fields and types, nullability, defaults, keys, indexes,
constraints, relationships, authorization, migrations/backfill and rollback.
Specify API requests/responses, errors, pagination and compatibility. For no
schema change, record why. Assign an actual backend implementation owner.

## State, networking, caching and offline
State owners/query keys, invalidation, retry/backoff/cancellation, idempotency,
cache keys/TTL/version/purge, offline fallback and sync/conflict policies.
Link specialist design annexes; do not defer material choices until coding.

## Security, quality and operations
Applicable security controls/CSP/headers/cookies, mobile/a11y and performance
budgets, tests, Sentry/alerts/source maps, privacy/consent, rollout/canary and
rollback. Specify tools, versions, config files, prerequisites and local commands;
record missing capabilities honestly. Never put secret values in this document.

## Constitution compliance
| Principle ID | Plan decision / section | Enforcement check | Result / evidence |
| --- | --- | --- | --- |

Every applicable principle needs a row; unresolved violations block implementation.
Record justified non-applicability without weakening mandatory project rules.

## Delivery sequence and risks
Dependencies and handoffs in Buildme Phase 3 order, affected routes/files,
verification commands, risks/mitigations, capability blockers and rollback scope.

## Change record
Plan revision, reason, affected requirements/tasks and renewed compliance checks.
