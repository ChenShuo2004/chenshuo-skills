---
name: li-auto-infographic-suite
description: Use when Codex needs to plan, generate, QA, archive, or publish Li Auto owner infographic carousel batches from the Obsidian Vault workflow, especially tasks involving account-link research, three-set-per-account production, multiple accounts, share codes, IP/Prompt Codes, imagegen prompts, resource rotation, quality checks, or the 信息图工作台.
---

# Li Auto Infographic Suite

## Overview

Use this skill to produce Li Auto owner infographic suites from the user's Obsidian Vault workflow. Support both account-link mode and daily/scenario mode. The highest priority rule is: sacrifice IP visuals, base labels, and decorative effects whenever needed to keep the main message clear, specific, and prominent.

## Input Contract

Before final planning or image generation, collect or infer the following fields. If the task type or theme is missing, ask for it before production.

```text
任务类型：账号链接模式 / 日常场景模式 / 每日6套 / 单套 / 指定主题多套
主题：这套图讲什么
目标用户：给谁看
核心场景：用户在哪个日常应用场景会用
分享码：自动从主库选 / 使用用户给定分享码
页数：默认6页 / 用户指定页数
平台：小红书 / 抖音 / 视频号 / 社群
CTA：评论「进群」/ 评论「分享码」/ 关注收藏 / 自定义
视觉要求：主体优先，IP 只做轻装饰，不挡内容
禁止内容：不要出现官方背书、永久有效、全车型通用；不要把用户需求输入原文写进信息图
补充说明：可选
```

Defaults when safe:

- 目标用户 defaults to 理想车主 / 车机功能使用者.
- 分享码 defaults to current unused resources from `分享码主库.md` and `资源轮转状态.md`.
- 页数 defaults to 6 pages per set.
- 平台 defaults to 小红书 + 抖音/视频号 compatible carousel copy.
- CTA defaults to 评论「进群」拉你进车主群.
- 视觉 defaults to main-content-first minimal style.

Do not generate images if the set cannot answer: who it serves, which scene it solves, which code/action matters, what benefit the user gets, where the CTA belongs, and which risk boundary is needed.

## Required Context

Before planning or generating, read the user's current local Vault files, not old memory. The Vault path is user-specific and is not bundled with this public skill; resolve it from the user's context or ask for the root path when missing.

1. `<Obsidian Vault>/00 收件箱/CODEX_README.md`
2. `<Obsidian Vault>/04 内容与创作/理想车主内容工具/信息图工作台/00_主控台/信息图主控台.md`
3. `<Obsidian Vault>/04 内容与创作/理想车主内容工具/信息图工作台/01_生产资产库/资源轮转状态.md`
4. `<Obsidian Vault>/04 内容与创作/理想车主内容工具/信息图工作台/01_生产资产库/分享码主库.md`
5. `<Obsidian Vault>/04 内容与创作/理想车主内容工具/信息图工作台/01_生产资产库/提示词IP主库.md`
6. `<Obsidian Vault>/04 内容与创作/理想车主内容工具/信息图工作台/02_生产模板/每日生产模板.md`
7. `<Obsidian Vault>/04 内容与创作/理想车主内容工具/信息图工作台/02_生产模板/交付与质检模板.md`

Do not use `90_历史资料` as a production source unless the user explicitly asks for old examples.

Read `references/current-workflow.md` when exact paths, naming rules, or production constraints are needed.

## Mode Selection

- 账号链接模式: require one account link per account, research each account, then produce 3 sets per account unless the user specifies otherwise.
- 日常场景模式 / 单套: use the user-provided theme, target user, and core scene to produce the requested set count.
- 每日6套: use the workbench's six default theme pools and the current resource rotation.
- 指定主题多套: use the user's theme list; if no list is provided, ask for it.

When user instructions conflict with older Vault template wording, follow the user's latest explicit task type and record the mismatch in the final report.

## Production Flow

