# Nestwood

AI multi-day itinerary layer for Nordic outdoor trekking. Mobile-first web, adapting to desktop later.

## Elevator pitch

Google Maps, Komoot, and AllTrails all shipped AI route assistants in 2026 — none go past a single day or a single track. None build a full multi-day trip: route + overnight stays (huts, campsites) + gear, adapted to fitness and weather. Nestwood is the AI-orchestration layer that does this, grounded on official open government geodata for Sweden and Norway (Lantmäteriet, Kartverket, DNT/UT.no) — legally, without depending on AllTrails'/Komoot's APIs or ToS.

## Problem

A hiker stitches a multi-day trip together by hand across disconnected sources: track in one tool, lodging in another, weather in a third, gear from experience/forums. 2026's AI features from the giants solve only the first slice (single-day route/search) — the multi-day planning gap remains open.

## Solution

An AI agent that takes fitness level, budget, time, existing gear, and preferences as input, and outputs a full personalized multi-day itinerary: daily walking legs, matched overnight stays (DNT huts/campsites), a gear checklist, and day-by-day adaptation to the weather forecast. Technically, this is a grounding layer (in the spirit of Google's Travel Concierge / ADK patterns) over Kartverket/Lantmäteriet/UT.no open data — not a proprietary geo database.

## Why now, why here

- Open Nordic government data (CC0, documented APIs) removes the legal risk that blocks this kind of aggregation in the US/DACH (closed AllTrails/Komoot ToS).
- Nordic *allemansrätten* culture already normalizes multi-day trekking with clear camping rules — a ready use case, not an invented one.
- The giants are already investing in an AI layer (proven product-market fit for the pattern), but none cover multi-day + overnight stays + Nordic open data — a specific, narrow, still-unclaimed gap in their own roadmap.

## Business model

Not a standalone venture (small, infrequent market, weak moat) — a feature-pitch / acquisition target for a player with distribution:

- **AllTrails / Komoot** — regional Nordic expansion + multi-day extension of their already-shipped AI assistant
- **Google Maps Geospatial AI agents team** — a concrete vertical use case for an existing grounding pattern
- **DNT/UT.no** — a non-profit-funded AI layer over their own hut/trail infrastructure, no venture model needed

What makes this pitchable rather than just an idea: a working prototype on real, legally accessible data (not a mockup) — concrete proof that the multi-day-orchestration layer is technically and legally feasible exactly where AllTrails/Komoot haven't gone.

**Packaging decision (2026-08-05)**: the demo is built and presented as a full standalone app — own brand, icon, and complete flow from onboarding to a finished itinerary — not a partial feature bolted onto someone else's UI. This doesn't change the business model above; it's the same feature-pitch/acquisition play, just packaged as convincingly as possible. Precedent from our own research: FatMap was a complete standalone app before being acquired by Strava, not a pitch deck. The one thing to keep explicit in the actual pitch narrative: this is a demo vehicle, not a go-to-market — otherwise a buyer might read "fully working app" as "why acquire instead of competing," rather than "technology ready to integrate."

## Target audience for the current prototype

External pitch to acquisition targets (AllTrails, Komoot, Google's Geospatial AI agents team, DNT/UT.no). This shapes what the prototype needs to prove: legal cleanliness of the data, technical soundness, and a clear, specific gap versus what the giants already shipped — not consumer growth metrics.

## Scope for v1

- **Geography / data**: Scandinavia — Norway (Kartverket + UT.no/DNT hut and trail data) and Sweden (Lantmäteriet), pitch-driven rather than phased by country.
- **Fidelity**: hybrid — a working frontend backed by mock data shaped like the real Kartverket/Lantmäteriet/UT.no API responses. No live integration yet; the mock layer is shaped so a real integration can be swapped in later without a rewrite.
- **Packaging**: a full standalone app (own name, icon, onboarding → itinerary flow) — see "Packaging decision" under Business model. Design and build accordingly (concept/wireframes should assume a complete app, not an embedded widget).
- **Tech stack**: not yet decided — deferred to the research phase (`research/`), which should include a stack evaluation before it's locked in.
- **UI language**: English (the audience is an international acquisition target, not a Nordic end-user yet).
- **Timeline**: no hard deadline — iterate phase by phase.

## Core user flow

**Input**: fitness level, budget, time window, existing gear, preferences.
**Output**: multi-day itinerary — daily walking legs, matched overnight stays (DNT huts/campsites), a gear checklist, and weather-driven adaptation per day.

## Non-goals for now

- Not building a standalone consumer venture or growth loop — the demo is a full app by packaging (see Packaging decision), but the business model stays acquisition-target, not an independent product with its own GTM.
- Not wiring up live third-party APIs yet (mock data shaped like real responses instead).
- Not covering regions outside Scandinavia.

## Repo / workflow structure

Repo was just cleared for this restart; the previous project's phase pipeline is being reused for this new product:

- `concept/` — problem framing, personas, scenarios
- `research/` — competitor audit, data source research, benchmarks, patterns
- `design-system/` + `tokens/` — visual language, design tokens
- `wireframes/` — low/mid-fidelity flows
- `components/` — built UI components
- `handoff/` — engineering handoff docs

## Key external data sources

- Kartverket (Norway) — https://kartverket.no
- Lantmäteriet (Sweden) — https://www.lantmateriet.se
- UT.no / DNT (Norway hut & trail data) — https://ut.no

## Open questions for the research phase

- Final tech stack for the mobile-first frontend.
- Visual/brand direction — the previous cycle had settled on a light Scandinavian-minimalist style; evaluate whether it carries over to Nestwood.
- Concrete demo scenario and success criteria to use when pitching to acquisition targets.
- App identity for the standalone packaging — name (working assumption: Nestwood), icon, and onboarding tone — to settle during concept/design-system phases.
