# Product

<!-- impeccable:product-schema 1 -->

> **Derived file. Do not edit by hand.**
> `CLAUDE.md` is the single source of product truth for Nestwood — it carries the
> evidence trail (primary sources, dated citations, rejected alternatives) that this
> schema has no place for. This file is a projection of `CLAUDE.md` into the
> impeccable/DESIGN.md product-record format, written so `context.mjs` has something
> to boot from. When the two disagree, `CLAUDE.md` wins and this file is wrong.
> Regenerate it when `CLAUDE.md` changes; never resolve a conflict in this direction.

## Platform

ios

Confirmed with the user, 2026-09-02. The shell is Next.js wrapped with Capacitor and
installed from the store, so by impeccable's own rule ("a native wrapper around a
website does not make its design language native") this would read as `web`. It is
recorded as `ios` because both stack-forcing constraints are iOS constraints: web push
works only for an installed app on iOS, and Live Activities exist only there. The wrap
is not an optimisation — it is the delivery condition for jobs 3 and 6. Android is in
scope but is not declared secondary anywhere in `CLAUDE.md`; treat that as undecided
rather than as a ranking.

Consequence for every future design session: load `reference/ios.md` before design work.

## Stack

Decided against evidenced constraints, not build convenience (`research/research.md` §7).

- **App shell**: Next.js (App Router) on Vercel, TypeScript — the AI call needs a server
  side (the API key cannot live in the browser) and met.no requires caching per its
  `Expires` header.
- **Maps + offline**: MapLibre GL JS with PMTiles in OPFS, one file per region served by
  byte range.
- **Packaging**: Capacitor wrap, installed from the store. See Platform.
- **Data**: adapter interfaces (`LodgingSource`, `WeatherSource`, `TransportSource`,
  `RouteSource`) with mocks shaped like real NTB / met.no / Entur responses.
- **Persistence**: IndexedDB for plan, gear inventory and booking-completion state;
  Service Worker for the shell.
- **AI**: `claude-opus-5` — structured outputs to the plan schema, grounding via tool use
  over the adapters, prompt caching for the stable system prompt, streaming generation.

## Users

**Primary — Kristin, 34, association member (DNT in Norway, STF in Sweden).** Experienced,
takes regular multi-day mountain trips. Even with full institutional knowledge she is
still the integration layer across her own association's disconnected tools: route
planning lives apart from hut booking, and DNT's booking flow makes her run one
transaction per hut in a chain. Her pain is structural, not a novice's gap.

**Second — Lukas, 29, foreign visitor** planning a trip into a lodging system they do not
know. Genuinely different jobs: translate the system, and fit a route into an
already-booked travel window. What this person actually lacks is not the hut taxonomy but
the unwritten rules — cleaning up, boots off, how sleeping space is divided, the
honour-system premise — plus the fact that self-service hut information exists only in
Norwegian.

A Swedish/STF persona and a "novice" persona were considered and **rejected**: they were a
demographic and a psychographic state, not distinct behaviours. Two axes carry what they
would have — lodging regime (country × object type × booking × arrival time) and first
multi-day trip versus repeat.

## Product Purpose

An AI orchestration layer that turns fitness, budget, time, gear and preferences into a
complete multi-day Nordic trekking itinerary: daily walking legs, matched overnight stays
(DNT/STF huts and campsites), a gear checklist, day-by-day weather adaptation, transport
legs to the trailhead and back, and an ordered list of what still has to be booked with
deadlines and handoff to the official systems.

Main job: *when I plan a multi-day mountain trip, I want to be confident that route,
lodging, gear and weather agree with each other, so I am not the one reconciling four
disconnected sources myself.*

Success is not consumer growth. The prototype exists to prove three things to an
acquisition buyer: the data is legally clean, the technology is sound, and the gap versus
what the giants already shipped is specific.

## Positioning

The hut-integrated multi-day pattern is **proven at scale in the Alps** — the four alpine
clubs run Hut Reservation across 500+ huts and ~1.5M bookings a year, with availability
embedded in the alpenvereinaktiv.com tour portal and *Bettencheck* showing beds across a
whole route. **The Nordics have no equivalent, and nobody anywhere has made it
generative.** That is the claim: a validated pattern moved into an unoccupied region.

The narrower claim matters. "Nobody pairs generative AI with official hut data" is too
strong and dies on a buyer's first question.

What no competitor can copy from community data: the **guarantee formula** — what any
given night actually guarantees, as a function of object type × booked or not × arrival
time × membership — and the **route nobody named**, assembled from segments to fit five
days, a chain of huts and August weather. In a community graph an unnamed route does not
exist.

## Operating Context

- **Planning happens months ahead**, at a desk or on a phone, outside met.no's ~10-day
  forecast horizon. Beyond it the plan shows a seasonal normal, labelled as a normal and
  excluded from the coherence verdict — never a forecast-shaped number.
