# ChenShuo Skills

![ChenShuo Skills cover](assets/chenshuo-skills-cover.png)

ChenShuo Skills 是我在真实项目里沉淀的一组 AI Agent 工作流。

这个仓库不追求把提示词堆满，而是把能反复使用、能交付结果、能验证质量的工作流整理成可安装的 skill。每个 skill 都围绕一个明确目标设计：先理解业务，再执行动作，最后给出可检查的结果。

当前状态：首版 13 个 skill 已发布。

## Goal Mode

Goal Mode 的用法很简单：先说目标，再选 skill。

如果你的工具界面没有可用的 Goal UI，不需要点任何平台按钮。直接安装并调用 `$goal-mode`，它会在对话里帮你填写任务卡。

不要先问“我该用哪个提示词”，而是先问：

```text
我现在想达成什么结果？
输入是什么？
输出应该长什么样？
怎么验证它真的完成了？
```

然后按目标选择入口：

| Goal | 使用入口 | 适合场景 | 产出 |
| --- | --- | --- | --- |
| 不知道该用哪个 skill | `$goal-mode` | 意图还不清楚、需要先规划、需要路由到合适 skill | 任务卡、推荐 skill、下一步 prompt |
| 把自动剪辑想法变成可执行方案 | `$auto-cutting-prd` | 有视频想法，但还没有需求文档、剪辑方案或 Ralph PRD | Markdown 需求、剪辑计划、PRD 草案 |
| 直接剪辑并导出视频 | `$auto-render-video` | 已有素材、脚本、字幕或 render-plan，希望直接生成 MP4 | 成片、渲染计划、验证报告 |
| 跑完整自动剪辑工程闭环 | `$auto-cutting-ralph` | 想把自动剪辑需求交给 Ralph/Codex dry-run 执行 | Ralph PRD、dry-run 结果、日志路径 |
| 做理想车主信息图 | `$li-info` | 想快速生成理想车主信息图、分享码图、账号运营图 | 页面文案、生成提示词、质检记录 |
| 做完整理想信息图批量生产 | `$li-auto-infographic-suite` | 多账号、多套图、资源轮转、归档、发布信息 | 批量套图工作流与交付文件 |
| 做极简分享码信息图 | `$li-auto-minimal-infographic` | 需要更轻、更清晰的分享码信息图 | 极简信息图方案与页面提示 |
| 写文章或改稿 | `$happy-writer` | 项目复盘、工具体验、公众号长文、内容改写 | 陈硕风格文章、提纲、角度建议 |
| 清理代码和交付状态 | `$clean-code` | 代码重构、review、文档同步、交付收尾 | 修复建议、代码整理、验证结果 |
| 设计或评审前端体验 | `$frontend-design` | Web app、后台、仪表盘、工具界面、落地页 | 前端实现建议、UI 约束、验证清单 |
| 使用 Open Design 做设计产物 | `$open-design` | HTML 原型、Dashboard、移动端、幻灯片、设计系统 | Open Design 产物路径与执行步骤 |
| 把 Markdown 需求跑成 Ralph PRD | `$ralph-runner` | 已有需求文档，想跑安全 dry-run 构建 | PRD JSON、overview、dry-run 输出 |

## 快速安装

在支持安装 GitHub skill 的 AI 编程工具里使用：

```text
帮我安装这个 skill：https://github.com/ChenShuo2004/chenshuo-skills/tree/main/<skill-name>
```

例如：

```text
帮我安装这个 skill：https://github.com/ChenShuo2004/chenshuo-skills/tree/main/happy-writer
```

```text
帮我安装这个 skill：https://github.com/ChenShuo2004/chenshuo-skills/tree/main/clean-code
```

如果你只是想先填写任务卡：

```text
帮我安装这个 skill：https://github.com/ChenShuo2004/chenshuo-skills/tree/main/goal-mode
```

## Skill Map

### 自动剪辑

- `auto-cutting`：自动剪辑主入口，负责规划、生成、渲染、验证。
- `auto-cutting-prd`：把想法整理成需求文档、剪辑方案或 Ralph PRD。
- `auto-cutting-ralph`：把自动剪辑需求拆成 Ralph PRD 并跑 dry-run。
- `auto-render-video`：根据素材和 render-plan 直接剪辑、渲染、验证 MP4。

### 内容与信息图

- `happy-writer`：把真实项目素材写成温暖、实用、好奇心驱动的陈硕风格内容。
- `li-auto-infographic-suite`：理想车主信息图套图生产、QA、归档和发布工作流。
- `li-auto-minimal-infographic`：理想车主极简分享码信息图工作流。
- `li-info`：理想信息图短命令入口。

### 设计、工程与执行

- `goal-mode`：目标澄清和 skill 路由入口。
- `frontend-design`：前端产品设计、实现和评审的质检层。
- `open-design`：连接本地 Open Design 项目，生成设计产物。
- `ralph-runner`：把 Markdown 需求转成 Ralph PRD 并执行安全 dry-run。
- `clean-code`：围绕需求、业务流程、文档同步和验证结果做工程收尾。

## 仓库结构

```text
chenshuo-skills/
  README.md
  LICENSE
  assets/
    chenshuo-skills-cover.png
  docs/
    goal-mode.md
    repository-plan.md
    skill-inventory.md
  auto-cutting/
  auto-cutting-prd/
  auto-cutting-ralph/
  auto-render-video/
  clean-code/
  frontend-design/
  goal-mode/
  happy-writer/
  li-auto-infographic-suite/
  li-auto-minimal-infographic/
  li-info/
  open-design/
  ralph-runner/
```

每个 skill 都尽量保持自包含：

- `SKILL.md`：核心触发说明和工作流。
- `agents/openai.yaml`：UI 展示文案和默认 prompt。
- `references/`：需要时再读取的详细规则。
- `assets/`：模板或生成所需资源。
- `scripts/`：可重复执行的确定性脚本。

## 维护原则

1. 只保留真实项目里有用的工作流。
2. 每个 skill 必须有明确 goal、输入、输出和验证方式。
3. `SKILL.md` 保持短而可触发，复杂规则放到 `references/`。
4. 不写死个人本机路径、账号信息、私有资料或不可公开链接。
5. 新增 skill 前先问：它解决的是一个稳定目标，还是一次性提示词？

## 发布信息

仓库地址：[ChenShuo2004/chenshuo-skills](https://github.com/ChenShuo2004/chenshuo-skills)

首版已完成：

1. 发布 13 个核心/入口/基础设施 skill。
2. 添加仓库封面图。
3. 补齐 `LICENSE` 和 `.gitignore`。
4. 校验所有 `SKILL.md` frontmatter。
5. 清理本机绝对路径和敏感信息。
