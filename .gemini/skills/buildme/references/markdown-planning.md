# Markdown planning contract — before implementation

These five living Markdown artifacts are the basis and rules for every Buildme
build. After Grill Me, Agent 0 dispatches Agent 21 to create/reconcile all five
and Agent 22 to independently review them before authorizing any application
implementation or Spec Kit implement command. Templates are
starting points, not completed project documents. Do not produce pretend app
specifications for the skill repository merely because Buildme itself is updated.

## Source and adaptation

Reviewed [GitHub Spec Kit](https://github.com/github/spec-kit) at
[c43849408ac0](https://github.com/github/spec-kit/tree/c43849408ac0de2ca6a52f14eaae71449776057b).
Its spec-driven sequence (constitution, specify, plan, tasks, implement) fits the
requested artifact gate. Reuse an existing installation when available. Buildme's
adapter adds repository context, specialist contracts, full dispatch and ordered
quality gates; Spec Kit is not a second orchestrator. No upstream source code is
vendored. The existing Superlite adapter consumes these tasks and evidence rather
than generating a second plan or task graph.

## Paths and ownership

Agent 21 (planning-agent) is the sole author of the five documents and their
revisions. Agent 22 (planning-reviewer) owns only planning-review.md and must not
edit the documents under review. Agent 0 coordinates specialist inputs, repair
dispatch and the path/approval checkpoint; it cannot self-award review PASS.
Default to project-root project_context.md, constitution.md, spec.md, plan.md
and tasks.md. Preserve existing content and reconcile changes; never
blindly overwrite an existing constitution or another feature's spec/tasks.

If Spec Kit is already in use, preserve its actual resolved paths: commonly
.specify/memory/constitution.md and specs/<active-feature>/spec.md, plan.md,
tasks.md. Inspect the installed version rather than assuming paths. Keep
project_context.md at the project root and root constitution.md/spec.md/plan.md/
tasks.md as clearly labeled indexes linking to the active canonical documents,
with feature ID and current revisions; do not maintain divergent content copies.
Workers read the canonical targets, not just indexes. Record the path map,
active feature, revisions and approval evidence in ORCHESTRATOR.md. Switching
features updates indexes; it never overwrites another feature's artifacts.

## Sequence and responsibilities

1. **Repository scan -> project_context.md.** Agent 21 scans existing code and
   records identity, stack/library versions, architecture, data/auth, tests, CI,
   design system and current constraints with file/command evidence. Never expose
   secrets. This scan can begin in Phase 0; after Grill Me reconcile its findings
   with the confirmed product answers. Greenfield work says what does not exist.
2. **Constitution -> constitution.md.** Derive durable non-negotiable principles
   from existing project rules and confirmed answers. Assign C001-style IDs,
   enforcement checks and an amendment process. Preserve established principles.
3. **Specify -> spec.md.** Convert Grill Me/BUILD_BRIEF.md and references into
   prioritized US001 stories, FR001 functional and NFR001 nonfunctional requirements,
   acceptance scenarios, exclusions and resolved material questions.
4. **Plan -> plan.md.** Synthesize technical strategy, architecture updates,
   schema fields/types/migrations, API contracts, state/cache policies, tool
   configurations, security/operations, risks, validation and constitution checks.
   Consult frontend-architect then architecture-agent in planning-only mode for
   rendering-decision.md and architecture annexes. Consult state/data, caching,
   security and observability owners for contracts/prerequisites. These passes
   produce documents only, not code, migrations, installations or deployment.
5. **Tasks -> tasks.md.** Convert the plan to sequential T001, T002, ... work units
   with stories/requirements/principles, dependencies, single owners, exact files,
   outputs, acceptance commands and evidence. Preserve Phase 3 dispatch order.
6. **Independent review -> implementation.** Agent 22 reads the complete actual
   documents and repository evidence, verifies traceability and writes
   planning-review.md with PASS / FAIL / BLOCKED and exact findings. Agent 0 routes
   repairs to Agent 21 and re-review to Agent 22; only a current PASS permits
   Agent 0 to record READY in ORCHESTRATOR.md and present the set with the brief.
   Reuse existing explicit scope approval;
   request clarification only for genuinely unresolved material decisions.
   Only READY documents permit application implementation / speckit implement.

The five files must exist, contain substantive project-specific content, agree
with one another and current repository facts, and have resolved material
unknowns. Unfilled prompts, copied template examples or headings alone are not
READY. Every in-scope requirement maps to a task and acceptance check. Every task
has unique ID, owner, dependency, implementation scope and retest criteria;
dependencies are acyclic and ready tasks reference the current approved revisions.
Record missing capabilities as BLOCKED; absence of a Spec Kit installation alone
does not block use of the complete bundled-template adapter.

## Authority and conflict handling

constitution.md is the highest **project-level** authority. Host/system/developer
instructions and explicit user-authorized amendments still apply. Below the
constitution, spec.md defines required behavior, plan.md defines implementation,
and tasks.md permits bounded execution; project_context.md supplies observed
facts. BUILD_BRIEF.md and research/design/specialist annexes must agree with these
sources. A worker prompt, local preference or generated code cannot silently
weaken the constitution. Facts contradicting a proposal require reconciliation,
not falsifying project_context.md.

When a requirement conflicts, pause the affected work. Agent 0 coordinates a compliant approach or the explicit user amendment needed;
Agent 21 records the reason/version and updates spec -> plan -> tasks plus impacted
annexes. Agent 22 re-reviews the changes before affected implementation resumes. Do not ask again for already authorized routine choices. Retain the
existing mandatory quality gates and two-round repair cap.

## Spec Kit commands and truthful fallback

"speckit constitution / specify / plan / tasks / implement" are logical stages,
not assumed shell executables. Use the installed host's real command/skill syntax.
Older integrations may expose /speckit.constitution, /speckit.specify,
/speckit.plan, /speckit.tasks and /speckit.implement; current integrations may use
/speckit-constitution, /speckit-specify, /speckit-plan, /speckit-tasks and
/speckit-implement. Inspect availability and version. These are agent invocations,
not commands to pass blindly to Bash. Never run implement before the document gate.

If unavailable, Agent 21 uses the five bundled templates to execute equivalent
planning and records `Mode: Buildme Markdown adapter; native Spec Kit not run`.
No Spec Kit CLI installation, initialized project, account or successful command
execution is implied by installing Buildme. Do not run init over an existing
project without first reviewing its changes. No new model service is required.

## Worker and review contract

Every implementation handoff includes the resolved five paths/revisions, relevant
constitution IDs, spec/story IDs, plan sections and Txxx task IDs. Workers read
the documents before editing, implement only assigned ready tasks, and attach
actual commands/results/evidence. Sequential execution is the default; [P] tasks
may run concurrently only with explicit authorization in tasks.md, satisfied
dependencies, disjoint ownership and preserved dispatch/gate order.

Agent 0 tracks runtime checkpoint/status in ORCHESTRATOR.md; tasks.md remains the
authoritative task list (do not duplicate it there). Mark a task DONE only after
its output and acceptance evidence are verified. QA reviewers check both behavior
and constitution/spec/plan compliance. Send failures to the original worker and
review again; unresolved mandatory FAIL/BLOCKED findings prevent ship.

For new scope or discoveries, update context where facts changed, amend the
constitution only when authorized, then reconcile spec/plan/tasks before further
affected code. Keep revisions and a change record; do not rewrite documents just
to excuse already-built deviations. Rerun impacted acceptance/security/mobile/
architecture/observability gates and keep the final anti-slop sign-off last.

## Independent planning-review gate

Always dispatch [Agent 21](../agents/planning-agent.md) then
[Agent 22](../agents/planning-reviewer.md) in Phase 2.5. Use the
[review report template](../templates/planning-review.md). Preserve every existing
role and the implementation dispatch order. Planning author/reviewer work can
start before READY because it creates and verifies that gate, but neither agent
may implement application code during this stage. Agent 0 remains coordinator.

Agent 22 reports per-document and per-check PASS / FAIL / BLOCKED, exact finding
IDs, severity, file/section, linked principle/requirement/task, evidence, repair
owner Agent 21 and objective retest. It verifies repo facts, constraints, schema/
tools/architecture feasibility, requirement coverage, ordered task dependencies,
canonical links and no material unknowns or unfilled template prompts. The author
cannot write the review report; the reviewer cannot patch the five source files.
Use separate host agents/contexts when available; a host with no delegation must
disclose a sequential read-only reviewer pass and its limited independence.

Record actual canonical paths, revisions and SHA-256 fingerprints of all five
documents and material annexes in planning-review.md. Agent 0 validates review
freshness against the current files before READY. Missing/stale review, FAIL or
BLOCKED prevents implementation; file existence or a planner self-check cannot
substitute. Two repair rounds maximum: Agent 21 fixes -> Agent 22 rechecks. Retain
open findings and escalate unresolved failures at the cap, without a waiver.

Any material change to scope, principles, requirements, schema, strategy, task
ownership/dependencies/acceptance or an input fact/annex invalidates review PASS
and Phase 2.5 READY for affected work. Agent 21 updates the dependent documents,
then Agent 22 re-reviews before continuation. Routine tasks.md status/evidence
updates after verified execution are the sole progress-only exception: Agent 0
must inspect and record the diff proving no scope, owner, dependency, acceptance
or other governing content changed, and record the new progress fingerprint with
the approved baseline. Mixed or ambiguous changes require Agent 22 review. Never
use this exception to mark unverified tasks DONE or weaken a requirement.
