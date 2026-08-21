# agent-prompts · Greenfield Pipeline Prompts

> **Positioning**: Stage prompts + overview for greenfield 01→04. Brownfield does not enter here—go to [`../../specs/`](../../specs/).  
> Paths are relative to the **docs root `docs/`**; when the workspace is the repo root, prefix with `docs/`. See [00-overview.md](./00-overview.md).

---

## Files

| File | Stage | Purpose |
|------|-------|---------|
| [00-overview.md](./00-overview.md) | Entry | Overview, immutable principles, dual path (including lite track), path I/O |
| [01-overall-design.md](./01-overall-design.md) | Architect | Generate overall-design / global-contract / progress |
| [02-module-spec.md](./02-module-spec.md) | Architect | Generate `modules/Fxx-*.md` |
| [03-implement.md](./03-implement.md) | Engineer | Code per module spec; may write back Fxx (level 1); progress → 🔍 |
| [04-accept.md](./04-accept.md) | Accept | Independent pass once; do not change spec body; on pass → ✅ |

Human–AI collaboration (applies to greenfield / brownfield alike): [`../hitl-alignment.md`](../hitl-alignment.md).

---

## How to use

Same IDE Agent **swaps prompts in order** (do not skip persisting to disk):

```text
Write explanation/PRD.md
  → 00-overview (read first · immutable principles)
  → 01-overall-design          (lite track: may skip after maintainer states explicitly)
  → 02-module-spec (one module at a time; lite track summary shorter, 12 sections still complete)
  → 03-implement
  → 04-accept
  → Next module starts again from 02
```

**Do not put here**: Task-pack working drafts → `specs/tasks/`; contract and module-spec bodies → `reference/`.
