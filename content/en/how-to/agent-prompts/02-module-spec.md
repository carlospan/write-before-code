# Generate Module Development Doc · Generic Prompt Template

---

## How to use

This is the **second** of the four-document system. Generation order:

```
Overall development doc → Module-level development docs (this template) → Code implementation → Independent acceptance
```

**Prerequisites**:
- `explanation/overall-design.md`
- `reference/global-contract.md`
- `reference/progress.md`

**Principle**: Follow the PRD, overall design, and global contract. DDL, types, paths, and implementation points are written per the confirmed tech stack—do not apply habits from other languages or frameworks.

**After generation, outputs**:
1. `reference/modules/F{two-digit-number}-{module-English-name}.md`
2. Update `reference/global-contract.md` (this module’s increment)
3. Update `reference/progress.md` (this module → 📝 Spec generated)

**Lite track** (maintainer must state explicitly; see [00-overview §3](./00-overview.md)): when 01 artifacts already exist and this module does not change architecture, still use this template, but understanding summary ≤ 5 items and contract diff lists only items this module touches; the 12 section headings must not be deleted—irrelevant ones write “Not applicable to this module” + one-sentence reason. §11 still requires WHEN/THEN. Then proceed 03 → 04 as usual.

Copy the prompt below to the **Architect-stage** Agent. Paths are relative to the **`docs/` docs root**; if the workspace is the repo root, prefix with `docs/` (see [00-overview.md](./00-overview.md) §2).

---

## Prompt body

