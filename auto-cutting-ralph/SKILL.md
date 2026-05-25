---
name: auto-cutting-ralph
description: "Use when the user types $auto-cutting-ralph or wants the complete automatic video editing workflow: requirements, Ralph PRD, dry-run build, output generation plan, and verification feedback."
---

# 自动剪辑 Ralph 闭环

## 目标

这是 `auto-cutting` 与 `ralph-runner` 的组合入口，用于把自动剪辑需求拆成 Ralph 可执行 PRD，并按安全策略跑 dry-run 构建和迭代反馈。

## 工作流

1. 读取已安装的 `$auto-cutting` skill；在本仓库中对应 `../auto-cutting/SKILL.md`。
2. 读取 `../auto-cutting/references/optimized-ralph-workflow.md`。
3. 读取 `../ralph-runner/SKILL.md`、`../ralph-runner/references/projects.json` 和 `../ralph-runner/references/run-policy.json`。
4. 如果用户没有指定项目别名，默认优先考虑 `li-auto-auto-cutting`，但仍要确认目标目录存在且是 Git 仓库。
5. 生成或更新 Markdown 需求文档。
6. 生成 Ralph PRD，默认写入目标项目 `.agents\tasks\prd-auto-cutting.json` 或同类短 slug 路径。
7. 按 `ralph-runner` 规则预检、展示命令预览、运行 overview 和 dry-run build。
8. 每轮后读取 `.ralph\runs\` 输出，汇报 story 状态、验证结果、日志路径和下一步。

## 安全规则

- 默认 dry-run 与 `--no-commit`。
- 目标 git 工作区不干净时停止并汇报。
- 只有用户明确允许 commit，才运行正式提交模式。
- 自动剪辑成片需求必须包含 render-plan 路径、渲染命令、输出路径和验证报告路径。

完成后按 `auto-cutting` 的汇报格式用中文汇报，并附 Ralph 命令、日志路径和 dry-run 结果。
