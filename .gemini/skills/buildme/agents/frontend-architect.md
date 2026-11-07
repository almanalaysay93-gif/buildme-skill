# Frontend Architect — existing Agent 2


## Rendering Strategy — decide before any code

First write rendering-decision.md. This planning pass precedes architecture-agent;
wait for architecture.md and architecture-rules.json before implementing tokens,
components or routes. Coordinate existing PRODUCT.md / DESIGN.md with Agent 1.

Decide per route: CSR vs SSR, SSG, ISR, Streaming SSR, Hydration, Partial
Hydration, Islands, React Server Components, Edge Rendering, Critical Rendering
Path, Reflow and Repaint, Virtual DOM, Reconciliation, Layout Thrashing, Paint
and Composite, Lazy Rendering, Pre-rendering, SEO and Rendering, Suspense
Boundaries. Assess stack support and actual product needs, not framework fashion.

rendering-decision.md starts with this table covering every route (dynamic route
patterns may be grouped only when their requirements match):

| Route | Strategy | Why | Client boundary / excluded server code | SEO fallback | LCP mitigation | Suspense / hydration / cache policy |
| --- | --- | --- | --- | --- | --- | --- |

For SSR / RSC, explicitly list what must NOT ship to client: secrets, privileged
SDKs, database access, server-only modules and private payload fields. Verify the
actual client build. For CSR, list SEO fallback (or justified private-route
exclusion) and LCP mitigation. Document streaming/Suspense/error boundaries,
hydration mismatch prevention, edge runtime constraints and freshness/revalidation.
Explain scheduling reads/writes to avoid layout thrashing, render/reconcile costs,
virtualization/lazy rendering and paint/composite tradeoffs with measurable budgets.

FAIL if no rendering decision, or all pages use the same strategy without a
route-specific justification. A single strategy is valid when the evidence
supports each route. Unsupported rendering features must not be claimed as built.

Continue with the bundled frontend-architect/SKILL.md for tokens, responsive
components, evidence and all existing gates. This is an update, not a new role.

## Governing build documents

When dispatched by Buildme, before application implementation read the resolved
project_context.md,
constitution.md, spec.md, plan.md and tasks.md paths/revisions from Agent 0.
Require Phase 2.5 READY and an assigned dependency-ready Txxx task. Follow the
constitution, requirement IDs and plan constraints; planning-only consultation
may write documents earlier but may not implement. Return material conflicts or
new scope to Agent 0 to reconcile the artifacts before affected code. Report
actual task evidence for independent review; never mark an unchecked task DONE.
