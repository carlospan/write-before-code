# How-to guides

> Diátaxis: **goal-oriented**  
> Answers: “I need to accomplish something — what are the steps?”

How-tos assume the reader already has basics and give executable steps. Do not write them as concept lessons, and do not expand into a full API encyclopedia.

---

## Shipped (template-universal)

The following ships with the template into new repos and is product-agnostic.

### Human–AI collaboration

| Guide | Purpose |
|------|------|
| [HITL iron rule — incremental consensus](./hitl-alignment.md) | **HITL + Spec-driven + agree one slice at a time** (default posture for locking Spec) |

### Agent / IDE prompts (greenfield)

System entry: [agent-prompts/README.md](./agent-prompts/README.md); read [00-overview.md](./agent-prompts/00-overview.md) first:

| Guide | Purpose |
|------|------|
| [00-overview.md](./agent-prompts/00-overview.md) | Overview, immutable principles, dual paths (incl. lightweight track), path I/O |
| [01-overall-design.md](./agent-prompts/01-overall-design.md) | Generate overall development docs |
| [02-module-spec.md](./agent-prompts/02-module-spec.md) | Generate module-level development docs |
| [03-implement.md](./agent-prompts/03-implement.md) | Code from the module doc (close with 🔍) |
| [04-accept.md](./agent-prompts/04-accept.md) | Independent acceptance pass (do not edit Spec body; mark ✅ on pass) |

### Brownfield / iteration (SDD)

Brownfield procedure lives under `specs/`; this page only provides entry points:

| Guide | Purpose |
|------|------|
| [../specs/README.md](../specs/README.md) | When to take the brownfield path |
| [../specs/SDD-GUIDE.md](../specs/SDD-GUIDE.md) | IDE single-line, §2.5 agree one slice at a time, HITL |
| [../specs/ci-probes.md](../specs/ci-probes.md) | CI machine probes (anti-drift) |
| [../specs/tasks/_template.md](../specs/tasks/_template.md) | Task-pack template |

---

## To add per project

The following is **not** fixed template content; link only when body exists — do not pre-create dead links:

| Type | Notes |
|------|------|
| `vertical-slice-accept.md` (optional) | Vertical-slice checklist for human acceptance |
| Project-specific how-tos | Steps bound to a product / environment (deploy, integration, release, etc.) |

Engineering bootstrap, client notes, etc. belong at **that project’s repo root** (or its agreed directory), not hard-wired into this template.

---

## Do not put here

- Full error-code tables, DDL, field inventories → [`../reference/`](../reference/)  
- Why it was designed this way → [`../explanation/`](../explanation/)  
- Iteration task-pack working drafts → [`../specs/`](../specs/)  
- Controlled onboarding exercises (one step, one expected result) → [`../tutorials/`](../tutorials/)
