# ChenShuo Skills 仓库规划

## 需求理解

目标是把当前本机已经沉淀的个人 skills，整理成一个可维护、可安装、可分享的 `ChenShuo Skills` GitHub 仓库。

这次先做文档和规划，不迁移源码、不创建远程仓库、不推送。

## 参考设计

参考仓库：[KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills)

它的核心设计可以概括为：

1. 根目录就是可安装 skill 目录，安装 URL 简单直接。
2. README 用人话解释每个 skill 适合什么、不适合什么、会做什么。
3. skill 和 prompt 分开，避免把可安装工作流和一次性提示词混在一起。
4. 仓库介绍强调“自己每天在用，跑通后再开源”，可信度来自真实使用。
5. 单个 skill 内部保持自包含，复杂方法论放进 `references/`，可执行工具放进 `scripts/`。

ChenShuo Skills 可以沿用这个骨架，但表达上更突出你的个人工作流：

- 自动剪辑工作流
- 理想车主信息图内容生产
- Open Design / Ralph 这类可复用执行底座
- 后续再补 prompts 或案例

## 仓库定位

一句话定位：

> ChenShuo Skills 是陈硕在真实项目里沉淀的 AI Agent 工作流集合，覆盖自动剪辑、内容运营信息图、设计产出和 PRD 执行闭环。

对外可以更简单：

> 我自己每天在项目里用的一些 AI Skills，跑通了就整理出来。

## 推荐仓库名

推荐：`chenshuo-skills`

原因：

- URL 清晰：`github.com/ChenShuo2004/chenshuo-skills`
- 全小写、短横线，适合作为安装 URL。
- 和 `Khazix Skills` 的命名方式一致，但不会混淆品牌归属。

备选：

- `ChenShuo-Skills`：展示名更好看，但 URL 大小写不稳定。
- `cs-skills`：短，但不够直观。
- `agent-skills`：太泛，缺少个人识别度。

## 目录设计

推荐首版：

```text
chenshuo-skills/
  README.md
  LICENSE
  docs/
    repository-plan.md
    skill-inventory.md
  prompts/
  auto-cutting/
  auto-cutting-prd/
  auto-cutting-ralph/
  auto-render-video/
  clean-code/
  frontend-design/
  happy-writer/
  li-auto-infographic-suite/
  li-auto-minimal-infographic/
  li-info/
  open-design/
  ralph-runner/
```

说明：

- skill 目录放在根目录，方便用户直接安装。
- `docs/` 只放仓库级规划、盘点、维护说明，不放到具体 skill 内部。
- `prompts/` 暂时保留空位，等有稳定 prompt 再放。
- 暂不放 `third-party/`，避免首版范围变复杂。

## 首版迁移清单

### P0：必须迁移

1. `auto-cutting`
2. `auto-cutting-prd`
3. `auto-cutting-ralph`
4. `auto-render-video`
5. `clean-code`
6. `happy-writer`
7. `li-auto-infographic-suite`
8. `li-auto-minimal-infographic`
9. `li-info`
10. `frontend-design`
11. `open-design`
12. `ralph-runner`

### P1：待确认后迁移

暂无。`frontend-design` 已优化成前端产品设计与实现质检 skill，建议进入首版。

### 暂不迁移

1. `khazix-writer`
2. `neat-freak`
3. `doc`
4. `pdf`
5. `playwright`

原因：

- `khazix-writer` 和 `neat-freak` 是上游参考或第三方强关联 skill。
- 它们已经分别转化为原创 `happy-writer` 和 `clean-code`，原始版本不直接混入首版。
- `doc`、`pdf`、`playwright` 是通用依赖，不是 ChenShuo 个人工作流本体。

## 单个 Skill 的发布标准

每个 skill 迁移前检查：

1. `SKILL.md` 有合法 frontmatter：`name` 和 `description`。
2. `description` 触发语明确，不要只写“这个 skill 用于某某任务”。
3. `SKILL.md` 不超过必要长度，详细方法论放 `references/`。
4. `agents/openai.yaml` 存在，且 `display_name`、`short_description`、`default_prompt` 与 `SKILL.md` 一致。
5. `references/` 中没有隐私信息、账号信息、客户信息、不可公开链接。
6. `scripts/` 可在干净环境中运行，不能写死本机绝对路径。
7. `assets/` 只放真正需要随 skill 分发的模板或素材。
8. 安装 URL 指向该 skill 目录时，用户能理解怎么触发。

## GitHub 发布流程

建议流程：

1. 在本地当前目录初始化仓库。
2. 复制 P0 skill 目录。
3. 做一次内容审查：隐私、路径、许可证、触发语、README 描述。
4. 本地提交：`docs: plan ChenShuo skills repository`，然后 `feat: add initial skills`。
5. 创建远程仓库 `ChenShuo2004/chenshuo-skills`。
6. 推送到 `main`。
7. 在 GitHub README 检查安装链接是否可点。
8. 用一个新 Codex/Claude 会话测试安装 URL 和触发语。

## 风险和待确认

1. 仓库公开还是私有：公开便于分享，私有更安全。
2. `frontend-design` 后续是否需要补充示例：目前已经可用，但还没有绑定具体案例或视觉样张。
3. `clean-code` 和 `happy-writer` 后续需要用真实任务验证触发语和输出边界。
4. 理想信息图相关内容是否可公开：需要检查 references 是否包含敏感运营资料。
5. 自动剪辑脚本是否可开源：需要检查脚本依赖、素材路径、模板内容。
6. 许可证：建议 MIT，但第三方内容不能混在原创 MIT 范围里。
7. 是否需要英文 README：首版可以先不做，等结构稳定后再补。
