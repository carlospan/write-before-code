# Contributing

Thanks for helping improve **write-before-code**.

**[English](CONTRIBUTING.md)** · **[中文](CONTRIBUTING.zh-CN.md)**

## Rules of the road

1. **Process changes must stay bilingual.** Edit matching files under `content/en/` and `content/zh/` in the same PR.
2. Keep `SKILL.md` under ~500 lines. Put long prompts and guides in `content/`.
3. Do not reintroduce a third copy of the docs tree (no `template/` duplicate).
4. Brownfield optional suffixes: English `-design` / `-receipt` / `-acceptance`; Chinese `-方案` / `-回执` / `-验收记录`. Do not mix inside one language tree.
5. Bump `metadata.version` in `SKILL.md`, `skill.json`, and [CHANGELOG.md](CHANGELOG.md) together.

## Local checks

```bash
# File-list parity between EN and ZH corpora
python scripts/check-parity.py
```

## Install for local Cursor testing

```bash
# macOS / Linux
./scripts/install.sh

# Windows PowerShell
./scripts/install.ps1
```

## Pull requests

- Prefer small PRs: docs wording vs process rule changes.
- Say whether you tested a toy greenfield pass (`examples/toy-prd.md`).
- Do not commit secrets or personal project PRDs.

## License

By contributing, you agree your changes are licensed under MIT (see [LICENSE](LICENSE)).
