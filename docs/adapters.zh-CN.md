# 多 Agent 适配说明

**write-before-code** 遵循开放的 [Agent Skills](https://agentskills.io) 布局：一个含 `SKILL.md`（及附属文件）的目录。凡能发现这类 Skill 的工具，都可以用同一份包。

流程正文在 `content/`；各 **兼容 Agent** 的差别主要是 **安装路径** 与 **调用方式**。

## 支持的 Agent

| Agent | 用户级安装 | 项目级安装 | 调用 |
|-------|------------|------------|------|
| **Cursor** | `~/.cursor/skills/write-before-code/` | `.cursor/skills/write-before-code/` | `/write-before-code` 或说「用 write-before-code」 |
| **Codex**（OpenAI） | `~/.agents/skills/write-before-code/` | `.agents/skills/write-before-code/` | `$write-before-code` 或说「用 write-before-code」 |
| **Trae** | `~/.trae/skills/write-before-code/` | `.trae/skills/write-before-code/` | `/write-before-code` 或 Skills 界面导入 |
| **Claude Code** | `~/.claude/skills/write-before-code/` | `.claude/skills/write-before-code/` | `/write-before-code` |

## 安装

```bash
./scripts/install.sh                          # 默认装到全部已支持 Agent
./scripts/install.sh --agent cursor
./scripts/install.sh --agent codex
./scripts/install.sh --agent trae
./scripts/install.sh --agent claude
./scripts/install.sh --agent all --scope project
```

Windows PowerShell：

```powershell
.\scripts\install.ps1
.\scripts\install.ps1 -Agent codex
.\scripts\install.ps1 -Agent all -Scope project
```

## 各 Agent 注意点

- **Codex**：官方发现路径是 `.agents/skills`；`SKILL.md` 必须在技能目录根下。装完若看不到，重启 Codex。
- **Trae**：可用 Skills UI 导入含 `SKILL.md` 的目录/zip；Rules（常驻）≠ Skills（按需）——本流程请用 Skill，不要整份塞进常驻 Rules。
- **Claude Code**：个人 `~/.claude/skills/`，项目 `.claude/skills/`。
- **所有已支持 Agent**：04 验收尽量新开对话；项目 `docs/` 仍从 `content/zh/` 或 `content/en/` 复制。

更完整的英文说明见 [adapters.md](adapters.md)。
