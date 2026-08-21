# Agent Document-Driven Development System · Overview

> This file is the **entry and overview** for the **four** prompts under `agent-prompts/` (01 overall design / 02 module spec / 03 IDE implementation / 04 independent acceptance), and explains the relationship to the **`specs/` brownfield bypass**.  
> Read this file first, then open the relevant booklet or [specs/SDD-GUIDE.md](../../specs/SDD-GUIDE.md) as needed.

---

## 1. What this system solves

It cuts “from requirements to runnable code / from change to acceptable patch” into a pipeline that is **stage-clear, persisted to files, and acceptable**.

Core assumption: **The easiest mistake in AI coding is “quietly drifting from the spec just to make it run.”** The entire mechanism fights that one mistake.

**Default executor**: The **IDE Agent** designated by the maintainer runs stages in order within the same product (swap prompts / swap stage mindset).

### Dual-path overview

```
【Greenfield · Full track】New project / architecture undecided (same IDE Agent swaps prompts in order)
PRD (explanation/PRD.md)
  │  [01 · Architect stage]
  ▼
explanation/overall-design.md
reference/global-contract.md      (contract version anchor)
reference/progress.md             (module state machine)
  │  [02 · Architect stage, module by module]
  ▼
reference/modules/Fxx-{module}.md
  │  [03 · Engineer stage]
  ▼
Code + contract write-back; progress → 🔍 pending acceptance
  │  [04 · Accept stage: re-run with “accept mindset,” or maintainer accepts in person]
  ▼
Module ✅ → next module

【Greenfield · Lite track】01 artifacts already exist, and this module does not change architecture (maintainer must state explicitly)
  Skip 01 → 02 (lite) → 03 → 04
  Module spec must still be written to disk; ✅ still belongs to 04 / maintainer

【Brownfield】Patches / evolution after a module is already ✅ (IDE single line)
specs/tasks/task pack (incremental Spec)
  │  When in doubt, ask the maintainer first
  ▼
IDE coding + engineering self-check (+ optional receipt)
  │  Maintainer HITL / optional acceptance record
  ▼
Move into specs/archive/ (do not delete)
If contract changes → sync global-contract (+0.1)
```

**Greenfield iron rule**: Overall design → module spec → code → **independent acceptance once**. Full track must not skip steps and write undocument-persisted architecture into code; lite track skipping 01 requires all four conditions at once and an explicit maintainer statement—that does not count as skipping steps. Must not use 03 self-check as a substitute for 04 / maintainer.  
**Brownfield iron rule**: Short spec before large code changes; self-check ≠ HITL pass; see [SDD-GUIDE](../../specs/SDD-GUIDE.md).  
**Human–AI collaboration iron rule (universal)**: HITL + Spec-driven + **progressive alignment (agree one slice at a time)**—when product boundaries are unclear, confirm only one small slice at a time, and persist to files as soon as agreed. See [hitl-alignment.md](../hitl-alignment.md) · [SDD §2.5](../../specs/SDD-GUIDE.md).

### Immutable principles (Agents read this first)

Details are spread across later sections and bypass docs; the items below **must not be relaxed on your own**. Violation is a process incident.

| # | Principle | Details |
|---|-----------|---------|
| 1 | Requirements only recognize the current project’s `explanation/PRD.md` (body must already be written) | §2, §4.1 |
| 2 | Persist to files before large code changes; chat is not the source of truth | §4.9 · [hitl-alignment.md](../hitl-alignment.md) |
| 3 | One focus at a time (greenfield: one module / brownfield: one task pack) | §4.4 |
| 4 | Every contract change must bump the version and write a changelog | §4.3 |
| 5 | 03 must not self-mark ✅; greenfield ✅ only from 04 or the maintainer | §3, §5 |
| 6 | High-risk enumerated items must stop; must not self-judge as low-risk and continue | §4.6 |
| 7 | Fake green is invalid: run tests for real + non-shell assertions | §4.10 |
| 8 | After code exists, changing behavior: change the spec first, then the code | SDD-GUIDE §3 |
| 9 | Brownfield Specs use increments (ADDED / MODIFIED / REMOVED); acceptance uses WHEN/THEN | SDD-GUIDE §1.1 |
| 10 | Unsettled product / architecture major pivots: Agent must not autonomously declare a new stage | §6 |

