---
name: write-before-code
description: >-
  HITL spec-driven agent skill (Cursor, Codex, Trae, Claude Code): overall
  design -> module spec -> implement -> independent accept, plus brownfield
  task packs. Enforces specs on disk before code, one-slice consensus, and
  forbids implementers from self-marking done. Use when starting a project
  with agents, writing specs before coding, accepting a module, fixing agent
  drift / fake-green tests / self-approved done, vibe-coding that needs
  structure, or when the user says write-before-code, 先写后码, 一块一拍,
  HITL spec, or SDD.
metadata:
  version: "0.3.0"
  license: MIT
---

# write-before-code

**Tagline:** Specs on disk first. Code second.

Works on any agent that loads [Agent Skills](https://agentskills.io) (`SKILL.md`).
Install paths: [docs/adapters.md](docs/adapters.md).

Match the **language of the user's latest message**:

| User language | Read corpus from |
|---------------|------------------|
| English | `content/en/` |
| 中文 | `content/zh/` |

Paths are relative to this skill directory. **Load only the active stage file** — do not ingest the whole corpus.

Human docs: [README.md](README.md) (English) · [README.zh-CN.md](README.zh-CN.md) (中文).

---

## Iron laws (never relax)

1. **Write before code** — no large implementation until the relevant spec is on disk. Chat is not the source of truth.
2. **HITL** — product/architecture decisions need maintainer approval.
3. **One focus** — one greenfield module or one brownfield task pack at a time.
4. **Agree one slice at a time** — confirm a small slice; write it to disk immediately.
5. **No self-pass** — implementers must not mark ✅. Only stage 04 or the maintainer may.
6. **No fake green** — real tests + non-vacuous assertions.

HITL guide: `content/<lang>/how-to/hitl-alignment.md`

---

## Path selection

```text
Greenfield full     PRD -> 01 -> 02 -> 03 -> 04
Greenfield lite     (maintainer says so; 01 artifacts exist; no arch change) -> 02 -> 03 -> 04
Brownfield          specs/tasks pack -> implement + self-check -> maintainer HITL -> archive
```

| Situation | Path | Start here |
|-----------|------|------------|
| New project / unset architecture | Greenfield full | 00 then 01 |
| Next module; design already exists | Greenfield lite (maintainer explicit only) | 02 |
| Behavior change on shipped modules | Brownfield | SDD-GUIDE |
| Accept a module at 🔍 | Accept only | 04 |

Overview: `content/<lang>/how-to/agent-prompts/00-overview.md`

---

## Stage routing

Same IDE agent; **swap stage mindset**; do not skip disk writes.

| Stage | Role | File under `content/<lang>/` |
|-------|------|------------------------------|
| 00 | Constitution | `how-to/agent-prompts/00-overview.md` |
| 01 | Architect | `how-to/agent-prompts/01-overall-design.md` |
| 02 | Architect | `how-to/agent-prompts/02-module-spec.md` |
| 03 | Engineer | `how-to/agent-prompts/03-implement.md` |
| 04 | Accept (independent) | `how-to/agent-prompts/04-accept.md` |
| Brownfield | IDE single line | `specs/SDD-GUIDE.md` + `specs/tasks/_template.md` |

### Stage 04 isolation

Prefer a **fresh chat / fresh agent** for 04. Do not reuse the implementer's warm context.

### Progress states

`⬜` -> `📝` -> `🔍` -> `✅` (or `⏸️`)  
Only 04/maintainer writes `✅`. Stage 03 writes `🔍` only.

---

## Project docs layout

Project docs root is usually `docs/` (Diátaxis + `specs/`).

Copy `content/en/` or `content/zh/` into the project's `docs/`.

| Path (under docs root) | Purpose |
|------------------------|---------|
| `explanation/PRD.md` | Sole requirements source (real body required before 01) |
| `explanation/overall-design.md` | From 01 |
| `reference/global-contract.md` | Versioned cross-module contract |
| `reference/progress.md` | Module state machine |
| `reference/modules/Fxx-*.md` | From 02 |
| `specs/tasks/` | Brownfield packs |
| `specs/archive/` | Closed packs (must include `INDEX.md`) |

If the workspace is the repo root, prefix with `docs/`. If the workspace *is* the docs root, use paths as above. Ask the maintainer if unclear — do not guess.

### Brownfield attachment filenames

Do not mix suffixes across language trees:

| Role | English tree (`content/en`) | Chinese tree (`content/zh`) |
|------|----------------------------|-----------------------------|
| Design (optional) | `-design.md` | `-方案.md` |
| Receipt (optional) | `-receipt.md` | `-回执.md` |
| Acceptance (optional) | `-acceptance.md` | `-验收记录.md` |

---

## Quick start

1. Ensure the project has `docs/` from `content/<lang>/`.
2. Fill `explanation/PRD.md` with real product requirements.
3. User: "use write-before-code, start stage 01" (or Chinese equivalent).
4. Agent: read 00 iron laws -> open 01 -> follow its prompt (understanding summary -> wait -> write artifacts).
5. Continue 02 -> 03 -> 04 per module. Prefer a new conversation for 04.

Brownfield: copy `specs/tasks/_template.md` -> fill HITL one slice at a time -> code after go-ahead -> archive with `INDEX.md`.

---

## Anti-patterns

| Don't | Do |
|-------|-----|
| Code architecture never written down | Finish 01/02 disk writes first |
| Mark ✅ in stage 03 | Mark 🔍; hand to 04 |
| One huge "approve all" list | One slice; disk; next slice |
| Treat chat as the spec | Update files when agreed |
| Skip 04 because "tests passed" | Independent accept against module section 11 / task acceptance |

---

## Examples

[examples/toy-prd.md](examples/toy-prd.md) · [examples/toy-prd.zh-CN.md](examples/toy-prd.zh-CN.md)

---

## Maintainer notes

- Opinionated. Not a Spec Kit / BMAD / OpenSpec replacement.
- Keep `content/en/` and `content/zh/` in sync when editing process rules.
- One skill package for all supported agents — do not fork prompt trees per IDE.
- Version: see frontmatter `metadata.version` and [CHANGELOG.md](CHANGELOG.md).
