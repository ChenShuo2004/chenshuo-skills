# ChenShuo Skills

![ChenShuo Skills cover](assets/chenshuo-skills-cover.png)

我自己沉淀的一组 AI Agent Skills 和工作流说明。

这个仓库的目标不是把所有提示词都堆在一起，而是把已经在真实项目里跑通过、能复用、能交付结果的工作流整理成可安装、可维护的 skill。

当前状态：首版 skill 已整理，准备发布到 GitHub。

设计参考：[KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills)。参考点主要是：根目录直接放可安装 skill、README 先讲清楚每个 skill 解决什么问题、安装方式足够简单、每个 skill 保持自包含。

## 首版范围

### 核心 Skills

| Skill | 中文名 | 用途 | 首版定位 |
| --- | --- | --- | --- |
| `auto-cutting` | 自动剪辑 | 规划、生成、渲染、验证自动剪辑流程，覆盖剪映/Jianying/CapCut 草稿、素材扫描、时间线、字幕、BGM、导出校验 | 核心 |
| `auto-cutting-prd` | 自动剪辑 PRD | 把自动剪辑想法整理成需求文档、剪辑方案或 Ralph PRD | 入口/轻量版 |
| `auto-cutting-ralph` | 自动剪辑 Ralph | 从需求到 Ralph PRD、dry-run、生成计划、验证反馈的完整闭环 | 工作流闭环 |
| `auto-render-video` | 自动成片 | 根据素材和剪辑计划直接裁剪、拼接、字幕、混音、导出 MP4 | 执行型 |
| `clean-code` | 代码洁癖 | 按需求、业务流程、文档同步和验证结果清理代码与交付状态 | 工程质量 |
| `happy-writer` | 快乐写作 | 把真实项目素材写成陈硕风格的温暖、实用、好奇心驱动内容 | 内容创作 |
| `li-auto-infographic-suite` | 理想信息图套图 | 从账号链接、日常场景、分享码和 Prompt Code 生成理想车主信息图套图 | 核心 |
| `li-auto-minimal-infographic` | 理想极简信息图 | 面向理想车主极简分享码信息图，含提问、生成、质检与归档 | 核心 |
| `li-info` | 理想信息图短命令 | 用 `$li-info` 快速触发理想信息图工作流 | 入口别名 |
| `frontend-design` | 前端产品设计 | 指导 Codex 设计、实现、评审和验证用户可见的前端界面 | 设计基础设施 |
| `open-design` | Open Design | 使用本地 Open Design 项目做 artifact-first 设计工作流 | 设计基础设施 |
| `ralph-runner` | Ralph Runner | 把 Markdown 需求转成 Ralph PRD，并运行安全的 Ralph/Codex 构建流程 | 执行基础设施 |

### 参考来源与通用依赖

| Skill | 当前判断 | 处理方式 |
| --- | --- | --- |
| `khazix-writer` | 已参考其写作工作流结构，转化为原创 `happy-writer` | 原始版本不直接迁移 |
| `neat-freak` | 已参考其收尾审查结构，转化为原创 `clean-code` | 原始版本不直接迁移 |
| `doc` / `pdf` / `playwright` | 通用能力包 | 更适合写在依赖说明中，不纳入个人原创目录 |

## 建议仓库结构

为了让安装 URL 简单，首版建议沿用卡兹克仓库的根目录 skill 结构：

```text
chenshuo-skills/
  README.md
  LICENSE
  assets/
    chenshuo-skills-cover.png
  docs/
    repository-plan.md
    skill-inventory.md
  prompts/
  auto-cutting/
    SKILL.md
    agents/openai.yaml
    assets/
    references/
    scripts/
  auto-cutting-prd/
    SKILL.md
    agents/openai.yaml
  auto-cutting-ralph/
    SKILL.md
    agents/openai.yaml
  auto-render-video/
    SKILL.md
    agents/openai.yaml
  clean-code/
    SKILL.md
    agents/openai.yaml
    references/
  happy-writer/
    SKILL.md
    agents/openai.yaml
    references/
  li-auto-infographic-suite/
    SKILL.md
    agents/openai.yaml
    references/
  li-auto-minimal-infographic/
    SKILL.md
    agents/openai.yaml
    references/
  li-info/
    SKILL.md
    agents/openai.yaml
  frontend-design/
    SKILL.md
    agents/openai.yaml
  open-design/
    SKILL.md
    agents/openai.yaml
    references/
  ralph-runner/
    SKILL.md
    agents/openai.yaml
    references/
```

后续安装方式预计是：

```text
帮我安装这个 skill：https://github.com/ChenShuo2004/chenshuo-skills/tree/main/<skill-name>
```

例如：

```text
帮我安装这个 skill：https://github.com/ChenShuo2004/chenshuo-skills/tree/main/auto-cutting
```

## 迁移原则

1. 只迁移已经在真实项目里跑通过的 skill。
2. 每个 skill 保持自包含，必要资源放在自己的 `references/`、`scripts/`、`assets/` 下。
3. `SKILL.md` 保持短、准、可触发；详细方法论放到 `references/`。
4. `agents/openai.yaml` 必须和 `SKILL.md` 保持一致。
5. 第三方或上游 skill 不混入原创清单，除非明确保留来源、许可证和修改说明。
6. 首版先保证安装、触发、验证路径通顺，不做过度包装。

## 下一步

1. 确认仓库名：推荐 `chenshuo-skills`。
2. 确认仓库可见性：公开更利于分享，私有更适合未整理完的工作流。
3. 逐个检查 `SKILL.md` frontmatter、`agents/openai.yaml`、资源引用和触发语。
4. 创建 GitHub 仓库 `ChenShuo2004/chenshuo-skills` 并推送。
5. 用一个新会话测试安装 URL 和触发语。
