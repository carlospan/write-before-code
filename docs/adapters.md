# Multi-agent adapters

**write-before-code** follows the open [Agent Skills](https://agentskills.io) layout: a folder with `SKILL.md` (+ supporting files). The same package works across tools that discover skills this way.

Process rules live in `content/`; each **compatible agent** mainly differs by **install path** and **how you invoke** the skill.

## Supported agents

| Agent | User (personal) install | Project install | Invoke |
|-------|-------------------------|-----------------|--------|
| **Cursor** | `~/.cursor/skills/write-before-code/` | `.cursor/skills/write-before-code/` | `/write-before-code` or “use write-before-code” |
| **Codex** (OpenAI) | `~/.agents/skills/write-before-code/` | `.agents/skills/write-before-code/` | `$write-before-code` or “use write-before-code” |
| **Trae** | `~/.trae/skills/write-before-code/` | `.trae/skills/write-before-code/` | `/write-before-code` or Skills UI import |
| **Claude Code** | `~/.claude/skills/write-before-code/` | `.claude/skills/write-before-code/` | `/write-before-code` |

Trae and Codex also honor the shared `.agents/skills/` convention in many setups; our installer still writes Trae’s native `.trae/skills/` path when you pick `--agent trae`.

## Install

From a clone of this repo:

```bash
# All supported agents (default)
./scripts/install.sh

# One agent
./scripts/install.sh --agent cursor
./scripts/install.sh --agent codex
./scripts/install.sh --agent trae
./scripts/install.sh --agent claude

# Commit into a product repo for the team
./scripts/install.sh --agent all --scope project
```

Windows PowerShell:

```powershell
.\scripts\install.ps1
.\scripts\install.ps1 -Agent codex
.\scripts\install.ps1 -Agent all -Scope project
```

Optional ecosystem CLI (if you use [skills.sh](https://skills.sh) / `npx skills`):

```bash
npx skills add carlospan/write-before-code -a cursor
npx skills add carlospan/write-before-code -a codex
```

(Exact `-a` flags depend on the CLI version; prefer our `scripts/install.*` when unsure.)

## What stays the same on every agent

1. Load **only** the active stage file under `content/<lang>/` — do not ingest the whole corpus.
2. Iron laws: write-before-code · HITL · one focus · agree one slice at a time · no self-pass · no fake green.
3. Prefer a **fresh chat / fresh session** for stage 04 accept.
4. Project docs still come from copying `content/en/` or `content/zh/` into the product’s `docs/`.

## Notes by agent

### Cursor
Personal skills under `~/.cursor/skills/`. Project skills under `.cursor/skills/`.

### Codex
Official discovery uses `.agents/skills` (user: `~/.agents/skills`). Keep `SKILL.md` at the skill directory root — no extra nesting. Restart Codex if a newly copied skill does not appear.

### Trae
Skills UI can import a folder / zip containing `SKILL.md`. Native project path is often `.trae/skills/`. Rules (always-on) ≠ Skills (on-demand) — keep this workflow as a **skill**, not a giant always-on rule.

### Claude Code
Personal: `~/.claude/skills/`. Project: `.claude/skills/`. Same `SKILL.md` frontmatter (`name`, `description`).

## One package, many agents

We do **not** ship separate prompt trees per IDE. One methodology corpus + one entry skill keeps EN/ZH parity maintainable. If an agent cannot load skills at all, fall back to pasting `SKILL.md` + pointing it at `content/<lang>/how-to/agent-prompts/00-overview.md`.
