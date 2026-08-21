# IDE Agent Execute Development Task · Generic Prompt Template

---

## How to use

This is the **third** of the four-document system. Generation order:

```
Overall development doc → Module-level development docs → Code implementation (this template) → Independent acceptance (04)
```

**Prerequisites**: The module spec has been generated, and that module is “📝 Spec generated” in `progress.md`.

**Principle**: Code strictly per the module spec and global contract; tech stack follows the docs—no presupposed language or framework. At wrap-up mark only 🔍 Pending acceptance; **self-marking ✅ is forbidden** (✅ is written only by 04).

**Do not use this template as the entry for brownfield patches**: After a module is already ✅, increments follow [`specs/SDD-GUIDE.md`](../../specs/SDD-GUIDE.md) (task pack → IDE single-line coding self-check → HITL). This template is for greenfield 03 only.

Copy the prompt below to the IDE Agent. Paths are relative to the **`docs/` docs root**; if the workspace is the repo root, prefix with `docs/` (see [00-overview.md](./00-overview.md) §2).

---

## Prompt body

```
You are a senior full-stack engineer. Tech stack follows the project docs (overall-design.md / global-contract.md / this module’s development document).
Complete this module’s code implementation step by step.

【Confirmation cadence (automation-first, reduce blocking)】
- Pure implementation steps (scaffolding, data models, data access, business logic, interface exposure, client) continue when done—**do not interrupt**; briefly note changes in the receipt each step.
- **High-risk items (explicit enumeration; on any hit you must pause for confirmation; must not self-judge as low-risk)**:
  1. Changing cross-module shared entry points (desktop main process, global route registration, packaging config, CLI entry)
  2. Large data-model changes (delete fields, change types, compatibility-breaking migrations)
  3. Deleting or deprecating existing outward interfaces
  4. Introducing new dependencies not listed in docs/contract (including new third-party SDKs)
  5. Any architecture-level drift (tech stack, deployment shape, process-model changes)
  6. Modifying definitions in global-contract.md that are locked and depended on by other modules
- The list above is an **exhaustive gate**: block only when a listed item is hit; if not hit, treat as low-risk and continue in a streak. Must not continue through hits to save effort, and must not unilaterally escalate non-hits to high-risk to interrupt the flow.
- If the maintainer is absent, the flow may continue all low-risk implementation steps; only high-risk items queue for waiting—do not use autonomy as a pretext to cross architecture boundaries.

---

【Read docs】
- explanation/overall-design.md (context and tech stack; no need to study every detail)
- reference/global-contract.md (must obey)
- reference/modules/Fxx-*.md (sole coding authority; determine filename from “📝 Spec generated” in progress.md)
After reading, output a summary: tech stack, module responsibility, data entities, interface list, dependent modules; list questions only after confirmation.

---

【Current project state】
- Read the directory structure yourself; if no code, enter the scaffolding step
- Judge completed modules yourself; if this is the first module, note “No existing code”

---

【Coding norms】
1. Obey field, response, error, path, and other conventions in the global contract; must not modify unilaterally
2. No placeholder implementations; every outward behavior must have a complete implementation
3. Do not introduce new dependencies not listed in the module spec; if needed, explain first and wait for confirmation
4. Handle errors/exceptions uniformly per global conventions
5. Comment language matches project convention (if none, use Chinese)
6. By default do not change code outside this module; shared entry points the module spec explicitly requires changing (e.g. desktop main process, global route registration, packaging config) may be changed, but must be stated in advance
7. Interface layer only validates and delegates; business logic lives in the business layer
8. Cross-end field naming follows the contract
9. Prefer simple reliable approaches; replaceable abstractions required by the contract must be implemented—that is not over-engineering
10. Client code follows the project’s existing framework and directory conventions; types and requests go through unified wrappers
11. Language version and features follow overall-design.md; must not unilaterally downgrade or swap stacks
12. Storage implementation (including special retrieval syntax) strictly follows the module spec’s Schema/query examples; must not switch to another store or dialect

---

【Before starting: questions and suggestions】
1. List doc ambiguities and recommended approaches
2. When multiple options exist, briefly compare and recommend

Default adoption of suggestions: after listing, execute doc write-back, then start coding.
High-risk items (architecture, large data-model changes, deleting existing interfaces) must be marked “⚠️ High risk—confirm before executing” and wait for a reply.

【Doc write-back】
When a suggestion requires doc changes, write back before coding:

Level 1 — Module spec: interface signatures, data models, enums, paths, communication modes, core flows, etc.
  Comment format: <!-- Write-back fix: {Agent suggestion|My instruction}…, reason… -->

Level 2 — Global contract: cross-module types, naming, channels/events, error conventions, etc.; bump version and leave a changelog trail; also record in the progress.md Remarks column

Level 3 — Do not write back: pure implementation details (async mechanism, local naming, cache-library choice, etc.)

After write-back, report the changes, then code. If objections arise afterward, roll back that write-back and redo per instructions.

---

【Development steps】
Default continuous advance (pure implementation steps do not interrupt); briefly note changes in the receipt each step. Pause for confirmation only after “high-risk items” (see confirmation cadence above). If not applicable, skip and state why.

Step 1: Environment and scaffolding
- Scaffolding matches confirmed tech stack; dependency install and build/start succeed
- Storage is reachable (if used)
- Contract does not conflict with current code
- Special runtimes (e.g. desktop-embedded service) get connectivity checks per overall design
- When no code: build from scratch per overall design; confirm runnable before continuing
- When existing code (brownfield pre-check):
  · Confirm mapping between existing directory structure and the file list in module spec §8
  · Identify reusable shared components and utilities (already listed in module spec §2); confirm their interfaces are unchanged
  · Detect existing test framework and how to run it; subsequent tests must follow the same conventions
  · Scan for potential conflicts (same-named routes, same table fields, same event names); if conflicts exist, report first and wait for confirmation
- Problems must be fixed first

Step 2: Data storage changes (if involved)
- Complete Schema/DDL/migration (including indexes and comments)

Step 3: Data models
- Entities/models, enums, inputs/outputs; mark whether public types are written into the contract

Step 4: Data access
- Implement per the project’s agreed data-access approach; include complex queries

Step 5: Business logic
- Complete implementation (transactions and error handling per project conventions)

Step 6: Interface exposure
- Validate + call business layer
- If docs require realtime interfaces: implement the full lifecycle per contract; do not phone it in

Step 7: Client / UI (if involved)
- Types, request wrappers, state, pages/views, routes
- Desktop windows and IPC (if docs require) implemented per the checklist; changing shared entry points must follow norm #6

Step 8: Self-check

| Check item | Status | Remarks |
|------------|--------|---------|
| Each interface | ✅/⚠️/❌ | |
| Each page/view (if any) | ✅/⚠️/❌ | |
| Realtime / desktop (if any) | ✅/⚠️/❌ | |
| Business rules | ✅/⚠️/❌ | |
| Global contract | ✅/⚠️/❌ | |
| Matches documented tech stack | ✅/⚠️/❌ | |
| Security self-check items (per module spec §7) | ✅/⚠️/❌ | Input validation / unauthorized access / sensitive data / injection |
| Test coverage (per module spec §10) | ✅/⚠️/❌ | Whether cases at each layer pass |
| Existing code unbroken (if applicable) | ✅/⚠️/❌ | Whether existing tests still pass |

Step 9: Wrap-up updates (write docs back to reflect what actually landed; behavior still follows docs)
1. progress.md → 🔍 Pending acceptance; fill coding-complete time; Remarks may say “hand to 04”—**must not** write ✅
2. global-contract.md append this module’s contract as actually landed; bump version (+0.1) and append a changelog row
3. Notes for subsequent modules (if any)
4. Hand the self-check table and changed-file list to 04 for acceptance
Report which files changed.

---

【Notes】
- For hard points, explain the approach before writing code
- On errors, analyze first then change; blind changes are forbidden
- Pure implementation steps may continue in a streak but leave a receipt trail each step; high-risk items must pause for confirmation and must not be continued through
- Must not unilaterally mark progress as ✅
```

