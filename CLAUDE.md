# Nestwood

AI multi-day itinerary layer for Nordic outdoor trekking. Mobile-first web, adapting to desktop later.

## Elevator pitch

Google Maps, Komoot, and AllTrails have all shipped AI route/trip features — Komoot's Multi-Day Planner auto-splits a route into stages and suggests lodging, and AllTrails-in-Claude generates multi-day itineraries with packing lists. None of them is generative *and* grounded in official hut infrastructure data (bed availability, keys, opening dates) *and* weather-adaptive day by day, in one flow.

**Precision added 2026-08-05 (research/research.md, §3 "Альпійський стек")** — the earlier phrasing, "nobody pairs generative AI with official hut data," was too strong and would not survive a buyer's first question. In the Alps that pairing minus the generative layer **already exists and is monetised**: the four alpine clubs (DAV, ÖAV, SAC, AVS) run *Hut Reservation* — 500+ huts, ~1.5M bookings a year — its availability calendar is embedded directly in the alpenvereinaktiv.com tour portal, and *Bettencheck* shows bed availability across an entire multi-day route. That portal runs on Outdooractive's white-label technology, i.e. on the very precedent we cite for our own business model.

So the honest, defensible claim is narrower and stronger: **the pattern is proven at scale in the Alps; the Nordics have no equivalent, and nobody anywhere has made it generative.** That reframes Nestwood from "new product" to "a validated pattern moved into an unoccupied region" — weaker on novelty, much stronger on feasibility, and it is the framing to use in the pitch.

