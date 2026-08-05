# Wireframes — Nestwood

Status: **not started** (phase 4, after concept, research, and design-system/tokens).

Low- and mid-fidelity flows for the core user journey: input (fitness, budget, time, gear, preferences) → multi-day itinerary output (route, overnight stays, gear checklist, weather adaptation).

## Required state, added 2026-08-05 (from research): hut availability "pending DNT partnership"

Research found that DNT's open API for live hut availability/booking status is currently closed (no verified open or licensed access path — see [../CLAUDE.md](../CLAUDE.md) Open questions and [../research/research.md](../research/research.md)). This isn't just a data-integration detail to sort out later — it needs its own explicit UI state in the itinerary output, designed alongside the happy path, not bolted on:

- **Happy-path state**: a day's overnight stay shows the matched hut with confirmed availability, sourced and attributed (per the named-contributor-breakdown pattern from [../research/benchmark.md](../research/benchmark.md) mechanism #2 — Oura Readiness Score precedent).
- **Degraded state ("availability pending DNT partnership")**: when live bed-availability data isn't available for a hut, the plan must say so plainly — which hut, why availability isn't confirmed, and what the hiker should do about it (e.g. official contact info, key/membership requirement) — rather than presenting a guess as fact. This is the graceful-degradation pattern from benchmark.md mechanism #1 (Monarch Money multi-provider fallback), applied to a real gap this research surfaced, not a hypothetical one.
- Both states should use the *same* explanatory UI pattern (named, sourced, per-day) so the degraded state reads as "the plan is being honest with you," not as an error or missing feature — this is also the direct counter-positioning to the AllTrails/Zillow failure modes documented in research (overconfident AI output, no per-source attribution).

This state should appear in the wireframe set from day one — at minimum one full example day showing it — not as a later edge-case pass.