- **In trip**: outdoors, in sunlight, on battery, often without coverage. Two in-trip
  screens ship in v1 (today's leg, and what changed with what can still be done).
- **The mechanism is lead time, not notification-at-breakage** — the signal must arrive
  while an alternative still exists.
- **Booking is someone else's transaction.** DNT chain booking is N sequential payments
  ("you must complete the booking and payment for one cabin before proceeding to the
  next"), and a logbook entry with a membership number is required even after paying
  online. Nestwood gives ordering, dependencies, deadlines and handoff. It never runs the
  transaction.
- **The catalogue is the entrance; there is no wizard.** Filters are the brief. A wizard
  was built and rejected — its first question ("region and month") is one the second
  persona cannot answer.

## Capabilities and Constraints

**Structure**: five tabs, 20 screens. Main flow: search → generation → new plan (unsaved) → save → plan → day. Карта (search bar + full-screen map + list sheet; a route of your own by tapping start and finish; the new plan), Плани (the plan opens with what's still needed from you and holds the map; days are pages that hold their night, transport and conditions), Довідник,
Безпека, Профіль. Home is contextual: the plan when one is active, the map otherwise.
Navigation is deliberately ordinary and will not differentiate the product. **Two screens
will: the new plan and the plan.**

**Hard constraints, all from primary sources:**

- **Surface the official difficulty grading; never compute our own.** DNT is publicly on
  record wanting the single national grading kept and no alternative systems. Personalise
  the *selection* of a route, never the *rating*.
- **The official grading field is mostly empty** — `gradering` is filled for 1 of 92 foot
  routes in Jotunheimen. "Not graded" is the typical case. Where it is missing, show the
  measurements (km, ascent, surface, exposure, fords) and let the person judge.
- **Load is a different object from terrain and is always computable.** Computed with a
  named published method cited in the UI — Naismith with Langmuir's descent correction,
  Tranter's fitness-and-load correction, or Munter — never a formula of ours. Tranter
  takes pack weight, so the gear checklist feeds the walking-time estimate.
- **An assembled route never leaves the officially marked network.** Route-finding is a
  search over the hut graph, not over trail vertices. Where the chain of nights cannot
  close, say where the gap is and why.
- **Offline-first is mandatory**, and it has a designed ceiling: v1 promises "an offline
  pack for this route" with a visible size in megabytes, never "offline everywhere".
- **No continuous tracking, by design.** A few pushes a day; position on the map on
  demand. A tracker would contradict the battery constraint rather than serve it.
- **Permission is asked where it is a means**: notifications when a plan is saved,
  location when the map or today's leg opens. Never at first launch.
- **©Kartverket attribution is permanent in the chrome** — CC BY 4.0, a legal requirement,
  not a credit. Compact, but always present.
- **Degrade honestly**: a source that is unavailable says so. If a non-critical source is
  missing the plan is still generated and names what is absent; if a critical one is, the
  plan is not faked.
- **A filter exists only if it is simultaneously a plan parameter.** This is what
  structurally disqualifies rating, popularity and top-10 lists from sort order.

**Data**: two classes are blocked — live bed availability (DNT/NTB and STF, a commercial
agreement, not a technical blocker) and mobile coverage as a geographic layer (does not
exist as reusable data in either country). Everything else is open with commercial use
permitted: Kartverket (CC BY 4.0), Lantmäteriet (CC0), Turrutebasen, met.no, SMHI, Entur,
NVDB, NVE Varsom. Say "one blocked field in the hut data", not "one blocked field in the
product".

**Undecided, deliberately:**

- Visual and brand direction — chosen (Прилад, signal blue + hi-vis yellow), not yet built; see Brand Commitments.
- Job 11 ("is this realistic for someone like me") has no content at launch; reviews start
  empty and cannot be seeded honestly. Either accept it unserved or substitute curated
  third-party trip reports with attribution.
- Довідник content sourcing is a licence question, not an editorial one. Working
  assumption: agreements will be reached, material bought if it has to be. First-aid
  content is never authored by us and is always attributed.
- App name — Nestwood is a working assumption.

## Brand Commitments

**Voice is derived, not chosen.** Full text in `design-system/voice.md`; every string in
the product is audited in `wireframes/microcopy.md`. Each of the five principles cites a
line in the research. A sixth candidate — AI transparency — was written up and **not
taken**, because there is no Nordic evidence for it; the rejection is kept in the file
deliberately.

**What this product is about is preparedness, not convenience.** Every competitor's copy
sells ease; ours sells knowing what you are walking into.

1. Name the condition under which a statement holds — the guarantee formula is four
   variables, so the sentence has to carry them.
2. Name the limit of our own knowledge on the field it applies to, never as a banner.
3. Our numbers are about the consequence for this person, not about popularity.
4. Explain someone else's system as a property of that system, never as something the
   person should have known.
5. When something changes, say what can still be done and how much time is left.

Three enforced sub-systems: a **словник** (one concept, one word; address fixed as «ти»;
explicit allowed/banned anglicism list), **eight bans** (error clichés, greetings,
celebration, the word «успішно», exclamation marks, emoji in system messages, promises of
ease, popularity counts, internal names leaking into the UI), and a **microcopy rule per
element type**.

Screen names get a blunt test: if a person has never met the phrase in any app, the name
is invented.

**The UI is English** (decision 2026-09-23, translated 2026-09-24 on the designer's command): wireframes, screen and tab names, and the stand's phones and components; design documents and review chrome stay Ukrainian. Source-language
terms (`Selvbetjent`, `fjällstuga`, `betjeningsgrad`, place names) stay in the original
either way.

### Binding visual constraints — recorded, not expanded

The visual direction is chosen — **Прилад** (`concept/directions-3.html`), designer's
decision 2026-09-23 — and now built in the main-flow wireframes; the system as it is in those
wireframes is recorded in [DESIGN.md](./DESIGN.md) (generated 2026-09-24 from the painted pages). Palette: Glass `#F4F5F5`, Graphite `#5E6368`, Instrument
ink `#0F1113`, **Signal blue `#2D5BFF` for action** (buttons, links; replaced ultramarine on 2026-09-24), **Hi-vis yellow
`#F2E500` for live state on the instrument** (active night on the track, alert hatch;
never a button fill). The official *blå* grading dot renders lighter, `#4A90E2`, so
it is never mistaken for the action colour. Alerts are an inverted ink panel with a hatched edge, readable
without colour. The round's log is `concept/directions.md`. What is binding:

1. **The grading colours do not constrain the brand** — designer's decision, 2026-09-23,
   reversing the earlier ban on green, blue, red and black as brand hues. The ban was our
   own inference, not a source: DNT asks for no alternative *grading systems*, not for a
   brand palette without those hues. What still holds: the official grading (grønn = enkel
   · blå = middels · rød = krevende · svart = ekstra krevende, plus *Godt tilgjengelig*) is
   surfaced, never recomputed, and its chip is recognised by **label and place**
   ("blå · middels"), not by colour alone.
2. **The load signal is text and hours, never the grading colours.** A load figure painted
   in them reads as terrain difficulty.
3. **The in-trip mode is a layout decision, not a theme decision.** Its metric is seconds
   of screen-on, not the colour of the background — "dark saves battery" holds only on
   OLED at low-to-mid brightness, and in sunlight a dark screen must be driven brighter.
   Everything needed visible at a glance, no scrolling. It turns on by itself when the
   trip starts.

## Evidence on Hand

Real, in-repo, and audited against primary sources:

- `concept/personas.md`, `concept/jtbd.md` — two personas and eleven jobs, sourcing inline.
- `research/research.md` — competitor audit, source audit (every source verified by direct
  request on 2026-08-06: licence, key requirement, liveness), stack evaluation §7.
- `wireframes/` — 33 pages: all 20 screens and their 13 states, with `_generate.py` as the
  single structural source, `_refresh.py` regenerating navigation, and `_audit.py` which
  must print zero. Plus `flow.html`, the main flow on one page with real mockups extracted
  by `_flow.py`. Contract in `wireframes/_conventions.md`; audit trail in `_screens.md`,
  `_gaps.md`, `_critique.md`.
- `design-system/voice.md` and `wireframes/microcopy.md` — 3 523 audited interface lines.

**Absences future work must not fabricate**: no live bed availability, no user reviews, no
photos without a source, licence and tier on the image itself, no field notes we invented
(they are curated, and fabricated "user reviews" in a buyer demo would be exactly the
antipattern we criticise competitors for). No usage metrics of any kind — there are no
users yet.

## Product Principles

1. **Orchestration, not another trail database.** The boundary sits on the object, not on
   a quantity: multi-day routes with overnight stays. A 6 km morning loop is not our object
   by definition, which keeps us outside AllTrails by kind rather than by size.
2. **Everything about a trip lives inside the plan, not beside it.** That is the
   orchestration thesis expressed as structure.
3. **Every surface that asserts anything carries its source.** Field notes, reviews,
   photos, Довідник articles, the load method — each names where it came from and which
   tier it sits in. A rating never feeds the coherence verdict, never alters the official
   grading, and never sorts routes.
4. **Order comes from fit to the brief, never from popularity.** Not a promise — a
   structural consequence of the filter rule.
5. **Say what can still be done, with the time left.** Lead time is the mechanism; a
   notification at the moment of breakage is a failure, not a feature.
6. **The plan always states the assumptions it ran on** — "for 2 people · 1 DNT member ·
   medium pace — change" — editable in place. This is what replaced the wizard's up-front
   questions, and it is load-bearing rather than decorative.

## Accessibility & Inclusion

- **Sunlight legibility and glanceability** are the in-trip requirement, and they are a
  layout constraint: everything needed visible without scrolling, minimal repaint.
- **Language is an accessibility problem here, not a localisation nicety.** Self-service
  hut information exists only in Norwegian, and DNT's own stated remedy is *"turveiledning
  og informasjon på flere språk"*. The culture-and-language layer is the second persona's
  whole job.
- **Preparedness over reassurance.** Røde Kors and DNT are on record that visitors
  misjudge difficulty, distance, elevation gain and how fast the weather turns. Copy that
  promises ease is banned for this reason, not for tone.
- No product-specific WCAG level has been established yet. The detector's own floors
  (11px functional text, contrast, tap targets) apply until one is.
