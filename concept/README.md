# Concept — Nestwood

Status: **not started** (phase 1).

Problem framing, personas, and core scenarios for the multi-day Nordic trekking itinerary flow (fitness/budget/time/gear input → route + overnight stays + gear checklist + weather adaptation output). See [../CLAUDE.md](../CLAUDE.md) for the underlying pitch.

## Constraints this phase must design around (added 2026-08-05, from research)

Two research findings narrow how the problem framing and scenarios should be written — full detail in [../research/research.md](../research/research.md) and [../research/competitors.md](../research/competitors.md):

- **Gap statement is narrower than "nobody does multi-day AI planning."** Komoot already auto-splits a route into stages with generic lodging suggestions; AllTrails-in-Claude already generates multi-day itineraries with packing lists. The actual open gap is: nobody pairs generative AI + *official* hut infrastructure data (bed availability, keys, opening dates) + day-by-day weather adaptation in one flow. Problem framing and personas should be written against this precise gap, not the broader one — a persona/scenario that only needs "a multi-day plan" doesn't differentiate us from Komoot; one that needs *trustworthy, official hut logistics* does.
- **Official hut *availability* data isn't confirmed accessible yet.** DNT closed the previously-open Nasjonal Turbase API; there's no verified open or licensed path to live bed availability/booking status right now (Kartverket's open data covers hut *location* and *type*, not live availability). At least one core scenario must be built around this being genuinely uncertain — not assumed solved — so the persona/scenario work doesn't quietly bake in a data assumption research has since shown to be shaky. See the matching wireframes requirement in [../wireframes/README.md](../wireframes/README.md).
