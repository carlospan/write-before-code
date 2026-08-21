# 贡献指南

感谢改进 **write-before-code**。

**[English](CONTRIBUTING.md)** · **[中文](CONTRIBUTING.zh-CN.md)**

## 基本规则

1. **改流程必须双语同步。** 同一 PR 内同时改 `content/en/` 与 `content/zh/` 对应文件。
2. `SKILL.md` 控制在约 500 行以内；长提示词与指南放进 `content/`。
3. 不要再引入第三份文档树（禁止恢复 `template/` 双份正文）。
4. 棕地可选附件后缀：英文 `-design` / `-receipt` / `-acceptance`；中文 `-方案` / `-回执` / `-验收记录`。同一语料树内不要混用。
5. 发版时同步更新 `SKILL.md` 的 `metadata.version`、`skill.json` 与 [CHANGELOG.md](CHANGELOG.md)。

## 本地检查

```bash
python scripts/check-parity.py
```

## 本地安装自测

```bash
./scripts/install.sh --agent all
# 或单个：--agent cursor|codex|trae|claude
```

```powershell
.\scripts\install.ps1 -Agent all
```

各 Agent 安装路径见 [docs/adapters.zh-CN.md](docs/adapters.zh-CN.md)。不要按 IDE 分叉提示词树。
## Pull Request

- 尽量小 PR：措辞润色与流程规则变更分开。
- 说明是否用 `examples/toy-prd.zh-CN.md` 跑过玩具绿场。
- 不要提交密钥或个人项目 PRD 正文。

## 许可证

贡献即表示同意以 MIT 许可（见 [LICENSE](LICENSE)）。
