# Nestwood

AI multi-day itinerary layer for Nordic outdoor trekking — route, overnight stays, and gear in one plan, grounded on open Nordic government geodata (Kartverket, Lantmäteriet, UT.no/DNT).

Google Maps, Komoot, and AllTrails all shipped single-day AI route assistants in 2026; none plan a full multi-day trip. Nestwood fills that gap as an AI-orchestration layer, not a proprietary geo database — legally, on CC0 open data.

Not a standalone venture — a feature-pitch / acquisition target for AllTrails, Komoot, Google's Geospatial AI team, or DNT/UT.no.

Native mobile app (Capacitor wrap from the start — push with lead time is a job requirement, not a nicety), current phase targets Scandinavia (Norway + Sweden) with a working frontend on mock data shaped like the real APIs.

**Structure**: the curated multi-day route catalogue is the entrance, there is no wizard, and the app has five tabs — Карта · Плани · Довідник · Безпека · Профіль. Navigation is deliberately ordinary; the two screens that differentiate are the **route card** and the **plan**.

Full brief, scope, and open questions: [CLAUDE.md](./CLAUDE.md).

## Voice

The product speaks one way, and the way is written down: [design-system/voice.md](./design-system/voice.md). Every string in the set is inventoried in [wireframes/microcopy.md](./wireframes/microcopy.md).

**Preparedness, not convenience.** Every competitor's copy sells ease; Nestwood sells knowing what you are walking into. Five principles operationalise it, and each cites a line in the research rather than a taste:

1. Name the condition under which a statement holds — a booked bed is guaranteed, an unbooked one still gets you indoors, possibly on a floor mattress.
2. Name the limit of our own knowledge on the field it applies to, never as a banner.
3. Numbers are about the consequence for this person, not about popularity.
4. Explain someone else's system as a property of that system, not as something the person should have known.
5. When something changes, say what can still be done and how much time is left.

A sixth candidate — AI transparency — was written up and deliberately **not taken**, for lack of any Nordic evidence. It stays in the file: a principle declined for a stated reason is part of the artefact.

Three enforced sub-systems make this checkable: a **dictionary** (one concept, one word; the address fixed as «ти»; an explicit anglicism list, scoped to product text only), **eight bans** each with a real було/треба pair (error clichés, celebration, «успішно», exclamation marks, emoji in system messages, promises of ease, popularity counts, internal screen names leaking into the UI), and **microcopy rules per element type** — button, heading, field, empty, error, loading, success, destructive.

Screen names get a blunt test, added after two invented ones shipped: if a person has never met the phrase in any app, the name is invented.

## Repo index

Phase pipeline — each folder tracks its own status; update the table below as phases progress.

| Phase | Folder | Status |
|---|---|---|
| 1. Concept | [concept/](./concept/) | Done — 2 personas + 2 axes, 12 jobs and 8 hypotheses; every claim audited against primary sources |
| 2. Research | [research/](./research/) ([research.md](./research/research.md), [competitors.md](./research/competitors.md), [benchmark.md](./research/benchmark.md), [patterns.md](./research/patterns.md), [screens/](./research/screens/)) | Done — 15 competitors, benchmark, UX patterns, 8 data-source classes verified by direct request, tech stack decided. Interface pattern: catalogue, not wizard |
| 3. Design system & tokens | [design-system/](./design-system/) ([voice.md](./design-system/voice.md)), [tokens/](./tokens/) | **Voice done and applied** — 5 principles each sourced to a line in the research, plus dictionary, bans and per-element microcopy rules; every one of the 63 wireframe pages rewritten under it. Visual language and tokens not started (brand accent still deferred: green/blue/red/black are the official grading) |
| 4. Wireframes | [wireframes/](./wireframes/) ([sitemap.md](./wireframes/sitemap.md), [flows.md](./wireframes/flows.md), [ia.html](./wireframes/ia.html), [flow.html](./wireframes/flow.html), [microcopy.md](./wireframes/microcopy.md), [_conventions.md](./wireframes/_conventions.md)) | **Done** — 63 pages (31 screens × 32 states) against the five-tab catalogue structure, plus [flow.html](./wireframes/flow.html), the main path as ten screens in a row. All copy rewritten under `voice.md`; `_audit.py` prints zero |
| 5. Components | [components/](./components/) | Not started |
| 6. Handoff | [handoff/](./handoff/) | Not started |

## What's in each folder

