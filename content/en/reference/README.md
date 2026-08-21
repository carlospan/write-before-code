# Reference

> Diátaxis: **information-oriented**  
> Answers: “What is X? Which fields / paths / constraints exist?”

Reference docs should be **objective, searchable, and accurate**. Readers consult them while working; they do not need narrative or persuasion.

---

## Files in this directory

| File | Status | Notes |
|------|--------|-------|
| `global-contract.md` | ⬜ No file yet | Initialized by **01**; later 02 / 03 / brownfield increments must bump the version |
| `progress.md` | ⬜ No file yet | Initialized by **01**; greenfield ✅ is written only by 04 (or the maintainer) |
| [modules/](./modules/) | ⬜ Empty | **02** produces `Fxx-*.md`; during 03 coding, level-1 write-backs are allowed |

**Do not pre-create empty shells**: contracts, progress, and module docs are **created complete** directly by greenfield stages.

Coding convention: **vertical slices** — when you ship a module, API + agreed UI are accepted together.

---

## Who may change what

| Artifact | Greenfield | Brownfield |
|----------|------------|------------|
| `global-contract.md` | 01 initializes; 02 / 03 increment | Write back when a task changes cross-module conventions; version +0.1 |
| `progress.md` | 01 builds the table; 02 → 📝; 03 → 🔍; **only 04 / maintainer → ✅** | Do not consume “not started” rows; leave a pointer in Notes when needed |
| `modules/Fxx-*.md` | **02 writes the body**; 03 may write back APIs / models / paths at level 1 (must use `<!-- write-back fix -->`) | After ✅, behavior patches go through `specs/`; generally do not open a new Fxx |

Brownfield process drafts do not live in this directory; see [`../specs/`](../specs/).

---

## Do not put here

- “Why was it designed this way” → [`../explanation/`](../explanation/)  
- Step-by-step how-to manuals → [`../how-to/`](../how-to/)  
- Task packs, receipts, acceptance records → [`../specs/`](../specs/)
