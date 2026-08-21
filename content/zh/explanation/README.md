# explanation/

本目录放**产品与架构说明**（需求源、整体设计）。字段级规格与操作步骤不在这里。

## 本目录内容

| 路径 | 状态 | 说明 |
|------|------|------|
| [PRD.md](./PRD.md) | ⬜ 骨架已就绪，正文待填 | **当前项目**唯一需求源；绿场 01 的输入 |
| `overall-design.md` | ⬜ 尚无文件 | 由 **01** 首次生成；勿预建空壳 |

PRD 骨架含功能编号 `F-x`、场景、约束、非功能、待确认；结构对齐 01，见 [`../how-to/agent-prompts/01-overall-design.md`](../how-to/agent-prompts/01-overall-design.md)。**未填正文前不要开 01**。

## 文件从哪来

1. 维护者写入 `PRD.md`（覆盖落点说明，勿沿用上一项目需求）。  
2. 绿场 **01** 读 PRD，创建 `overall-design.md`，并初始化 `reference/` 下契约与进度。  
3. 产品范围被后续变更改写时再回写 PRD；日常修补走 [`../specs/`](../specs/)。

字段 / 路径 / 错误码 → [`../reference/`](../reference/)。逐步操作 → [`../how-to/`](../how-to/)。
