# Explanation

> Diátaxis: **understanding-oriented**  
> Answers: “Why was it designed this way? What is the background and the trade-offs?”

Explanation builds a mental model: motivation, constraints, and alternatives.  
Do not put step-by-step procedures or field-level specs here—those belong in How-to and Reference respectively.

---

## Files in this directory

| File | Status | Notes |
|------|--------|-------|
| [PRD.md](./PRD.md) | ⬜ Skeleton ready; body TBD | **Sole requirements source** for the current project; input to greenfield 01 |
| `overall-design.md` | ⬜ No file yet | First created by **01**; do not pre-create an empty shell |

The PRD already includes a fillable skeleton (feature IDs `F-x`, scenarios, constraints, non-functionals, open questions); it aligns with 01’s output structure—see [`../how-to/agent-prompts/01-overall-design.md`](../how-to/agent-prompts/01-overall-design.md). **Do not start 01 before the body is filled** (empty headings are not requirements).

---

## Where files come from

1. The maintainer writes `PRD.md` (overwrite the landing notes; do not reuse the previous project’s requirements).  
2. Greenfield **01** reads the PRD, creates `overall-design.md`, and initializes contracts and progress under `reference/`.  
3. When later changes rewrite product scope, write back to the PRD; routine patches do not go here.

After there is code, behavior patches go through brownfield task packs in [`../specs/`](../specs/); you do not need to rewrite the PRD for every small change.

---

## Do not put here

- Fields, paths, error codes, table schemas → [`../reference/`](../reference/)  
- “To achieve X, follow these steps” → [`../how-to/`](../how-to/)  
- Iteration task packs / HITL process drafts → [`../specs/`](../specs/)
