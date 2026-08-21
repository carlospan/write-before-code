# specs · 棕地 / 迭代旁路（SDD）

> **定位**：模块已落地、有代码之后的修补与演进走这里；**不替代**绿场 `01→02→03→04`。  
> **现行流程**：**IDE 单线**（同一会话起草规格 → 编码 → 自验 → 回写）+ **§2.5 渐进对齐**（一块一拍 HITL）。权威细则见 [SDD-GUIDE.md](./SDD-GUIDE.md)。  
> **入口**：本目录 GUIDE；人机协作专页 [../how-to/hitl-alignment.md](../how-to/hitl-alignment.md)；体系总览 [../how-to/agent-prompts/00-overview.md](../how-to/agent-prompts/00-overview.md)。

---

## 何时走绿场，何时走本目录

| 场景 | 走哪条 |
|------|--------|
| 新项目从零，或架构未定（换栈、改模块拆分） | **绿场满配**：PRD → 01 → 02 → 03 → 04 |
| 01 产物已在，按 `progress.md` 开下一个未写文档的模块，且不改架构 | **绿场轻量档**（须维护者明示）：跳过 01 → 02（轻量）→ 03 → 04 |
| 已有模块 ✅ 之后的行为修补、回归修复、小演进、协议微调 | **棕地**：`specs/tasks/` 任务包 → IDE 编码自验 →（可选验收记录）→ `archive/` |
| 改动会动到跨模块契约 | 棕地任务包 **同时** 回写 `reference/global-contract.md`（版本 +0.1） |
| 不确定 | 维护者定；默认：**会改对外行为 → 棕地任务包** |

---

## 目录结构

```text
specs/
├── README.md                 ← 本页
├── SDD-GUIDE.md              ← 流程权威（单线、§2.5 一块一拍、HITL）
├── ci-probes.md              ← CI 机检规格（可选接入工程仓）
├── ci-probes-reference.py    ← 探针参考实现
├── tasks/                    ← 进行中任务包（只放未闭环）
│   ├── README.md
│   └── _template.md
└── archive/                  ← 闭环后迁入，不删历史；桶内必有 INDEX.md
    ├── README.md
    └── _index-template.md
```

| 文档 | 用途 |
|------|------|
| [SDD-GUIDE.md](./SDD-GUIDE.md) | 棕地怎么写规格、怎么验收；**§2.5 渐进对齐【必守】** |
| [ci-probes.md](./ci-probes.md) | 防文档 drift 的机检探针清单 |
| [tasks/_template.md](./tasks/_template.md) | 任务包模板（复制后改名使用） |
| [tasks/](./tasks/) | 未闭环任务包目录 |
| [archive/](./archive/) | 已闭环任务归档（不删；桶内必有 INDEX.md） |
| [archive/_index-template.md](./archive/_index-template.md) | 归档结论页模板 |

---

## 怎么开一个棕地任务（最短路径）

1. 复制 [`tasks/_template.md`](./tasks/_template.md) → `tasks/YYYY-MM-DD-短名.md`  
2. 写清 **当前行为** + **ADDED / MODIFIED / REMOVED**；验收用 WHEN/THEN  
3. 产品边界未清时，按 **一块一拍** 填 HITL，谈定立刻落盘  
4. 维护者 **编码放行** 后再大改码；同一会话做工程自验  
5. 若动契约，回写 `reference/global-contract.md`（版本递增）  
6. 写好 `archive/_index-template.md` 对应的 `INDEX.md`（结论 + 契约是否回写）后，整组迁入 `archive/YYYY-MM-DD-主题/`，勿删过程稿。**无 INDEX 不得迁。**  

细节与反模式见 [SDD-GUIDE.md](./SDD-GUIDE.md)。

---

## 与 reference / progress 的关系

- **绿场模块状态**仍以 `reference/progress.md`（⬜→📝→🔍→✅）为准。  
- **棕地任务**不占用 progress 里「未开始」的模块行；在任务包与验收记录里闭环即可。  
- 若棕地改出了新的跨模块约定，必须反映进 `global-contract.md`；必要时在 progress 备注列留一句指针。

---

## 不要放在这里

- 绿场整体设计 / 模块规格 → [`../explanation/`](../explanation/)、[`../reference/`](../reference/)  
- 可重复执行的操作步骤手册 → [`../how-to/`](../how-to/)  
- 受控上手练习 → [`../tutorials/`](../tutorials/)
