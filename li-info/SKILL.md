---
name: li-info
description: Short trigger alias for the Li Auto owner infographic workflow. Use when the user types $li-info or asks to generate, plan, QA, archive, or publish Li Auto owner infographics from account links, daily use scenarios, share codes, IP/Prompt Codes, imagegen prompts, or the Obsidian 信息图工作台.
---

# Li Info

## Purpose

This skill is a short `$li-info` trigger for the full Li Auto infographic workflow stored in this repository or the user's installed skills directory:

`../li-auto-infographic-suite`

Use it to produce main-content-first Li Auto owner infographics from account links or daily use scenarios.

## Required Action

When this skill triggers:

1. Read and follow the full workflow in:
   `../li-auto-infographic-suite/SKILL.md`
2. Read the reference when paths, naming rules, or production constraints are needed:
   `../li-auto-infographic-suite/references/current-workflow.md`
3. Treat the highest priority rule as mandatory:
   main content clarity beats IP visuals. Sacrifice IP visuals, base labels, badges, and decorative effects whenever needed to keep the title, scene, share code/action, benefit, and CTA clear.

## User Input Template

Accept this compact prompt shape:

```text
用 $li-info 生成信息图：

任务类型：账号链接模式 / 日常场景模式 / 每日6套 / 单套 / 指定主题多套
主题：
目标用户：
核心场景：
分享码：自动从主库选 / 使用以下分享码
页数：默认6页 / 指定页数
平台：小红书 / 抖音 / 视频号 / 社群
CTA：评论「进群」/ 评论「分享码」/ 关注收藏 / 自定义
视觉要求：主体优先，IP 只做轻装饰，不挡内容
禁止内容：不要出现官方背书、永久有效、全车型通用；不要将用户需求输入原文写进信息图
补充说明：
```

If task type or theme/core scene is missing, ask for it before production. Do not generate images from an underspecified request.

## Forbidden Visible Content

Never put these into the visible infographic:

- the user's raw input prompt or template labels
- internal file names
- `IP Code`, `Prompt Code`, or resource rotation wording
- official endorsement, permanent validity, or all-model compatibility claims unless verified by source material