1. Confirm task scope from the input contract:
   - Ask the user how many accounts to produce for unless they already specified it.
   - In account-link mode, require one account link per account before final planning.
   - In daily/scenario mode, require at least task type and theme/core scene.
   - If required inputs are missing, stop and ask for them; do not invent account positioning or production goals.
2. Create or update a production directory under the matching mode:
   `信息图工作台\03_每日生产中\YYYY-MM-DD_<账号数>账号各3套信息图\`
   Use `YYYY-MM-DD_<账号名>_3套信息图` for a single-account job.
   For daily mode, use `YYYY-MM-DD_每日6套信息图`. For scenario/single-set mode, use `YYYY-MM-DD_<主题>信息图`.
3. In account-link mode, research each account link in a browser or web search before choosing themes.
4. Produce an account profile card for account-link mode. Produce a scene brief for daily/scenario mode.
5. Read resource rotation before choosing IP Codes, Prompt Codes, or share codes.
6. Select set themes, subthemes, IP Codes, Prompt Codes, and share codes from the current unused pools unless the user gave exact resources.
7. Draft every page's Chinese copy before image generation. Make the content concrete: target user, scene, code/action, and benefit must be visible.
8. Generate final 3:4 PNG pages with imagegen. Do not create blank templates, mockups, background-only images, or images where IP/base labels compete with the main content.
9. Create `发布信息.md`, `制作提示词.md`, and `质检记录.md` for each set.
10. Run quality checks, retry failed pages, then archive only accepted files.
11. Update `资源轮转状态.md` with actual IP Codes, share codes, date, account, themes, archive directory, and cross-round status.

## Account Research

Before generating any set, inspect each account link with a browser or web search. Account information is time-sensitive; do not rely on memory.

For each account, capture:

- account name, handle, platform, and URL
- bio/description and visible positioning
- audience signals: owner type, interest, pain points, comment themes, community intent
- content attributes: tutorial, review, lifestyle, family use, emotional companion, news, product tips, or conversion-oriented
- visual attributes: cover style, color tendency, title density, person/IP presence, screenshot/tutorial use
- tone: practical, expert, friendly, emotional, punchy, warning, or community-service
- useful content pillars for 3 sets
- CTA fit: follow, collect, comment keyword, group entry, feedback, or checklist
- risks and boundaries: platform restrictions, unsupported claims, sensitive topics, copied style risks

Use the profile card to assign the 3 sets. Example:

```text
账号A：
- 属性：理想车主实用教程 / 强收藏导向 / 评论进群承接
- 3套方向：安全守护、舒适座舱、出行效率
- 视觉：大标题 + 工具卡 + 车机场景
- CTA：收藏 + 评论「进群」
```

If the account page cannot be accessed because of login, region, anti-bot, deleted content, or private visibility, search the account name/handle on the web. If still blocked, ask the user for screenshots or a short account positioning note before final generation.

## Scene Brief

Use this for daily/scenario mode before production:

```text
任务类型：
主题：
目标用户：
核心场景：
用户痛点：
关键分享码/动作：
页面主信息：
CTA：
风险边界：
禁止写入图面的信息：
```

Never copy the user's raw prompt, input template labels, internal file names, IP Code, Prompt Code, rotation status, or production instructions into the visible infographic copy.

## Selection Rules

- Share codes only come from `分享码主库.md`.
- IP Codes, Prompt Codes, CTA modules, style rules, and official/authorized IP notes only come from `提示词IP主库.md`.
- Prefer resources not yet used in the current rotation.
- If a multi-account batch needs more resources than remain in the current round, use the remaining resources first, open the next round, and record the reason.
- Each account gets 3 distinct set themes unless the account profile clearly supports a focused series. Avoid repeating the same exact topic across accounts unless their account attributes call for different angles.
- Split broad pools into concrete subthemes, such as "安全守护-下车提醒", "安全守护-盲区影像", "舒适座舱-夏季降温", or "桌面与调音-桌面游戏".
- Avoid consecutive reuse of yesterday's IP Code or share-code cluster unless the current round is exhausted.
- Use no more than 3 share codes on any one page.

## Set Structure

Default each set to 6 pages unless the theme needs 7-8:

| Page | Role | Requirement |
| --- | --- | --- |
| 01 | 封面 | Main topic, target scene, owner benefit, light CTA; IP/base labels must stay secondary |
| 02 | 总览 | 3-5 concrete conclusions for the target user and scene |
| 03 | 分享码页 | Up to 3 codes with exact use scenes and benefits |
| 04 | 分享码页 | Up to 3 codes with exact use scenes and benefits |
| 05 | 场景组合 | How codes/actions work together in a daily use flow |
| 06 | 尾页承接 | Group CTA, follow CTA, risk boundary |
| 07 | 可选扩展 | Comparison, checklist, tutorial, or pitfall |
| 08 | 可选扩展 | Comment handoff or next-set teaser |

Middle pages should focus on utility, scenes, and save-worthy value. Put group/follow CTAs only on cover and closing pages unless the user asks otherwise.

## Main Content Priority

This is the highest priority quality rule:

- The visible hierarchy must prioritize title, scenario, core conclusion, share code/action, benefit, and risk boundary.
- IP visuals, base labels, badges, ornaments, and background elements may be removed or reduced whenever they reduce readability.
- IP/base elements must not cover, intersect, crowd, or visually compete with title, body copy, share codes, or CTA.
- Each page must have one primary message only.
- Avoid vague claims such as "更安全", "更舒适", or "效率更高" unless paired with a concrete action, such as "右转低速打开盲区影像" or "下车前提醒检查随身物".
- The page should still work if every IP decoration is removed.

## Imagegen Prompt Standard

Build prompts from:

`page role + Prompt Code + IP Code + official/authorized IP prompt + share-code facts + CTA + risk boundary`

Every image prompt must require:

- final vertical 3:4 PNG infographic
- complete Chinese text rendered directly in the image
- exact Chinese copy, exact share codes with spaces removed
- mobile-readable hierarchy
- main content remains unobstructed; IP/base labels are tiny secondary accents or removed
- no raw user requirement labels such as "任务类型", "目标用户", "核心场景", "视觉要求", or internal workflow wording in the image
- no fake QR code, fake official label, watermark, random numbers, random English, or placeholder boxes
- no official logo or copyrighted character likeness unless the current source marks the IP as authorized or the user provides usable reference/permission

If imagegen returns garbled Chinese, tiny text, wrong share codes, missing pages, mismatched IP, blocked main content, or visible input-template text, simplify the copy, reduce/remove IP decoration, and regenerate that page.

## Quality Gate

Do not mark a set complete until these pass:

- dimensions are 3:4 vertical
- every required page exists
- Chinese is readable and not garbled
- share codes match `分享码主库.md`
- each page has no more than 3 share codes
- title, body copy, share codes, and CTA are not blocked by IP/base labels or decorative elements
- each page has a concrete target scene, code/action, and benefit
- a reader can identify what the page is about within 3 seconds
- no raw user input, input-template labels, internal file names, Prompt Code, IP Code, or rotation terms appear in the visible image
- IP Code, visual attributes, and topic are consistent
- cover has only light CTA
- closing page has full group and follow CTA
- risk boundary appears for safety, assisted driving, OTA, official features, vehicle compatibility, or strong claims
- files are in the expected production or archive directory
- `资源轮转状态.md` reflects actual used resources
- each account has a researched profile card linked to the production plan

## Output Report

When finished, report in Chinese with:

1. 需求理解
2. 实现方案
3. 关键逻辑
4. 修改文件 or 生成文件
5. 验证方式
6. 风险与待确认

Always mention the task type, required inputs received, total set/page count, account links checked when relevant, resource rotation updates, and any mismatch between the current Vault templates and the user's latest rule.
