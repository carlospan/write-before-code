# Task-pack template

> Copy this file and rename to `YYYY-MM-DD-task-name.md`.  
> **Flow** (see [`../SDD-GUIDE.md`](../SDD-GUIDE.md) §2): **IDE single-line** — same session drafts the task pack, lands code, engineering self-verify, writes docs back. Maintainer does HITL only. Process attachments grow/shrink as needed; do not pad a full set.  
> **HITL iron rule**: when product boundaries are unclear, fill HITL with **§2.5 incremental consensus (agree one slice at a time)** — write into this pack as soon as agreed, then authorize coding. See [hitl-alignment.md](../../how-to/hitl-alignment.md) · root README opening ★.  
> **Coverage** (traceability; one required line): which PRD / module / contract clause does this pack map to? e.g. `F03-orders` payment callback; or `global-contract` error-code section.

---

## Spec (external behavior)

Observable outcomes only — no implementation detail. **Use increments**; do not rewrite the whole module Spec.

### Current behavior

What code + tests do today. For new capability, write “none.”

### Target behavior (increments)

- **ADDED**: …  
- **MODIFIED**: from “…” to “…”  
- **REMOVED**: … (must state reason; breaking changes must enter HITL)  

Delete unused rows; do not leave empty boilerplate.

## Implementation (steps)

1. …  
2. …  
> Checkable; for large change surface, attach `-design.md`. Coding happens in the same session as this doc.

## Acceptance (criteria)

Each item must be externally decidable. Default form: **WHEN** &lt;condition&gt; **THEN** &lt;observable result&gt;. Ban “works fine” / “good UX.”

- [ ] WHEN … THEN …  
- [ ] WHEN … THEN …  

> IDE engineering self-verify (must include machine checks); product / feel items belong to the maintainer (may add “human-only: …” and why it cannot be machine-checked). Write `-acceptance.md` when needed.

## Contract change (if any)

- [ ] None  
- If any: which section of `global-contract.md` changed; version must +0.1; changelog written  

## HITL decision points

- Which nodes need maintainer approval (**write here after agreeing one slice at a time**; do not leave only in chat)  
- Coding authorization as its own line; no large code changes before authorization  
- If none, write “none”  
> You may note a preferred leaning for reference; it does **not** replace maintainer approval.
