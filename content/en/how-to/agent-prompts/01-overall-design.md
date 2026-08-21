# Generate Overall Development Doc · Generic Prompt Template

---

## How to use

This is the **first** of the four-document system. Generation order:

```
Overall development doc (this template) → Module-level development docs → Code implementation → Independent acceptance
```

**When to use**: A complete PRD already exists, and you need to generate the overall development doc from it (architecture, module split, global conventions).

**When you need not run this template (greenfield lite track)**: `overall-design.md` / `global-contract.md` / `progress.md` **already exist**, this module does not change architecture, and the maintainer explicitly says “use lite track” → skip 01 and go straight to [02-module-spec.md](./02-module-spec.md). First time on a new project, or when module split / tech stack changes, still run this template (incremental revision is fine; do not pretend the existing baseline does not exist and start a parallel stove).

**Principle**: The PRD is the sole source of requirements and constraints; tech choices, interface conventions, and directory structure all subordinate to the PRD. Where the PRD is silent, propose in the understanding summary and write into formal docs only after confirmation. This template presupposes no language, framework, or product shape.

**After generation, outputs**:
1. `explanation/overall-design.md`
2. `reference/global-contract.md` (initialize)
3. `reference/progress.md` (initialize)

Copy the prompt below to the **Architect-stage** Agent. Paths are relative to the **`docs/` docs root**; if the workspace is the repo root, prefix with `docs/` (see [00-overview.md](./00-overview.md) §2).

---

## Prompt body

