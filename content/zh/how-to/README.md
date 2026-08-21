# How-to guides · 操作指南

> Diátaxis：**任务导向（goal-oriented）**  
> 回答：「我要完成某件事，步骤是什么？」

How-to 假设读者已有基础，直接给可执行步骤。不要写成概念课，也不要展开整份 API 百科。

---

## 已落地（模板通用）

以下内容随模板复制到新仓库，与具体产品无关。

### 人机协作

| 指南 | 用途 |
|------|------|
| [人机协作铁律-渐进对齐](./hitl-alignment.md) | **HITL + Spec-driven + 一块一拍**（定 Spec 的默认姿势） |

### Agent / IDE 提示词（绿场）

体系入口为 [agent-prompts/README.md](./agent-prompts/README.md)；先读 [00-overview.md](./agent-prompts/00-overview.md)：

| 指南 | 用途 |
|------|------|
| [00-overview.md](./agent-prompts/00-overview.md) | 总纲、不可变原则、双路径（含轻量档）、路径 I/O |
| [01-overall-design.md](./agent-prompts/01-overall-design.md) | 生成整体开发文档 |
| [02-module-spec.md](./agent-prompts/02-module-spec.md) | 生成模块级开发文档 |
| [03-implement.md](./agent-prompts/03-implement.md) | 按模块文档编码（收尾 🔍） |
| [04-accept.md](./agent-prompts/04-accept.md) | 独立验收过一遍（不改规格正文；通过标 ✅） |

### 棕地 / 迭代（SDD）

棕地流程正文在 `specs/`，此处只给入口：

| 指南 | 用途 |
|------|------|
| [../specs/README.md](../specs/README.md) | 何时走棕地 |
| [../specs/SDD-GUIDE.md](../specs/SDD-GUIDE.md) | IDE 单线、§2.5 一块一拍、HITL |
| [../specs/ci-probes.md](../specs/ci-probes.md) | CI 机检探针（防 drift） |
| [../specs/tasks/_template.md](../specs/tasks/_template.md) | 任务包模板 |

---

## 待按项目补充

以下**不属于**模板固定内容；有正文再挂链，勿预建死链：

| 类型 | 说明 |
|------|------|
| `vertical-slice-accept.md`（可选） | 做人验收时的垂直切片 checklist |
| 项目专用操作指南 | 绑定某产品 / 环境的步骤（部署、联调、发版等） |

工程启动、客户端等说明放在**该项目仓库根**（或该仓库约定目录），不绑死在本模板里。

---

## 不要放在这里

- 错误码全表、DDL、字段清单 → [`../reference/`](../reference/)  
- 为什么这样设计 → [`../explanation/`](../explanation/)  
- 迭代任务包过程稿 → [`../specs/`](../specs/)  
- 受控上手练习（一步一预期结果）→ [`../tutorials/`](../tutorials/)
