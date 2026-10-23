# Superlite execution adapter

This package adapts planning, dependency scheduling, targeted repairs and fresh
review from [iha2/superlite](https://github.com/iha2/superlite), inspected at
[`0a852888c898`](https://github.com/iha2/superlite/tree/0a852888c8986a6ac03e9bc82519ff8f99c0377a).
It ships instructions, not the upstream plugin, hooks, Python tools or model services.
No upstream source code is bundled. Upstream is MIT; this package keeps its license.

## Choose one coordinator

The invoking skill owns the approved brief, creative decisions, specialist roles,
quality gates and delivery. This adapter is its default execution discipline.
Do not start a second top-level brainstorming or dispatch workflow. Reuse approved
answers; apply existing brief/optional-tool gates once. Do not interpret an upstream
AI-orchestrator mode as permission to skip the invoking skill's gates.

Never enable Superlite and Superpowers together: their lifecycle skill names and
session-start context conflict. If Superpowers is active, report the conflict and
have the user select a clean session before enabling the native Superlite plugin.
The local adapter can be read without installing either plugin.

## Plan and execute

1. After brief confirmation, classify the request as small, new build, feature,
   debug or review. Keep small edits inline. For bugs, reproduce and find the
   cause first; for features, inspect existing interfaces before planning.
2. In the invoking skill's plan, give each task an ID, dependencies, one specialist,
   allowed files, input/output contracts, acceptance checks and evidence paths.
   Freeze shared interfaces before implementation. The coordinator owns shared
   entry points, dependency manifests, lockfiles and final integration.
3. Run only ready tasks with disjoint file ownership concurrently. Use the host's
   real delegation tools and agent limit; otherwise execute roles sequentially
   and disclose that. Never assume Claude tool names or a fixed number of agents.
4. Pass each specialist only the relevant approved brief, contract, source docs
   and constraints. Reuse that specialist for fixes. Use the current host model;
   route to a different model only when host rules and existing user authorization
   allow it. Never request keys, buy credits or install a paid model service.
5. Integrate completed tasks and check seams: producer/consumer data, shared
   styles, entry points, timing and teardown. Run actual checks, recording command,
   result and artifact. Missing browser/render tools mean BLOCKED, not PASS.
6. Return failures to the owning specialist with reproduction evidence. Apply the
   invoking skill's retry limit; stop and report an unresolved blocker at the cap.
7. Run a fresh final review of the diff, contracts and evidence after integration.
   The reviewer reports findings without editing. The owner fixes findings, then
   the coordinator reruns affected checks and review before declaring success.

Record task status, decisions, changed files, check results and next steps in the
existing state document. Do not invent `.superlite/` metrics, hidden checkpoints,
benchmark gains, or successful native-plugin execution. No automatic commit,
push, merge or deployment is granted by this adapter.

## Optional native plugin

Native Superlite is optional. Use its [official installation instructions](https://github.com/iha2/superlite#installation)
for the actual host. Claude Code's documented commands are:

```text
/plugin marketplace add iha2/superlite
/plugin install superlite@superlite-dev
```

Disable Superpowers first and start a fresh session. For Codex, upstream currently
labels marketplace installation unverified; do not promise these commands work
there. Keep using this bundled adapter if the plugin is unavailable.

When using a native installation, record its version/ref, inspect its current
host mapping, and designate the invoking skill as the sole coordinator. Use native
task dispatch only where its gates and model policy can honor this contract;
otherwise use the adapter. Never invoke nonexistent `sl` commands or plugin agents.
Installing a plugin alone does not wire the specialty skill's contracts into it.

## Buildme contract

The Master Orchestrator is the sole coordinator. Phase 0 may record setup and
provisional tasks, but Grill Me confirmation must precede specialist dispatch.
Keep the task graph and final review in `ORCHESTRATOR.md`. Respect the existing
20% per-agent token budget and two revision rounds. Preserve design ownership,
Design Arena selection, token snapshots and the ordered anti-slop → bugs →
performance/accessibility gates. Generate llms.txt only against the passing build;
post-launch monitoring starts only after an authorized deployment exists.
