#!/usr/bin/env bash
# Install write-before-code into one or more Agent Skills directories.
# Compatible with the open Agent Skills layout (SKILL.md at skill root).
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SKILL_NAME="write-before-code"
AGENT="${AGENT:-all}"
SCOPE="${SCOPE:-user}"
PROJECT_ROOT="${PROJECT_ROOT:-}"
DESTINATION="${DESTINATION:-}"

usage() {
  cat <<'EOF'
Usage: ./scripts/install.sh [--agent cursor|codex|trae|claude|all] [--scope user|project] [--project-root DIR] [--destination DIR]

Defaults: --agent all --scope user

Examples:
  ./scripts/install.sh --agent cursor
  ./scripts/install.sh --agent codex
  ./scripts/install.sh --agent trae
  ./scripts/install.sh --agent claude
  ./scripts/install.sh --agent all
  ./scripts/install.sh --agent all --scope project
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --agent) AGENT="$2"; shift 2 ;;
    --scope) SCOPE="$2"; shift 2 ;;
    --project-root) PROJECT_ROOT="$2"; shift 2 ;;
    --destination) DESTINATION="$2"; shift 2 ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown arg: $1" >&2; usage; exit 1 ;;
  esac
done

install_one() {
  local dest="$1"
  mkdir -p "$(dirname "$dest")"
  rm -rf "$dest"
  mkdir -p "$dest"

  if command -v rsync >/dev/null 2>&1; then
    rsync -a --exclude '.git/' --exclude '.github/' "$ROOT/" "$dest/"
  else
    # Portable fallback (bash)
    shopt -s dotglob nullglob 2>/dev/null || true
    for item in "$ROOT"/*; do
      base="$(basename "$item")"
      case "$base" in
        .git|.github) continue ;;
      esac
      cp -R "$item" "$dest/"
    done
  fi

  if [[ ! -f "$dest/SKILL.md" ]]; then
    echo "Install failed: SKILL.md missing at $dest" >&2
    exit 1
  fi
  echo "Installed -> $dest"
}

resolve_targets() {
  local home="${HOME}"
  local proj="${PROJECT_ROOT:-$PWD}"
  case "$SCOPE" in
    user)
      case "$AGENT" in
        cursor) echo "$home/.cursor/skills/$SKILL_NAME" ;;
        codex)  echo "$home/.agents/skills/$SKILL_NAME" ;;
        trae)   echo "$home/.trae/skills/$SKILL_NAME" ;;
        claude) echo "$home/.claude/skills/$SKILL_NAME" ;;
        all)
          echo "$home/.cursor/skills/$SKILL_NAME"
          echo "$home/.agents/skills/$SKILL_NAME"
          echo "$home/.trae/skills/$SKILL_NAME"
          echo "$home/.claude/skills/$SKILL_NAME"
          ;;
        *) echo "Unknown agent: $AGENT" >&2; exit 1 ;;
      esac
      ;;
    project)
      case "$AGENT" in
        cursor) echo "$proj/.cursor/skills/$SKILL_NAME" ;;
        codex)  echo "$proj/.agents/skills/$SKILL_NAME" ;;
        trae)   echo "$proj/.trae/skills/$SKILL_NAME" ;;
        claude) echo "$proj/.claude/skills/$SKILL_NAME" ;;
        all)
          echo "$proj/.cursor/skills/$SKILL_NAME"
          echo "$proj/.agents/skills/$SKILL_NAME"
          echo "$proj/.trae/skills/$SKILL_NAME"
          echo "$proj/.claude/skills/$SKILL_NAME"
          ;;
        *) echo "Unknown agent: $AGENT" >&2; exit 1 ;;
      esac
      ;;
    *) echo "Unknown scope: $SCOPE" >&2; exit 1 ;;
  esac
}

if [[ -n "$DESTINATION" ]]; then
  install_one "$DESTINATION"
else
  while IFS= read -r t; do
    [[ -z "$t" ]] && continue
    install_one "$t"
  done < <(resolve_targets)
fi

cat <<'EOF'

Restart the agent (or open a new session), then invoke write-before-code:
  Cursor / Trae / Claude Code:  /write-before-code   or say "use write-before-code"
  Codex:                        $write-before-code   or say "use write-before-code"
EOF