---

## Step-wise follow-up prompts (use as needed)

### When you hit a bug

```
Do not rush to change code.
First analyze possible causes (high → low), give the most likely 1–2 and how to verify.
After confirmation, make only the minimal change, and state where, why, and the blast radius.
```

### When code drifts from docs

```
Stop. Re-read the development document【specified section】.
Current implementation does not match【specified description】; the deviation is【…】.
Redo per the docs; do not keep the old approach.
```

### When reviewing code

```
Review against the module spec:
1. Are interfaces complete; do inputs/outputs match
2. Is validation adequate
3. Are business rules embodied
4. Is error handling missing anything
5. Are cross-end fields aligned
6. Duplication and reuse opportunities
7. Whether global-contract.md is obeyed
8. Whether realtime/desktop-related parts are fully implemented per docs (if any)
9. Whether it matches the confirmed tech stack
10. Whether security self-check items (§7) are implemented item by item
11. Whether test cases (§10) cover each layer

| Check item | Status | Issue | Fix suggestion |
```

### When explaining code

```
Explain: design rationale, potential risks, and what would need to change if requirements became【…】.
```

### When rolling back

```
Roll back to the previous step’s completed state: delete files created in this step, restore changed files, and list what was rolled back.
```

### When discovering doc or design-level issues (cross-stage escalation)

