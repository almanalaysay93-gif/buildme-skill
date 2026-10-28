#!/usr/bin/env node
// Free local browser QA for BuildMe gates (Agents 8, 10 and 12).
//
// Usage: node browser-qa.mjs <url> <outDir> [--widths 320,768,1024,1440,390]
//
// Drives the local Chromium through Playwright (no API key, no paid service) and writes:
//   <outDir>/<width>.png       full-page screenshot per viewport width
//   <outDir>/report.json       console/page errors, failed requests, overflow, keyboard focus
// Exit code 0 = no block or major findings; 1 = block or major findings present; 2 = setup problem.
//
// Playwright is loaded from $PLAYWRIGHT_MODULE, else from ~/.agents/tools/playwright.
// Setup: see references/browser-qa.md.

import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { pathToFileURL } from 'node:url';

const args = process.argv.slice(2);
const url = args[0];
const outDir = args[1];
const widthsFlag = args.indexOf('--widths');
const widths = widthsFlag > -1
  ? args[widthsFlag + 1].split(',').map(Number)
  : [320, 390, 768, 1024, 1440];

if (!url || !outDir) {
  console.error('usage: node browser-qa.mjs <url> <outDir> [--widths 320,768,1440]');
  process.exit(2);
}

const candidates = [
  process.env.PLAYWRIGHT_MODULE,
  path.join(os.homedir(), '.agents/tools/playwright/node_modules/playwright/index.mjs'),
].filter(Boolean);

let chromium = null;
for (const candidate of candidates) {
  if (!fs.existsSync(candidate)) continue;
  try {
    ({ chromium } = await import(pathToFileURL(candidate).href));
    break;
  } catch {
    // try next candidate
  }
}
if (!chromium) {
  console.error('NEED_SETUP: Playwright not found. See references/browser-qa.md (set PLAYWRIGHT_MODULE or install it).');
  process.exit(2);
}

fs.mkdirSync(outDir, { recursive: true });

let browser;
try {
  browser = await chromium.launch({ headless: true });
} catch (error) {
  console.error(`NEED_SETUP: Chromium failed to launch (${error.message.split('\n')[0]}). Run: npx playwright install chromium`);
  process.exit(2);
}

// Keyboard walkthrough runs once, at desktop width when measured, else at the widest viewport.
const keyboardWidth = widths.includes(1440) ? 1440 : Math.max(...widths);

const report = { url, browser: browser.version(), generatedAt: new Date().toISOString(), viewports: [], keyboard: null, block: [], major: [], minor: [] };

for (const width of widths) {
  const page = await browser.newPage({ viewport: { width, height: 900 } });
  const consoleErrors = [];
  const pageErrors = [];
  const failed = [];

  page.on('console', (msg) => {
    if (msg.type() === 'error' || msg.type() === 'warning') consoleErrors.push(`${msg.type()}: ${msg.text()}`);
  });
  page.on('pageerror', (error) => pageErrors.push(error.message));
  page.on('requestfailed', (req) => failed.push(`${req.method()} ${req.url()} ${req.failure()?.errorText ?? ''}`.trim()));
  page.on('response', (res) => { if (res.status() >= 400) failed.push(`HTTP ${res.status()} ${res.url()}`); });

  const response = await page.goto(url, { waitUntil: 'networkidle', timeout: 30000 }).catch((error) => {
    pageErrors.push(`navigation: ${error.message}`);
    return null;
  });

  const overflow = await page.evaluate(() => {
    const root = document.documentElement;
    return { scrollWidth: root.scrollWidth, clientWidth: root.clientWidth, overflowing: root.scrollWidth > root.clientWidth + 1 };
  });

  const screenshot = path.join(outDir, `${width}.png`);
  await page.screenshot({ path: screenshot, fullPage: true });

  const entry = {
    width,
    status: response?.status() ?? null,
    horizontalOverflow: overflow.overflowing,
    scrollWidth: overflow.scrollWidth,
    consoleErrors,
    pageErrors,
    failedRequests: failed,
    screenshot,
  };
  report.viewports.push(entry);

  if (pageErrors.length || (response && response.status() >= 400)) report.block.push(`${width}px: page errors or HTTP ${response?.status()}`);
  if (overflow.overflowing) report.major.push(`${width}px: horizontal overflow (scrollWidth ${overflow.scrollWidth} > ${overflow.clientWidth})`);
  if (consoleErrors.some((line) => line.startsWith('error'))) report.major.push(`${width}px: console errors`);
  if (failed.length) report.minor.push(`${width}px: ${failed.length} failed request(s)`);

  if (width === keyboardWidth) {
    // Keyboard walkthrough at desktop width: record the first 25 tab stops and flag invisible focus.
    const stops = [];
    for (let i = 0; i < 25; i++) {
      await page.keyboard.press('Tab');
      const stop = await page.evaluate(() => {
        const el = document.activeElement;
        if (!el || el === document.body) return null;
        const style = getComputedStyle(el);
        const visible = (style.outlineStyle !== 'none' && parseFloat(style.outlineWidth) > 0) || style.boxShadow !== 'none';
        return { tag: el.tagName.toLowerCase(), label: (el.getAttribute('aria-label') || el.textContent || '').trim().slice(0, 60), focusVisible: visible };
      });
      if (!stop) continue;
      const key = `${stop.tag}|${stop.label}`;
      if (stops.some((s) => `${s.tag}|${s.label}` === key)) break; // focus wrapped around the page
      stops.push(stop);
    }
    report.keyboard = { uniqueTabStops: stops.length, withoutVisibleFocus: stops.filter((s) => !s.focusVisible).map((s) => s.label || s.tag) };
    if (report.keyboard.withoutVisibleFocus.length) report.major.push(`keyboard: ${report.keyboard.withoutVisibleFocus.length} focus stop(s) without a visible focus style`);
  }

  await page.close();
}

await browser.close();
fs.writeFileSync(path.join(outDir, 'report.json'), JSON.stringify(report, null, 2));

console.log(`browser-qa: ${url}`);
console.log(`  chromium ${report.browser}; screenshots and report.json in ${outDir}`);
console.log(`  block: ${report.block.length}  major: ${report.major.length}  minor: ${report.minor.length}`);
for (const line of [...report.block.map((x) => `BLOCK ${x}`), ...report.major.map((x) => `MAJOR ${x}`), ...report.minor.map((x) => `MINOR ${x}`)]) console.log(`  ${line}`);

process.exit(report.block.length || report.major.length ? 1 : 0);
