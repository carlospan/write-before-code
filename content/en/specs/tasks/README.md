# specs/tasks · in-progress task packs

> **Open (not yet closed) tasks only**. After close, move the whole set to [`../archive/`](../archive/) (naming: see that directory’s README).  
> **Template**: [_template.md](./_template.md)  
> **Process authority**: [../SDD-GUIDE.md](../SDD-GUIDE.md) (IDE single-line + §2.5 incremental consensus)

---

## Purpose

Brownfield iteration’s **working-draft landing spot**: short Spec, implementation steps, acceptance criteria, HITL decision points, plus optional design / receipt / acceptance record.  
Maintainer and IDE Agent treat files in this directory as the source of truth — not chat history.

---

## Naming conventions

| Type | Name | Notes |
|------|------|------|
| Main task pack (required) | `YYYY-MM-DD-short-name.md` | Copy `_template.md` and rename |
| Design (optional) | `YYYY-MM-DD-short-name-design.md` | Attach implementation approach for large changes |
| Receipt (optional) | `YYYY-MM-DD-short-name-receipt.md` | Self-verify summary after coding |
| Acceptance record (optional) | `YYYY-MM-DD-short-name-acceptance.md` | Maintainer HITL / written acceptance |

Default is **IDE single-line**: same session completes draft → code → engineering self-verify → write-back; maintainer does HITL only. Process files grow/shrink as needed; do not pad a full attachment set.

---

## Current tasks

| Task | Notes |
|------|------|
| (none yet) | Copy `_template.md` to create |

---

## Discipline summary

1. **Do not archive until closed**; closing requires `INDEX.md` already written, then move the whole set to [`../archive/`](../archive/) so this directory stays in-progress only.  
2. When product boundaries are unclear, **agree one slice at a time**, write into this pack’s HITL, then request coding authorization.  
3. When touching cross-module conventions, also write back `reference/global-contract.md` (version +0.1).  
4. Greenfield new modules: no 01 artifacts or architecture change needed → full `01→04`; 01 exists, architecture unchanged, maintainer says so → lightweight `02→04`. Do not use a task pack as a substitute for a module Spec that has not landed yet.