- **concept/** — problem framing, personas, core scenarios. [personas.md](./concept/personas.md) holds **2 personas and 2 axes** (Kristin/primary — association member, knows the system; Lukas/second — foreign visitor into a lodging system he doesn't know. The Swedish-STF and novice personas folded into axes: they were demographics and a psychographic state, with zero jobs of their own); [jtbd.md](./concept/jtbd.md) holds the Jobs-to-be-Done hierarchy (1 main job, 7 related, 2 emotional, 2 social, plus 8 hypotheses including H6) and a JTBD matrix; [personas.html](./concept/personas.html) is a static summary page mirroring `research/research.html`'s style. `[?]`/hypothesis markers are kept visible throughout — none of the four are validated by primary interviews yet.
- **research/** — `research.md` is the synthesized entry point (product, competitors, benchmark, patterns, conclusions); `competitors.md`, `benchmark.md`, `patterns.md` hold the full sourced detail; screenshots in `research/screens/`; data sources verified by direct request (only live bed availability and mobile coverage are blocked) and the tech stack decided in §7
- **design-system/** + **tokens/** — visual language and design tokens
- **wireframes/** — information architecture, then low/mid-fidelity screens. Structure of the two working documents:

  **[sitemap.md](./wireframes/sitemap.md)** — the IA source of truth, five sections that build on each other:
  - *Сутності* — 19 objects the person actually deals with, each traced to the job that produces it. Field names for lodging objects come from DNT's real public NTB schema, not invented, so the mock layer has the shape of real responses.
  - *Під питанням* — objects with no job of their own, kept visible so they don't slip into the data model unnoticed.
  - *Екрани* — the screen tree (23 screens + 4 inline layers), each labelled with its job and its persona, plus the states (`empty`, `loading`, `error`, `degraded`, `offline`) and an explicit list of what the tree deliberately lacks.
  - *Навігація* — four global entries plus one conditional, three levels (global / contextual / deep), depth in taps, and nine movement rules.
  - *Трасування* — the 12 × 20 coverage matrix with both orphan lists, and a note on what the matrix method cannot catch.

  **[flows.md](./wireframes/flows.md)** — six Mermaid flows (MAIN, 2, 7, 3+6, 11, 10). Every flow carries decision points, states as separate nodes, and both ends — success *and* dead ends. Rule: every named exit from a dead end must exist in the sitemap.

  **[ia.html](./wireframes/ia.html)** — rendered readout of both, in the shared document style: tree with job labels, all six diagrams live, and the traceability matrix with orphans highlighted.

  **The screens themselves — 63 pages, complete.** Open any of them and the left tree shows the whole structure: section → screen → state, current one marked. Start at catalogue.html and the main path is clickable end to end, state transitions included; [flow.html](./wireframes/flow.html) lays the same ten screens out in a row for reading it as one story.
  - **[microcopy.md](./wireframes/microcopy.md)** — every interface line in the set as one table (screen · zone · line · line type), regenerated from the pages rather than maintained by hand, with the було/стало record of the voice rewrite. It is what makes "the same action is called the same everywhere" a check instead of a wish.
  - **[_conventions.md](./wireframes/_conventions.md)** — the contract every screen obeys: greyscale only (no colour, icons, images, JS or libraries), semantic markup, real Ukrainian domain copy instead of placeholders, file naming, and a **closed** state vocabulary (`empty · error · loading · offline · degraded · conflict · seasonal · nooptions`). Written before the screens, which is why a set drawn partly by parallel subagents came out as one pattern rather than six.
  - **A state is a separate page, never an afterthought.** Same landmarks, same order, same headings — only content differs. Every state carries a named exit, and a target that isn't drawn renders as inert text rather than a broken link.
  - **_screens.md** — which states are real for which screen, and why. Two screens have none of the four canonical states, and the file says why rather than leaving it blank.
  - **_gaps.md** — the framework audited against five hard competitors: six critical holes, what is merely worse but fine, and where we are ahead.
  - **_critique.md** — the final pass over all pages: four defects found and fixed, plus the rule that came out of it — a state you decide not to draw has to be named in the conventions at that moment, or it stops being *deferred* and becomes *lost*.
  - **[_generate.py](./wireframes/_generate.py) · [_refresh.py](./wireframes/_refresh.py) · [_audit.py](./wireframes/_audit.py) · `_flow.py` · `_microcopy.py`** — structure is regenerated from one source, not copied by hand: `TREE` holds sections → screens → states and is the only place a screen is named, `_refresh.py` rewrites the tree, header, title and state row across every page, `_flow.py` rebuilds `flow.html`, `_microcopy.py` rebuilds `microcopy.md`, and `_audit.py` must print zero defects — including a name-drift check across the four places a screen name appears.
- **components/** — built UI components
- **handoff/** — engineering handoff docs (incl. swapping mock data for live APIs)
