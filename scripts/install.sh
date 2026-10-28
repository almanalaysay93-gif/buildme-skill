#!/usr/bin/env bash
# Install BuildMe and its companion skills for Claude Code, Codex, Grok and Antigravity.
#
# Usage (from a clone of this repo):  bash scripts/install.sh
#
# What it does:
#   1. Copies every skill folder under skills/ into ~/.agents/skills/ (the shared folder).
#   2. Links them into ~/.claude/skills and ~/.grok/skills (only if those agents are installed).
#   3. Links them into ~/.gemini/config/skills (Antigravity global skills).
#   4. Copies them into ~/.codex/skills (Codex does not follow symlinks).
#
# Companion skills (installed with BuildMe, required for Agents 1-5):
#   impeccable-director, frontend-architect, taste-specialist, ui-ux-auditor, motion-specialist
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
[ "$missing" -eq 0 ] && echo "BuildMe and the five companion skills are installed."
exit "$missing"
