# HITL iron rule · incremental consensus (agree one slice at a time)

> **Role**: A **product-agnostic requirements workflow**. After you copy this template into any repo’s `docs/`, this is the default.  
> **Authoritative detail**: [`../specs/SDD-GUIDE.md`](../specs/SDD-GUIDE.md) **§2.5**; also linked from the ★ at the top of [`../README.md`](../README.md).

---

## In one sentence

**Incremental consensus under HITL + Spec-driven**: the maintainer must approve key decisions; write observable Specs first; **confirm one small slice at a time, write to disk as soon as agreed**, then code.

This is not a chat habit — it is a formal workflow.

---

## Three names (easy to say externally)

| Name | Meaning |
|------|------|
| **HITL (human in the loop)** | Key product / direction decisions need **maintainer approval**; the Agent must not lock them in unilaterally |
| **Spec-driven** | Write observable behavior into the spec first (greenfield: module doc section 11; brownfield: task pack), then code |
| **Incremental consensus / agree one slice at a time** | One slice at a time; write to disk as soon as agreed; do not batch until the end, and do not treat chat history as the source of truth |

Cousin: agile **Example Mapping** (short dialogues to pin rules and edges) — no mandatory card ritual; take only the small-step alignment.  
Common AI cadence Plan → Confirm → Implement: here Confirm is **split into multiple beats**, and each beat **writes docs immediately**.

---

## When to use

- New capability / unclear new module boundaries  
- How intent is recognized, and how to draw lines with neighboring capabilities  
- Persona, confirmation strategy, permissive vs. cautious product judgment calls  

Trivial bugfixes (typos, unit-test assertions) need not run the full loop.

---

## How to do it (default cadence)

1. The Agent **offers only one slice** of idea or decision at a time (keep it short; if the maintainer says “don’t say too much at once,” obey).  
2. The maintainer responds (yes / change / no).  
3. **Write to disk as soon as agreed** — greenfield: into 01 / 02 understanding summaries, the matching module-doc section, or the HITL table; brownfield: into the task pack (incremental Spec: ADDED / MODIFIED / REMOVED + WHEN/THEN acceptance + HITL table). Sync contract / design docs when needed — **do not wait until the end to record**.  
4. Then offer the next slice; once key HITL items are settled → maintainer **authorizes coding** → then make large code changes.  
5. If a new decision appears during coding: stop, return to 1–3; do not silently expand scope.

Both greenfield `01→04` and brownfield `specs/tasks` apply the “agree one slice at a time” spirit. **The most common greenfield landing spots are understanding summaries / module docs; the most common brownfield landing spot is the task pack.** Do not create a separate task pack solely for “agree one slice at a time” when greenfield has not yet opened a task.

---

## Anti-patterns (treat as process violations)

- Dumping a long list of “please decide all of these together” in one go  
- Talking a lot without writing to disk, treating chat history as the source of truth  
- Starting implementation before authorization; or after authorization, folding “separate knife-work” into this pack

---

## Relationship to other template files

| File | Relationship |
|------|------|
| [README.md](../README.md) | Opening ★ iron rule (first glance) |
| [SDD-GUIDE §2.5](../specs/SDD-GUIDE.md) | Mandatory detail inside the brownfield flow |
| [00 overview](./agent-prompts/00-overview.md) | Greenfield / dual-path entry mentions this iron rule |
| [tasks/_template.md](../specs/tasks/_template.md) | Where HITL decision points are written to disk |

When copying this `docs/` into a new repo, **keep this section and the README ★**, then write that project’s PRD.
