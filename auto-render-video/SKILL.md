---
name: auto-render-video
description: "Use when the user types $auto-render-video or wants Codex to directly cut, concatenate, subtitle, mix audio, render, export, or validate an MP4 video from source materials."
---

# 自动渲染视频

## 目标

这是 `auto-cutting` 的直接成片入口。用户触发 `$auto-render-video` 时，优先生成或读取 render-plan JSON，然后使用项目已有渲染链路；没有项目链路时，使用内置 FFmpeg 脚本。

## 工作流

1. 读取已安装的 `$auto-cutting` skill；在本仓库中对应 `../auto-cutting/SKILL.md`。
2. 读取 `../auto-cutting/references/workflow.md` 的“直接渲染计划”。
3. 盘点素材、脚本、字幕、BGM、输出目录和目标画幅。
4. 生成或更新 render-plan JSON，可从 `../auto-cutting/assets/render-plan-template.json` 复制。
5. 先校验素材路径、片段时长、输出目录、FFmpeg/FFprobe 可用性。
6. 没有项目专用渲染命令时运行：

```text
py -3 ..\auto-cutting\scripts\render_plan_ffmpeg.py path\to\render-plan.json
```

7. 验证 mp4 文件存在、大小非零、可被媒体探测工具读取，并生成报告。

## 安全规则

- 不修改原始素材。
- 不覆盖已有输出，除非用户明确允许。
- 输出写入新的目录或带时间戳文件名。
- FFmpeg 不可用时，不伪装完成；保留 render-plan 并报告缺失工具。

完成后按 `auto-cutting` 的汇报格式用中文汇报。
