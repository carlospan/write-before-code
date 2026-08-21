# specs/archive · closed task archive

> **Role**: **Long-lived process assets** after brownfield tasks close. **Move** here from [`../tasks/`](../tasks/); **do not delete** history.  
> Working drafts keep “Spec / decisions / acceptance criteria as of then,” for replay and audit.

---

## When to move in

The task pack in `tasks/` **simultaneously** satisfies:

1. Spec landed (current behavior + increments)  
2. Coding and engineering self-verify done  
3. Maintainer HITL (or written acceptance) passed  
4. This bucket already copied [`_index-template.md`](./_index-template.md) and renamed to `INDEX.md` (conclusion + whether contract was written back + file list for this bucket)

Then move **all related files** for that task together with `INDEX.md` into the matching sub-bucket.  
**No INDEX → must not leave `tasks/`** — missing conclusion page means not closed.

---

## Bucket naming

```text
YYYY-MM-DD-topic/
├── INDEX.md                 ← required: conclusion + write-back checks + file list
├── YYYY-MM-DD-short-name.md ← original task pack
└── (optional) -design / -receipt / -acceptance
```

- Date = task **close day** (or the main pack’s open day — pick one convention per team).  
- `topic` = short hyphenated English or pinyin phrase for search.  
- `INDEX.md` must state: one-sentence conclusion, ADDED / MODIFIED / REMOVED summary, whether contract was written back, HITL date. Template: [`_index-template.md`](./_index-template.md).

---

## Archived

| Bucket | Conclusion |
|----|------|
| (none yet) | — |

---

## Do not put here

- Open tasks (including missing INDEX) → stay in [`../tasks/`](../tasks/)  
- Greenfield module specs → [`../../reference/modules/`](../../reference/modules/)  
- Repeatable how-to manuals → [`../../how-to/`](../../how-to/)