---

## 2. Document path conventions

Paths in booklet bodies are written as `explanation/...`, `reference/...`, `specs/...`, semantically relative to the **docs root `docs/`**—**do not** resolve them relative to `how-to/agent-prompts/`.

| Current workspace | Prefix to use when reading/writing |
|-------------------|-------------------------------------|
| Workspace is the docs root itself (directory often named `docs/`) | Use the paths below as-is |
| Workspace is the repo root, and docs live under `docs/` | Prefix all doc paths with `docs/` |
| Docs root is not named `docs` | Confirm with the maintainer first; guessing is forbidden |

Code, tests, and engineering config are relative to the **repo root**.

### Greenfield pipeline I/O

| Stage | Role | Read | Write |
|-------|------|------|-------|
| — | Maintainer | — | `explanation/PRD.md` |
| 01 | Architect | PRD | `overall-design.md`; `global-contract.md`; `progress.md` |
| 02 | Architect | 01 three files + PRD | `modules/Fxx-*.md`; incremental contract / progress (→ 📝) |
| 03 | Engineer | Design + contract + this module’s spec | Code (repo root); write back contract and module spec (level 1); progress → 🔍 (✅ forbidden) |
| 04 | Accept | Module spec + contract + code | progress → ✅ or ⏸️; **do not change spec body** (if unqualified, escalate to 02 / 01; do not assign 03 to patch docs) |

### Brownfield pipeline I/O

| Stage | Role | Read | Write |
|-------|------|------|-------|
| Intake / spec | IDE Agent | Related module specs / contract / code | `specs/tasks/YYYY-MM-DD-*.md` (optional `-plan.md`) |
| Coding | IDE Agent | Task pack | Code; optional `-receipt.md` |
| HITL | Maintainer | Receipt / diff / feel | Decision; optional `-acceptance-record.md` |
| Archive | IDE / maintainer | — | Write `INDEX.md` then move into `specs/archive/YYYY-MM-DD-topic/` |

**Requirements only recognize** the current project’s `explanation/PRD.md`. If the landing note has not been written into the body, or the body belongs to a previous project, do not start 01.

### Persist-to-disk discipline

1. Greenfield **docs** may only land on the explanation / reference paths in the tables above: 01 writes overall-design / contract / progress; 02 writes Fxx + incremental contract / progress; 03 writes code (repo root) and writes back contract / module spec / progress (🔍); 04 **only changes** progress (✅ / ⏸️), not the spec body.  
2. Brownfield working drafts may only land under `specs/tasks/` (archive into `specs/archive/`; each bucket must have `INDEX.md`).  
3. Module spec naming: `F{two-digits}-{English-name}.md`.  
4. **Do not pre-create empty shells**: overall-design / global-contract / progress / Fxx are **created as complete files** by 01 / 02.  
5. Writing to the wrong directory is a process incident: move back and delete the miscreated files.

---

## 3. Greenfield four stages

| Booklet | Stage mindset | Input | Output | Confirmation gate |
|---------|---------------|-------|--------|-------------------|
| 01 | Architect | PRD | overall-design / global-contract / progress | Understanding summary confirmed first |
| 02 | Architect | Overall design + contract | `Fxx-*.md` + update contract / progress | Understanding summary + **contract diff** (lite track: summary ≤ 5 items; diff lists only touched items) |
| 03 | Engineer | Module spec + contract | Code + write back contract / module spec; progress → 🔍 | High-risk item confirmation + self-check table |
| 04 | Accept | Module spec + contract + code | Acceptance verdict; progress → ✅ or ⏸️; do not change spec body | Per module spec §11; if hollow, return to 02 |

