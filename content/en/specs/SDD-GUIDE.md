# SDD-GUIDE: how to write brownfield / iteration specs (anti-drift)

> **Role**: Spec-driven process after code exists. Parallel to greenfield `01→04`; neither replaces the other.  
> **References**: ThoughtWorks SDD, GitHub Spec Kit; archive without deleting (working drafts are long-lived assets).  
> **HITL iron rule** (same meaning as the ★ at the top of [`../README.md`](../README.md)): **HITL + Spec-driven + incremental consensus (agree one slice at a time)** — see **§2.5** and [how-to/hitl-alignment.md](../how-to/hitl-alignment.md). This is the default posture for locking Spec, not optional chat.

---

## 1. When to write a task pack

Any change that **alters external behavior / cross-module conventions** first lands a task pack under `specs/tasks/` (use `_template.md`):

- Spec: observable outcomes, written **incrementally** (current behavior + ADDED / MODIFIED / REMOVED) — no implementation detail, no full rewrite of the module spec  
- Implementation: checkable steps; large changes may attach an optional `-design.md`  
- Acceptance: WHEN … THEN … checkable list (ban “works fine”)  
- Contract change: if you touch the contract, check it and write back the version  
- HITL: what needs maintainer approval  
- **When product boundaries are unclear**: fill HITL with §2.5 agree-one-slice-at-a-time, then authorize coding — **forbid** dumping a long list at once or finishing chat without writing to disk  

Pure typos, pure comments, agreed formatting → pack optional (maintainer may tighten).

### 1.1 How to write Spec increments

Against code + tests, write “current behavior,” then express “target behavior” with three increment markers:

| Marker | Meaning |
|------|------|
| **ADDED** | New observable behavior |
| **MODIFIED** | Existing behavior changes from A to B (must state both A and B) |
| **REMOVED** | Behavior removed (state the reason; breaking changes require HITL) |

On archive, these increments are the audit trail; if you changed cross-module conventions, you must also write back `global-contract.md` — do not leave the change only in the task pack.

---

## 2. Separate Spec from implementation + IDE single-line default

- Short Spec first → then implement → check acceptance → write back authoritative docs.  
- After the task closes, **archive under `specs/archive/` without deleting**.  
- `specs/tasks/` = in progress; closed items move to archive.

> **Why single-line:** Splitting across two Agents yields no shared working memory; thick process docs still drift in understanding. When the maintainer stays in one IDE, one continuous IDE Agent run is stabler.

### 2.1 Default: one continuous IDE Agent run

| Duty | Who |
|------|-----|
| Draft / revise task pack and implementation plan | IDE Agent (or maintainer dictates, then write to disk) |
| Land business code / tests | IDE Agent |
| Engineering self-verify (tests / lint / acceptance column) | IDE Agent |
| Write back contract / module docs / progress notes | IDE Agent |
| Feel / product / direction / breaking-contract approval | **Maintainer** (HITL) |

**Discipline:**

1. **Write to disk before large code changes**: for non-trivial work, write/update the task pack first.  
2. **Ask when unsure**: stack swaps, breaking contracts, large product-scope shifts → stop and ask the maintainer.  
3. **One pack at a time**.  
4. **Thin working drafts**: default is the task pack itself; design / receipt / acceptance record only as needed — do not pad a full set.

### 2.2 Write to disk; do not pass long text only via chat

- In progress → `specs/tasks/`  
- After close → `specs/archive/YYYY-MM-DD-topic/` (**do not delete**; bucket **must** have `INDEX.md`, copied from [`archive/_index-template.md`](./archive/_index-template.md))  
- The Agent **reads the directory directly**.

**Naming** (prefix `YYYY-MM-DD-task-name`):

| Suffix | When |
|------|------|
| `.md` (task-pack body) | **Always** |
| `-design.md` (optional) | Large change surface / maintainer should see design first |
| `-receipt.md` (optional) | After coding, leave a change + self-verify summary |
| `-acceptance.md` (optional) | When acceptance is checked in writing (maintainer or IDE) |

> Chinese corpus (`content/zh`) uses the same attachment roles with suffixes `-方案.md`, `-回执.md`, and `-验收记录.md`. Do not mix suffixes inside one language tree.

### 2.3 Pre-coding self-check

```
① Read code + write/update task pack (Spec / acceptance / HITL)
       ↓
② HITL: when boundaries are unclear, use §2.5 incremental consensus (agree one slice at a time, write to disk when agreed); when ready, wait for maintainer coding authorization
       ↓
③ Code + test
       ↓
④ Write back docs; drop a receipt when needed; write `INDEX.md` then move the whole set to archive
```

