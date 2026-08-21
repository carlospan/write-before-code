# reference/

Lookup facts and constraints for this docs tree (contract, progress, module specs). Consult while working; narrative and “why” do not live here.

## Contents of this directory

| Path | Status | Notes |
|------|--------|-------|
| `global-contract.md` | ⬜ No file yet | Initialized by **01**; later increments must bump the version |
| `progress.md` | ⬜ No file yet | Initialized by **01**; greenfield ✅ only by 04 (or the maintainer) |
| [modules/](./modules/) | ⬜ Empty | **02** produces `Fxx-*.md`; see [modules/README.md](./modules/README.md) |

**Do not pre-create empty shells** — greenfield stages create complete files. Coding convention: **vertical slices** (API + agreed UI accepted together).

## Who may change what

| Artifact | Greenfield | Brownfield |
|----------|------------|------------|
| `global-contract.md` | 01 initializes; 02 / 03 increment | Write back on cross-module convention changes; version +0.1 |
| `progress.md` | 01 builds table; 02 → 📝; 03 → 🔍; **only 04 / maintainer → ✅** | Do not consume “not started” rows; leave a Notes pointer when needed |
| `modules/Fxx-*.md` | **02 writes body**; 03 may write back at level 1 (`<!-- write-back fix -->`) | After ✅, behavior patches go through `specs/` |

Brownfield drafts → [`../specs/`](../specs/). Design rationale → [`../explanation/`](../explanation/). Steps → [`../how-to/`](../how-to/).
