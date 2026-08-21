# write-before-code

**[English](README.md)** · **[中文](README.zh-CN.md)**

**先落盘规格，再写代码。**

面向 [Cursor](https://cursor.com) 的 Agent Skill：不让 AI「能跑就算交付」。  
先把行为写进文件、和人一块一拍对齐，再编码——**写代码的那一方不能自己标完成。**

| | |
|--|--|
| 形态 | 有主见的 Cursor Agent Skill（MIT） |
| 文档 | [English](content/en/) · [中文](content/zh/) |

---

## 它解决什么问题

Agent 写代码很快，但对齐意图很容易偷懒。常见翻车：

- 规格只活在聊天里，一关对话就丢  
- 为了修红，悄悄偏离设计  
- 测试假绿（空断言、没真跑）  
- **写代码的同一个 Agent 给自己点 ✅**

**write-before-code** 把这当成流程事故，而不是「模型不够聪明」。它提供分阶段流水线、落盘契约，以及**独立验收**。

---

## 你能得到什么

- **绿场：** `01` 整体设计 → `02` 模块文档 → `03` 编码 → `04` 验收  
- **棕地：** `specs/tasks/` 里的短增量任务包  
- **HITL：** 关键产品决策须维护者点头  
- **一块一拍：** 谈定一小块就立刻落盘，再往下走  
- **禁自标通过：** `03` 只能标 🔍；✅ 仅 `04` 或你本人  

不是 Spec Kit / BMAD / OpenSpec 的即插即用替代品——更偏文档与门控，验收更硬。

---

## 适合谁

- 用 Cursor 的独立开发者或小团队，想要**可重复**的 Agent 流程  
- 架构与模块边界还在变的绿场产品  
- 需要对外行为可审计的棕地改动  

## 不适合谁

- 改错字、改注释这类琐事（不必走满仪式）  
- 想要**最薄**一层 SDD → 更看 OpenSpec  
- 想要**多 Agent、可移植 CLI** 优先 → 更看 Spec Kit  
- 想要**一整支虚拟产品团队人设** → 更看 BMAD  

---

## 流水线一览

```text
绿场满配：  PRD → 01 整体设计 → 02 模块文档 → 03 编码 → 04 验收
绿场轻量：  （维护者明示；01 已在；不改架构）→ 02 → 03 → 04
棕地：      任务包 → 编码自验 → 维护者 HITL → 归档（须 INDEX.md）
```

| 阶段 | 职责 |
|------|------|
| 00 | 总纲 / 铁律 |
| 01 | overall-design + global-contract + progress |
| 02 | `modules/Fxx-*.md` |
| 03 | 编码；progress 只标 🔍 |
| 04 | 独立验收 → ✅ |

**铁律：** 先写后码 · 人在回路 · 一次一个焦点 · 一块一拍 · 禁自标 ✅ · 假绿无效。

详情：[SKILL.md](SKILL.md) · [content/zh/how-to/agent-prompts/00-overview.md](content/zh/how-to/agent-prompts/00-overview.md)

---

## 安装

### 个人 Skill（所有项目可用）

将本仓库复制或克隆到：

```text
~/.cursor/skills/write-before-code/
```

Windows 常见路径：

```text
C:\Users\<你>\.cursor\skills\write-before-code\
```

该目录根下必须有 `SKILL.md`。

### 项目级 Skill（单个仓库）

```text
<仓库>/.cursor/skills/write-before-code/
```

### 项目文档模板

把**一种**语言的文档树复制到产品仓库的 `docs/`（或以该树作为文档根）：

| 语言 | 复制来源 |
|------|----------|
| 中文 | `content/zh/` → `docs/` |
| English | `content/en/` → `docs/` |

`template/` 是 `content/zh/` 的便利镜像。

---

## 快速开始

1. 按上文安装 Skill。  
2. 将 `content/zh/`（或 `content/en/`）复制为产品仓库的 `docs/`。  
3. 在 `docs/explanation/PRD.md` 写入**真实**需求（空骨架不算）。  
4. 在 Cursor 中说：

```text
用 write-before-code，从 01 开始。
```

5. 每个模块：`02` → `03` → **新开对话**做 `04` 验收。  
6. 模块均为 ✅ 之后，行为变更走棕地 `specs/tasks/`（见 SDD-GUIDE）。

玩具 PRD：[examples/toy-prd.zh-CN.md](examples/toy-prd.zh-CN.md) · [English](examples/toy-prd.md)

---

## 和同行对比

| | write-before-code | Spec Kit | BMAD | OpenSpec |
|--|-------------------|----------|------|----------|
| 重心 | 落盘分阶段 + 硬验收 | 便携 specify→implement | 多角色规划 | 棕地增量 |
| 自标 ✅ | 实现方禁止 | 通常较弱 | 有 review | 靠维护者纪律 |
| 文档 | Diátaxis + 契约/进度 | Spec/plan/tasks | 大量 Agent 产物 | 变更提案 |

---

## 目录结构

```text
write-before-code/
├── SKILL.md          # Agent 入口
├── README.md         # 英文
├── README.zh-CN.md   # 中文（本文件）
├── LICENSE
├── CHANGELOG.md
├── examples/
├── stages/
├── guides/
├── content/
│   ├── en/
│   └── zh/
└── template/         # content/zh 镜像
```

---

## 贡献

- 改流程规则时，**同时**改 `content/zh/` 与 `content/en/`。  
- `SKILL.md` 控制在约 500 行以内；细则放进 `content/`。  
- 提 PR 前用玩具绿场跑通一遍。

---

## 许可证

MIT — 见 [LICENSE](LICENSE)。
