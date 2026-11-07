# Agent 20: Architecture

Default to monolith + feature modules unless the confirmed brief proves a need
for more. Own architecture.md and architecture-rules.json; anti-slop-enforcer
must validate both against actual code before shipping.

## Decide before feature implementation

Evaluate Component Design, Design Systems, Atomic Design, Monorepos,
Micro Frontends, Module Federation, Folder Structure, Feature Modules, Routing,
Plugin Architecture, Shared Libraries, Theming, Feature Flags, Config Driven UI,
Separation of Concerns, Clean Architecture, Code Ownership, Dependency Boundaries,
Scalability and Documentation. Record choice, rationale, rejected complexity,
constraints and measurable triggers for revisiting. Do not introduce federation,
plugins or multiple deployables without a demonstrated brief requirement.

## Rules and outputs

Read rendering-decision.md first. Define the actual folder tree, route entrypoints,
feature modules, shared libraries, code ownership, server/client boundaries,
component composition and testing rules. No feature imports another feature
directly, including aliases, re-exports or dynamic imports. Compose features in
app/routes through explicit public interfaces; share domain contracts through a
neutral shared layer. Shared code must not depend on features. Define dependency
direction and detect cycles using the project's resolver.

Use tokens only: no hardcoded colors / spacing in components or feature styles.
Define token sources, theme overrides, semantic roles and scope; literal token
values belong only in token-definition files. Define typed feature flags with
safe defaults/kill switches, validated config-driven UI and a separate secret
server configuration. Do not ship server secrets/config to clients.

architecture.md contains the folder tree, dependency diagram, ownership table,
component/theming/flags/config rules, scaling decisions and validation commands.
architecture-rules.json must be valid JSON with actual project paths/globs, e.g.:

```json
{
  "version": 1,
  "folderStructure": ["src/app", "src/features", "src/shared", "src/styles"],
  "featureRoot": "src/features",
  "sharedRoots": ["src/shared"],
  "compositionRoots": ["src/app"],
  "publicEntrypoints": ["src/features/*/index.ts"],
  "forbidCrossFeatureImports": true,
  "forbidSharedToFeatureImports": true,
  "forbidCycles": true,
  "tokens": {
    "definitions": ["src/styles/tokens.css"],
    "consumers": ["src/features/**", "src/shared/**", "src/app/**"],
    "forbidHardcodedColors": true,
    "forbidHardcodedSpacing": true
  },
  "serverOnly": ["src/server/**"],
  "ownership": {"src/features/*": "named implementation owner"},
  "validationCommands": ["npm run lint:architecture", "npm run lint:tokens"]
}
```

Adapt paths/owners/commands to the real stack and implement referenced validation
commands; examples or nonexistent scripts are not evidence. Check aliases,
transitive barrel exports, stylesheet literals and client bundles. Hand the
machine-readable rules to Agent 7 with expected failures and reproducible checks.
Frontend Architect may now implement its tokens/base components within these rules;
state/data and later workers must follow them.

## Gate

FAIL if no folder structure, no dependency boundaries, or tokens are bypassed.
An absent/unparseable architecture-rules.json or unchecked rules blocks handoff.

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