```
You are a senior full-stack architect. Strictly follow this project's PRD and produce a high-quality overall development document.
That document will later be split into module-level development docs, and ultimately used by an IDE Agent to implement code.
Give a clear architecture direction and module boundaries; leave field and interface details to the module-level docs.
(Paths under explanation/ and reference/ are relative to the docs/ docs root.)

---

【PRD requirements document】
- This project's PRD path: explanation/PRD.md (if missing, confirm the actual path with the maintainer)
- If that file is still a landing note, or the body clearly belongs to a previous project, stop and confirm with the maintainer; **do not** invent requirements on your own
First read **this project's PRD**, and output a requirements summary: project positioning, core features, tech stack and constraints, target users, non-functional requirements.
Continue only after confirmation.
If the PRD does not specify a tech stack or key conventions, you must give recommendations and rationale in the understanding summary, and write them into formal docs only after I confirm.

---

【Step 1: Output an understanding summary; wait for my confirmation before continuing】
1. Project core positioning (one sentence)
2. Preliminary feature-module split (suggest development-order numbers by dependency)
3. Users and permissions: if multi-user, state roles and permission boundaries; if single-user, note that and how configuration is managed
4. Tech stack: if the PRD already specifies it, restate and sanity-check; if not, recommend with rationale (language/framework/data store/build and package management and major versions)
5. Key architecture decision recommendations (deployment shape, service split, whether async/queues are needed—only for this project's actual needs)
6. Paradigm recognition: list only when the PRD involves the following—desktop/embedded runtime, realtime communication, long-running background tasks, swappable external services, etc.; if none, write “No special paradigms”
7. Places in the PRD that are unclear or need supplementation
8. PRD self risk assessment (challenge the PRD, do not only restate):
   - Feasibility: whether core technical needs have known infeasible / extremely high-risk points (performance, compliance, third-party dependency availability)
   - Consistency: whether the PRD contradicts itself (conflicts between features, scope vs resources mismatch)
   - Scope-creep risk: whether there are implicit “scope expansion” triggers (e.g. “and we might also need…”)
   - If assessment finds major risks, they must be explicitly flagged in the confirmation summary with mitigation or pending-confirmation suggestions; do not silently carry them past
9. Existing-code detection: read the project directory and judge whether a codebase already exists. If yes, briefly describe existing directory structure, tech stack, shared components, and test status; assess gaps vs PRD requirements and an integration strategy; if none, note “Greenfield project”

Generate the full document only after I confirm.

---

【Step 2: Generate the overall development document】
Generate in the structure below. Sections unrelated to this project write “Not applicable to this project” with a brief reason; do not skip headings.
For normative content: if the PRD already defines it, adopt and cite directly; if the PRD does not define it, give a landable draft convention, consistent with the confirmed tech stack.

1. Project overview
   - Positioning and core value
   - Target users and usage scenarios
   - Feature module list (by development order):

   | Dev order | Feature module | Module responsibility (brief) | Covered PRD items |
   |-----------|----------------|-------------------------------|-------------------|
   | 1 | (fill from PRD) | (one sentence) | (PRD feature IDs/sections, e.g. F-1, F-3) |

2. Technical architecture
   - Overall architecture diagram (ASCII: client/server/storage/external deps and how they communicate)
   - Runtime and deployment: how processes or services are split, started, and communicate; non-standard deployments (e.g. desktop-embedded backend) must state process model and port binding clearly
   - Tech selection table (layer / choice / version / rationale; consistent with confirmed tech stack)
   - External dependency list (purpose; note cost or alternatives if any)

3. Module split plan
   - Module table: development order / module name / responsibility / predecessor dependencies
   - Dependency graph (ASCII)
   - Core data-flow diagram (ASCII: data carriers and trigger timing)
   - Split rationale

4. Roles and permissions overview
   - Per PRD: if present, list and explain; if none, note “Not applicable to this project”

5. Data storage design overview
   - Core entity list (name + purpose + owning module); for non-relational stores use that store’s corresponding concepts
   - Core associations among entities
   - Do not write full fields (leave to module specs); if the PRD already has structure, cite and sanity-review

6. Global technical norms (subsequent modules must obey; content follows the PRD; undefined parts finalized after confirmation)
   Expand only items this project needs; unneeded ones write “Not applicable to this project”:
   - Interface conventions: unified success/failure response shape, error codes or error representation, path and versioning strategy (always adopt PRD definitions when present; draft only when PRD is silent)
   - Security and auth boundaries (per PRD: multi-user auth, or single-machine/local communication boundaries, etc.); must cover the following dimensions (trim to project reality):
     · Auth model: authentication method, session/token mechanism, permission granularity (RBAC/ABAC/simple roles)
     · Input validation: global validation strategy (allowlists/type constraints/length limits), injection and XSS baseline
     · Data isolation: multi-tenant or inter-user data isolation boundaries
     · Sensitive data: encryption at rest, encryption in transit, log redaction, key rotation strategy
     · Communication security: TLS requirements, local communication boundaries (e.g. access control for desktop IPC)
   - Naming conventions (storage / backend / frontend; explain conversions when they differ)
   - Pagination and list conventions (if the project has list APIs)
   - Logging and observability conventions
   - Directory and module organization conventions (fit confirmed tech-stack conventions)
   - Realtime communication conventions (only when paradigm recognition involves it)
   - External service integration conventions (only when swappable or isolated third-party deps are needed: abstraction boundary, timeout/retry/degrade, secrets not in repo)
   - Background task conventions (only when long-running/scheduled tasks exist)
   - Sensitive config and secrets management (only when PRD or compliance requires it)

7. Environment and configuration management
   - Development environment requirements
   - Environment variables and config partitions
   - Build, distribute, update (only when the PRD involves them)

8. Non-functional requirements
   - From the PRD: performance, security, stability, i18n, etc.; if the PRD is silent, note “Not required by PRD” or give a minimum suggestion for confirmation
   - **Quantified baselines must enter the contract**: distill performance (latency/throughput), stability (availability/error rate), security baselines (encryption/audit), and other quantifiable items into concrete numbers, and write them into the “Non-functional baselines” section of global-contract.md (see Step 3), so modules do not freestyle and become unalignable across modules

9. Development order
   - The single recommended order; advance only one module at a time: docs done → coding done → next
   - Table: order / module name / predecessor deps / rationale
   - Foundation and depended-on modules first; deferrable features later
   - progress.md must match this order

10. Risks and pending confirmations
    - PRD ambiguities, selection trade-offs, technical hard points and coping ideas

11. Stage rollback and escalation mechanism
    - When the module-spec stage finds overall-design defects (e.g. unreasonable module split, tech selection needs adjustment):
      · Pause current module-spec generation; mark as “⏸️ Blocked”
      · Output problem description and impact scope; I decide whether to roll back and revise overall-design.md
      · After revision, bump contract version and note “Architecture revision” in the changelog
    - When the coding stage finds errors in the module spec or overall design:
      · Small scope (interface signatures, field tweaks): IDE Agent handles via the doc write-back mechanism
      · Large scope (module responsibility change, split adjustment): pause coding; roll back to the module-spec stage and regenerate
    - progress.md state rollback rules: ✅ → 📝 (needs re-coding) or 📝 → ⬜ (needs doc regeneration); on rollback note reason and date in the Remarks column

---

【Step 3: Generate companion files】

1. reference/global-contract.md (initialize)
   - Distill cross-module must-unify conventions from §§5 and 6
   - Include: entity list (no fields yet), interface and error conventions, naming, pagination (if any), and realtime/external-service/task/secret conventions actually enabled for this project
   - **Non-functional baselines section** (quantified values distilled from §8): latency/throughput/availability/error rate/security baselines and other quantifiable items, as the cross-module alignment anchor
   - Note “Per-module contracts will be supplemented gradually after module specs are generated”
   - Establish version and changelog at the file header:

     # Global Contract

     > Contract version: v1.0 | Baseline date: {generation date}

     ## Changelog

     | Version | Date | Change summary | Triggering module |
     |---------|------|----------------|-------------------|
     | v1.0 | {date} | Initialize: distill global conventions from overall design | — |

   - Later, each time module-spec generation or code write-back changes the contract, append a changelog row and bump the version (minor +0.1)

2. reference/progress.md (initialize)
   - List all modules in development order; status all “⬜ Not started”

     # Development Progress Record

     | Dev order | Module name | Status | Doc path | Covered PRD items | Completed at | Remarks |
     |-----------|-------------|--------|----------|-------------------|--------------|---------|
     | 1 | (fill) | ⬜ Not started | - | (PRD items) | - | - |

   - Five statuses: ⬜ Not started / 📝 Spec generated / 🔍 Pending acceptance / ✅ Done / ⏸️ Blocked (needs rollback or a decision)
   - ✅ is written only after 04 acceptance passes; on 01 initialize everything is ⬜

---

【Constraints】
- Everything follows the PRD; must not introduce tech stacks, middleware, or norms the PRD does not require and that were not confirmed
- Tech selection, directory structure, and example syntax must match the confirmed tech stack
- This document does not expand module-level field and interface details
- No placeholders (“omitted here,” “TBD,” etc.); if not applicable write “Not applicable to this project”
- Use Markdown; code blocks mark the actual language

---

【Output requirements】
Write directly into the corresponding directories and report which files were generated:
1. explanation/overall-design.md
2. reference/global-contract.md
3. reference/progress.md
```

