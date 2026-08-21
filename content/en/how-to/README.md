# how-to/

Executable how-tos for this docs tree (HITL + greenfield agent prompts). Brownfield procedures live under [`../specs/`](../specs/).

## Contents of this directory

| Path | Purpose |
|------|---------|
| [hitl-alignment.md](./hitl-alignment.md) | HITL + Spec-driven + agree one slice at a time |
| [agent-prompts/](./agent-prompts/) | Greenfield stages 00–04; see [agent-prompts/README.md](./agent-prompts/README.md) |

### agent-prompts/ quick map

| File | Purpose |
|------|---------|
| [00-overview.md](./agent-prompts/00-overview.md) | Overview, iron laws, dual paths, path I/O |
| [01-overall-design.md](./agent-prompts/01-overall-design.md) | Overall development docs |
| [02-module-spec.md](./agent-prompts/02-module-spec.md) | Module-level specs |
| [03-implement.md](./agent-prompts/03-implement.md) | Implement from module doc (close with 🔍) |
| [04-accept.md](./agent-prompts/04-accept.md) | Independent accept (mark ✅ on pass) |

### Brownfield entry points (bodies under specs/)

| File | Purpose |
|------|---------|
| [../specs/README.md](../specs/README.md) | When to use brownfield |
| [../specs/SDD-GUIDE.md](../specs/SDD-GUIDE.md) | IDE single-line, one-slice HITL |
| [../specs/ci-probes.md](../specs/ci-probes.md) | CI machine probes |
| [../specs/tasks/_template.md](../specs/tasks/_template.md) | Task-pack template |

## Optional per-project additions (link only when body exists)

| Type | Notes |
|------|-------|
| `vertical-slice-accept.md` (optional) | Vertical-slice accept checklist |
| Project-specific how-tos | Deploy / integration / release (may live at product repo root) |

Field inventories / design rationale / task packs / guided drills → `reference/` · `explanation/` · `specs/` · `tutorials/`.
