# Project PRD

> **Status**: ⬜ Skeleton ready; **body TBD**. Unfilled sections are **invalid** for 01 (do not treat empty headings as requirements).  
> **Role**: **Sole requirements source** for the current project; input to greenfield 01.  
> **How to use**: Fill each section; for sections irrelevant to this project, keep the heading and write “Not in scope for this project” plus one sentence why.  
> **IDs**: Use stable feature IDs `F-1`, `F-2`, … (01’s “covers PRD items” will cite these).  
> **Tech**: If decided, write it; if not, write “Recommend in 01, confirm with maintainer”—do not leave empty “TBD” fluff.  
> **Brownfield**: Small patches go through `specs/`; write back here only when product scope changes.

---

## 1. Positioning and goals

### 1.1 One-line positioning

(What this product is, who it is for, and what problem it solves.)

### 1.2 Core value

- …

### 1.3 Success criteria (testable)

- [ ] … (prefer observables; avoid “great UX” / “easy to use”)

### 1.4 Explicitly out of scope

- …
- …

---

## 2. Users and scenarios

### 2.1 Target users

| Role | Description | Primary goals |
|------|-------------|----------------|
| (e.g. end user) | | |
| (e.g. admin) | | |

> Single-user / no accounts: state clearly “This project does not involve multi-user,” and say who owns config/data.

### 2.2 Key usage scenarios

1. **Scenario A**: …  
2. **Scenario B**: …  

### 2.3 Roles and permissions (if any)

| Role | Can do | Cannot do |
|------|--------|-----------|
| | | |

> If none, write “Not in scope for this project.”

---

## 3. Functional requirements (by deliverable module)

> One ID per feature. Write **observable behavior**, not implementation details (class names and table schemas belong in 01/02).  
> Suggested grain: 01 can map each item straight into a module in the build order; one `F-x` should not span many unrelated capabilities.

### F-1 (module / capability name)

- **What it does**: …  
- **Who uses it**: …  
- **Main flow**: …  
- **Boundaries / errors**: …  
- **Acceptance intent** (can be rough; detailed WHEN/THEN locked in 02):  
  - WHEN … THEN …  

### F-2 (module / capability name)

- **What it does**: …  
- **Who uses it**: …  
- **Main flow**: …  
- **Boundaries / errors**: …  
- **Acceptance intent**:  
  - WHEN … THEN …  

### F-3 …

(Add/remove as needed; keep IDs stable—do not renumber casually mid-flight.)

### Feature dependencies and suggested build order (optional)

| Order | Feature ID | Depends on | Notes |
|-------|------------|------------|-------|
| 1 | F-1 | — | |
| 2 | F-2 | F-1 | |

> Final build order is owned by 01’s `progress.md`; this table only expresses product-side dependencies.

---

## 4. Data and entities (summary)

> List only **core entities and relationships**, not full fields (full schema in 02).

| Entity | Purpose | Primary owning feature |
|--------|---------|------------------------|
| | | F-x |

Entity relationships (one sentence or ASCII):

```text
(e.g. User 1—N Order)
```

---

## 5. Interface and interaction constraints (if any)

> If global conventions already exist, lock them in; otherwise write “01 drafts a proposal; after confirmation it enters the contract.”

- **Client form**: Web / desktop / CLI / other: …  
- **Communication**: HTTP / RPC / IPC / other: …  
- **Unified response / error shape**: … or “Drafted in 01”  
- **Auth**: none / yes (mechanism and boundaries): …  
- **Realtime / push** (if any): …  
- **External services** (if any): purpose, whether must be swappable, secrets not in repo: …  

---

## 6. Technical constraints (if decided)

| Item | Requirement | Notes |
|------|-------------|-------|
| Language / runtime | Decided … / recommend in 01 | |
| Framework | | |
| Data storage | | |
| Deployment shape | Single machine / server / embedded in desktop … | |
| Compatibility (browser/OS, etc.) | | |
| Forbidden tech / dependencies | | |

---

## 7. Non-functional requirements

> Quantify where possible; after they are in the PRD, 01 will distill them into the `global-contract` non-functional baseline.

| Category | Requirement | Quantified (if any) |
|----------|-------------|---------------------|
| Performance | | e.g. P95 latency … |
| Availability / stability | | |
| Security | | |
| Privacy / compliance | | If none: “Not in scope” |
| Logging / observability | | |
| Internationalization | | If none: “Not in scope” |
| Other | | |

---

## 8. Environment, config, and delivery (if any)

- **Runtime environment**: …  
- **Config / secrets**: how provided; which must never enter the repo: …  
- **Build / distribution / updates**: … or “Not in scope”  
- **Backup / migration**: … or “Not in scope”  

---

## 9. Open questions and risks

> Ambiguities must live here; do not let the Agent silently assume. You may also use: `[Open: …]`.

| ID | Question | Impact | Lean (optional) | Status |
|----|----------|--------|-----------------|--------|
| Q-1 | | | | Open / Decided: … |

**Known risks**:

- …

---

## 10. Revision history

| Date | Summary | Author |
|------|---------|--------|
| YYYY-MM-DD | Created skeleton | |

---

## Self-check before handing to 01

- [ ] §1 positioning and out-of-scope are clear  
- [ ] §3 has at least one deliverable `F-x` with a stable ID  
- [ ] Key behavior can be sketched with WHEN/THEN (or marked open)  
- [ ] Undecided tech is marked “recommend in 01”; no hollow “TBD”  
- [ ] §9 lists open questions; or writes “None”  
- [ ] All remaining “example / placeholder” sentences are removed or rewritten  

When ready: hand this document to greenfield **01** (see `how-to/agent-prompts/01-overall-design.md`).
