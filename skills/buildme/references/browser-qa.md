# Browser QA runner (free, local)

BuildMe's quality gates (Agents 8, 10 and 12) need real browser evidence: screenshots at each
width, console and network errors, horizontal overflow, and keyboard focus. The bundled runner
`scripts/browser-qa.mjs` produces that evidence with Playwright and the local Chromium. No API
key, no account, no paid service.

## Setup (once)

The runner loads Playwright from `$PLAYWRIGHT_MODULE` if set, else from
`~/.agents/tools/playwright/node_modules/playwright/index.mjs`.

```bash
mkdir -p ~/.agents/tools/playwright && cd ~/.agents/tools/playwright
npm init -y >/dev/null && npm install playwright
npx playwright install chromium
```

Check it:

```bash
node -e "import('playwright').then(async m=>{const b=await m.chromium.launch();console.log('chromium',b.version());await b.close()})"
```

If the check fails, the runner exits with `NEED_SETUP` and the gate is recorded as "not run",
never "passed".

## Run

```bash
node ~/.agents/skills/buildme/scripts/browser-qa.mjs http://localhost:3000/ .buildme/qa/home
```

Options: `--widths 320,390,768,1024,1440` (default `320,390,768,1024,1440`).

Outputs in the given directory:

- `<width>.png`: full-page screenshot per width (before/after pairs for the bug-hunter loop).
- `report.json`: `block`, `major` and `minor` findings, per-width console errors, page errors,
  failed or 4xx/5xx requests, `horizontalOverflow`, and `keyboard` (unique tab stops and those
  without a visible focus style, measured at 1440px or the widest width).

Exit codes: `0` no block or major findings; `1` findings present (gate fails); `2` setup problem.

## Lighthouse (also free)

Agent 10 runs Lighthouse twice and keeps the worst score. Use the Chromium installed above:

```bash
CHROME_PATH="$(node -e "import('playwright').then(m=>console.log(m.chromium.executablePath()))" 2>/dev/null | tail -1)" \
  npx -y lighthouse http://localhost:3000/ --output=json --output-path=.buildme/qa/lh-1.json \
  --chrome-flags="--headless --no-sandbox"
```

Repeat for `lh-2.json`. Record the device/tool versions in `PERF_A11Y_AUDIT.md`. Lab results
are not field INP; label them as lab data.

## Rules

- Run against the built or dev server the agent just started, and stop the server afterwards.
- Store artifacts under `.buildme/qa/`, not in the source tree.
- A runner result of "not run" (setup missing) is never a pass. Say which check was skipped.
- The runner does not log in to anything. For pages behind a login, record the gap and test the
  public routes only.
