---
name: goal-mode
description: |
  Use when the user wants to set, clarify, or route a goal before choosing another ChenShuo skill. Trigger for "$goal-mode", "goal mode", "设置目标", "无法设置目标", "帮我选 skill", "不知道用哪个 skill", "先规划目标", or any request where the user's goal, inputs, expected output, constraints, validation, or best skill route is unclear. This skill turns vague intent into a Goal Card and recommends the next skill.
---

# Goal Mode

## Purpose

Use this skill as the goal-setting entrypoint for ChenShuo Skills.

Some tools do not have a real "set goal" UI. That is fine. Goal Mode works inside the conversation: ask the right questions, fill a Goal Card, then route to the best skill.

## When To Use

- The user says they cannot set a goal in Goal Mode.
- The user wants to start from an outcome, not from a specific skill name.
- The user is unsure whether to use `happy-writer`, `clean-code`, `auto-render-video`, `li-info`, or another skill.
- The request is vague and needs goal, input, output, constraints, or validation clarified first.
- The user asks for planning before execution.

Do not use this skill when the user already named a specific skill and gave enough input to proceed.

## Goal Card

Always try to produce this card:

```text
Goal:
Inputs:
Expected output:
Audience/user:
Constraints:
Validation:
Recommended skill:
Next action:
```

If some fields are missing but safe to infer, fill them and mark assumptions. If critical fields are missing, ask only the minimum questions needed to proceed.

## Workflow

1. Restate the user's rough intent in one sentence.
2. Identify missing fields in the Goal Card.
3. Ask up to three concise questions only when the missing fields block routing.
4. Recommend one primary skill and, when helpful, one fallback skill.
5. Provide a ready-to-send prompt that invokes the recommended skill.

## Routing Rules

| User goal | Primary skill | Fallback |
| --- | --- | --- |
| Clarify or route an unclear goal | `$goal-mode` | none |
| Automatic video editing idea to plan | `$auto-cutting-prd` | `$auto-cutting` |
| Direct video rendering | `$auto-render-video` | `$auto-cutting` |
| Automatic video editing dry-run build | `$auto-cutting-ralph` | `$ralph-runner` |
| Li Auto infographic quick task | `$li-info` | `$li-auto-infographic-suite` |
| Minimal share-code infographic | `$li-auto-minimal-infographic` | `$li-info` |
| Long-form writing or rewrite | `$happy-writer` | none |
| Code cleanup or handoff | `$clean-code` | none |
| Frontend UI design or review | `$frontend-design` | `$open-design` |
| Open Design artifact generation | `$open-design` | `$frontend-design` |
| Markdown PRD to Ralph dry-run | `$ralph-runner` | `$clean-code` |

## Ready Prompt Format

After routing, output a prompt like:

```text
使用 $<skill-name>：

Goal:
Inputs:
Expected output:
Audience/user:
Constraints:
Validation:
```

The user can paste that prompt into the next message, or Codex can continue directly if the user asked to proceed.

## Boundaries

- Do not pretend Goal Mode is a platform UI switch.
- Do not force the user to fill every field when the next step is obvious.
- Do not ask broad questionnaires. Ask the smallest useful question.
- Do not execute the downstream task unless the user asked to continue after goal routing.
