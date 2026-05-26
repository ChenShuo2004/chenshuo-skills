---
name: ending-time
description: |
  Use when the user wants to finish, ship, publish, commit, push, create a release handoff, deploy to Vercel, or turn implemented page/function work into a verified GitHub + Vercel delivery. Trigger for "收尾", "提交到 GitHub", "部署到 Vercel", "发布上线", "对应的页面和功能实现", "ship it", "finish this", or any request where implementation, verification, git scope, GitHub push, and Vercel deployment must close as one workflow.
---

# Ending Time

## Purpose

Use this skill as the final-mile delivery workflow for web and app projects.

The goal is to turn a requested page or feature into a verified delivery: requirements understood, implementation scoped, checks run, Git history clean, GitHub updated, Vercel deployment verified, and the user left with exact links and remaining risks.

## When To Use

- The user asks to implement a page or function and publish it.
- The user asks to commit, push, submit to GitHub, deploy to Vercel, or make a change live.
- The work is already implemented but needs a reliable finish: validation, commit, push, deploy, and handoff.
- The user says "收尾", "上线", "发布", "部署", "提交 GitHub", "Vercel", "对应页面和功能实现", or "一键使用".

Do not use this skill for pure planning, pure code review, or non-Git/non-Vercel delivery unless the user explicitly asks for this finish-line workflow.

## Core Rules

- Requirements first: read `README`, `AGENTS.md`, product docs, page docs, issue notes, or deployment docs before changing code.
- Scope before staging: inspect `git status` and relevant diffs. Never stage unrelated user changes silently.
- Small edits: implement only the requested page/function/deploy support. Avoid unrelated refactors.
- Verify before publishing: do not commit or deploy a broken build unless the user explicitly accepts that state.
- GitHub and Vercel are output surfaces, not substitutes for local validation.
- Keep secrets out of Git. Never commit `.env`, `.env.local`, tokens, project auth files, or local cache/output directories.

## Workflow

1. Orient in the repo.
   - Confirm the current working directory and Git remote.
   - Read the nearest project instructions: `AGENTS.md`, `README.md`, `docs/`, PRD files, page docs, and deploy notes.
   - Identify the framework, package manager, build command, test command, and Vercel config.

2. Restate the delivery target.
   - User goal.
   - Inputs and expected output.
   - Pages, routes, APIs, data files, or deployment config affected.
   - Assumptions and unclear requirements.

3. Plan briefly before editing.
   - List the smallest useful implementation steps.
   - Note public contracts that could be affected: routes, schemas, environment variables, permissions, data shape, or state flow.

4. Implement the requested work.
   - Follow existing project patterns, components, names, and styling.
   - Update docs when behavior, commands, env vars, routes, or deployment steps changed.
   - For frontend work, verify the real page when a browser/dev server is available.

5. Verify locally.
   - Prefer project scripts such as `npm.cmd run build`, `npm.cmd test`, `npm.cmd run lint`, `pnpm build`, `yarn build`, or repo-specific checks.
   - If scripts are missing, inspect package files and run the nearest meaningful check.
   - If verification is blocked by auth, missing env vars, external services, or local tooling, say exactly what is blocked.

6. Prepare Git.
   - Run `git status --short --branch`.
   - Inspect diffs for changed files that will be staged.
   - If the worktree is mixed, stage explicit files only.
   - If on `main`, `master`, or a protected/default branch and the user did not ask for direct commit, create a branch named `codex/<short-purpose>`.
   - Commit with a concise message that describes the delivered behavior.

7. Push to GitHub.
   - Push the current branch with tracking.
   - If the user asks for a PR, create one after push and include validation in the PR body.
   - If the user asks for direct production delivery and the repo normally deploys from the pushed branch, confirm the branch/deploy relationship.

8. Deploy with Vercel.
   - Prefer the repo's existing GitHub-to-Vercel integration when it is configured and the pushed branch is expected to deploy.
   - Use Vercel CLI as fallback or when the user asks for immediate production deployment: `vercel --prod`.
   - If `.vercel/project.json` exists, confirm the linked project name before deployment.
   - If Vercel auth or project linking is missing, stop before guessing and report the exact command or dashboard action needed.

9. Verify the live result.
   - Capture the deployment URL.
   - Inspect Vercel output or deployment status.
   - Open or request-check the relevant route when possible.
   - Confirm SPA rewrites, asset loading, API routes, and key page flows for the changed surface.

10. Report in the user's preferred closeout format.

## Git Safety

- Do not run `git add -A` when unrelated files exist.
- Do not rewrite history, reset, force-push, or delete branches unless the user explicitly asks.
- Do not commit generated dependency folders, build output, logs, local browser caches, or secrets unless the repo intentionally tracks them.
- If pre-existing changes are present, work with them. Do not revert them.
- If a deploy requires environment variable changes, explain the required variables and where they must be configured.

## Vercel Checks

Look for these signals before deploying:

- `vercel.json`
- `.vercel/project.json`
- `.vercelignore`
- framework config such as Vite, Next.js, Remix, Astro, or SvelteKit
- build output expectations such as `dist`, `.next`, `out`, or `build`
- required environment variables from `.env.example`, docs, or runtime errors

For Vite SPA projects, ensure route refreshes are covered by rewrites, usually through `vercel.json`.

## Output Format

Use this format after completing work:

```markdown
### 需求理解
...

### 实现方案
...

### 关键逻辑
...

### 修改文件
...

### 验证方式
...

### GitHub / Vercel
...

### 风险与待确认
...
```

Include exact commands run, commit hash, branch name, remote URL or PR URL, Vercel deployment URL, and any verification blockers.

## Common Mistakes

- Shipping before reading the page or product docs.
- Treating a successful push as a verified deployment.
- Staging the user's unrelated work because it happened to be in the same checkout.
- Deploying from the wrong Vercel project or team.
- Forgetting that preview and production deployments can use different environment variables.
- Reporting "done" without a route, deployment URL, or repeatable verification step.
