#!/usr/bin/env bash
# Install BuildMe and its companion skills for Claude Code, Codex, Grok and Antigravity.
#
# Usage (from a clone of this repo):  bash scripts/install.sh
#
# What it does:
#   0. Installs Agent-Reach from its official GitHub release, runs setup and verifies its skill.
#   1. Copies every skill folder under skills/ into ~/.agents/skills/ (the shared folder).
#   2. Links them into ~/.claude/skills and ~/.grok/skills (only if those agents are installed).
#   3. Links them into ~/.gemini/config/skills (Antigravity global skills).
#   4. Copies them into ~/.codex/skills (Codex does not follow symlinks).
#
# Companion skills (installed with BuildMe, required for Agents 1-5):
#   impeccable-director, frontend-architect, taste-specialist, ui-ux-auditor, motion-specialist
# Optional richer companions are reported at the end, not installed here.
#
# It replaces only skills with the same name as one in this repo. Other skills are left alone.
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC="$REPO/skills"
SHARED="$HOME/.agents/skills"

if [ ! -d "$SRC" ]; then
  echo "error: $SRC not found. Run this from a clone of the buildme-skill repo." >&2
  exit 1
fi

# Install the research dependency before registering Buildme as ready. This does
# not configure keys, accounts, optional channels or browser-session imports.
if command -v python3 >/dev/null 2>&1; then
  BUILDME_PYTHON="$(command -v python3)"
elif command -v python >/dev/null 2>&1; then
  BUILDME_PYTHON="$(command -v python)"
else
  echo "error: Python 3.10+ is required to install Agent-Reach." >&2
  exit 1
fi
"$BUILDME_PYTHON" "$REPO/scripts/install_agent_reach.py" --skills-dir "$SHARED"

mkdir -p "$SHARED"
count=0
for dir in "$SRC"/*/; do
  name="$(basename "$dir")"
  [ -f "$dir/SKILL.md" ] || continue

  rm -rf "$SHARED/$name"
  cp -R "$dir" "$SHARED/$name"

  if [ -d "$HOME/.claude" ]; then
    mkdir -p "$HOME/.claude/skills"
    ln -sfn "../../.agents/skills/$name" "$HOME/.claude/skills/$name"
  fi
  if [ -d "$HOME/.grok" ]; then
    mkdir -p "$HOME/.grok/skills"
    ln -sfn "../../.agents/skills/$name" "$HOME/.grok/skills/$name"
  fi
  if [ -d "$HOME/.gemini/config" ]; then
    mkdir -p "$HOME/.gemini/config/skills"
    ln -sfn "../../../.agents/skills/$name" "$HOME/.gemini/config/skills/$name"
  fi
  if [ -d "$HOME/.codex" ]; then
    mkdir -p "$HOME/.codex/skills"
    rm -rf "$HOME/.codex/skills/$name"
    cp -R "$dir" "$HOME/.codex/skills/$name"
  fi

  count=$((count + 1))
done

echo "Installed $count skills into $SHARED and linked them into the agents found on this machine."

# Verify the companions and the orchestrator are reachable.
missing=0
for name in buildme master-orchestrator impeccable-director frontend-architect taste-specialist ui-ux-auditor motion-specialist competitor-researcher; do
  if [ ! -f "$SHARED/$name/SKILL.md" ]; then
    echo "missing: $name" >&2
    missing=1
  fi
done
[ "$missing" -eq 0 ] && echo "BuildMe, its companion skills and Agent-Reach are installed."

# Report optional richer companions (read by Agents 2-5 when present; never blocking).
optional=""
missing_optional=""
for name in frontend-design taste-skill ui-ux-pro-max impeccable emil-design-eng motion-design-lottie; do
  if [ -f "$SHARED/$name/SKILL.md" ]; then optional="$optional $name"; else missing_optional="$missing_optional $name"; fi
done
echo "Optional companions found:${optional:- none}"
echo "Optional companions not installed:${missing_optional:- none}"
echo "  (install any you want with: npx skills add <repo>; see README.md)"
exit "$missing"