**By default the same IDE Agent may execute in order** (swap prompts / swap stage; do not skip persisting to disk).

### Greenfield lite track (skip 01)

May proceed only when **all** conditions are met; missing any one means full track 01→04. The Agent **must not self-declare** lite track.

| Condition | Requirement |
|-----------|-------------|
| 01 artifacts already exist | `overall-design.md`, `global-contract.md`, and `progress.md` all exist and are the current baseline |
| This module does not change architecture | No change to tech stack / process model / module split / cross-module dependency graph |
| Order is valid | Take the next ⬜ module per progress; all predecessors are ✅ |
| Maintainer states explicitly | Oral or written “use lite track” |

Lite track still requires: 02 generate a complete 12-section-titled `Fxx-*.md` (irrelevant sections write “Not applicable to this module” + one-sentence reason); understanding summary ≤ 5 items; contract diff lists only conventions this module touches; §11 uses WHEN/THEN; then 03 → 04. **Do not reduce 04; do not self-mark ✅.**

If while working you discover architecture must change: stop, return to 01 for incremental revision of overall-design / contract, then continue.

**Boundary red lines**:

- Architecture decisions enter 03 only after 01 / 02 have persisted them to disk; 03 must not unilaterally change undocumented architecture, tech stack, or data models.  
- 03 only implements; it does not define “what should be done.”  
- 04 only accepts; it does not code or change the spec body (except progress ✅ / ⏸️); code mismatch returns to 03; unqualified specs escalate back to 02 / 01. **✅ only after 04 once or the maintainer**; 03 must not self-mark ✅.  
- **Forbidden to write implementation before design is persisted** (you may do 01→confirm→02→confirm→03 in the same session, but each stage must finish writing docs first).

---

## 4. Global discipline (applies to greenfield + brownfield alike)

1. **Clear requirements source**: Greenfield uses the current project’s `explanation/PRD.md` (body must already be written; must not use a landing note or a previous project’s requirements). Brownfield uses the task-pack Spec + existing contract / module specs.  
2. **Authority by state**: Greenfield (no code yet) uses docs as authority; **after code exists**, observable behavior uses code + tests as authority; changing behavior requires changing the spec first, then the code (see SDD-GUIDE §3).  
3. **Contract version must increment**: Every `global-contract.md` change is +0.1 + changelog.  
4. **One focus at a time**: Greenfield one module at a time (predecessors ✅); brownfield one task pack at a time.  
5. **No placeholders**: If not applicable, write “Not applicable to this project”; must not delete required module-spec headings.  
6. **Confirmation gate tiers**: 01 / 02 understanding summary and 02 contract diff are mandatory; 03 / brownfield coding pure-implementation steps may continue in a streak; **high-risk enumerated items** must stop.  
7. **Rollback is process, not failure**: Design defects go through rollback / escalation; quiet drift is forbidden.  
8. **Acceptance runs independently once**: Greenfield 04 (re-run with accept mindset or maintainer) / brownfield HITL; coding-stage self-check cannot substitute.  
9. **Process persisted to disk**: Specs, receipts, and acceptance written as files; do not pass long text via chat; brownfield defaults to thin drafts (see SDD-GUIDE).  
10. **Fake green is invalid**: Must run tests for real + non-shell assertions.

---

## 5. State machine and acceptance

```
⬜ Not started → 📝 Spec generated → 🔍 Pending acceptance → ✅ Done
Any state → ⏸️ Blocked (must reach a terminal state; note the reason)
```

| State | Who writes it |
|-------|---------------|
| ⬜ / 📝 | 01 / 02 |
| 🔍 | 03 (✅ forbidden) |
| ✅ | **Only 04 / maintainer** |
| ⏸️ | Whoever discovers it; must then reach a terminal state |

Brownfield tasks **do not** use this state machine in place of module rows; task closure lives under `specs/archive/`.

