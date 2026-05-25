---
name: auto-cutting-prd
description: "Use when the user types $auto-cutting-prd or wants to turn an automatic video editing idea into a Markdown requirements document, editing plan, or Ralph-compatible PRD before implementation."
---

# 自动剪辑需求与 PRD

## 目标

这是 `auto-cutting` 的快捷入口，用于先把自动剪辑想法整理成需求文档、剪辑方案或 Ralph PRD。它不直接渲染视频，除非用户明确要求切换到 `$auto-render-video` 或 `$auto-cutting-ralph`。

## 工作流

1. 读取已安装的 `$auto-cutting` skill；在本仓库中对应 `../auto-cutting/SKILL.md`。
2. 读取目标项目的 README、需求文档、产品说明、接口说明、草稿样例和输出样例。
3. 如果缺少需求文档，使用 `../auto-cutting/assets/requirements-template.md` 创建或补全。
4. 明确输出模式、素材路径、目标时长、画幅、字幕、BGM、是否允许覆盖和验收标准。
5. 如果用户要 Ralph PRD，读取 `../auto-cutting/references/optimized-ralph-workflow.md` 和 `../auto-cutting/assets/ralph-prd-template.json`，拆成小而可测的 stories。

## 输出

默认输出：

- Markdown 需求文档。
- 剪辑计划或决策清单。
- 可选 Ralph PRD JSON。
- 待确认项与风险列表。

完成后按 `auto-cutting` 的汇报格式用中文汇报。
