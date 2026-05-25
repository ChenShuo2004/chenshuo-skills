# Open Design Map

## Project Root

- Product and onboarding: `README.md`, `README.zh-CN.md`, `QUICKSTART.md`.
- Architecture and protocols: `docs/spec.md`, `docs/architecture.md`, `docs/skills-protocol.md`, `docs/agent-adapters.md`, `docs/modes.md`.
- Runtime apps: `apps/web`, `apps/daemon`, `apps/desktop`, `apps/packaged`.
- Shared packages: `packages/contracts`, `packages/sidecar-proto`, `packages/sidecar`, `packages/platform`.
- Lifecycle tools: `tools/dev`, `tools/pack`.
- Design material: `skills`, `design-systems`, `craft`, `prompt-templates`, `assets/frames`.

## Skill Families

- Web and product UI: `web-prototype`, `saas-landing`, `dashboard`, `pricing-page`, `docs-page`, `blog-post`.
- Mobile: `mobile-app`, `mobile-onboarding`, `gamified-app`.
- Decks: `guizang-ppt`, `simple-deck`, `replit-deck`, `weekly-update`, `html-ppt`.
- Social and marketing: `email-marketing`, `social-carousel`, `magazine-poster`, `image-poster`, `motion-frames`, `sprite-animation`.
- Docs and operations: `pm-spec`, `team-okrs`, `meeting-notes`, `kanban-board`, `eng-runbook`, `finance-report`, `invoice`, `hr-onboarding`.
- Video and motion: `hyperframes`, `video-shortform`, `audio-jingle`.

## Validation

- For repo code changes: run `pnpm typecheck`; run `pnpm test`; run `pnpm build` when build boundaries change.
- For web UI: run `pnpm tools-dev run web --daemon-port <port> --web-port <port>` and verify in a browser.
- For desktop work: use `pnpm tools-dev inspect desktop status --json` and screenshots on GUI-capable machines.