03 self-check cannot substitute for acceptance. 04 checks against module spec §11, and **prefers machine checks** (tests / lint / diff / red lines). Mark ✅ only on pass. When the same IDE Agent does 04, it must **swap to accept mindset** (check only; no code changes; no spec-body changes), or the maintainer accepts in person. Booklet: [04-accept.md](./04-accept.md). Brownfield acceptance: SDD-GUIDE §2.4 and the task-pack acceptance column.

---

## 6. Anti-patterns and boundaries

| Anti-pattern | Consequence | Correct practice |
|--------------|-------------|------------------|
| Let coding stage set architecture before persistence | Cross-module inconsistency | Architecture enters 03 only after 01 / 02 persist to disk |
| Quietly drift from docs just to make it run | Spec decouples | Write back first, then change code |
| Skip contract version increment | Diff becomes useless | Every time +0.1 + changelog |
| 03 self-marks ✅ | Self-checking self | Mark only 🔍; only 04 / maintainer marks ✅ |
| Treat empty-shell PRD / previous project requirements as input | Build the wrong product | Only current project `explanation/PRD.md` |
| Start coding before direction is clear | Wrongness enters implementation | Short spec first + ask when unsure |
| Pad a full set of process attachments for ceremony | Throughput collapses, context drifts | Brownfield IDE single line + thin persistence (attachments as needed) |
| Advance multiple modules / architecture packs in parallel | Contract conflicts | One at a time |
| Fake green | Behavior not landed | Run tests for real + non-shell |
| Coding side self-judges “whether high-risk” beyond authority | Overreach | High-risk enumerated list; if HITL is touched, ask |
| Skip 01 without explicit permission | Architecture quietly drifts | Lite track requires maintainer announcement; otherwise full track |

This system **explicitly does not support**:

1. **Multi-module parallel development** (greenfield): Must be one at a time; for parallelism choose another approach.  
2. **Production canary Schema migration**: 02 covers new-DB DDL, not canary playbooks.  
3. **Third-party API version-drift feedback loops**: Projects should nail down strategy in overall-design / contract themselves.  
4. **Executable Schema as sole authority**: This system carries “why” in natural-language specs; OpenAPI etc. may coexist and must be mapped by the project.  
5. **Unsettled product / milestone major pivots**: Requires maintainer HITL; Agent must not autonomously declare a “new stage.”

---

## 7. Delivery criteria and automation

Greenfield exit:

1. All modules ✅, order matches overall-design.  
2. global-contract has no pending changes; versions are continuous.  
3. Each module passed 04 independent acceptance (or maintainer sign-off).  
4. Full regression tests all green.  
5. PRD core features are traceable to module specs / code.

Brownfield has no “whole-repo delivery” concept; task acceptance records + contract sync are the standard.

Automation conventions:

1. Confirmation gates: pure implementation may continue in a streak; only high-risk enumeration blocks.  
2. Acceptance: machine check first, human judgment second.  
3. Engineering repos should harden how test suites and lint are run; recommended CI: dead links, tests, lint; docs side connects to [`specs/ci-probes.md`](../../specs/ci-probes.md) (reference implementation `ci-probes-reference.py`).  
4. Recommended: contract version continuity self-check (probe P1).

---

## 8. Booklet navigation

| File | Purpose |
|------|---------|
| [01-overall-design.md](./01-overall-design.md) | Greenfield: overall design + contract + progress |
| [02-module-spec.md](./02-module-spec.md) | Greenfield: module spec |
| [03-implement.md](./03-implement.md) | Greenfield: implement → 🔍 |
| [04-accept.md](./04-accept.md) | Greenfield: accept → ✅ |
| [../../specs/SDD-GUIDE.md](../../specs/SDD-GUIDE.md) | Brownfield: task packs / IDE single line / archive |
| [../../specs/ci-probes.md](../../specs/ci-probes.md) | CI machine-check probes |

---

*Overview · Brownfield IDE single line · Greenfield same Agent by stage · Human–AI collaboration iron rule (agree one slice at a time)*
