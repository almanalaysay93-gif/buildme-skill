# Project constitution

Status: DRAFT — fill from confirmed requirements; preserve existing principles.
Version / date / canonical path / amendment record:
Authority: highest project-level rulebook, subject to host instructions and
explicitly authorized user amendments. Worker prompts cannot silently override it.

## Non-negotiable principles
Assign stable IDs (C001, C002, ...). Each principle has MUST/MUST NOT wording,
rationale, scope, owner and a measurable enforcement check. Cover approved stack,
monolith + feature modules by default, no direct cross-feature imports, token-only
colors/spacing, rendering/client boundaries, data/auth/security/privacy,
accessibility/mobile, caching/invalidation, observability and delivery constraints.
Record which requirements apply to this project; never invent extra product scope.

## Source-of-truth rules
project_context.md records observed facts; spec.md defines required behavior;
plan.md chooses a constitution-compliant implementation; tasks.md authorizes
bounded work. Design/research/specialist documents are linked annexes, not competing
plans. Identify canonical paths and revisions, including existing Spec Kit files.

## Quality and evidence rules
Define mandatory gates, measured budgets, test evidence, repair/review routing,
missing-capability behavior and deployment authorization. No FAIL/BLOCKED mandatory
gate can be silently waived. Existing two-round repair cap remains in force.

## Amendment process
Record an explicit user-authorized change with reason, version and impacted
requirements/tasks. Pause affected implementation on conflict; update dependent
spec/plan/tasks and recheck compliance before resuming. Do not weaken rules to
make an already-written implementation pass.
