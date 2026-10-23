# Mandatory UX laws workflow

Read the complete [user-supplied UX laws reference](ux-laws.md) before planning,
designing, building or auditing an interface. The reference is bundled unchanged;
this file connects it to this skill's execution and reporting.

## Planning and specialist handoff

In the existing design/execution plan, map all 14 laws to the actual pages, flows,
components or scenes. State how each relevant law will be satisfied and tested.
For a law without a corresponding interaction, record the reason explicitly.
Pass the relevant mapping and acceptance checks to every design, copy, motion,
implementation and review specialist. The coordinator owns the combined audit;
individual specialists return evidence and fixes for their assigned work.

Keep the reference's 44×44 CSS-pixel touch-target and interaction-feedback targets
as explicit checks. Context-dependent option counts, chunk sizes and placement
recommendations require reasoning about the actual task; counting items alone is
not evidence of usability. Preserve applicable accessibility/security constraints:
flexible input handling must still validate data, resolve ambiguity and protect
trust boundaries. Do not weaken authentication or server validation for Postel's law.

## Mandatory audit, fixes and re-audit

After every build or significant change, create/update `UX_LAWS_AUDIT.md` using the
reference's complete 14-row audit template. Record build/version, scope, viewport,
device/browser, reviewer, date and evidence paths. Review actual UI behavior and
rendered output where available, alongside code. For every law record exactly
`Compliant`, `Partial` or `Violated`, concrete evidence, and any required fix.

- Every Partial/Violated finding needs an owner, reproduction, expected behavior,
  repair and retest evidence. Resolve findings, then re-audit affected behavior
  and confirm coverage of all 14 laws. Retain previous results as audit history.
- A justifiably Partial result needs a specific scope/context reason, evidence,
  impact and remaining limitation. Non-applicability must be explicit (for example,
  a rendered film has no clickable controls); never claim tested compliance for it.
- Missing evidence/tooling is an unresolved Partial, with the containing quality
  report marked BLOCKED. It is not a justified exception or a pass. Label code-only
  conclusions clearly and do not infer measured latency from implementation.
- Completion requires no Violated rows and only Compliant or documented,
  justifiably Partial rows. Necessary browser, performance or accessibility checks
  remain mandatory under the skill's existing quality gates.
- Use the invoking skill's repair cap. When it is reached, retain FAIL/BLOCKED,
  report unresolved findings and escalate; never waive a defect or retry forever.

The audit is required regardless of optional UX tooling. Link it from the existing
quality report and delivery summary. No deployment, publishing or external messages
are authorized by this workflow.
