# Goal Mode

Goal Mode 是这个仓库的使用方式：先定义目标，再选择 skill。

它避免把 AI 协作变成“试提示词”。每次开始前，先把任务压成四个问题：

1. 我要达成什么结果？
2. 我已经有什么输入？
3. 我需要什么输出？
4. 我怎么验证它完成了？

## Goal Card

可以用这张卡片快速描述任务：

```text
Goal：
输入：
期望输出：
目标用户：
限制条件：
验证方式：
推荐 skill：
```

示例：

```text
Goal：把一批素材剪成 60 秒横屏视频
输入：视频素材目录、口播稿、BGM、目标时长
期望输出：MP4 成片、render-plan、验证报告
目标用户：小红书/视频号观众
限制条件：不覆盖原素材，字幕必须可读
验证方式：输出文件存在、大小非零、时长在容差内
推荐 skill：$auto-render-video
```

## Goal Routing

| 目标类型 | 优先 skill | 备选 skill |
| --- | --- | --- |
| 自动剪辑需求整理 | `$auto-cutting-prd` | `$auto-cutting` |
| 自动剪辑直接成片 | `$auto-render-video` | `$auto-cutting` |
| 自动剪辑工程执行 | `$auto-cutting-ralph` | `$ralph-runner` |
| 理想车主信息图 | `$li-info` | `$li-auto-infographic-suite` |
| 极简分享码信息图 | `$li-auto-minimal-infographic` | `$li-info` |
| 长文写作和改稿 | `$happy-writer` | `$clean-code` 用于文档收尾 |
| 前端产品体验 | `$frontend-design` | `$open-design` |
| 设计产物生成 | `$open-design` | `$frontend-design` |
| 代码质量收尾 | `$clean-code` | `$ralph-runner` |
| Markdown PRD 执行 | `$ralph-runner` | `$clean-code` |

## Output Standard

每个目标完成时都应该能回答：

- 改了什么？
- 为什么这样做？
- 核心流程是什么？
- 哪些边界被处理？
- 如何验证？
- 还有什么风险？

这也是 ChenShuo Skills 的默认交付标准。
