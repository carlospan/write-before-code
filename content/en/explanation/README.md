# explanation/

Product and architecture explanation for this docs tree (requirements source, overall design). Field-level specs and step-by-step procedures do not live here.

## Contents of this directory

| Path | Status | Notes |
|------|--------|-------|
| [PRD.md](./PRD.md) | ⬜ Skeleton ready; body TBD | **Sole requirements source** for the current project; input to greenfield 01 |
| `overall-design.md` | ⬜ No file yet | First created by **01**; do not pre-create an empty shell |

The PRD skeleton includes feature IDs `F-x`, scenarios, constraints, non-functionals, open questions; it aligns with 01 — see [`../how-to/agent-prompts/01-overall-design.md`](../how-to/agent-prompts/01-overall-design.md). **Do not start 01 before the body is filled.**

## Where files come from

1. Maintainer writes `PRD.md` (overwrite landing notes; do not reuse the previous project’s requirements).  
2. Greenfield **01** reads the PRD, creates `overall-design.md`, and initializes contract + progress under `reference/`.  
3. When later changes rewrite product scope, write back to the PRD; routine patches go through [`../specs/`](../specs/).

Fields / paths / error codes → [`../reference/`](../reference/). Steps → [`../how-to/`](../how-to/).