- Trivial changes may skip a full task pack, but must still write back to prevent drift.  
- High risk / uncertain: maintainer may require “design only, no code yet,” or **optionally** ask another reviewer to **read one short design page** (advisory; not a default pipeline stage).  
- “Coding before the direction is clear” is still an incident — use a short Spec + ask when unsure + **§2.5**.  
- When product boundaries are unclear: prefer §2.5; do not dump a long design checklist at once.

### 2.4 Acceptance ownership

| Action | Meaning |
|------|------|
| Engineering self-verify | IDE against acceptance column (WHEN/THEN) + machine checks; **≠ product pass** |
| HITL / product acceptance | Maintainer; may write `-acceptance.md` when needed |

Acceptance column forbids non-decidable phrases like “works fine.” IDE receipts must not self-mark “product acceptance passed / ✅” to fake HITL.

### 2.5 Incremental consensus (agree one slice at a time · HITL dialogue discipline) 【core · mandatory】

**What it is:**

- **HITL**: maintainer approves key decisions; Agent does not lock them unilaterally.  
- **Spec-driven**: alignment results go into **this task pack** Spec / HITL table, then coding (this section governs brownfield; greenfield landing spots: [hitl-alignment.md](../how-to/hitl-alignment.md)).  
- **Incremental consensus**: one small slice at a time; write to disk when agreed — avoid one long dump that causes forgetting and oral drift.  
- Cousin: Example Mapping (small steps to pin edges).  
- Plan → Confirm → Implement: Confirm in **multiple beats** + **docs written each beat**.

**One sentence:** Incremental consensus under HITL + Spec-driven; not ad-hoc chat — a real requirements workflow.

**When to use:** Opening a pack for a new capability; confirmation/intent strategy; boundaries with neighbors still unclear. Trivial bugfixes need not run the full loop.

**How:**

1. Agent **offers only one slice** at a time (keep it short).  
2. Maintainer responds (yes / change / no).  
3. **Write into the task pack Spec + HITL (and contract, etc.) as soon as agreed** — **do not batch until the end**.  
4. Key HITL settled → **coding authorization** → then large code changes.  
5. New decisions during coding: stop, return to 1–3.

**Anti-patterns (process violations):** Approve a long list in one go; finish chat without writing to disk; change code before authorization; fold “separate knife-work” into this pack.

**With §2.1–2.3:** Incremental consensus is the **default method** for filling HITL / clarifying Spec on the IDE single-line. Dedicated page: [hitl-alignment.md](../how-to/hitl-alignment.md).

---

## 3. Authority by stage (greenfield vs after code exists)

| Stage | Who wins on behavior conflict | How to change behavior |
|------|------------------|--------------|
| **Greenfield** (module has no code yet, or 03 in progress) | Module docs + `global-contract` win | Write back docs first, then change code |
| **After code exists** (brownfield task) | **Observable behavior: code + tests win**; stale specs must be written back | **Change Spec (task pack/contract) first, then code** — forbid “just change code and leave docs” |

Do not use “docs always override code” in brownfield to hide unwritten drift.

---

## 4. Anti-drift

1. Changing constants, defaults, public protocols, module/file names, feature flags → find hard-coded same values under `docs/` and write them back.  
2. Contract changes must bump `global-contract` version +0.1 + changelog.  
3. Prefer machine checks for acceptance: tests / lint / diff scope / red-line grep (call project `tools/verify_*` when provided).  
4. Fake green is invalid: shell implementations, tests that never run → reject.  

---

## 5. HITL decision routing

| Category | Examples | Route |
|------|------|------|
| Autonomous | Draft task pack, implementation detail, engineering self-verify, write to disk, routine commit | IDE Agent |
| Needs maintainer approval | Stack swap, large product-scope shift, breaking contract change, whether to open a new milestone, workflow track change | Block @maintainer |
| Async OK | Copy tone, non-blocking observation cadence | Do not block the current pack; decide when convenient |

Autonomous items must not quietly change architecture direction or locked contracts; if they do, escalate to approval.

---

## 6. Handoff with greenfield 01–04

- **New project / architecture undecided**: run full 01→02→03→04.  
- **overall-design / contract / progress already exist, and this module does not change architecture**: maintainer may declare **greenfield lightweight track** — skip 01, run only 02 (lightweight) → 03 → 04. Detail: [00-overview §3](../how-to/agent-prompts/00-overview.md).  
- **Increments after a module is ✅** follow this GUIDE (task packs); do not open a new Fxx for small patches.  
- Greenfield 03 close marks progress 🔍 only; ✅ still belongs to independent 04 or the maintainer — same shape as brownfield “self-verify ≠ HITL pass.”  

See [00-overview](../how-to/agent-prompts/00-overview.md) “dual paths.”
