# Agent Desktop: primary UI-control tool

Source: https://github.com/vercel-labs/agent-desktop (Apache-2.0).
Pinned npm package: agent-desktop@1.1.0, JSON protocol 2.6, inspected 2026-11-03.
Reviewed README, install/JSON contracts, native desktop skill, platform packaging,
and observation/interaction command references. The binary serves version-matched
skills; read those before use rather than assuming flags from older examples.

## Tool choice

Agent Desktop is a local CLI, not an autonomous model or a replacement orchestrator.
The current Buildme agent chooses actions from OS accessibility observations and
runs observe → act → observe → independently verify. No separate provider keys,
model account or API credits are needed. Existing coding-host/compute costs still
apply. Its optional hosted/model helpers are not installed or activated.

Use this as the default for browser/native application navigation, forms, menus,
dialogs and GUI journeys. Agent 8 owns execution, Agent 4 defines UX outcomes,
Agent 0 coordinates scope/repairs, and Agents 10/12 review evidence. Keep the
Playwright browser runner and Lighthouse for specialized web-only tasks: CSS
viewports, DOM/schema parity, network/console, timing and SEO. OS window resizing
is not equivalent to a mobile CSS viewport. Do not call the web tools a substitute
for a required desktop/native check or use them silently when desktop access is blocked.

## Install and readiness

Run `bash scripts/install.sh` from the updated Buildme checkout. It installs
Agent-Reach as before plus agent-desktop@1.1.0 into
`~/.agents/tools/agent-desktop`, verifies the native version and caches its embedded
skills. Node.js 18+ and npm are required, in addition to existing Python/Bash needs.
No app is read/launched, no GUI permission requested and no account created by the
Buildme helper. Successful package installation is not a successful GUI test.

The adapter resolves the managed native executable; an existing native CLI on
PATH is also supported. Before first use, read the version-matched skills:

```text
agent-desktop skills get desktop
agent-desktop skills get platform
agent-desktop status
agent-desktop permissions
```

If only the managed binary is installed, use the receipt's binary path, or read
its cached `skills/desktop.md` and `skills/platform.md`. The adapter's `doctor`
checks status without listing or controlling apps:

```bash
python3 <buildme-skill-directory>/scripts/desktop_qa.py doctor
```

macOS needs Accessibility permission and Screen Recording for screenshots. Windows
can act only at a compatible integrity level. Linux requires the user's graphical
session, AT-SPI and appropriate display/session buses (Ubuntu 24.04+/GNOME 46 is
the primary upstream target). Cloud/SSH/CI without a desktop cannot see apps:
record BLOCKED with setup requirements. Do not fabricate desktop evidence.
Permission-grant UI belongs to the user; do not auto-enable it in the installer.

## Scope and observe–act–verify

Agent 0 records the approved test app/window, synthetic input, task, expected
outcomes and artifact scope in BUILD_BRIEF.md. Do not scan the whole desktop,
clipboard, notifications or unrelated applications to satisfy a product test.
Workers load the actual CLI skill before selecting operations.

1. Observe the specific app/window. Multiple windows require an explicit
   window id from the observed candidates; never pick an unrelated window.
2. Read `data.complete`, `truncated` and `identity_unproven`. A partial tree does
   not prove absence, uniqueness or completion. Read the appropriate bounded
   region using the native skill's drill-down rules before relying on it.
3. Choose only refs in that observation, qualified as `@snapshot_id:eN`.
   Never invent a selector, raw coordinate or ref. Re-observe after a UI change.
4. Act headlessly through semantic ref operations. No automatic --headed,
   coordinate, keyboard or clipboard fallback. Physical input requires explicit
   user authorization and the platform skill; the bundled adapter does not expose it.
5. Inspect delivery/retry disposition. `ok: true` or delivered_unverified is not
   application success. Retry a mutation only if `disposition.retry` is safe;
   unknown/unsafe delivery requires a fresh read before deciding. Even a safe
   stale-ref error needs a new observation/ref, never the same blind retry.
6. Independently observe the expected effect. Element value readback is not proof
   of document save, backend persistence or a completed flow. Verify the actual
   application outcome and run all other applicable quality gates.

## Bundled scoped adapter

```bash
python3 <buildme-skill-directory>/scripts/desktop_qa.py observe   --app "Approved test app" --window-id w-123 --output .buildme/qa/desktop/observed.json
python3 <buildme-skill-directory>/scripts/desktop_qa.py act   --observation .buildme/qa/desktop/observed.json --action click   --ref '@snapshot_id:e1' --output .buildme/qa/desktop/action.json
python3 <buildme-skill-directory>/scripts/desktop_qa.py verify   --app "Approved test app" --window-id w-123   --checks .buildme/qa/desktop/checks.json --output .buildme/qa/desktop/verified.json
```

Refs/window ids above are placeholders; replace them only with actual observed
values. Copy [the assertion template](../templates/desktop-checks.json) and adapt
roles/names/states to this app/platform. Checks are declarative data, not scripts.
The adapter does not automatically retry mutations or escalate physical input.
Its conservative action mode requires a complete, identity-proven observation.
Use the native skill's deliberate scoped observation flow for dense apps; do not
relax completeness or identity to force the adapter through.

Action reports remain BLOCKED pending verification even when delivery is verified.
Independent assertion PASS covers accessibility state only; overall QA remains
BLOCKED until the orchestrator combines application-persistence and all required
web/mobile/accessibility/performance/SEO evidence. No new numbered role is added.

Return failures with actual app/window/ref context, reproduction, expected effect,
worker owner and retest criteria. Repair with that worker, then re-observe/recheck.
Keep two revision rounds; unresolved requirements stay FAIL/BLOCKED at the cap.

## Privacy

Accessibility snapshots and screenshots can contain private desktop data. The
adapter saves scoped snapshots locally with restrictive POSIX permissions and
prints only a summary. Do not commit raw snapshots, clipboard data or screen
captures, or upload them publicly. Review/redact any artifacts before sharing.
Do not assume Windows file ACLs provide the same guarantee as POSIX modes.
