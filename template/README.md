# 文档驱动开发 · 通用工作流模板（Diátaxis + SDD）

> **write-before-code** 项目模板（中文）。复制本目录到产品仓库的 `docs/` 即可。
> 英语请改用仓库内 `content/en/`。说明见仓库根 `README.zh-CN.md`。

本目录是一套**可复用的文档 + Agent 流水线模板**，用于：

1. **绿场**：从 PRD 经 01→02→03→04 产出设计、契约、模块规格与可验收实现（**同一 IDE Agent 可按序执行**）。01 产物已在且本模块不改架构时，维护者可明示走**轻量档**（跳过 01，仍须 02→04）  
2. **棕地 / 迭代**：有代码之后走 `specs/`（**增量 Spec**、IDE 单线；闭环须写 `INDEX.md` 后再归档，过程稿不删）

文档按 [Diátaxis](https://diataxis.fr/) 四象限组织；`specs/` 为 SDD 扩展。

**用法**：复制本目录（或以其为 `docs/`）到新仓库 → 写入该项目的 `explanation/PRD.md` → 按 [00 总纲](./how-to/agent-prompts/00-overview.md) 执行。不绑定特定产品或技术栈。

当前工作区以本目录为文档根。若嵌在更大仓库中，工程启动说明见仓库根 README（无则不必挂链）。

---

## ★ 人机协作铁律（必读）

> **怎么和 AI 一起定需求、再写代码——这不是闲聊习惯，是正式工作流。**（与具体产品无关。）

| 名字 | 意思 |
|------|------|
| **HITL（人在回路）** | 关键产品决策由**维护者点头**；Agent 不擅自定死 |
| **Spec-driven（规范驱动）** | 先把可观测行为写进规格（绿场模块文档 / 棕地任务包），再编码 |
| **渐进对齐（一块一拍）** | **一次只确认一小块**；谈定立刻落盘（绿场：理解摘要 / 模块文档；棕地：任务包），不攒到最后、不靠聊天记录当真源 |

一句话：**HITL + 规范驱动下的渐进对齐。**  
专页：[how-to/hitl-alignment.md](./how-to/hitl-alignment.md) · 细则权威：[specs/SDD-GUIDE.md](./specs/SDD-GUIDE.md) **§2.5**

---

## 当前状态（模板自身）

| 区域 | 状态 |
|------|------|
| Agent 流水线 `how-to/agent-prompts/` | ✅ 绿场满配 01–04 + **轻量档**（须维护者明示）+ 棕地单线 + 人机协作铁律 |
| 棕地旁路 `specs/` | ✅ SDD-GUIDE（增量 Spec + **§2.5**）+ tasks / archive（桶内必有 INDEX）+ [ci-probes](./specs/ci-probes.md) |
| 归档 INDEX 模板 | ✅ [specs/archive/_index-template.md](./specs/archive/_index-template.md) |
| 人机协作专页 | ✅ [how-to/hitl-alignment.md](./how-to/hitl-alignment.md) |
| 某次立项的 PRD `explanation/PRD.md` | ⬜ 章节骨架已就绪；**填入本项目正文后再开 01** |
| 整体设计 / 契约 / 进度 | ⬜ 无预建；由该项目的 **01** 生成 |
| 模块规格 `reference/modules/` | ⬜ 无预建；由该项目的 **02** 生成（03 可按层级 1 回写） |
| tutorials/ | ⬜ Diátaxis 象限已预留；正文待项目补 |

**新项目第一步**：写入 `explanation/PRD.md` → 满配 01→02→03→04。后续模块在 01 已在且不改架构时，可由维护者明示走轻量档 02→04。  
**有代码后的修补**：任务包 → HITL → 写 `INDEX.md` 后迁 [archive](./specs/archive/)；见 [specs/README.md](./specs/README.md)。

---

## 双路径（怎么选）

```text
绿场满配（新项目 / 架构未定）
  PRD → 01 → 02 → 03 → 04
  产物：explanation/ + reference/

绿场轻量档（01 产物已在，本模块不改架构，须维护者明示）
  02（轻量）→ 03 → 04
  仍须模块文档；✅ 仍归 04

棕地（模块已 ✅ 后的修补 / 演进）
  specs/tasks 任务包（增量 Spec）→ IDE 编码自验 →（可选验收记录）→ archive/
  动契约时回写 reference/global-contract.md（版本 +0.1）
```

详情：[00 总纲 · 双路径](./how-to/agent-prompts/00-overview.md) · [specs/SDD-GUIDE.md](./specs/SDD-GUIDE.md)

---

## 地图

```text
                 学习（acquisition）          应用（application）
              ┌─────────────────────┬─────────────────────┐
   实践       │  tutorials/         │  how-to/            │
   (action)   │  教程：带我学会     │  指南：完成某任务   │
              ├─────────────────────┼─────────────────────┤
   认知       │  explanation/       │  reference/         │
   (cognition)│  解释：理解为何     │  参考：查是什么     │
              └─────────────────────┴─────────────────────┘

  specs/      ← SDD：任务包 / 自验 / HITL / 归档（棕地旁路）+ ci-probes
```

| 你想… | 去哪 |
|------|------|
| **人机怎么一块一拍定 Spec** | [how-to/hitl-alignment.md](./how-to/hitl-alignment.md) · [SDD §2.5](./specs/SDD-GUIDE.md) |
| 开新项目 / 跑绿场 Agent | [how-to/agent-prompts/00-overview.md](./how-to/agent-prompts/00-overview.md) |
| 有代码后开修补任务 | [specs/](./specs/) · [SDD-GUIDE](./specs/SDD-GUIDE.md) |
| 接 CI 防文档 drift | [specs/ci-probes.md](./specs/ci-probes.md) |
| 查契约、模块规格、进度 | [reference/](./reference/) |
| 理解范围与架构取舍 | [explanation/](./explanation/) |
| 跟着做建立手感 | [tutorials/](./tutorials/)（象限已预留） |

---

## 推荐阅读路径

**绿场：用本模板开一个新项目**

1. [how-to/agent-prompts/00-overview.md](./how-to/agent-prompts/00-overview.md)  
2. 写入 [explanation/PRD.md](./explanation/PRD.md)（章节结构对照 [01-overall-design.md](./how-to/agent-prompts/01-overall-design.md)「第二步」）  
3. 满配 01 → 02 → 03 → 04，一次一个模块；轻量档条件见 [00 §三](./how-to/agent-prompts/00-overview.md)  

**棕地：已有代码要改行为**

1. [specs/SDD-GUIDE.md](./specs/SDD-GUIDE.md)（含 **§2.5 渐进对齐**）  
2. 复制 [specs/tasks/_template.md](./specs/tasks/_template.md) → IDE 一块一拍填 HITL → 编码放行后自验 → 维护者 HITL → 从 [`_index-template.md`](./specs/archive/_index-template.md) 写出 `INDEX.md` 后迁 archive（无 INDEX 不得迁）  

**01/02 产出之后（绿场查阅）**

1. `explanation/PRD.md` → `explanation/overall-design.md`  
2. `reference/global-contract.md` + `reference/progress.md`  
3. 编码某模块时打开 `reference/modules/Fxx-*.md`  

---

## 目录结构

```text
docs/
├── README.md                 ← 本页（含 ★ 人机协作铁律）
├── tutorials/                ← Diátaxis 教程象限（正文待补）
├── how-to/
│   ├── hitl-alignment.md     ← 通用一块一拍（与产品无关）
│   └── agent-prompts/
│       ├── README.md         ← 本目录索引
│       ├── 00-overview.md
│       ├── 01-overall-design.md
│       ├── 02-module-spec.md
│       ├── 03-implement.md
│       └── 04-accept.md
├── reference/                ← 契约 / 进度 / modules/（01/02 生成）
├── explanation/              ← PRD；overall-design 由 01 生成
└── specs/                    ← 棕地 SDD（tasks + archive + ci-probes）
    ├── SDD-GUIDE.md
    ├── ci-probes.md
    ├── ci-probes-reference.py
    ├── tasks/
    └── archive/              ← 闭环迁入；桶内必有 INDEX.md
```

编码约定：**垂直切片** — 做一个模块，API + 约定界面一起验收。  
绿场模块 ✅ **仅由 04 过一遍（或维护者）**写入；棕地产品通过 **仅由维护者 HITL（或书面验收记录）**确认。  

---

## 路径规范（Agent 读写文档时）

完整纪律见 [00 总纲 · 路径规范](./how-to/agent-prompts/00-overview.md)。

| 当前工作区 | 文档路径怎么写 |
|-----------|----------------|
| `docs/` 本身 | `explanation/PRD.md`、`specs/tasks/…` |
| 仓库根（文档在子目录 `docs/`） | `docs/explanation/PRD.md`、`docs/specs/…` |

工程代码路径相对仓库根；不要相对 `how-to/agent-prompts/` 解析文档路径。

需求只认 `explanation/PRD.md`。该文件仍是落点说明、或正文属于上一项目时，不得开 01。

---

## 分类原则（写新文档时）

| 若内容主要是… | 应放在… |
|--------------|---------|
| 带领读者完成一段受控学习旅程 | `tutorials/` |
| 「要达成 X，按这些步骤做」 | `how-to/` |
| 字段、路径、错误码、表结构、清单 | `reference/` |
| 背景、动机、权衡、概念澄清 | `explanation/` |
| 迭代任务包、回执、验收、归档 | `specs/` |

模块 `Fxx` 文档多为**可编码规格**，归入 `reference/modules/`。大段「为什么」再抽到 `explanation/`。

---

*模板导航 · 棕地 IDE 单线；绿场同一 Agent 分阶段执行*
