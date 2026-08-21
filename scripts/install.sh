#!/usr/bin/env bash
# Install write-before-code into Cursor personal skills.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DEST="${CURSOR_SKILLS_DIR:-$HOME/.cursor/skills/write-before-code}"

mkdir -p "$(dirname "$DEST")"
rm -rf "$DEST"
mkdir -p "$DEST"

if command -v rsync >/dev/null 2>&1; then
  rsync -a --exclude '.git/' --exclude '.github/' "$ROOT/" "$DEST/"
else
  shopt -s dotglob nullglob
  for item in "$ROOT"/*; do
    base="$(basename "$item")"
    case "$base" in
      .git|.github) continue ;;
    esac
    cp -R "$item" "$DEST/"
  done
fi

echo "Installed to: $DEST"
echo "Restart Cursor or start a new agent chat, then say: use write-before-code"
