# Changelog

## 0.2.0 — 2026-08-21

- Repo hygiene: removed duplicate `template/`, thin `stages/`, and `guides/`.
- Skill packaging: `skill.json`, UTF-8-safe `SKILL.md` description, install scripts.
- Contributing + EN/ZH corpus parity check (`scripts/check-parity.py`) and GitHub Action.
- Issue templates; README install one-liners, mermaid pipeline, attachment filename table.

## 0.1.3 — 2026-08-21

- README product intro first (problem, value, who it’s for / not for), then install and quick start.

## 0.1.2 — 2026-08-21

- Bilingual readability pass: split interleaved docs into language-specific files (`README`, stages, guides, toy PRD).
- English brownfield corpus uses `-design` / `-receipt` / `-acceptance` suffixes; Chinese corpus keeps `-方案` / `-回执` / `-验收记录`.
- English `ci-probes-reference.py` messages and probes aligned with EN naming.

## 0.1.1 — 2026-08-21

- Split human docs: `README.md` (English) + `README.zh-CN.md` (中文); stop interleaving languages in one file.
- `SKILL.md` English-primary with corpus routing by user language.

## 0.1.0 — 2026-08-21

- Initial public skeleton: Cursor skill `write-before-code`.
- Full bilingual corpus under `content/en/` and `content/zh/` (Diátaxis docs + agent stages 00–04 + brownfield SDD).
- Iron laws: write-before-code, HITL, one focus, agree one slice at a time, no self-pass, no fake green.
- Example: `examples/toy-prd.md`.
