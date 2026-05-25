---
name: li-auto-minimal-infographic
description: Use when creating, planning, QAing, archiving, or sharing Li Auto owner minimal share-code infographic carousel sets, especially question-first workflows that ask for account, goal, target audience, CTA, IP attribute, forbidden content, share-code source/count, and output needs. Trigger for 理想信息图, 极简分享码, 轻IP/IP属性, NO-IP 极简清单, 账号运营信息图, Obsidian 信息图工作台, or reusable/shareable Li Auto infographic workflows.
---

# Li Auto Minimal Infographic

## Overview

Use this skill to produce Li Auto owner share-code carousel infographics in the latest minimalist checklist style. The workflow is question-first, main-content-first, and delivery-ready: clarify the account and goal, select or accept share codes, choose NO-IP or light IP attributes, draft concrete owner-scene copy, generate or render pages, QA, write publish docs, and archive.

This skill is designed for the user's own production and for sharing with other creators. If the expected Vault files are missing, ask for the missing source data instead of assuming it exists.

## First Move

Before producing anything:

1. Read available project instructions and workbench docs.
2. Identify which required inputs are already known from the user request.
3. Ask only the missing questions needed to proceed.
4. State assumptions when the user says "默认".

When working in the user's Obsidian Vault, prefer these files if present:

- `00 收件箱/CODEX_README.md`
- `04 内容与创作/理想车主内容工具/信息图工作台/00_主控台/信息图主控台.md`
- `04 内容与创作/理想车主内容工具/信息图工作台/01_生产资产库/资源轮转状态.md`
- `04 内容与创作/理想车主内容工具/信息图工作台/01_生产资产库/分享码主库.md`
- `04 内容与创作/理想车主内容工具/信息图工作台/01_生产资产库/提示词IP主库.md`
- `04 内容与创作/理想车主内容工具/信息图工作台/02_生产模板/交付与质检模板.md`

Also read `references/minimal-style-spec.md` inside this skill for the portable visual spec and prompt rules. Do not use `90_历史资料` as the active source unless the user explicitly asks.

## Intake Questions

Ask in Chinese by default. Keep the first question bundle short. If the user already gave an answer, do not ask it again.

Required questions when missing:

```text
1. 账号：这套图给哪个账号用？有账号链接/账号名吗？没有就按通用理想车主账号。
2. 目标：这次主要要什么结果？收藏、评论进群、涨粉、私信领取、社群转发、卖课/工具承接，还是别的？
3. 主题/场景：这套图讲什么？车主在哪个用车场景会用？
4. 目标用户：给谁看？新车主、家庭用户、通勤用户、露营/长途用户、车机重度用户，还是潜在车主？
5. 分享码：用多少个？从主库自动选，还是你提供码和功能说明？
6. CTA：底部/结尾怎么承接？默认是评论「进群」拉你进车主群。
7. IP属性：NO-IP，还是轻 IP 属性？如果轻 IP，要什么感觉，例如线索感、能量感、游戏感、电影感。
8. 禁止内容：哪些不能出现？默认不写官方背书、永久有效、全车型通用、未授权角色/logo、用户原始需求和内部流程词。
```

Minimum first question when almost nothing is specified:

```text
这套图先确认 5 件事：给哪个账号用、目标是什么、主题/场景是什么、准备用多少个分享码、CTA 怎么写？IP 默认 NO-IP，也可以做轻 IP 属性。
```

Defaults when the user says "默认":

- 账号: 通用理想车主账号.
- 目标: 收藏 + 评论「进群」承接.
- 目标用户: 理想车主 / 车机功能使用者.
- 分享码来源: 当前主库和资源轮转状态.
- CTA: `评论「进群」拉你进车主群`.
- IP: `NO-IP`, unless the user asks for light IP.
- Visual style: latest minimal checklist with clear `理想汽车分享码｜极简清单` cover identity, high contrast, no mascot, no QR code, no fake official endorsement.

## Mode Selection

Choose the mode from the user's request:

- 账号链接模式: research the account link or ask for screenshots/positioning notes, then assign themes and CTA fit.
- 轻 IP 极简清单: use the 2026-05-20 style with a dark oversized cover, account icon, red CTA, and clean code pages. IP appears only as tiny attributes.
- NO-IP 密集清单: use the 40/60/custom-code dense list style. Default density is 6 share codes per content page.
- 单套场景图: use one concrete owner scene and 6-8 pages unless the user specifies otherwise.
- 每日/多套生产: use the workbench pools and resource rotation when the Vault exists.

If the local template prefers 3 codes per page but the user asks for 40/60 dense sets, use 6 codes per page as a dense-list override and record it in QA.

## Planning Workflow

