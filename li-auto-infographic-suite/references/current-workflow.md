# Current Workflow Reference

This reference captures the user's current Li Auto owner infographic workflow. Use the live Vault files as the source of truth for data, and apply the user's latest rules for task type, input contract, and main-content-first image generation.

## Vault Roots

- Vault: `<Obsidian Vault>` (user-specific local path)
- Codex entry: `00 收件箱\CODEX_README.md`
- Account context: `03 项目与产品\理想汽车账号运营\ACCOUNT_CONTEXT.md`
- Main infographic workbench: `04 内容与创作\理想车主内容工具\信息图工作台`

## Current Workbench Files

- Master control: `信息图工作台\00_主控台\信息图主控台.md`
- Share-code source: `信息图工作台\01_生产资产库\分享码主库.md`
- Prompt and IP source: `信息图工作台\01_生产资产库\提示词IP主库.md`
- Rotation ledger: `信息图工作台\01_生产资产库\资源轮转状态.md`
- Production template: `信息图工作台\02_生产模板\每日生产模板.md`
- Delivery and QA template: `信息图工作台\02_生产模板\交付与质检模板.md`
- Active production: `信息图工作台\03_每日生产中`
- Archive: `信息图工作台\04_交付归档`
- Historical material: `信息图工作台\90_历史资料`

## Priority Rules

1. The latest user instruction overrides older template wording about batch count.
2. Highest visual priority: sacrifice IP visuals, base labels, and decorative effects whenever needed to keep the main message clear, specific, and prominent.
3. Supported task types: 账号链接模式, 日常场景模式, 每日6套, 单套, 指定主题多套.
4. Account-link mode is account-based: research every account link in a browser/search before assigning topics and style; default is 3 sets per account unless the user specifies otherwise.
5. Daily/scenario mode is theme-based: the user must provide a theme or core scene before production.
6. Each set is 6-8 pages unless the user specifies a different page count.
7. Use only `分享码主库.md` for share codes.
8. Use only `提示词IP主库.md` for Prompt Codes, IP Codes, CTA modules, and style mappings.
9. Read `资源轮转状态.md` before selection and update it after delivery.
10. Do not use `90_历史资料` as a source for production resources unless the user explicitly asks for archive examples.

## Input Contract

Use this contract before planning. Ask for missing required fields when they cannot be safely inferred.

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

Required by mode:

- 账号链接模式: task type, account link(s), CTA or default CTA. Use account research to infer theme, target user, and core scenes if the user did not provide them.
- 日常场景模式 / 单套: task type, theme, core scene. Infer target user only when obvious.
- 每日6套: task type; use the six default theme pools, current resource rotation, and the user's default CTA.
- 指定主题多套: task type and theme list.

Never put input labels or raw planning text into visible image copy. Forbidden visible text includes "任务类型", "目标用户", "核心场景", "视觉要求", file names, `IP Code`, `Prompt Code`, and rotation wording.

## Main Content First

Apply this when drafting copy, prompts, QA, and retries:

- The largest visual elements should be the title, concrete scene, share code/action, and benefit.
- IP/base labels are optional accents only: small corner mark, thin line, subtle texture, or removed entirely.
- No IP/base label, badge, decoration, or character-like element may overlap or crowd the title, body copy, share codes, or CTA.
- Each page must answer at least three questions: what scene is this, what should the user do/copy, and what benefit does it bring.
- Replace vague claims with concrete scene language: "下车前提醒随身物", "右转低速打开盲区影像", "通勤前自动播报天气和路况".
- The page fails QA if users cannot tell what it is about within 3 seconds.

## Theme Pool

The workbench's default pools are:

- 安全守护: 语音播报, 安全提醒, 驾驶辅助, 门锁上下车
- 舒适座舱: 空调, 空气, 遮阳帘, 座椅, 方向盘, 乘坐舒适
- 出行效率: 出行模式, 动力能耗, 导航, 到达提醒, 驾驶模式
- 能源补能: 低电量, 充电完成, 长途模式, 能耗策略
- 娱乐氛围: 灯光, 氛围灯, 屏幕联动, 媒体, 仪式感
- 桌面与调音: 桌面大师组件, 桌面游戏, 调音大师

For multi-account batches, choose subtheme variants from these pools instead of duplicating the same exact topic across accounts. Each account gets 3 distinct set themes unless the researched account profile supports a focused series.

## Account Research Card

Create this before production:

```text
账号：
链接：
平台：
账号属性：
受众/痛点：
内容语气：
视觉风格：
适合的3套主题：
CTA策略：
风险边界：
调研依据：
```

If a link cannot be opened, search the account name or handle. If the account still cannot be inspected, ask for screenshots or a short positioning note.

## Scene Brief

Create this for daily/scenario production:

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

Scene briefs are internal planning notes. Do not copy the labels into the image.

## Production Directory Naming

Preferred full-batch directory:

```text
信息图工作台\03_每日生产中\YYYY-MM-DD_<账号数>账号各3套信息图\
```

Preferred single-account directory:

```text
信息图工作台\03_每日生产中\YYYY-MM-DD_<账号名>_3套信息图\
```

If the existing workspace already has a `YYYY-MM-DD_每日6套信息图`, `YYYY-MM-DD_随机N套信息图`, or fixed `三账号` directory for the same date, continue it only when the user asks to resume that batch. Otherwise create the account-count-based directory and note the naming difference.

Preferred daily/scenario directories:

```text
信息图工作台\03_每日生产中\YYYY-MM-DD_每日6套信息图\
信息图工作台\03_每日生产中\YYYY-MM-DD_<主题>信息图\
```

Each set directory should include:

```text
01_封面.png
02_总览.png
03_分享码页.png
04_分享码页.png
05_场景组合.png
06_尾页承接.png
发布信息.md
制作提示词.md
质检记录.md
```

Add pages 07-08 only when needed.

## Safety and Claims

- Do not write "官方推荐", "永久有效", "全车型通用", or similar unverified promises.
- Do not write the user's prompt, raw requirements, internal production notes, file names, Prompt Codes, IP Codes, or resource rotation status into visible image copy.
- Share-code availability depends on real vehicle import results.
- Automation reminders do not replace driver observation or safety judgment.
- Vehicle version, model, OTA, assisted driving, and compatibility claims need a risk boundary.

## Completion Record

After delivery, update `资源轮转状态.md` in this form:

```text
YYYY-MM-DD：
- 使用 IP：<IP Codes>
- 使用分享码：<all share codes shown in images or prompts>
- 任务类型：<账号链接模式 / 日常场景模式 / 每日6套 / 单套 / 指定主题多套>
- 账号：<账号名或账号编号；无则写无>
- 账号链接：<URL；无则写无>
- 主题/场景：<short theme and scene>
- 交付目录：<archive directory>
- 是否跨轮：否 / 是，原因
```
