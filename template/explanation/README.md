# Explanation · 解释

> Diátaxis：**理解导向（understanding-oriented）**  
> 回答：「为什么这样设计？背景与取舍是什么？」

解释用来建立心智模型：讨论动机、约束、替代方案。  
不要把逐步操作或字段级规格塞在这里——那些分别属于 How-to 与 Reference。

---

## 本目录文件

| 文件 | 状态 | 说明 |
|------|------|------|
| [PRD.md](./PRD.md) | ⬜ 骨架已就绪，正文待填 | **当前项目**唯一需求源；绿场 01 的输入 |
| `overall-design.md` | ⬜ 尚无文件 | 由 **01** 首次生成；勿预建空壳 |

PRD 已含可填骨架（功能编号 `F-x`、场景、约束、非功能、待确认）；与 01 产出结构对齐，细节见 [`../how-to/agent-prompts/01-overall-design.md`](../how-to/agent-prompts/01-overall-design.md)。**未填正文前不要开 01**（空标题不等于需求）。

---

## 文件从哪来

1. 维护者写入 `PRD.md`（覆盖落点说明，不要沿用上一项目需求）。  
2. 绿场 **01** 读取 PRD，创建 `overall-design.md`，并初始化 `reference/` 下的契约与进度。  
3. 产品范围被后续变更改写时，再回写 PRD；日常修补不走这里。

有代码之后的行为修补，走 [`../specs/`](../specs/) 棕地任务包，不必为每个小改动改写 PRD。

---

## 不要放在这里

- 字段、路径、错误码、表结构 → [`../reference/`](../reference/)  
- 「要达成 X，按这些步骤做」→ [`../how-to/`](../how-to/)  
- 迭代任务包 / HITL 过程稿 → [`../specs/`](../specs/)