---

## Usage tips

**Source quality determines downstream cost.** After generation, prioritize checking: whether the tech stack matches the PRD/confirmation; whether module boundaries and dependencies are sound; whether §6 contains only conventions this project truly needs; whether the development order is executable.

**Settle §10 risk items early**, to avoid mid-development architecture changes.

**Advance in order; contract only appends.** One module at a time; after a module is ✅ via 04, contract and code are aligned; later modules only append—do not break definitions already-completed modules depend on.

**Special shapes get a separate review.** If the PRD includes desktop runtime, realtime communication, or long-running tasks, confirm the corresponding sections have substantive conventions, not a hand-wave.

**High-sensitivity projects do threat modeling.** If payment, healthcare, personal privacy, or other high-sensitivity domains are involved, the five security dimensions checklist in §6 is not enough; add STRIDE-level threat modeling (data-flow diagram + mitigation per threat), not merely filling checklist items.

**Contract version must increment.** Every contract change (whether from module specs or code write-back) must append a changelog entry. The version number is the cross-document alignment anchor; skipping it makes later module diffs fail.

**Brownfield / existing projects: survey before acting.** If understanding-summary item 9 detects an existing codebase, first confirm whether existing directory structure and tech stack are reusable; if not, state the migration strategy clearly in §2 so conflicts are not discovered only at the module-spec stage.

**Rollback is not scary; quiet drift is.** When design defects are found, follow the §11 rollback mechanism, update progress status and contract version; forbid changing code to “make do” without changing docs.

---

*Overall design template · Greenfield 01; for brownfield see specs/SDD-GUIDE*
