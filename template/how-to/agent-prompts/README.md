# agent-prompts · 绿场流水线提示词

> **定位**：绿场 01→04 的阶段提示词 + 总纲。棕地不从这里进，走 [`../../specs/`](../../specs/)。  
> 路径均相对 **文档根 `docs/`**；工作区是仓库根时加前缀 `docs/`。详见 [00-overview.md](./00-overview.md)。

---

## 文件

| 文件 | 阶段 | 用途 |
|------|------|------|
| [00-overview.md](./00-overview.md) | 入口 | 总纲、不可变原则、双路径（含轻量档）、路径 I/O |
| [01-overall-design.md](./01-overall-design.md) | 架构师 | 生成 overall-design / global-contract / progress |
| [02-module-spec.md](./02-module-spec.md) | 架构师 | 生成 `modules/Fxx-*.md` |
| [03-implement.md](./03-implement.md) | 工程师 | 按模块文档编码；可回写 Fxx（层级 1）；progress → 🔍 |
| [04-accept.md](./04-accept.md) | 验收 | 独立过一遍；不改规格正文；通过则 ✅ |

人机协作（绿场 / 棕地都适用）：[`../hitl-alignment.md`](../hitl-alignment.md)。

---

## 怎么用

同一 IDE Agent **按序换提示词**（不要跳过落盘）：

```text
写入 explanation/PRD.md
  → 00-overview（先读 · 不可变原则）
  → 01-overall-design          （轻量档：维护者明示后可跳过）
  → 02-module-spec（一次一个模块；轻量档摘要更短，12 节仍全）
  → 03-implement
  → 04-accept
  → 下一模块从 02 再来
```

**不要放在这里**：任务包过程稿 → `specs/tasks/`；契约与模块规格正文 → `reference/`。
