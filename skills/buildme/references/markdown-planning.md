# Markdown planning contract — before implementation

These five living Markdown artifacts are the basis and rules for every Buildme
build. After Grill Me, Agent 0 must create/reconcile all five before authorizing
any application implementation or Spec Kit implement command. Templates are
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

Agent 0 owns the five documents and their version/approval record. Specialists
supply planning inputs through the coordinator; only a designated owner edits a
file. Default to project-root project_context.md, constitution.md, spec.md,
plan.md and tasks.md. Preserve existing content and reconcile changes; never
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

1. **Repository scan -> project_context.md.** Agent 0 scans existing code and
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
6. **Consistency gate -> implementation.** Agent 0 reviews the complete documents
   and traceability, records READY or BLOCKED with reasons in ORCHESTRATOR.md,
   and presents them with the brief. Reuse existing explicit scope approval;
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

When a requirement conflicts, pause the affected work. Agent 0 either chooses a
compliant approach or obtains the explicit user amendment needed, records its
reason/version and updates spec -> plan -> tasks plus impacted annexes before
resuming. Do not ask again for already authorized routine choices. Retain the
existing mandatory quality gates and two-round repair cap.

## Spec Kit commands and truthful fallback

"speckit constitution / specify / plan / tasks / implement" are logical stages,
not assumed shell executables. Use the installed host's real command/skill syntax.
Older integrations may expose /speckit.constitution, /speckit.specify,
/speckit.plan, /speckit.tasks and /speckit.implement; current integrations may use
/speckit-constitution, /speckit-specify, /speckit-plan, /speckit-tasks and
/speckit-implement. Inspect availability and version. These are agent invocations,
not commands to pass blindly to Bash. Never run implement before the document gate.

If unavailable, Agent 0 uses the five bundled templates to execute equivalent
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
