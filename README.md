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
| 1. Concept | [concept/](./concept/) | Not started |
| 2. Research | [research/](./research/) ([research.md](./research/research.md), [screens/](./research/screens/)) | Not started |
| 3. Design system & tokens | [design-system/](./design-system/), [tokens/](./tokens/) | Not started |
| 4. Wireframes | [wireframes/](./wireframes/) | Not started |
| 5. Components | [components/](./components/) | Not started |
| 6. Handoff | [handoff/](./handoff/) | Not started |

## What's in each folder

- **concept/** — problem framing, personas, core scenarios
- **research/** — competitor audit, data source research (Kartverket, Lantmäteriet, UT.no/DNT), benchmark, tech stack evaluation, visual direction; screenshots in `research/screens/`
- **design-system/** + **tokens/** — visual language and design tokens
- **wireframes/** — low/mid-fidelity flows for the core input → itinerary journey
- **components/** — built UI components
- **handoff/** — engineering handoff docs (incl. swapping mock data for live APIs)