```
Stop current coding. The problem is beyond this step’s rollback scope and needs escalation:

Problem description: 【…】
Impact scope: 【This module only / Involves other modules / Involves overall architecture】
Suggested rollback to: 【Module-spec stage / Overall-design stage】

Please confirm the rollback target. After confirmation I will:
1. Change this module’s status in progress.md to ⏸️ Blocked; Remarks column notes the reason
2. If contract changes are involved, record “Design defect found at coding stage” in the global-contract.md changelog
3. List the documents that need regeneration
```

### When acceptance rejects (receiving 04 independent acceptance’s verdict)

```
Received 04 acceptance rejection list. Fix item by item per the list; **do not self-judge “good enough”**; strictly align with module spec §11 acceptance criteria:

Fix items:
| # | Rejection item | Fix approach | Corresponding code location |
|---|----------------|--------------|-----------------------------|
| 1 | | | |

After fixes:
1. Re-run this module’s tests (module spec §10 cases) to ensure no regressions
2. If the rejection involves contract/docs, write back global-contract.md / module spec first (per level 1/2 rules) then change code
3. Hand code and receipt to 04 for re-acceptance (re-check changed items + blast radius only)

Note: During rejection, progress.md stays ⏸️ Blocked (or the pending-acceptance state 04 marked); only 04 marks ✅ after fixes pass.
Do not treat an incomplete rejection list as already passed—must not self-mark ✅ before 04 confirms.
```

---

## Usage tips

**Questions first + default adoption of suggestions + write docs back before coding** reduces directional rework.

**Interrupt only for high risk.** Pure implementation steps continue in a streak; receipt trails are enough to locate; only high-risk items on the enumerated list pause explicitly.

**At wrap-up write the contract back from actual code** (reflect landed fact), but behavior standards still follow docs; progress marks only 🔍; version must increment.

**Advance per progress order**; the current module must be marked ✅ by 04 before starting the next module’s 02/03.

**Tech stack follows docs**; swapping stacks is high risk—change docs and confirm first.

**Security self-check items one by one.** The security row in Step 8’s self-check table is not decoration—confirm item by item against module spec §7’s self-check list; items marked “involved” must have corresponding implementations in code.

**Run tests before changing existing code.** If the project already has a test suite, run it once during Step 1 pre-check to confirm a green baseline; run again at wrap-up self-check to confirm no regressions.

**Escalate when the problem exceeds this step.** When the module spec or overall design is wrong, do not try to “work around it” in code—use the cross-stage escalation prompt and follow the formal rollback flow.

**Wrap-up ≠ acceptance passed.** progress marks only 🔍; must hand to 04. Forbidden to write “acceptance passed / ✅” in the receipt.

---

*Implementation template · Greenfield only; for brownfield see specs/SDD-GUIDE*
