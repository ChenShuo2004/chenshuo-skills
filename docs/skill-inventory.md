# Skill 盘点

盘点日期：2026-05-25

来源目录：本机 Codex skills 目录。

当前工作目录原本为空，本文件用于规划未来的 ChenShuo Skills 仓库，不会修改原始 skill。

## 总览

| Skill | 行数 | references | scripts | assets | agents/openai.yaml | 更新时间 | 归类 |
| --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| `auto-cutting` | 79 | 2 | 1 | 3 | 有 | 2026-05-21 20:42 | 原创核心 |
| `auto-cutting-prd` | 20 | 0 | 0 | 0 | 有 | 2026-05-21 20:54 | 原创入口 |
| `auto-cutting-ralph` | 22 | 0 | 0 | 0 | 有 | 2026-05-21 20:54 | 原创闭环 |
| `auto-render-video` | 24 | 0 | 0 | 0 | 有 | 2026-05-21 20:54 | 原创执行 |
| `clean-code` | 71 | 1 | 0 | 0 | 有 | 2026-05-25 17:35 | 原创工程质量 |
| `doc` | 65 | 0 | 1 | 2 | 有 | 2026-04-30 11:58 | 通用依赖 |
| `frontend-design` | 75 | 0 | 0 | 0 | 有 | 2026-05-25 17:31 | 原创设计基础设施 |
| `happy-writer` | 75 | 1 | 0 | 0 | 有 | 2026-05-25 17:35 | 原创内容创作 |
| `khazix-writer` | 282 | 2 | 0 | 0 | 无 | 2026-05-25 17:06 | 上游参考 |
| `li-auto-infographic-suite` | 172 | 1 | 0 | 0 | 有 | 2026-05-16 15:26 | 原创核心 |
| `li-auto-minimal-infographic` | 159 | 1 | 0 | 0 | 有 | 2026-05-22 21:15 | 原创核心 |
| `li-info` | 40 | 0 | 0 | 0 | 有 | 2026-05-21 20:53 | 原创入口 |
| `neat-freak` | 143 | 2 | 0 | 0 | 无 | 2026-05-25 17:06 | 上游参考 |
| `open-design` | 74 | 1 | 0 | 0 | 有 | 2026-05-21 20:50 | 原创基础设施 |
| `pdf` | 54 | 0 | 0 | 1 | 有 | 2026-04-30 11:58 | 通用依赖 |
| `playwright` | 105 | 2 | 1 | 2 | 有 | 2026-04-30 11:58 | 通用依赖 |
| `ralph-runner` | 216 | 2 | 0 | 0 | 有 | 2026-05-21 09:02 | 原创基础设施 |

## 建议纳入首版

### 自动剪辑组

这组是当前最完整的个人工作流，已经形成“需求整理 -> PRD -> Ralph 执行 -> 渲染验证”的链路。

- `auto-cutting`：主 skill，覆盖自动剪辑规划、实现、渲染和验证。
- `auto-cutting-prd`：把想法变成需求文档或 Ralph PRD。
- `auto-cutting-ralph`：串起 Ralph PRD、dry-run、生成计划和反馈。
- `auto-render-video`：直接执行剪辑、拼接、字幕、混音和 MP4 导出。

建议处理：

- 保留四个 skill，但在 README 里讲清楚它们的层级关系。
- 检查 `auto-cutting` 的 `scripts/render_plan_ffmpeg.py` 是否包含本机路径或项目私有路径。
- 检查 `assets/ralph-prd-template.json`、`assets/render-plan-template.json`、`assets/requirements-template.md` 是否适合公开。

### 理想信息图组

这组面向理想汽车车主内容生产，已经有核心套件、极简分享码版本和短命令入口。

- `li-auto-infographic-suite`：完整套图生产、QA、归档和发布工作流。
- `li-auto-minimal-infographic`：极简分享码信息图工作流。
- `li-info`：短触发入口。

建议处理：

- 首版保留三者，但把 `li-info` 明确标注为入口别名，不把它说成独立产品。
- 检查 references 中是否包含账号私密信息、投放策略、客户资料或不能公开的链接。
- README 中避免写成“理想官方工具”，定位为车主内容运营工作流。

### 设计和执行基础设施

- `open-design`：把本地 Open Design 项目接入 artifact-first 设计工作流。
- `ralph-runner`：把 Markdown PRD 转成 Ralph 可执行流程。
- `frontend-design`：前端产品设计与实现质检 skill，用于指导 Codex 设计、实现、评审和验证用户可见界面。
- `clean-code`：从需求、业务流程、代码质量、文档同步和验证结果五层做工程收尾。
- `happy-writer`：把真实项目素材转成陈硕风格的温暖、实用、好奇心驱动内容。

建议处理：

- `open-design` 和 `ralph-runner` 可作为 ChenShuo 工作流底座。
- `frontend-design` 已补强触发边界、业务流程理解、控件选择、布局约束、交互状态和验证要求，建议纳入首版。
- `clean-code` 和 `happy-writer` 已基于上游参考重新写成原创 skill，避免直接搬运第三方个人风格。

## 不建议作为原创首版发布

### 上游参考

- `khazix-writer`：来自或强关联“数字生命卡兹克”的个人写作风格 skill。已作为结构参考转化为原创 `happy-writer`，原始版本不直接发布。
- `neat-freak`：卡兹克仓库中也有同名 skill。已作为结构参考转化为原创 `clean-code`，原始版本不直接发布。

处理建议：

- README 可以写“设计参考”，链接到上游仓库。
- 不把它们放入首版原创目录。
- 如果未来要收录，建议放在 `third-party/` 或单独 fork，并保留许可证、来源、修改记录。

### 通用依赖

- `doc`
- `pdf`
- `playwright`

处理建议：

- 不放入首版个人 skill 清单。
- 在具体 skill 的依赖说明中提及即可。
- 如果确实需要随仓库分发，应先确认来源许可证。

## 发现的问题

1. 原始 `khazix-writer` 和 `neat-freak` 当前没有 `agents/openai.yaml`，但它们不再作为首版直接迁移对象。
2. `auto-cutting` 有脚本和模板资产，迁移前需要做一次路径、隐私和可公开性检查。
3. 理想信息图相关 references 可能包含运营细节，公开前需要人工确认。
4. `clean-code` 和 `happy-writer` 已有首版，但还需要后续用真实任务验证触发边界。
5. 当前 GitHub 账号 `ChenShuo2004` 下未发现 `chenshuo-skills` 仓库。
6. GitHub 连接器当前只能列仓库，没有直接创建仓库能力；后续创建可能需要用 `gh` CLI 或你先在 GitHub 创建空仓库。