1. Summarize the user goal, input, output, core flow, edge cases, and risks.
2. Create an internal brief:
   - Account mode: account attributes, audience, tone, visual signals, suitable themes, CTA fit, and risks.
   - Scenario mode: target user, pain point, codes/actions, page messages, CTA, forbidden visible content.
3. Select or validate share codes:
   - Use the live share-code source and rotation ledger when available.
   - If sharing this skill outside the user's Vault, ask the user to provide codes or a source file.
   - Preserve exact code strings and feature/use-case notes.
4. Select visual identity:
   - NO-IP for general dense lists.
   - Light IP attributes only when user asks or the account style benefits from it.
5. Draft all visible Chinese copy before image generation or rendering.
6. Generate or render 3:4 vertical PNG pages, default `1080x1440`.
7. Package delivery docs and QA record.
8. Update the rotation ledger if working in the user's Vault and resources were actually used.

## Visual Rules

Read `references/minimal-style-spec.md` when exact style decisions are needed. Core rules:

- Cover: deep ink-green / near-black grain background, top-left `理想汽车分享码｜极简清单`, optional `理想汽车 / LI AUTO` trademark text or `理想车主分享码收藏版`, oversized Chinese title, account icon when available, short benefit line, bottom red CTA, small risk note.
- Content pages: off-white or cream body, dark green header/footer, large title, short concrete subtitle, clear share-code cards.
- Code density:
  - Light IP scene set: usually 3 codes per content page.
  - Dense 40/60/custom list: usually 6 codes per content page.
- CTA placement: cover may use a light group CTA; pure share-code pages should not repeat group/follow CTA. Closing page may strengthen CTA.
- Main content priority: title, scene, share code/action, benefit, and risk boundary beat decoration.
- IP policy: Li Auto trademark/text identity is allowed on the cover; no unlicensed character likeness, fake badge, fake QR code, watermark, or IP element that competes with text.

## Forbidden Visible Content

Never place these in the infographic image or public post copy:

- User raw prompt, intake labels, planning notes, local paths, file names.
- `IP Code`, `Prompt Code`, resource rotation wording, source-library names, model instructions.
- Official endorsement, permanent validity, all-model compatibility, safety guarantees, or unverified claims.
- Fake QR codes, fake official labels, watermarks, random numbers, random English, placeholder boxes.
- Unlicensed copyrighted character likenesses, fake official badges, or high-similarity IP visuals.

## Prompt Template

Use this page-specific prompt structure for imagegen:

```text
Create a 1080x1440 vertical Chinese minimalist infographic page for Li Auto owners.
Style: 极简清单, high-contrast, practical, mobile-readable.
Visual identity: 理想汽车分享码｜极简清单
IP policy: {NO-IP or tiny abstract attributes only, Li Auto trademark/text allowed for identity, no unlicensed character/fake official badge}

Page type: {cover/content/closing content}
Visible page meta: {page_meta}
Main title: {title}
Subtitle: {subtitle}
CTA if present: {cta}
Risk note if present: {risk_note}

Layout rules:
- Keep all Chinese text readable.
- Use stable margins.
- Do not overlap text.
- Do not add extra codes, icons, badges, or invented words.
- Copy every share code exactly as written.

Share-code rows:
1. {code} — {feature/use case}
2. {code} — {feature/use case}
...
```

When exact digits matter more than image texture, offer deterministic SVG/Sharp rendering before using imagegen.

## Delivery Package

For the user's current Vault, use this archive pattern when appropriate:

```text
04 内容与创作/理想车主内容工具/信息图工作台/04_交付归档/YYYY-MM-DD_<主题或N码>极简分享码信息图/
```

Each final set should include:

```text
01_封面.png
02_<页面主题>.png
...
事实底稿.md
制作提示词.md
发布信息.md
质检记录.md
文件清单.md
```

`发布信息.md` must be public-ready and include:

- 一句话定位
- 4 个发布标题：首选、小红书、抖音/视频号、社群转发
- 120-220 字发布正文
- 8-12 个标签
- 评论区承接
- CTA
- 使用分享码表格
- 风险边界

## QA Gate

Do not claim the set is complete until these checks pass or are explicitly marked as needing human review:

- final PNG count matches the plan;
- every final PNG is `1080x1440` unless another size was requested;
- every visible share code matches the fact sheet;
- no requested code is missing unless documented;
- CTA matches the user's selected wording;
- no mascot, QR code, fake badge, watermark, or fake endorsement appears;
- no internal production terms appear in artwork or public copy;
- account icon and IP attributes do not block title, body, codes, or CTA;
- risk boundaries appear for share-code validity, safety reminders, OTA/model compatibility, assisted driving, or strong claims;
- rotation record is updated when the local main library was used.

## Response Pattern

After finishing, report in Chinese with:

- 需求理解
- 实现方案
- 关键逻辑
- 修改文件
- 验证方式
- 风险与待确认

Keep the final response short and include the final folder path or package path.
