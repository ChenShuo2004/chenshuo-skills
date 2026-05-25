---
name: open-design
description: Use when Codex needs to use the local Open Design project for artifact-first design workflows such as selecting Open Design skills, generating HTML prototypes, dashboards, mobile screens, decks, or adapting Open Design skills into another project.
---

# Open Design

## Overview

Use the existing local Open Design checkout as the source of truth. The checkout path is user-specific; ask for it or resolve it from the current workspace when needed.

When the exact workspace folder is needed, search likely workspace roots for the directory that contains `open-design\AGENTS.md`:

```powershell
Get-ChildItem -LiteralPath <workspace-root> -Directory |
  Where-Object { Test-Path -LiteralPath (Join-Path $_.FullName 'open-design\AGENTS.md') } |
  Select-Object -First 1 -ExpandProperty FullName
```

Open Design is an artifact-first design runtime with a local daemon, web app, desktop app, built-in design skills, design systems, prompt templates, and coding-agent adapters. Treat it as a separate external project unless the user explicitly asks to copy files into another repo.

## First Steps

1. Resolve the Open Design checkout path, then read `open-design\AGENTS.md`.
2. Read only the docs needed for the task:
   - `README.zh-CN.md` or `README.md` for product overview.
   - `QUICKSTART.md` for running the app.
   - `docs\skills-protocol.md` when adding or adapting skills.
   - `docs\architecture.md` or `docs\agent-adapters.md` for runtime or agent-adapter work.
3. If working inside `apps`, `packages`, or `tools`, read that layer's `AGENTS.md`.
4. For orientation, load `references\open-design-map.md` from this skill only when a compact project map is useful.

## Common Workflows

### Run or inspect Open Design

Use the project lifecycle entry from the Open Design repo:

```powershell
cd <resolved-workspace>\open-design
corepack enable
pnpm install
pnpm tools-dev
```

Use fixed ports when needed:

```powershell
pnpm tools-dev run web --daemon-port <port> --web-port <port>
```

Useful inspection commands:

```powershell
pnpm tools-dev status --json
pnpm tools-dev logs --json
pnpm typecheck
pnpm test
pnpm build
pnpm check:residual-js
```

### Use an Open Design artifact skill

1. Pick the most specific folder under `<resolved-workspace>\open-design\skills`.
2. Read that skill's `SKILL.md`.
3. Read only the referenced `assets`, `references`, templates, or active `DESIGN.md` files needed for the requested artifact.
4. Follow the selected skill's output contract. Many Open Design skills produce a self-contained HTML artifact.
5. Use the repo's existing design-system and craft references when the selected skill requires them.

Useful starting skills:

- `skills\web-prototype`
- `skills\dashboard`
- `skills\mobile-app`
- `skills\guizang-ppt`
- `skills\html-ppt`
- `skills\social-carousel`
- `skills\magazine-poster`
- `skills\hyperframes`

### Add or adapt an Open Design skill

1. Read `<resolved-workspace>\open-design\docs\skills-protocol.md`.
2. Start from the closest existing `skills\<name>\SKILL.md`.
3. Keep standard `name` and `description` frontmatter compatible with Codex.
4. Keep Open Design-specific metadata under `od:` only when Open Design needs it.
5. Add assets or references only when they remove repeated work.
6. Validate with the project command that matches the changed package.

## Boundaries

- Keep Open Design separate from `lixiang.com-1` unless the user explicitly asks to integrate them.
- Do not recreate removed paths such as `apps\nextjs`.
- Do not add root lifecycle aliases like `pnpm dev` or `pnpm start`.
- Runtime target is Node `~24` and `pnpm@10.33.2`.
- Project-owned source should stay TypeScript-first.
