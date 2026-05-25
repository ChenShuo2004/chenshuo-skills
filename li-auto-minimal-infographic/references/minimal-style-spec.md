# Minimal Style Spec

This reference captures the current Li Auto owner minimal share-code infographic style. It supports two related modes:

- Light-IP minimal checklist, based on the 2026-05-20 `安全守护轻IP极简清单` set.
- NO-IP dense checklist, based on later 40/60/custom-code list sets.

## Core Positioning

- Purpose: make a practical owner-scene share-code checklist, not a brand ad.
- Cover identity: `理想汽车分享码｜极简清单`, with optional `理想汽车 / LI AUTO` trademark text or `理想车主分享码收藏版`.
- IP mode: `NO-IP` or `<IP属性>` remains a secondary style note, not the main cover identity.
- Default size: `1080x1440` PNG.
- Workflow: ask intake questions first, then plan pages, then generate/render, then QA.
- Main priority: reader can understand the scene, action, share code, benefit, and risk boundary within 3 seconds.

## Intake Must Cover

Before production, clarify:

- Account: account link/name/positioning, or general Li Auto owner account.
- Goal: save/collect, comment to join group, follow, private message, community forwarding, conversion, or custom.
- Theme and scene: what the set is about and when the owner will use it.
- Target user: new owners, family users, commuters, long-distance users, camping users, car-machine heavy users, or potential buyers.
- Share-code count and source: main library, user-supplied list, or prompt-only.
- CTA: default `评论「进群」拉你进车主群`.
- IP style: NO-IP, light IP attribute, or specified authorized IP.
- Forbidden content: official endorsement, permanent validity, all-model compatibility, fake official badges, QR codes, unlicensed characters, raw user prompt, internal workflow terms. The user allows Li Auto trademark/text identity on the cover.

## Visual DNA

Cover:

- Deep ink green or near-black background.
- Subtle paper grain or fine noise.
- Top-left label: `理想汽车分享码｜极简清单`.
- Add a clear Li Auto identity line such as `理想汽车 / LI AUTO` or `理想车主分享码收藏版`.
- Main title is the strongest element.
- Optional account/avatar icon at top-right.
- Short benefit line.
- Red CTA at the bottom.
- Small risk note near the footer.

Light-IP content page:

- Dark green header.
- Off-white or cream body.
- Page label at top-left and account/avatar mark at top-right.
- Very large black title.
- One short concrete subtitle.
- 3 clean code cards by default.
- Each card includes index, feature name, use-case note, and large exact code digits.
- Small IP attribute only: clue line, magnifier, scan line, energy mark, game pixel, film frame, etc.

NO-IP dense content page:

- Off-white paper body.
- Dark green top and bottom bars.
- Top-left category pill.
- Top-right generic account/avatar icon only.
- Small page meta, such as `03 / 60 个分享码速查`.
- Large black page title.
- One short subtitle.
- 6 horizontal code cards by default.
- Left card number block alternates dark green and red.
- Right code block is black with exact white share-code digits.

Closing content page:

- Same as a normal content page.
- Bottom CTA can be stronger.
- Do not add a separate pure marketing end card unless requested.

## Copy Rules

Visible copy should feel like a fast owner checklist:

- specific owner scenarios;
- concrete actions;
- short feature names;
- plain Chinese;
- no internal production language.

Good visible phrasing:

- `转弯前先看清`
- `下车前再查一遍`
- `P/N 档和后排安全带，家人共用车更稳`
- `右转低速打开盲区影像`
- `通勤前自动播报天气和路况`

Forbidden visible labels:

- `IP Code`
- `Prompt Code`
- `rotation`
- `batch`
- `main library`
- local file paths
- raw user prompt
- official endorsement or official badge language

## Imagegen Prompt Notes

Every prompt should explicitly require:

- `1080x1440 vertical Chinese infographic`;
- clean minimalist editorial layout;
- exact Chinese visible text;
- exact share codes copied without changing digits;
- no mascot;
- Li Auto trademark/text identity is allowed on the cover when used as identification;
- no QR code;
- no fake screenshots;
- no watermark;
- no random extra numbers or English;
- no text overlap.

Cover prompt skeleton:

```text
Create a 1080x1440 vertical Chinese minimalist cover page.
Style: 极简清单, dark ink-green background, subtle grain, high contrast, editorial.
Visible identity: 理想汽车分享码｜极简清单
Visible text:
- 理想汽车 / LI AUTO or 理想车主分享码收藏版
- {main title}
- {subtitle}
- {benefit line}
- {cta}
- {risk note}
No mascot, no QR code, no watermark, no fake official endorsement.
Keep all text readable and leave generous margins.
```

Content prompt skeleton:

```text
Create a 1080x1440 vertical Chinese minimalist content page for Li Auto owners.
Style: off-white paper background, dark green bars, black typography, red accents, clean checklist.
Visible identity: 理想汽车分享码｜极简清单; page label may show {NO-IP or <IP属性>}
Page meta: {page_index / total or category}
Title: {title}
Subtitle: {subtitle}
Rows:
1. {code} — {feature/use case}
2. {code} — {feature/use case}
...
Copy every share code exactly.
No mascot, no QR code, no watermark, no random extra numbers, no fake official badge.
Keep all text readable and non-overlapping.
```

## QA Checklist

Before delivery, verify:

- final PNG count matches the planned page count;
- every final PNG is exactly `1080x1440` unless another size was requested;
- every visible share code matches the fact sheet;
- every requested code appears exactly once unless duplicates were explicitly allowed;
- CTA matches the user's selected wording;
- no mascot, QR code, fake badge, watermark, or fake endorsement appears;
- no internal production terms appear;
- IP attributes are small, abstract, and do not compete with text;
- `事实底稿.md`, `制作提示词.md`, `发布信息.md`, `质检记录.md`, and `文件清单.md` are present;
- dense-list override is recorded when using 6 codes per page while a local template prefers fewer codes.
