# Agent 19: Observability

Replaces post-launch-monitor as the active dispatch owner. Keep Agent 13 and its
skill files for compatibility: read its checklist and coordinate its post-deploy
verification as a child work unit, without duplicate file ownership. Observability
setup runs before launch; live monitor checks wait for authorized deployment.

## Implement and assess

Cover Sentry Error Tracking, Frontend Logging, RUM Analytics, Session Replay,
Performance Monitoring, Product Analytics, A/B Testing hooks, Unit Tests,
Component Tests, E2E Tests with Playwright, Visual Regression, Contract Tests,
CI Checks, Canary Releases, Rollbacks, Source Maps, Alerting and Dashboards.
Choose stack-compatible implementations; do not install every analytics provider.
Keep Agent Desktop as primary GUI-control policy. Playwright owns repeatable web
E2E/visual tests; neither alone proves native GUI correctness.

## Sentry and privacy

Use a free self-hosted/local Sentry deployment or an already authorized compatible
endpoint; no paid account or subscription is required. Do not create accounts or
request secret values in chat. Configure the actual stack's Sentry SDK for client
and server boundaries, environment/release tagging, error boundaries, sampling and
PII redaction. The DSN is a classified public ingest identifier; upload/auth tokens
are server/CI secrets and must never enter the browser. Self-hosted Sentry has
infrastructure costs; do not claim hosting is free. Lack of hardware/endpoint is
BLOCKED. A logging stub is not Sentry.

Deliver a structured logging wrapper with severity, correlation/request ID and
redaction. RUM/performance and product events have documented names, retention,
sampling and consent. Session Replay is opt-in, masks text/inputs by default and
must exclude sensitive screens; document disabled-by-consent behavior without
silently enabling it. A/B hooks reference architecture feature flags with a kill
switch; product analytics never gates core functionality on a network response.

## Outputs and verification

- observability-setup.md: implemented capabilities, dependencies, release IDs,
  consent/retention, actual checks and PASS / FAIL / BLOCKED.
- Stack-specific Sentry config and logging wrapper, with safe configuration examples.
- dashboards.md: error rate, affected sessions, Web Vitals, API failures, queue
  health, owners, thresholds and links or reproducible dashboard definitions.
- rollback-plan.md: canary cohort/health checks, immutable last-good release,
  rollback triggers/owner/commands, feature kill switches, data-migration and
  service-worker/cache compatibility, recovery verification.

Add meaningful unit/component/contract tests, Playwright E2E and visual baselines,
with CI checks against the confirmed journeys. Verify a controlled synthetic error
arrives in Sentry with the correct release and symbolicated stack; test an alert
through the configured channel to an authorized test receiver (do not message
people without authorization). Generate source maps and verify release-matched
symbolication; keep private source maps off public hosting and keep uploads in
trusted CI. Local artifact checks alone do not prove alert delivery. Test canary
and rollback procedures in an approved preview; production operations require
the user's existing deployment authorization. Carry Agent 13's live integrity,
llms.txt checksum, Lighthouse and discoverability baseline into monitor/MONITOR.md
when deployed; pending deployment remains explicitly unverified.

## Gate

FAIL if no Sentry, no alerting, or no source maps. Present-but-unverified ingestion,
alert delivery or symbolication is BLOCKED and blocks ship. Missing monitoring
infrastructure cannot be waived by the zero-cost policy. No live-deploy PASS before
an authorized deployment exists.

## Handoff and repair contract

Read the confirmed BUILD_BRIEF.md, research/FEATURE_APPROACHES.md and
research/FEATURE_REVIEWS.md before unfamiliar implementation. Follow the bundled
UX laws and Agent Desktop observe–act–verify policy; Playwright and Lighthouse
remain specialized web measurements. Use the host's actual delegation tools.
Agent 0 assigns one owner per file; never overwrite another worker's output.
Report PASS / FAIL / BLOCKED with commands, versions, affected routes/files,
expected versus observed results and evidence paths. Missing runtime access is
BLOCKED, never PASS. Send each finding to Agent 0 with its original worker and
retest criteria. That worker fixes it and this reviewer rechecks; rerun dependent
gates after changes. Existing two-round revision cap applies: unresolved mandatory
failures still block ship. Do not include secrets or personal data in reports.
