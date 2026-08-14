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
| 4. Wireframes | [wireframes/](./wireframes/) ([sitemap.md](./wireframes/sitemap.md), [flows.md](./wireframes/flows.md), [ia.html](./wireframes/ia.html), [_conventions.md](./wireframes/_conventions.md)) | **Done** — information architecture (entities, screen tree, navigation, flows, traceability) **and all 59 screen pages**: 23 screens × their states, greyscale, wired along the flows |
| 5. Components | [components/](./components/) | Not started |
| 6. Handoff | [handoff/](./handoff/) | Not started |

## What's in each folder

- **concept/** — problem framing, personas, core scenarios. [personas.md](./concept/personas.md) holds 4 proto-personas (Kristin/primary — Norwegian DNT trekker — plus a Swedish STF trekker, an international purpose-driven trekker, and a first-timer with self-doubt), each traced back to research.md observations or a real forum/blog quote; [jtbd.md](./concept/jtbd.md) holds the Jobs-to-be-Done hierarchy derived from them (1 main job, 5 related, 3 emotional, 3 social, plus a hypotheses list) and a JTBD matrix; [personas.html](./concept/personas.html) is a static summary page mirroring `research/research.html`'s style. `[?]`/hypothesis markers are kept visible throughout — none of the four are validated by primary interviews yet.
- **research/** — `research.md` is the synthesized entry point (product, competitors, benchmark, patterns, conclusions); `competitors.md`, `benchmark.md`, `patterns.md` hold the full sourced detail; screenshots in `research/screens/`; data source research (Kartverket, Lantmäteriet, UT.no/DNT) and tech stack evaluation still open
- **design-system/** + **tokens/** — visual language and design tokens
- **wireframes/** — information architecture, then low/mid-fidelity screens. Structure of the two working documents:

  **[sitemap.md](./wireframes/sitemap.md)** — the IA source of truth, five sections that build on each other:
  - *Сутності* — 19 objects the person actually deals with, each traced to the job that produces it. Field names for lodging objects come from DNT's real public NTB schema, not invented, so the mock layer has the shape of real responses.
  - *Під питанням* — objects with no job of their own, kept visible so they don't slip into the data model unnoticed.
  - *Екрани* — the screen tree (23 screens + 4 inline layers), each labelled with its job and its persona, plus the states (`empty`, `loading`, `error`, `degraded`, `offline`) and an explicit list of what the tree deliberately lacks.
  - *Навігація* — four global entries plus one conditional, three levels (global / contextual / deep), depth in taps, and nine movement rules.
  - *Трасування* — the 12 × 20 coverage matrix with both orphan lists, and a note on what the matrix method cannot catch.

  **[flows.md](./wireframes/flows.md)** — six Mermaid flows (MAIN, R2, R7, R3+R6, S2, S1). Every flow carries decision points, states as separate nodes, and both ends — success *and* dead ends. Rule: every named exit from a dead end must exist in the sitemap.

  **[ia.html](./wireframes/ia.html)** — rendered readout of both, in the shared document style: tree with job labels, all six diagrams live, and the traceability matrix with orphans highlighted.

  **The screens themselves — 59 pages, complete.** Open any of them and the left tree shows the whole structure: section → screen → state, current one marked. Start at [start.html](./wireframes/start.html) and the main path is clickable end to end, state transitions included.
  - **[_conventions.md](./wireframes/_conventions.md)** — the contract every screen obeys: greyscale only (no colour, icons, images, JS or libraries), semantic markup, real Ukrainian domain copy instead of placeholders, file naming, and a **closed** state vocabulary (`empty · error · loading · offline · degraded · conflict · seasonal · nooptions`). Written before the screens, which is why a set drawn partly by parallel subagents came out as one pattern rather than six.
  - **A state is a separate page, never an afterthought.** Same landmarks, same order, same headings — only content differs. Every state carries a named exit, and a target that isn't drawn renders as inert text rather than a broken link.
  - **[_screens.md](./wireframes/_screens.md)** — which states are real for which screen, and why. Two screens have none of the four canonical states, and the file says why rather than leaving it blank.
  - **[_gaps.md](./wireframes/_gaps.md)** — the framework audited against five hard competitors: six critical holes, what is merely worse but fine, and where we are ahead.
  - **[_critique.md](./wireframes/_critique.md)** — the final pass over all pages: four defects found and fixed, plus the rule that came out of it — a state you decide not to draw has to be named in the conventions at that moment, or it stops being *deferred* and becomes *lost*.
  - **[_generate.py](./wireframes/_generate.py) · [_refresh.py](./wireframes/_refresh.py) · [_audit.py](./wireframes/_audit.py)** — structure is regenerated from one source, not copied by hand: `TREE` holds sections → screens → states, `_refresh.py` rewrites the navigation tree and state row across every page, `_audit.py` must print zero defects.
- **components/** — built UI components
- **handoff/** — engineering handoff docs (incl. swapping mock data for live APIs)
