# Wireframes — Nestwood

Status: **documents updated for the catalogue structure, pages being redrawn.**

The catalogue is now the navigation root, there is no wizard, and there are five tabs instead of seven clusters. The IA documents below are rewritten against that; the 59 drawn pages were built against the wizard-spine structure and are the next step.

| Step | Output | State |
|---|---|---|
| 1 · Entities | [sitemap.md](./sitemap.md) § Сутності — 23 entities, each traced to a job | done |
| 2 · Screen tree | [sitemap.md](./sitemap.md) § Екрани — five tabs, ~27 screens, states, coverage both ways | **rewritten** |
| 3 · Navigation | [sitemap.md](./sitemap.md) § Навігація — five tabs, contextual home, depth in taps | **rewritten** — 3 taps to a plan, value at tap zero |
| 4 · User flows | [flows.md](./flows.md) — MAIN, 2, 7, 3+6, 11, 10 as Mermaid | **rewritten** |
| 5 · Traceability | [sitemap.md](./sitemap.md) § Трасування — 12 jobs × 27 screens + hypothesis H6, orphan lists with a decision each | **recomputed** |
| 6 · Wireframes | 59 pages drawn against the old structure | **being redrawn** — new order in _screens.md |

Low- and mid-fidelity flows for the core user journey: input (fitness, time, what to walk, lodging regime + membership, gear, preferences; budget optional) → multi-day itinerary output (route, overnight stays, gear checklist, weather adaptation, transport legs, and what still has to be booked).

## Required state: hut availability "pending DNT partnership"

Research found that DNT's open API for live hut availability/booking status is currently closed (no verified open or licensed access path — see [../CLAUDE.md](../CLAUDE.md) Open questions and [../research/research.md](../research/research.md)). This isn't just a data-integration detail to sort out later — it needs its own explicit UI state in the itinerary output, designed alongside the happy path, not bolted on:

- **Happy-path state**: a day's overnight stay shows the matched hut with confirmed availability, sourced and attributed (per the named-contributor-breakdown pattern from [../research/benchmark.md](../research/benchmark.md) mechanism #2 — Oura Readiness Score precedent).
- **Degraded state ("availability pending DNT partnership")**: when live bed-availability data isn't available for a hut, the plan must say so plainly — which hut, why availability isn't confirmed, and what the hiker should do about it (e.g. official contact info, key/membership requirement) — rather than presenting a guess as fact. This is the graceful-degradation pattern from benchmark.md mechanism #1 (Monarch Money multi-provider fallback), applied to a real gap this research surfaced, not a hypothetical one.
- Both states should use the *same* explanatory UI pattern (named, sourced, per-day) so the degraded state reads as "the plan is being honest with you," not as an error or missing feature — this is also the direct counter-positioning to the AllTrails/Zillow failure modes documented in research (overconfident AI output, no per-source attribution).

This state should appear in the wireframe set from day one — at minimum one full example day showing it — not as a later edge-case pass.
