# 自动剪辑流程参考

## 需求字段

实现前尽量收集这些字段：

- 业务目标：视频类型、目标平台、受众、目标时长、画幅比例、语言。
- 输入来源：素材目录、文件命名规则、脚本文案、字幕文件、BGM、封面、已有草稿路径。
- 输出产物：方案 JSON、剪映/CapCut 草稿、渲染视频、验证报告。
- 剪辑风格：节奏、开场、结尾、转场、字幕样式、品牌叠加层、音量规则。
- 约束条件：受保护文件、允许输出目录、依赖策略、导出格式。
- 验收标准：时长容差、必需素材、验证命令、人工复核步骤。

## 推荐数据模型

优先使用结构化数据，不要依赖临时拼接文本：

```json
{
  "project": "auto-cutting-demo",
  "outputMode": "draft",
  "target": {
    "durationSec": 60,
    "durationToleranceSec": 5,
    "aspectRatio": "9:16",
    "language": "zh-CN"
  },
  "inputs": {
    "materialsDir": "path/to/materials",
    "scriptPath": "path/to/script.md",
    "subtitlePath": null,
    "bgmPath": null
  },
  "timeline": [
    {
      "source": "clip001.mp4",
      "inSec": 1.2,
      "outSec": 6.8,
      "role": "hook",
      "caption": "开场钩子"
    }
  ]
}
```

## 直接渲染计划

当用户要求直接剪辑视频时，使用 `assets/render-plan-template.json` 作为最小可执行计划。核心字段：

- `output`：最终 mp4 输出路径，必须写到新位置。
- `target`：统一输出画布，包含 `width`、`height`、`fps`、`crf`、`preset`。
- `clips`：按顺序排列的视频片段，每个片段必须有 `source`、`inSec`，并提供 `outSec` 或 `durationSec`。
- `bgm`：可选，包含 `source` 和 `volume`，用于把背景音乐混入原声。
- `subtitles`：可选，当前支持 SRT 文件烧录到画面。
- `report`：验证报告路径。

没有项目内渲染链路时，运行 `scripts/render_plan_ffmpeg.py`。在 Windows 上优先用 `py -3` 执行；如果 FFmpeg 不在 PATH 中，通过脚本参数传入 `--ffmpeg` 和 `--ffprobe`。它适合裁剪、拼接、统一画幅、BGM 混音、SRT 字幕烧录；不适合剪映专属模板、花字和素材库强绑定效果。

## 边界情况

- 素材文件缺失或被重命名。
- 混合画幅、手机竖拍旋转信息、横竖屏混剪。
- 可变帧率视频。
- 静音片段、多音轨或音频不可用。
- 字幕过长，超出移动端安全区域。
- 目标时长短于脚本必需表达内容。
- 现有草稿 schema 版本不匹配。
- Windows 路径包含中文、空格或特殊字符。

## 校验建议

- 优先使用项目已有媒体探测工具；没有时再考虑 FFmpeg。
- 快速校验 JSON 时，可使用项目运行时或 PowerShell `ConvertFrom-Json`。
- 如果生成草稿，声明完成前必须解析所有生成的草稿 JSON。
- 如果生成视频，检查文件存在、大小非零、时长、分辨率、容器信息和可播放性。
- 如果使用 `scripts/render_plan_ffmpeg.py`，先用 `--check-only` 验证计划和素材路径，再正式渲染。
- 在输出产物附近保留验证报告，例如 `output/auto-cutting-report.json`。

## Ralph Story 拆分

好的 Ralph story 应该小而可测：

- `US-001` 素材清单：扫描输入并生成 manifest。
- `US-002` 元数据探测：补充时长、分辨率、帧率、音轨信息。
- `US-003` 剪辑规划：根据脚本和素材清单生成时间线。
- `US-004` 输出写入：创建草稿、渲染文件或方案 JSON，不触碰原始文件。
- `US-005` 验证报告：报告缺失素材、时间线错误、时长偏差和输出产物状态。