Nestwood is the AI-orchestration layer that does this, grounded on official open government geodata for Sweden and Norway (Lantmäteriet — CC0; Kartverket — CC BY 4.0, commercial use expressly permitted; DNT/UT.no) — without depending on AllTrails'/Komoot's APIs or ToS for the *trail/basic-hut* data (see the caveat on DNT/UT.no's operational hut data under "Why now, why here").

**Competitive risk, resolved to a sharper shape 2026-08-05**: Outdooractive is our precedent *and* a competitor, but on a different axis than first feared. It is already in Scandinavia — a partnership with Visit Group as map/routing provider, a customer base in Denmark, Sweden and especially Norway, and the Geilo project as its reference — but that is destination/DMO technology, **not hut booking**, and there is no evidence of any Outdooractive–DNT link. DNT builds ut.no itself (with Statskog, Friluftsrådenes Landsforbund, Miljødirektoratet, Kartverket; Atea as IT partner) and runs its own public engineering org. An alpine club handed its portal to a white-label vendor; DNT most likely will not.

**So the real risk is that DNT builds this itself** — it has the platform, the data, the engineers, and a publicly stated need. That makes the pitch to DNT one about *speed*, not about owning unmatchable technology. Per-buyer entry points: **DNT** — "you have everything except the generative layer and the multilingual guidance you said you need"; **AllTrails / Komoot** — "Nordic hut logistics is a moat you cannot build from community data"; **Google** — "a concrete vertical case for your existing grounding pattern".

## Problem

A hiker stitches a multi-day trip together by hand across disconnected sources: track in one tool, lodging in another, weather in a third, gear from experience/forums. 2026's AI features from the giants solve only the first slice (single-day route/search) — the multi-day planning gap remains open.

## Solution

An AI agent that takes fitness level, budget, time, existing gear, and preferences as input, and outputs a full personalized multi-day itinerary: daily walking legs, matched overnight stays (DNT huts/campsites), a gear checklist, and day-by-day adaptation to the weather forecast. Technically, this is a grounding layer (in the spirit of Google's Travel Concierge / ADK patterns) over Kartverket/Lantmäteriet/UT.no open data — not a proprietary geo database.

## Why now, why here

- Open Nordic government data (Lantmäteriet: CC0; Kartverket: CC BY 4.0 with attribution — corrected 2026-08-05, research/research.md) removes the legal risk that blocks this kind of aggregation in the US/DACH (closed AllTrails/Komoot ToS). **Caveat**: this holds for trail/basic-hut-location data from Kartverket and Lantmäteriet. It does not yet hold for DNT/UT.no's operational hut data (bed availability, booking status, opening dates) — see Open questions below.
- Nordic *allemansrätten* culture already normalizes multi-day trekking with clear camping rules — a ready use case, not an invented one.
- The giants are already investing in an AI layer (proven product-market fit for the pattern), and the Alps prove the hut-integrated multi-day pattern itself works at scale — but nobody covers Nordic hut logistics, and nobody has made it generative. That is the specific, narrow, still-unclaimed gap in their own roadmap.

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
- **The real NTB schema is public — shape mock data to it** (found 2026-08-05). DNT's own MIT-licensed engineering org, [github.com/Turistforeningen](https://github.com/Turistforeningen), contains `Hytteadmin` / `Turadmin` — "publication and administration tool for cabins/trips on UT.no **and Nasjonal Turbase**". `client/app/models/cabin.js` gives the actual field names and enums: `betjeningsgrad` (Betjent/Servering/Selvbetjent/Ubetjent/Dagshytte/Nødbu/Stengt), `NØKKEL_CHOICES` (Ulåst/Spesialnøkkel/DNT-nøkkel), `senger` `{betjent, selvbetjent, ubetjent, vinter}`, `privat.åpningstider` (`helårs`/`fra`/`til`), a `Booking` flag in `fasiliteter`, `hyttetype` (DNT/Rabatt/Privat), `geojson`, `fylke`, `kommune`, `juridisk_eier`, `tilrettelegginger`. Use it **only to shape the mock layer** — not to work around the closed access, and not from old data dumps.
- **Integration is deferred by decision (2026-08-05)**, treated as a future commercial conversation rather than a technical blocker — DNT closed NTB for economic and security reasons and that is accepted. Two rules follow: the demo must never present live availability as real (label mock data, and show the "degrade honestly" principle in the UI itself), and the pitch must name the data dependency **on the slide, not in an appendix** — framed as "requires a data agreement with DNT/STF, a commercial conversation." A buyer with distribution obtains such an agreement far more easily than we can, which is part of the reason to buy; a buyer who discovers the dependency alone reads the demo as misleading.
- **Only one parameter is actually blocked.** Key type, bed capacity, opening season and the bookable flag are *static* attributes with a public schema — and those are what the four-variable guarantee formula needs. So Top Job #1 is buildable almost entirely without integration. The single blocked item is live availability ("how many beds are free on 14 August"), which matters least in a demo (the date is illustrative) and is exactly what the buyer's agreement unlocks.
- **Interface pattern: wizard as the spine, conversational layer on top** (decided 2026-08-05, research.md "Питання 3"). The wizard stays because a live acquisition demo must not improvise and it maps 1:1 to the input schema above; a conversational refinement layer sits over the *already generated* plan ("make day 3 shorter", "we need a hut with a shower"), which keeps it constrained yet current. Pure-form-only was rejected: all four AI players in the category went conversational (Google "Ask Maps", AllTrails-in-Claude, Komoot in ChatGPT, Outdooractive Tourism AI), and a buyer judging whether our tech leads theirs would read a bare form as behind.
- **Packaging**: a full standalone app (own name, icon, onboarding → itinerary flow) — see "Packaging decision" under Business model. Design and build accordingly (concept/wireframes should assume a complete app, not an embedded widget).
- **Three scope decisions taken during the sitemap phase (2026-08-05) that this file did not previously record** — all three are in the v1 build, all three came from evidence rather than from this spec:
  - **A thin in-trip layer, not planning only.** v1 ships two in-trip screens (today's leg + "what changed and what can still be done"). The mechanism is not notification-at-breakage but **lead time**: the signal must arrive while an alternative still exists. Consequence for the still-open tech-stack question: **offline and battery economy are stack-forcing requirements, not nice-to-haves** — Swedish hikers abandoned Lantmäteriet's own official app precisely because it lost offline on iOS, and DNT/NRK make offline-first mandatory.
  - **A community layer.** Field notes on *conditions* (trail state, actual waymarking, water, snow, on-site weather) as an explicitly separate, labelled source tier.
    ⚠️ **Revised 2026-08-13 (decision #21).** This bullet used to read "**not ratings, not reviews**". After auditing our own framework against the five hard competitors, that exclusion did not survive: the argument against ratings was never "no need" — S2 ("is this realistic for someone like me") stands on exactly this — it was **risk of blurring source traceability**. The risk is real, so it is now held by **four explicit boundaries** rather than by the absence of the entity: a rating never feeds the coherence verdict, never alters the official grading, **never sorts routes** (order comes from fit to the brief, not popularity), and a review (opinion) is a different object from a field note (condition). Photos are in for the same reason: the original objection was **no source**, not harm — so every photo now carries its source, licence and tier on the image itself, which turns it into evidence of traceability instead of a threat to it.
    The field-note half of this layer keeps its original justification, which is not the social job but a hole in our own main asset: official trail data diverges from the terrain in both directions, and no official dataset can close that by definition. Demo rule: notes are curated and labelled illustrative, under the same rule as mock hut data — invented "user reviews" in a buyer demo would be exactly the antipattern we criticise competitors for.
  - **An account exists in v1, but is not the entrance.** It is storage for a credential (membership, key), a gear inventory and the accumulating booking-completion state — not a preferences screen, and not personalisation (the wizard covers that within a session). Registration never stands in front of the generated plan: the demo starts with the substance, not with a signup form.
- **Tech stack**: not yet decided — deferred to the research phase (`research/`), which should include a stack evaluation before it's locked in.
- **UI language**: **Ukrainian during design (changed 2026-08-13)**, English at productisation. The earlier "English, because the audience is an international acquisition target" rested on pitch logic, which is no longer the basis for product decisions. Wireframes and product copy are written in Ukrainian so the team writes them for real rather than translating them; the finished product gets translated when there is a finished product to translate. Source-language terms (`Selvbetjent`, `fjällstuga`, `betjeningsgrad`, place names) stay in the original either way.
- **Timeline**: no hard deadline — iterate phase by phase.

## Core user flow

**Input**, in this order — **corrected 2026-08-13**: **first the route** (region + rough month → a map showing only the routes that fit, named ones alongside ones assembled for the brief; the person picks one), then the time window (with a "dates don't move" flag, desired duration, spare day), then everything about the person (fitness, existing gear, lodging regime + association membership, optional budget).

The order matters and the earlier version had it wrong. A named route used to be an *optional field* buried in the middle of the wizard, which meant the product chose where the trip happens **without the person seeing it** — and "route, lodging, gear and weather agree" is worthless if the four agree around a trip nobody picked. Route selection is now the product's first question. The guard that keeps this from becoming AllTrails: it is a **step in the funnel, not a navigation root**, it shows only what fits the brief rather than everything in the region, and it carries no ratings, popularity, top-10 lists or photo cards (`wireframes/sitemap.md`, entity 20 and decision #20). **Budget is an optional input** — decided 2026-08-06: no persona and no research documents a pain around it (jtbd.md H3), so it stays available but never blocks the path to a plan.

**Output**: multi-day itinerary — daily walking legs, matched overnight stays (DNT huts/campsites), a gear checklist, weather-driven adaptation per day, **transport legs to the trailhead and back (R6)**, and **a list of what still has to be actually booked, in order, with deadlines and handoff to the official systems (R7)** — we guide and hand off, we never run the transaction.

**Two output surfaces are obligations, not features** (added 2026-08-06, `wireframes/sitemap.md` entity 14): the ©Kartverket attribution string (legally required by CC BY 4.0) and the "illustrative mock data" label must be **visible on the happy path** — not only in a degraded state, and not buried in a separate "about the data" screen.

**Refined 2026-08-13 (UX review, decision #17)**: "persistently visible" was collapsing the two obligations into one banner, and a banner that is always on screen stops being read — which defeats the purpose of the mock-data label specifically. They are now split by nature: **©Kartverket stays compact and permanent in the chrome** (the legal requirement is about presence), while the **"illustrative data" label moves onto the field it applies to** — the bed-availability line on B3, the field notes on B7 — where it is new information every time it appears rather than wallpaper.

**A third honesty obligation, found the same day**: met.no's forecast horizon is ~10 days, and the primary persona plans months ahead. Outside that horizon the plan shows a **seasonal normal, explicitly labelled as a normal and excluded from the coherence verdict** — never a forecast-shaped number. The product then returns on its own with the real forecast ~10 days out, which turns the gap into the R3 lead-time mechanism rather than a hole.

## People & top jobs

Full detail, sourcing, and the second persona: [concept/personas.md](./concept/personas.md), [concept/jtbd.md](./concept/jtbd.md). Every claim behind them audited against primary sources in [concept/personas-audit-2026-08-05.md](./concept/personas-audit-2026-08-05.md) — read that before designing on any of this.

**Structure (revised 2026-08-05)**: **two** personas, not four. The Swedish/STF persona and the "novice" persona were demographics and a psychographic state, not distinct behaviours — both had zero jobs of their own and folded into axes. Two axes carry what they used to: *lodging regime* (country × object type × booking × arrival time) and *first multi-day trip vs. repeat*.

**Primary persona**: Kristin, 34, association member (DNT in Norway, STF in Sweden) — experienced, takes regular multi-day mountain trips. Even with full institutional knowledge of the system, she still has to be her own "integration layer" across the association's own disconnected tools (route planning vs. hut booking) — and DNT's own booking flow makes her do one transaction per hut in a chain. Proof this pain is structural, not a novice problem.

**Second persona**: Lukas, 29, foreign visitor planning a trip into a lodging system she doesn't know — genuinely different jobs (translate the system, fit the route into an already-booked travel window). Evidence base upgraded 2026-08-05: an academic field study of DNT cabins and foreign visitors (Westskog/Leikanger, UiO + Aase, UiB, 2021) plus the first dated account of a foreigner who actually stayed in DNT huts (2022).

**Pitch-relevant finding from that study**: what a foreign visitor actually lacks is not the hut taxonomy but the **unwritten rules** (cleaning up, boots off, how sleeping space is divided, the honor-system premise) — plus the fact that self-service hut information exists only in Norwegian. None of that lives in any API, open or closed. It is a culture-and-language layer written by hand once — cheap for us, and DNT's own Secretary General is on record calling it their unsolved problem. That makes it an argument *for* the DNT pitch, not just a feature.

**Main job**: *When I plan a multi-day mountain trip, I want to be confident that route, lodging, gear, and weather agree with each other, so I'm not the one reconciling four disconnected sources myself.*

**Top 3 jobs for MVP** (each with its live risk — none is settled):
1. Know exactly what's needed for each night's lodging — the core differentiator vs. Komoot's/AllTrails' generic lodging. ✅ **Content verified and closed 2026-08-05** against Norwegian- and Swedish-language primary sources (the English pages of both associations omit exactly what matters). Both countries share one principle: **booking buys a guaranteed bed; no booking still guarantees indoor space, possibly a floor mattress — nobody is turned away.** The answer for any given night is a function of **object type × booked or not × arrival time (18:00 in Sweden) × membership**. That four-variable formula is the sharpest form of our differentiator: a generic lodging suggester cannot express it. Also: not all beds at a hut are pre-bookable (some held for drop-ins), the DNT key is members-only (a 100 NOK deposit, not a walk-up price — thelocal.no had this wrong), and a logbook entry with membership number is required even after booking online. Full table: `concept/personas.md`, Ось A. Rule going forward: **verify lodging rules in Norwegian and Swedish; treat the English pages as incomplete.**
2. Learn how a change in the weather forecast affects the plan already made — the other differentiator named in the elevator pitch above. ⚠️ Thinnest evidence of the three: no first-hand account of how anyone reacts to a forecast change mid-trip.
3. Understand why the plan makes each choice it makes. ⚠️ **Downgraded 2026-08-05 from "backed by national AI-trust data" to "our bet".** Norwegian/Swedish media checks found **no Scandinavian AI backlash at all** — neither DNT, Røde Kors, nor Sweden's Fjällsäkerhetsrådet has published any warning about AI-planned routes. The AllTrails/SAR criticism we built a defence against is a Canadian event with no Nordic counterpart. Keep the named-contributor mechanism (cheap, harmless, and we can set the standard first), but do not rest positioning on it.

**Two more jobs, found after this list was written — and neither came from this file** (2026-08-06, [concept/jtbd.md](./concept/jtbd.md), [wireframes/sitemap.md](./wireframes/sitemap.md)). This matters for the pitch: the five jobs above map 1:1 onto the input/output fields of this spec, i.e. they were derived from the product idea and evidence was fitted to them afterwards. These two ran the other way — evidence first.
- **R6 — transport to and from the trailhead.** Three independent Swedish voices in a single week, including one documented case of a hiker *abandoning the region* over it, and a trailhead (Katterat) with no road access at all, so replacement buses are physically impossible. This is the strongest fresh evidence in the entire research, and it is also the best real-world illustration of the live-re-sync mechanism: what the hiker needed was not a cancellation notice, but a signal a day or two earlier, while turning off toward Riksgränsen was still an option.
- **R7 — getting the plan to actually-booked nights.** DNT's own chain booking is N sequential transactions ("you must complete the booking and payment for one cabin before proceeding to the next"), and a logbook entry with a membership number is required even after paying online. Nestwood gives ordering, dependencies, deadlines and handoff — **it does not run the transaction** (research §2: orchestration layer, no legal liability for bed availability).

**What replaces it as the institutional argument** — named, dated, and publicly stated by two of our four acquisition targets, four days before this was written: Røde Kors and DNT say foreign visitors *misjudge difficulty, distance, elevation gain, how fast the weather turns, and how much steeper/wetter/rougher Norwegian terrain is* — attributed partly to social-media images. DNT's own stated remedy is **"turveiledning og informasjon på flere språk"**, and Røde Kors is calling for joint *fjellvett-opplysning* with DNT and the police. That is close to a description of this product. Source: [NRK Vestland, 2026-08-01](https://www.nrk.no/vestland/turister-far-trobbel-pa-tur-i-fjellet-i-norge---rode-kors-og-dnt-vil-se-pa-fjellvett-tiltak-1.17970478). So the real hook is **preparedness and language, not AI transparency.**

**Hard constraint from the same source**: DNT wants the *single national difficulty grading* kept and explicitly does not want alternative systems. Nestwood therefore surfaces the official Norwegian grading and must not invent its own fitness→difficulty scale — personalise the *selection* of a route, never the *rating* of it. Also, per [NRK 2026-08-05](https://www.nrk.no/vestland/telenor-ut-mot-dnt-etter-redningsaksjonar-i-fjellet_-_-marknadsforer-omrade-utan-dekning-1.17973749): offline-first is mandatory, and "share your route and expected return time" is a feature DNT itself recommends.

## 🔴 Business-model risk found 2026-08-05 — settle the pitch narrative before contacting DNT

Foreign tour operators are charging clients 20,000+ NOK while using DNT cabins **without booking, registration, or payment** (one Swedish operator arrived at Cunojávrihytta with 8 tourists and 50 sled dogs, unannounced). Jon Sommerseth, director of DNT Narvik: *"Det provoserer at vår frivillige innsats skal være grunnlag for kommersiell drift hos andre."* **From 2027 Troms Turlag bans all commercial use of its huts**, and DNT centrally calls this a growing problem. Source: [NRK Nordland, 2026-02-20](https://www.nrk.no/nordland/mener-dnt-hytter-misbrukes-av-turoperatorer_-_-det-provoserer-1.17771097).

A commercial AI layer that routes foreign visitors into DNT huts sits structurally next to exactly what is provoking DNT right now: outside parties monetising volunteer-maintained infrastructure. Pitching "we will bring you tourists" hits that nerve directly. The same fact supports a stronger framing: Nestwood as the layer that makes this traffic **register, book, and pay correctly** — an ally against the abuse rather than another instance of it. Choose this narrative deliberately, before the first DNT contact, not during it.

## Information architecture

Full detail: [wireframes/sitemap.md](./wireframes/sitemap.md) (entities, screen tree, navigation, traceability), [wireframes/flows.md](./wireframes/flows.md) (six flows with decisions, states and dead ends), [wireframes/ia.html](./wireframes/ia.html) (rendered readout). **23 entities → 23 screens → 12 jobs, and the matrix is closed in both directions**: no job without a surface, and every screen without a job has a named non-job reason.

**Top-level sitemap** — seven clusters, derived from jobs rather than from competitors' structure. **Revised 2026-08-13 (decision #21)**: there is still no trail catalogue as a *navigation root*, but there is now a **curated route-discovery cluster and a route card with photos and ratings** — the boundary moved from "we don't have this object" to "we have it under four explicit rules". What holds the line is curation (10–20 multi-day routes per country, not a trail database) and ordering by fit to the brief rather than by popularity:

- **G · Where to go** — G1 curated regions · G2 route card (map, profile, conditions, huts, photos, reviews) · G3 the map surface. Exists because the funnel used to start by asking "region and month", i.e. it worked only for someone who already knew where they wanted to go.
- **0 · Entry** — start screen. The one screen with no job behind it; it exists because of the standalone-app packaging decision, and its scope is frozen.
- **A · Wizard** — nine input steps packed onto three screens: *Route* · *When and how many of us* · *About me*. Group size is a required field (booking is N beds, not "a place"); flexible dates open a week-by-week grid when the window can move; budget stays optional.
- **B · The plan** — B1 day-by-day plan (MAIN) → B2 day → B3 night: guarantee and access · B4 how this lodging system works · B5 gear checklist · B6 transport · B8 the chain of nights · B7 field notes.
- **C · Make it real** — C1 what still has to be booked, in order and with deadlines · C2 membership and key.
- **D · The plan is live and the world changed** — D1 today (in-trip only) · D2 what changed and what can still be done.
- **E · Show someone** — shareable summary, in two registers: trust for family, and the safety share DNT itself recommends.
- **F · Mine** — saved trips, gear inventory, profile. The account is storage for a credential and accumulating state, never an entry gate.

**Main flow**: start → three wizard screens → generation → **B1, where route, lodging, gear and weather are visible together** → per-day drill-down → either C1 (book it) or E (share it). If a non-critical source is unavailable the plan is still generated and says what is missing; if a critical one is, the plan is not faked — the user goes back and changes region or dates.

**Global navigation — four entries plus one conditional**, each an entry into a job cluster rather than a content section: **План** (MAIN) · **Ночівлі** (R2, the chain of nights — DNT books them one transaction at a time) · **Закріпити** (R7, the only counter in the product) · **Моє** (credential + inventory) · **Сьогодні** (R3/R6, appears only in the in-trip state and then takes over as home). Transport and gear deliberately stay contextual: strength of evidence is not frequency of access.

**Depth to the main job**: **0 taps** with a saved trip · **3 taps** for the primary persona starting a new one (the account prefills two of the three wizard screens) · **4 on a cold start and in the buyer demo**. The fourth tap is not cut on purpose — reaching three would mean generating before we know membership, which is variable #4 of the guarantee formula, so the differentiator screen would open degraded on its first render. Four is the ceiling. Everything else is within 2 taps of home.

## Non-goals for now

- Not building a standalone consumer venture or growth loop — the demo is a full app by packaging (see Packaging decision), but the business model stays acquisition-target, not an independent product with its own GTM.
- Not wiring up live third-party APIs yet (mock data shaped like real responses instead).
- Not covering regions outside Scandinavia.
- Not becoming a trail database or a discovery product: the route-discovery cluster is **curated and bounded**, and nothing in the product is ordered by popularity.

## Repo / workflow structure

Repo was just cleared for this restart; the previous project's phase pipeline is being reused for this new product:

- `concept/` — problem framing, personas, scenarios
- `research/` — competitor audit, data source research, benchmarks, patterns
- `design-system/` + `tokens/` — visual language, design tokens
- `wireframes/` — low/mid-fidelity flows **and the drawn screens themselves**
- `components/` — built UI components
- `handoff/` — engineering handoff docs

## Wireframes

**Complete as of 2026-08-14: 59 pages — all 23 sitemap screens plus 36 states. No screen is left undrawn.** Greyscale, semantic HTML, real Ukrainian domain copy, no colour, icons, images, JS or libraries.

**The contract, not the pictures, is the artefact.** [`wireframes/_conventions.md`](./wireframes/_conventions.md) fixes the rules every screen obeys — detail level, semantic markup, file naming, the closed state vocabulary, and the three kinds of review chrome. It exists because the set was drawn partly by parallel subagents: with the contract they cloned one pattern instead of inventing six.

Four things worth knowing before touching this folder:

1. **A state is a separate page, never a variant appended at the end.** Same landmarks, same section order, same headings — only content differs. The states are `empty · error · loading · offline · degraded · conflict · seasonal · nooptions`, and the vocabulary is closed: a state outside it is a change to the sitemap, not a new filename.
2. **Every state has a named exit, and no link is broken.** A target that isn't drawn yet renders as inert text, never as a dead `href` — a 404 is exactly the dead end the flows forbid.
3. **Structure is regenerated, not copied by hand.** `_generate.py` holds `TREE` (sections → screens → states) as the single source; `_refresh.py` rewrites the navigation tree and the state row across all pages; `_audit.py` checks structure, zones, semantics, colour, attribution, broken links and dead ends, and must print zero.
4. **Two obligations are visible on every page**: the ©Kartverket attribution in the footer (CC BY 4.0, a legal requirement, not a credit) and the mock-data label **on the field it applies to** — the bed-availability line — never as chrome.

The audit trail is in [`wireframes/_screens.md`](./wireframes/_screens.md) (which states are real and why), [`wireframes/_gaps.md`](./wireframes/_gaps.md) (what the framework was missing against five competitors) and [`wireframes/_critique.md`](./wireframes/_critique.md) (the final pass: four defects found and fixed, and why "deferred" only differs from "lost" if it is written down).

**UI language of the wireframes is Ukrainian** — see the note under Scope for v1.

## Tech stack

Decided 2026-08-06 against the evidenced constraints, not against build convenience. Full evaluation: [research/research.md](./research/research.md) §7.

| Layer | Choice | Why this one |
|---|---|---|
| App shell | **Next.js (App Router) on Vercel**, TypeScript | The AI call needs a server side (the API key can't live in the browser) and met.no requires caching per its `Expires` header — both belong in route handlers next to the frontend, one repo, one deploy. A buyer opens the demo from their phone by link |
| Maps + offline | **MapLibre GL JS + PMTiles stored in OPFS** | PMTiles is one file per region served by byte range; OPFS gives near-native performance for large files in the browser. Explicitly suited to a bounded regional dataset on static hosting — which is exactly our scope |
| Packaging | **PWA now, written to be wrapped in Capacitor later** | Keeps "mobile-first web" while leaving a native path open. The wrap removes the buyer's most likely objection ("how does it behave in the mountains") without rewriting the product |
| Data | **Adapter interfaces** (`LodgingSource`, `WeatherSource`, `TransportSource`, `RouteSource`) with mocks shaped like real NTB / met.no / Entur responses | This is the swap-without-rewrite requirement made concrete. After the source audit, three of the four adapters could be implemented for real today |
| Persistence | IndexedDB for plan, gear inventory and booking-completion state; Service Worker for the shell | These are exactly the things that must survive a closed tab (account decision) |
| AI | **`claude-opus-5`** — structured outputs to the plan schema, grounding via tool use over the adapters, prompt caching for the stable system prompt and reference tables, streaming generation | Structured outputs bound improvisation **by schema rather than by hoping the prompt holds** — which is what makes a live demo safe. Tool use over adapters is the orchestration layer we're actually selling |

**Three consequences to design around, not discover later:**

1. **Offline has a ceiling, and it must be designed rather than declared.** iOS evicts PWA storage under memory pressure; the seven-day script-writable cap does not apply to *installed* PWAs, and Safari 17+ offers the Persistent Storage API — but there is never a guarantee. So v1 promises **"an offline pack for this route"** — a screen, a state and a size in megabytes the person can see — not "offline everywhere". Anything stronger repeats the exact failure we cite as the pain (Swedish hikers left Lantmäteriet's own app when it lost iOS offline).
2. **Installing the PWA is part of the flow, but not of the entrance** — because the offline cache's survival on iOS depends on it, we need the install, but asking for it before the person has received anything is the same antipattern as putting registration in front of value. **Corrected 2026-08-13 (UX review, `wireframes/sitemap.md` decision #14)**: the earlier version put the install on the start screen as a deliberate exception to its zero-functional-elements freeze. That exception is **withdrawn** — the prompt now lives on B1, next to the offline pack, where it becomes a means rather than a request, and the start screen is back to zero.
3. **We must generate our own PMTiles from downloadable datasets.** Kartverket's zoom levels 12–20 come from the Geovekst cooperation and need the licensees' separate permission to copy, so packaging offline tiles by pulling their cache service is not open to us. Unplanned work that sits between us and the first offline demo.

**Demo rule**: generation is live (a real `claude-opus-5` call), with a pre-generated plan held in reserve against bad conference-room wifi. A scripted demo would collapse the moment a buyer asks to enter their own dates — and "a working prototype, not a mockup" is the whole pitch.

## Key external data sources

All verified by direct request on 2026-08-06 — licence, key requirement and liveness. Full detail, quoted terms and query results: [research/research.md](./research/research.md), "Решта джерел під продуктом".

| Need | Norway | Sweden |
|---|---|---|
| Maps, terrain | Kartverket — CC BY 4.0, ©Kartverket attribution **mandatory in the UI** | Lantmäteriet — CC0 |
| Trails **+ the official difficulty grading as a field** | Turrutebasen (Kartverket) — open, live WFS | Lantmäteriet / Naturvårdsverket |
| Weather | met.no Locationforecast 2.0 — CC BY 4.0, no key | SMHI `snow1g` v1 — CC BY 4.0 SE, no key |
| Transport to and from the trailhead (R6) | Entur JourneyPlanner v3 — NLOD, **no key**, `ET-Client-Name` required | ResRobot v2.1 (CC0, key) + Trafikverket (CC0, key) |
| Road access to a trailhead / station (entity 19) | NVDB API Les v4 — NLOD, no auth, `X-Client` required since 2026-01-05 | Lantmäteriet CC0, but bulk download + account |
| Avalanche danger | NVE Varsom v6.3.0 — NLOD | lavinprognoser.se (Naturvårdsverket) — CC0, six areas only |
| Live bed availability | **DNT / NTB — closed.** Commercial agreement, not a technical blocker | STF — closed |
| Mobile coverage as a spatial layer | **Does not exist as reusable data** — Nkom publishes per-household XLSX | Same — PTS publishes per-municipality Excel |

**Three things to carry into the pitch and the build:**

1. **Exactly two classes are blocked**: live bed availability, and mobile coverage as a geographic layer. Everything else — weather, transport, road access, avalanche, trails with official grading — is open with commercial use permitted. Say "one blocked field in the hut data", not "one blocked field in the product".
2. **R6 is now provable on the exact case it came from.** Katterat is in Entur as `NSR:StopPlace:58610` with a `cancellation` field, and NVDB returns **zero road segments** around it against fifteen at the neighbouring station — so "you can walk in but no bus can reach you" is computable from open data, with no key and no agreements.
3. **Sources move.** One audit turned up two switched-off APIs (SMHI `pmp3g`, killed 2026-03-31; NVDB v3 being decommissioned) and one new mandatory header. Multi-provider fallback is a response to a documented rate of change, not architectural taste.

## Open questions for the research phase

- **~~⚠ Highest priority~~ → RESOLVED as a working assumption, 2026-08-05.** DNT closed the previously-open Nasjonal Turbase (NTB) API — verified directly (uniform 404 across all documented endpoints; the root domain no longer resolves) and via DNT's own open-data page ("for economic, security, and strategic reasons"). **This is no longer treated as a blocker**: integration is deferred by decision, the schema is public (see Scope for v1), and only live availability is actually missing. It no longer blocks the tech-stack decision. What remains open is the *commercial* conversation, and it belongs to whoever acquires this — see the two disclosure rules under Scope for v1.
- ~~Final tech stack for the mobile-first frontend.~~ → **DECIDED 2026-08-06.** See "Tech stack" below; full evaluation in [research/research.md](./research/research.md) §7.
- Visual/brand direction — the previous cycle had settled on a light Scandinavian-minimalist style; evaluate whether it carries over to Nestwood. **Now has a hard constraint that rules out the obvious answer** (found 2026-08-06): green, blue, red and black are already taken by the official Norwegian grading — verified verbatim on DNT's own support pages: **grønn = enkel · blå = middels · rød = krevende · svart = ekstra krevende**, plus a fifth marker, *Godt tilgjengelig*. We committed to surfacing that grading and never inventing our own, so those four colours **mean route difficulty inside our UI** and cannot simultaneously mean brand, success or error. This kills the default: light Scandinavian minimalism almost always lands on a muted green accent — as our own `design-system/docs/doc.css` does — and in the product a green accent would read as "easy route". The brand accent is **deferred by decision, not forgotten**; whatever it becomes, it comes from outside those four hues.
- **Deliberate consequence of the offline decision**: the in-trip screen (D1) is used outdoors in sunlight and must save battery. That is not the same layout in a light theme — it argues for a dedicated in-trip mode (dark, high contrast, large type, minimal repaint) rather than one aesthetic everywhere. Settle this with the visual direction.
- Concrete demo scenario and success criteria to use when pitching to acquisition targets.
- App identity for the standalone packaging — name (working assumption: Nestwood), icon, and onboarding tone — to settle during concept/design-system phases.