```
You are a senior full-stack architect. Based on the project's overall design and global contract, generate a module development document for the specified module that an IDE Agent can code from directly.
Fields, interfaces, and business rules must be precise enough to generate code; syntax and structure must match the confirmed tech stack.

---

【Prerequisite docs: read and consistency check】
- explanation/overall-design.md
- reference/global-contract.md (must obey)
- reference/progress.md
After reading, understand: overall architecture, confirmed tech stack, existing contract, current progress.
Record the current contract version (header of global-contract.md: “Contract version: vX.X”); subsequent updates in this run increment from that version.
If both global-contract.md and progress.md annotate a contract baseline version and they disagree, stop and tell me to align first; if no baseline version number has been established yet, skip this check and add it during this contract update.

---

【This module’s info】
Purpose: Generate a development document for this module
Selection rule: Per progress.md development order, take the next module that is “⬜ Not started, and all predecessor dependencies are ✅ Done” (if you need to specify, replace the next line)
Module name: Determine automatically per the rule above
Track: Full (default) / Lite (only when the maintainer states explicitly, and 01 artifacts already exist, and this module does not change architecture)
  - Lite: understanding summary no more than 5 items; contract diff lists only convention rows this module actually touches; all 12 section headings still present
Special requirements: None (note if any, e.g. realtime streaming, external services, desktop windows, background tasks—must be consistent with PRD/overall design)

---

【Step 1: Output an understanding summary; wait for my confirmation before continuing】
1. Core responsibility (one sentence)
2. Data entities involved (names, main fields, relationships to existing entities)
3. Main interface list and approximate count (per this project's actual interface shape: HTTP / RPC / CLI / events, etc.)
4. Dependencies on existing modules (what is called, what is reused)
5. Technical hard points (if any)
6. This module’s tech-stack highlights (restate from overall-design.md; do not invent)
7. Places in the overall design that are unclear about this module

Do the contract diff only after confirmation.

---

【Step 2: Contract diff; wait for my confirmation before generating the document】
Diff this module’s design against global-contract.md and output a table. Scope trimmed to conventions this project actually enables:

1. Data entities: field names/types/defaults/null constraints
2. Existing modules’ outward interfaces: params and return types (enums must use contract definitions, not bare strings)
3. Enums: value sets must match exactly; additions must change the contract first
4. Error representation: must not conflict with existing error codes/types; must fit global segment or classification conventions
5. Interface paths or routes: must fit global path/naming conventions
6. If the project enables realtime channels, IPC, etc.: new names must not conflict with the contract

| Diff item | Contract definition (section & line) | This module’s design | Result |
|-----------|--------------------------------------|----------------------|--------|
| … | … | … | Match / Diff → contract wins |

The “Contract definition” column must cite section and approximate line numbers, proving the original text was read rather than recalled from memory.
On any difference, the contract wins. If the contract has gaps, patch the contract first, then write the module spec, and list this run’s supplements in §12.
**Contract conflict arbitration**: If this module’s design reveals contradictions among existing contract definitions (e.g. module A’s contract and module B’s contract disagree on the same concept), do not pick one yourself—pause, list both sides’ original text and impact scope, and hand to the maintainer to decide (or roll back to 01 to revise overall design). Contract conflicts are architecture-level; they are not silently resolved at the module-spec stage.

---

【Step 3: Generate the module development document】
Generate in the structure below; irrelevant sections write “Not applicable to this module”; do not delete headings.

1. Module positioning
   - Responsibility and place in the project
   - **Covered PRD items** (IDs/sections, aligned with the “Covered PRD items” column in overall-design.md’s development-order table; if multiple modules share one item, note each module’s part)
   - Core business flow (ASCII)
   - Data flow (upstream/downstream; if simple, may merge into the flow diagram)

2. Dependencies on existing modules and brownfield code adaptation
   - Forward dependencies: who is depended on, what specifically is used
   - Reverse impact: whether existing code/config must change; if yes, write impact assessment item by item; if no, note not applicable
   - Brownfield code adaptation (if the project is not greenfield):
     · Mapping between existing directory structure and this module’s file list
     · Reusable shared components, utility functions, middleware (list paths and purposes)
     · Existing test framework and case organization; this module’s tests must follow the same conventions
     · Potential conflict points (e.g. same-named routes, same table fields, same event names) and avoidance plans

3. Data storage design
   - Complete Schema / DDL / migration notes (syntax matches the chosen store)
   - Field purpose comments; types, constraints, defaults written in full
   - Index or retrieval design and rationale
   - Structure changes must include change statements or migration steps
   - Only when this module needs vector/full-text or other special retrieval: supplement types, metrics, indexes, and query examples (dialect per chosen store)

4. Type definitions (new in this module)
   - Backend: persistence models, inputs, outputs (correspond to storage fields; syntax per confirmed backend language)
   - Frontend or other clients: write in the project’s agreed type system (if no frontend, note not applicable)
   - Enums (if any)
   - Mark which must enter the global contract

5. States and rules (if any)
   - Discrete states: state values, transition diagram, operations allowed per state
   - Scoring/rule-driven: input factors → decision → action; attach flow
   - If neither, note not applicable

6. Interface detailed design
   - Overview table (method or operation name / path or id / description / auth requirements)
   - Each interface: inputs, success response (business data portion per global response conventions), failure response
   - Lists/pagination follow global conventions
   - Realtime interfaces (only when involved): event types, payloads, connection lifecycle, chunking and end conventions
   - If not involved, note so

7. Core business logic
   - Key operation steps
   - Boundaries and exceptions
   - Data isolation or permission rules (if applicable)
   - Security and performance self-check (trim to what this module actually involves; note if not involved):
     · Input validation: which inputs need validation, validation rules (type/range/format/length)
     · Privilege escalation / unauthorized access prevention: which operations need resource ownership or role checks
     · Sensitive data: whether this module involves sensitive fields; how storage/transit/logs handle them
     · Injection prevention: where queries/commands/templates are concatenated and how they are protected
     · Concurrency and idempotency: whether write ops need idempotent design or optimistic locks
     · Performance boundaries: pagination/rate-limit/cache strategy for large-data scenarios; slow-query risk points

8. Server implementation points
   - Planned file list (full paths, matching directory conventions)
   - Reused existing capabilities
   - Hard-point approaches (recommended + alternatives)
   - Forbidden items (e.g. must not change other modules, must not add dependencies unilaterally)
   - Background tasks (only when involved): triggers, lifecycle, outward status, relationship to global task conventions
   - External services (only when involved): dependency abstraction boundary, config and secret sources, timeout/retry/degrade (cite global conventions)

9. Client / UI implementation points (per project shape: Web / desktop / other)
   - Pages or views, routing, key interactions, state-management points
   - Desktop windows / IPC / system integration (only when involved)
   - If no UI, note not applicable

10. Test strategy and cases
    - Test layering (per the project’s existing test framework; if none, note “Manual verification primary,” but cases must still be fully listed):
      · Unit tests: pure business logic, utilities, state transitions, rule computation—no external service dependency
      · Integration tests: data access layer (including complex queries and transactions), inter-module interface calls, external service mocks
      · Interface/E2E: each outward interface at least 1 happy path + 1 exception; if auth is involved, add unauthorized-access cases
      · **Contract tests**: write automatic assertions per global-contract.md’s interface/error/enum/path conventions so this module’s implementation does not drift from the contract—this is the machine-checkable extension of contract versioning, especially effective for cross-module regression
    - Happy / exception flow table (label each case’s layer)
    - When realtime or background tasks are involved, add matching scenarios (disconnect/reconnect, task timeout/retry/cancel)
    - Security-related cases: injection attempts, unauthorized access, sensitive-data leak checks (corresponding to §7 self-check items)
    - Performance baselines (if §7 identified performance risk points): give quantifiable response-time or throughput expectations

11. Acceptance criteria
    - Each item must be externally decidable. Forbidden: “works normally,” “good UX,” “works as expected”
    - Default phrasing: WHEN <condition> THEN <observable result> (EARS); Given / When / Then is also fine
    - Each item must map to at least one test in §10; items that truly can only be human-judged are listed separately with why they cannot be machine-checked
    - Example: WHEN an unauthenticated user requests a protected interface THEN return 401 and do not leak whether the resource exists

12. Updates required after document generation
    - Content to append to global-contract.md, bump contract version (+0.1), append a changelog row (version/date/change summary/triggering module)
    - progress.md: this module → 📝 Spec generated

---

【Constraints】
- Naming, types, response and error conventions follow the global contract; must not unilaterally change existing definitions
- No placeholders; irrelevant write “Not applicable to this module”
- Paths and error representation follow overall design and contract
- Markdown; code blocks mark the actual language

---

【Output requirements】
Save under reference/modules/, naming: F{two-digit-number}-{module-English-name}.md (number aligns with progress development order; English name uses hyphens).
Also update reference/global-contract.md and reference/progress.md, and summarize the changes.
```

