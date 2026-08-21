# CI probe Spec (anti-drift · machine checks)

> **Role**: Turn the overview’s “machine check first, human judgment second” into **automatable checks**. This file is Spec, not a full language implementation; engineering repos should provide `tools/verify_docs_workflow.*` (or equivalent) and call it from CI.  
> **Authority**: Check failure = merge block (or mark red with maintainer waiver and a trail).

---

## 1. Probe list

| ID | Name | Input | Failure condition | Severity |
|----|------|------|----------|--------|
| P1 | Contract version monotonic | `reference/global-contract.md` changelog table | Version not incremented per rules (compatible append +0.1 / breaking +1.0); or header “contract version” disagrees with latest log row; or log missing date/summary/change nature; or breaking change (+1.0) in the same PR without HITL decision-point mark | Block |
| P2 | progress status legal | `reference/progress.md` | Illegal transition traces: same diff marks a module ✅ via a path other than 04/maintainer; or status not in {⬜,📝,🔍,✅,⏸️}; or ✅ row has no completion time | Block |
| P3 | 03 must not self-mark ✅ | This PR’s diff + progress | Diff shows a progress row `→ ✅`, and same PR has **no** 04 acceptance conclusion file / no maintainer sign-off comment | Block |
| P4 | Brownfield receipt has completion section (if receipt exists) | `specs/tasks/*-receipt.md` and `specs/archive/**/*-receipt.md` | File exists but has no “Completion” section (or equivalent heading) | Block |
| P5 | Acceptance record has machine-check evidence (if record exists) | `specs/tasks/*-acceptance.md` and `specs/archive/**/*-acceptance.md` | Conclusion is pass, but no recognizable test/CI/command-output summary (e.g. passed/failed, exit code) | Block |
| P6 | Greenfield 04 conclusion is traceable | When a module is marked ✅ | `progress` notes or side file does not point to an acceptance conclusion (allow maintainer sign-off sentence: `maintainer accept YYYY-MM-DD`) | Warn → prefer block |
| P7 | Dead links | `docs/**/*.md` relative links | Link targets a missing path | Block |
| P8 | Task-pack contract section (if contract touched) | Task pack `.md` + contract diff | PR changes `global-contract.md`, but matching task pack has no “contract change” section or does not list the paragraphs | Block |
| P9 | Archive bucket must have INDEX | `specs/archive/*/` subdirs | Archive sub-bucket exists (with files) but lacks `INDEX.md` | Block |

> **File not yet present**: P1 / P2 **skip, not failure** when `global-contract.md` / `progress.md` have not been created by 01 yet (empty-template self-check should pass). P3 likewise skips when there is no progress.  
> Small projects may demote P6 to warning; keep P1–P3, P7–P9 blocking when applicable. P4/P5 fire only when matching files exist (under single-line flow, receipt/acceptance record are optional). After archive, receipts must still be scannable, so P4/P5 look at both `tasks/` and `archive/`.

---

## 2. Implementation conventions (for engineering repos)

1. **Prefer stdlib only** (e.g. Python); no mandatory third-party deps.  
2. **Workspace baseline**: support both “docs root = repo/`docs`” and “workspace is docs”; use env `DOCS_ROOT` or auto-detect.  
3. **Exit codes**: any blocking failure → exit 1; warnings only → exit 0 and print WARN.  
4. **Output**: human-readable summary + optional JSON (`probe_id`, `ok`, `detail`).  
5. **CI**: must run on `pull_request` / `push`; local pre-commit optional.  
6. **Reference implementation**: sibling [`ci-probes-reference.py`](./ci-probes-reference.py) covers P1/P2/P3/P4/P5/P7/P9; engineering repos may extend P6/P8 on top.  

Example invocation (engineering repo chooses script name):

```bash
python tools/verify_docs_workflow.py --docs-root docs
# or when workspace is docs:
python specs/ci-probes-reference.py --docs-root .
```

---

## 3. Division of labor with human acceptance

| Machine checks (these probes) | Human / 04 / HITL |
|----------------|----------------|
| Version numbers, state machine, file completeness, whether evidence fields exist | Whether business rules truly hold, design intent, PRD traceability |
| Whether there is a **trace** of tests having run | Whether assertions are non-shell, whether the right behavior was checked |

Probe pass ≠ business acceptance pass.

---

## 4. Waivers

Maintainer may write `docs-probe-skip: P3 reason…` in the PR description (must list ID + reason). CI then demotes that ID to warning; abuse is a process incident.

Hotfix task packs (title prefixed `HOTFIX-`) automatically demote P5 to warning; other probes unchanged.
