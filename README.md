# Nestwood

AI multi-day itinerary layer for Nordic outdoor trekking — route, overnight stays, and gear in one plan, grounded on open Nordic government geodata (Kartverket, Lantmäteriet, UT.no/DNT).

Google Maps, Komoot, and AllTrails all shipped single-day AI route assistants in 2026; none plan a full multi-day trip. Nestwood fills that gap as an AI-orchestration layer, not a proprietary geo database — legally, on CC0 open data.

Not a standalone venture — a feature-pitch / acquisition target for AllTrails, Komoot, Google's Geospatial AI team, or DNT/UT.no.

Mobile-first web, current phase targets Scandinavia (Norway + Sweden) with a working frontend on mock data shaped like the real APIs.

Full brief, scope, and open questions: [CLAUDE.md](./CLAUDE.md).

## Repo index

Phase pipeline — each folder tracks its own status; update the table below as phases progress.

| Phase | Folder | Status |
|---|---|---|
| 1. Concept | [concept/](./concept/) | In progress — people data inventory, 4 proto-personas, and Jobs-to-be-Done done (Steps 1–3); scenarios next |
| 2. Research | [research/](./research/) ([research.md](./research/research.md), [competitors.md](./research/competitors.md), [benchmark.md](./research/benchmark.md), [patterns.md](./research/patterns.md), [screens/](./research/screens/)) | In progress — competitors, benchmark, UX patterns synthesized (Steps 3–7); data sources & tech stack next |
| 3. Design system & tokens | [design-system/](./design-system/), [tokens/](./tokens/) | Not started |
| 4. Wireframes | [wireframes/](./wireframes/) | Not started |
| 5. Components | [components/](./components/) | Not started |
| 6. Handoff | [handoff/](./handoff/) | Not started |

## What's in each folder

- **concept/** — problem framing, personas, core scenarios. [personas.md](./concept/personas.md) holds 4 proto-personas (Kristin/primary — Norwegian DNT trekker — plus a Swedish STF trekker, an international purpose-driven trekker, and a first-timer with self-doubt), each traced back to research.md observations or a real forum/blog quote; [jtbd.md](./concept/jtbd.md) holds the Jobs-to-be-Done hierarchy derived from them (1 main job, 5 related, 3 emotional, 3 social, plus a hypotheses list) and a JTBD matrix; [personas.html](./concept/personas.html) is a static summary page mirroring `research/research.html`'s style. `[?]`/hypothesis markers are kept visible throughout — none of the four are validated by primary interviews yet.
- **research/** — `research.md` is the synthesized entry point (product, competitors, benchmark, patterns, conclusions); `competitors.md`, `benchmark.md`, `patterns.md` hold the full sourced detail; screenshots in `research/screens/`; data source research (Kartverket, Lantmäteriet, UT.no/DNT) and tech stack evaluation still open
- **design-system/** + **tokens/** — visual language and design tokens
- **wireframes/** — low/mid-fidelity flows for the core input → itinerary journey
- **components/** — built UI components
- **handoff/** — engineering handoff docs (incl. swapping mock data for live APIs)