---

## Progress record format reference

```markdown
# Development Progress Record

| Dev order | Module name | Status | Doc path | Covered PRD items | Completed at | Remarks |
|-----------|-------------|--------|----------|-------------------|--------------|---------|
| 1 | (module name) | ✅ Done | reference/modules/F01-example.md | F-1 | YYYY-MM-DD | 04 acceptance passed |
| 2 | (module name) | 🔍 Pending acceptance | reference/modules/F02-example.md | F-2 | - | 03 coding complete |
| 3 | (module name) | 📝 Spec generated | reference/modules/F03-example.md | F-3 | - | - |
| 4 | (module name) | ⬜ Not started | - | F-4 | - | - |
```

- ⬜ Not started → 📝 Spec generated → 🔍 Pending acceptance → ✅ Done
- ⏸️ Blocked: mark when rolling back for design defects or when acceptance rejects; Remarks column notes reason and rollback target
- Selecting the next module: predecessor dependencies must all be ✅ (📝 / 🔍 alone is not enough)

---

## Usage tips

**Confirm understanding first, then diff the contract, then write the doc.** Two gates catch most cross-document inconsistency.

**Strictly follow progress.md order**, one module at a time. When order and dependencies conflict, dependencies win and the order is written back.

**Contract updates must land**, or the next module will duplicate or conflict definitions. Each update bumps the version and writes a changelog—this is the anchor for later module diffs.

**Precision standard (operational judgment)**: Measure by “clarification-question budget before coding”—if the IDE Agent raises **≤ 3** clarifying questions about this module’s doc before starting, it is considered adequate; more than that means the doc fails and this module’s doc is rolled back for supplementation rather than letting the coding Agent hard-guess. When realtime, desktop, or background tasks are involved, channel names, events, and lifecycles must be pinned down—no hand-waves. When the question budget is exceeded, 02 should finish the doc before handing to 03, not rely on 03 asking while building.

**Test layering must state ownership clearly.** Each case labels whether it is unit/integration/E2E so the IDE Agent can choose the correct test approach and avoid truly connecting dependencies that should be mocked.

**Security self-check is not ceremonial.** §7 self-check items map directly to §10 security cases; if self-check says “involved” but tests have no corresponding entry, the doc contradicts itself.

**§11 must be decidable.** 04 only checks WHEN/THEN (or equivalent checkboxes); hollow wording gets rejected for doc supplementation—not “the coding side will figure it out.”

**For existing projects, focus on §2.** Reuse lists and conflict-avoidance plans for existing codebases must be clear, or the IDE Agent will reinvent wheels or step on existing logic.

---

*Module spec template · Greenfield 02; for brownfield see specs/SDD-GUIDE*
