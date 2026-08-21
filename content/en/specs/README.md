# specs · brownfield / iteration bypass (SDD)

> **Role**: After modules are landed and code exists, patches and evolution go here; **does not replace** greenfield `01→02→03→04`.  
> **Current flow**: **IDE single-line** (same session: draft Spec → code → self-verify → write back) + **§2.5 incremental consensus** (agree one slice at a time HITL). Authoritative detail: [SDD-GUIDE.md](./SDD-GUIDE.md).  
> **Entry**: this directory’s GUIDE; HITL page [../how-to/hitl-alignment.md](../how-to/hitl-alignment.md); system overview [../how-to/agent-prompts/00-overview.md](../how-to/agent-prompts/00-overview.md).

---

## When greenfield vs this directory

| Scenario | Which path |
|------|--------|
| New project from scratch, or architecture undecided (stack swap, module split change) | **Greenfield full track**: PRD → 01 → 02 → 03 → 04 |
| 01 artifacts exist; open the next undocumented module per `progress.md`, without changing architecture | **Greenfield lightweight track** (maintainer must say so): skip 01 → 02 (lightweight) → 03 → 04 |
| Behavior patches, regression fixes, small evolution, protocol tweaks after a module is ✅ | **Brownfield**: `specs/tasks/` task pack → IDE code + self-verify → (optional acceptance record) → `archive/` |
| Change touches cross-module contract | Brownfield task pack **also** writes back `reference/global-contract.md` (version +0.1) |
| Unsure | Maintainer decides; default: **changes external behavior → brownfield task pack** |

---

## Directory structure

```text
specs/
├── README.md                 ← this page
├── SDD-GUIDE.md              ← process authority (single-line, §2.5 agree one slice at a time, HITL)
├── ci-probes.md              ← CI machine-check Spec (optional wire into engineering repo)
├── ci-probes-reference.py    ← probe reference implementation
├── tasks/                    ← in-progress task packs (open items only)
│   ├── README.md
│   └── _template.md
└── archive/                  ← move here after close; keep history; bucket must have INDEX.md
    ├── README.md
    └── _index-template.md
```

| Doc | Purpose |
|------|------|
| [SDD-GUIDE.md](./SDD-GUIDE.md) | How to write brownfield Specs and accept them; **§2.5 incremental consensus 【mandatory】** |
| [ci-probes.md](./ci-probes.md) | Machine-probe checklist against docs drift |
| [tasks/_template.md](./tasks/_template.md) | Task-pack template (copy and rename) |
| [tasks/](./tasks/) | Open task-pack directory |
| [archive/](./archive/) | Closed task archive (keep; bucket must have INDEX.md) |
| [archive/_index-template.md](./archive/_index-template.md) | Archive conclusion-page template |

---

## How to open a brownfield task (shortest path)

1. Copy [`tasks/_template.md`](./tasks/_template.md) → `tasks/YYYY-MM-DD-short-name.md`  
2. Write **current behavior** + **ADDED / MODIFIED / REMOVED**; acceptance uses WHEN/THEN  
3. When product boundaries are unclear, fill HITL **one slice at a time**; write to disk as soon as agreed  
4. After maintainer **coding authorization**, make large code changes; same session for engineering self-verify  
5. If you touch the contract, write back `reference/global-contract.md` (bump version)  
6. Write the matching `INDEX.md` from `archive/_index-template.md` (conclusion + whether contract was written back), then move the whole set into `archive/YYYY-MM-DD-topic/`; do not delete working drafts. **No INDEX → must not move.**  

Detail and anti-patterns: [SDD-GUIDE.md](./SDD-GUIDE.md).

---

## Relationship to reference / progress

- **Greenfield module status** still follows `reference/progress.md` (⬜→📝→🔍→✅).  
- **Brownfield tasks** do not occupy “not started” module rows in progress; close them in the task pack and acceptance record.  
- If brownfield creates new cross-module conventions, they must land in `global-contract.md`; leave a one-line pointer in the progress notes column when needed.

---

## Do not put here

- Greenfield overall design / module specs → [`../explanation/`](../explanation/), [`../reference/`](../reference/)  
- Repeatable how-to manuals → [`../how-to/`](../how-to/)  
- Controlled onboarding exercises → [`../tutorials/`](../tutorials/)
