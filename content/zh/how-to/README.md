# how-to/

本目录放**可执行操作步骤**（人机协作 + Agent 阶段提示词）。棕地流程正文在 [`../specs/`](../specs/)。

## 本目录内容

| 路径 | 说明 |
|------|------|
| [hitl-alignment.md](./hitl-alignment.md) | HITL + Spec-driven + 一块一拍（定 Spec 的默认姿势） |
| [agent-prompts/](./agent-prompts/) | 绿场 00–04 提示词；入口见 [agent-prompts/README.md](./agent-prompts/README.md) |

### agent-prompts/ 速查

| 文件 | 用途 |
|------|------|
| [00-overview.md](./agent-prompts/00-overview.md) | 总纲、铁律、双路径、路径 I/O |
| [01-overall-design.md](./agent-prompts/01-overall-design.md) | 生成整体开发文档 |
| [02-module-spec.md](./agent-prompts/02-module-spec.md) | 生成模块级开发文档 |
| [03-implement.md](./agent-prompts/03-implement.md) | 按模块文档编码（收尾 🔍） |
| [04-accept.md](./agent-prompts/04-accept.md) | 独立验收（通过标 ✅） |

### 棕地入口（正文在 specs/）

| 文件 | 用途 |
|------|------|
| [../specs/README.md](../specs/README.md) | 何时走棕地 |
| [../specs/SDD-GUIDE.md](../specs/SDD-GUIDE.md) | IDE 单线、一块一拍、HITL |
| [../specs/ci-probes.md](../specs/ci-probes.md) | CI 机检探针 |
| [../specs/tasks/_template.md](../specs/tasks/_template.md) | 任务包模板 |

## 可按项目补充（有正文再挂链）

| 类型 | 说明 |
|------|------|
| `vertical-slice-accept.md`（可选） | 垂直切片验收 checklist |
| 项目专用操作指南 | 部署、联调、发版等（放产品仓约定目录亦可） |

字段表 / 设计动机 / 任务包过程稿 / 受控练习分别见 `reference/`、`explanation/`、`specs/`、`tutorials/`。
