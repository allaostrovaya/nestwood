# Nestwood

AI multi-day itinerary layer for Nordic outdoor trekking. Mobile-first web, adapting to desktop later.

## Elevator pitch

Google Maps, Komoot, and AllTrails have all shipped AI route/trip features — Komoot's Multi-Day Planner auto-splits a route into stages and suggests lodging, and AllTrails-in-Claude generates multi-day itineraries with packing lists. None of them is generative *and* grounded in official hut infrastructure data (bed availability, keys, opening dates) *and* weather-adaptive day by day, in one flow.

**The claim has to be narrow to survive a buyer's first question.** "Nobody pairs generative AI with official hut data" is too strong: in the Alps that pairing minus the generative layer **already exists and is monetised**: the four alpine clubs (DAV, ÖAV, SAC, AVS) run *Hut Reservation* — 500+ huts, ~1.5M bookings a year — its availability calendar is embedded directly in the alpenvereinaktiv.com tour portal, and *Bettencheck* shows bed availability across an entire multi-day route. That portal runs on Outdooractive's white-label technology, i.e. on the very precedent we cite for our own business model.

So the honest, defensible claim is narrower and stronger: **the pattern is proven at scale in the Alps; the Nordics have no equivalent, and nobody anywhere has made it generative.** That reframes Nestwood from "new product" to "a validated pattern moved into an unoccupied region" — weaker on novelty, much stronger on feasibility, and it is the framing to use in the pitch.

Nestwood is the AI-orchestration layer that does this, grounded on official open government geodata for Sweden and Norway (Lantmäteriet — CC0; Kartverket — CC BY 4.0, commercial use expressly permitted; DNT/UT.no) — without depending on AllTrails'/Komoot's APIs or ToS for the *trail/basic-hut* data (see the caveat on DNT/UT.no's operational hut data under "Why now, why here").

**Competitive risk, in its sharper shape**: Outdooractive is our precedent *and* a competitor, but on a different axis than first feared. It is already in Scandinavia — a partnership with Visit Group as map/routing provider, a customer base in Denmark, Sweden and especially Norway, and the Geilo project as its reference — but that is destination/DMO technology, **not hut booking**, and there is no evidence of any Outdooractive–DNT link. DNT builds ut.no itself (with Statskog, Friluftsrådenes Landsforbund, Miljødirektoratet, Kartverket; Atea as IT partner) and runs its own public engineering org. An alpine club handed its portal to a white-label vendor; DNT most likely will not.

**So the real risk is that DNT builds this itself** — it has the platform, the data, the engineers, and a publicly stated need. That makes the pitch to DNT one about *speed*, not about owning unmatchable technology. Per-buyer entry points: **DNT** — "you have everything except the generative layer and the multilingual guidance you said you need"; **AllTrails / Komoot** — "Nordic hut logistics is a moat you cannot build from community data"; **Google** — "a concrete vertical case for your existing grounding pattern".

## Problem

A hiker stitches a multi-day trip together by hand across disconnected sources: track in one tool, lodging in another, weather in a third, gear from experience/forums. 2026's AI features from the giants solve only the first slice (single-day route/search) — the multi-day planning gap remains open.

## Solution

An AI agent that takes fitness level, budget, time, existing gear, and preferences as input, and outputs a full personalized multi-day itinerary: daily walking legs, matched overnight stays (DNT huts/campsites), a gear checklist, and day-by-day adaptation to the weather forecast. Technically, this is a grounding layer (in the spirit of Google's Travel Concierge / ADK patterns) over Kartverket/Lantmäteriet/UT.no open data — not a proprietary geo database.

## Why now, why here

- Open Nordic government data (Lantmäteriet: CC0; Kartverket: CC BY 4.0 with attribution) removes the legal risk that blocks this kind of aggregation in the US/DACH (closed AllTrails/Komoot ToS). **Caveat**: this holds for trail/basic-hut-location data from Kartverket and Lantmäteriet. It does not yet hold for DNT/UT.no's operational hut data (bed availability, booking status, opening dates) — see Open questions below.
- Nordic *allemansrätten* culture already normalizes multi-day trekking with clear camping rules — a ready use case, not an invented one.
- The giants are already investing in an AI layer (proven product-market fit for the pattern), and the Alps prove the hut-integrated multi-day pattern itself works at scale — but nobody covers Nordic hut logistics, and nobody has made it generative. That is the specific, narrow, still-unclaimed gap in their own roadmap.

## Business model

Not a standalone venture (small, infrequent market, weak moat) — a feature-pitch / acquisition target for a player with distribution:

- **AllTrails / Komoot** — regional Nordic expansion + multi-day extension of their already-shipped AI assistant
- **Google Maps Geospatial AI agents team** — a concrete vertical use case for an existing grounding pattern
- **DNT/UT.no** — a non-profit-funded AI layer over their own hut/trail infrastructure, no venture model needed

What makes this pitchable rather than just an idea: a working prototype on real, legally accessible data (not a mockup) — concrete proof that the multi-day-orchestration layer is technically and legally feasible exactly where AllTrails/Komoot haven't gone.

**Packaging decision**: the demo is built and presented as a full standalone app — own brand, icon, and complete flow from onboarding to a finished itinerary — not a partial feature bolted onto someone else's UI. This doesn't change the business model above; it's the same feature-pitch/acquisition play, just packaged as convincingly as possible. Precedent from our own research: FatMap was a complete standalone app before being acquired by Strava, not a pitch deck. The one thing to keep explicit in the actual pitch narrative: this is a demo vehicle, not a go-to-market — otherwise a buyer might read "fully working app" as "why acquire instead of competing," rather than "technology ready to integrate."

## Target audience for the current prototype

External pitch to acquisition targets (AllTrails, Komoot, Google's Geospatial AI agents team, DNT/UT.no). This shapes what the prototype needs to prove: legal cleanliness of the data, technical soundness, and a clear, specific gap versus what the giants already shipped — not consumer growth metrics.

## Scope for v1

- **Geography / data**: Scandinavia — Norway (Kartverket + UT.no/DNT hut and trail data) and Sweden (Lantmäteriet), pitch-driven rather than phased by country.
- **Fidelity**: hybrid — a working frontend backed by mock data shaped like the real Kartverket/Lantmäteriet/UT.no API responses. No live integration yet; the mock layer is shaped so a real integration can be swapped in later without a rewrite.
- **The real NTB schema is public — shape mock data to it.** DNT's own MIT-licensed engineering org, [github.com/Turistforeningen](https://github.com/Turistforeningen), contains `Hytteadmin` / `Turadmin` — "publication and administration tool for cabins/trips on UT.no **and Nasjonal Turbase**". `client/app/models/cabin.js` gives the actual field names and enums: `betjeningsgrad` (Betjent/Servering/Selvbetjent/Ubetjent/Dagshytte/Nødbu/Stengt), `NØKKEL_CHOICES` (Ulåst/Spesialnøkkel/DNT-nøkkel), `senger` `{betjent, selvbetjent, ubetjent, vinter}`, `privat.åpningstider` (`helårs`/`fra`/`til`), a `Booking` flag in `fasiliteter`, `hyttetype` (DNT/Rabatt/Privat), `geojson`, `fylke`, `kommune`, `juridisk_eier`, `tilrettelegginger`. Use it **only to shape the mock layer** — not to work around the closed access, and not from old data dumps.
- **Integration is deferred by decision**, treated as a future commercial conversation rather than a technical blocker — DNT closed NTB for economic and security reasons and that is accepted. One rule follows: the pitch must name the data dependency **on the slide, not in an appendix** — framed as "requires a data agreement with DNT/STF, a commercial conversation." A buyer with distribution obtains such an agreement far more easily than we can, which is part of the reason to buy; a buyer who discovers the dependency alone reads the demo as misleading. **The disclosure lives in the pitch, not in the interface**: the screens are a prototype and are built to look like the product, not like a labelled mock-up. What the UI does keep is the "degrade honestly" principle — a source that is unavailable says so, which is real app behaviour rather than a mock-up marker.
- **Only one parameter is actually blocked.** Key type, bed capacity, opening season and the bookable flag are *static* attributes with a public schema — and those are what the four-variable guarantee formula needs. So Top Job #1 is buildable almost entirely without integration. The single blocked item is live availability ("how many beds are free on 14 August"), which matters least in a demo (the date is illustrative) and is exactly what the buyer's agreement unlocks.
- **Interface pattern: the catalogue is the spine. There is no wizard.** A wizard was tried and rejected: it puts a form in front of the value, and its first question — "region and month" — is one the second persona cannot answer, because Lukas does not know Norwegian regions. The entrance is a **curated multi-day route catalogue** — map plus list — where **the filters are the brief**: region, month, number of days, lodging regime. What the wizard used to ask is now split three ways: **derived from the filters** (never asked twice), **prefilled from the account** (fitness, membership, gear inventory), and **asked only as the remaining gap** — for a cold user that is group size and membership, one line on the route card, because those two change the *answer* rather than the sort order.
  The conversational refinement layer survives unchanged and still sits over the *already generated* plan ("make day 3 shorter", "we need a hut with a shower"). What killed the wizard was not fashion but four things that all point the same way: recognition beats recall; a question asked *after* commitment converts far better than the same question asked before it; every step of a pre-value form leaks; and in travel the pre-funnel wizard is extinct — Booking, Airbnb, Skyscanner and Komoot all run minimal input → results → progressive refinement. The pattern survives only where there is nothing to show and complexity is forced: tax filing, insurance, KYC.
  **What the inversion makes load-bearing.** With a catalogue as the entrance, "ordered by fit to the brief, never by popularity" stops being a declaration and becomes structural: **a filter exists only if it is simultaneously a plan parameter**, which disqualifies rating, popularity and top-10 by construction rather than by promise.
  **The one residual cost, accepted deliberately.** 9 ("this accounts for me, not generic advice") is no longer secured by asking up front. It is held instead by an invariant: **the plan always states the assumptions it ran on** — "for 2 people · 1 DNT member · medium pace — change" — editable in place. The same invariant serves 5.
- **The generative entry is a separate feature, not a fallback.** A catalogue can only show what someone has already named. The genuinely unique output of generation is the **route nobody named** — assembled from segments to fit five days, a chain of huts and August weather. Neither AllTrails nor Komoot can produce it from community data, because in a community graph an unnamed route does not exist. So it is a headline feature, not a consolation prize for a failed search. Two entrances: the **"nothing fits this brief"** state (which also gives our own former dead end a fourth exit) and the **profile**, for a repeat user who has already walked everything named in their region. It returns **the same object as the catalogue** — an ordinary route card labelled "assembled for your brief" — so the rest of the product is shared and no second screen tree exists.
  ⚠️ **Hard rule: an assembled route never leaves the officially marked network.** Not a technical limit — DNT and Røde Kors are publicly on record that visitors underestimate the terrain, so a product that draws a line across open country becomes precisely the thing our own pitch criticises. Consequence for the search: route-finding for us is a search over the **hut graph**, not over every trail vertex. DNT and STF huts sit roughly a day's walk apart, so the graph is sparse and the real problem is the *chain of nights*, not the geometry. Where the chain cannot close we say where the gap is and why — "38 km between Sitasjaure and Vaisaluokta is not a day's leg: tent on night 4 · different finish · +1 day" — which is an answer none of the five competitors gives.
- **Packaging**: a full standalone app (own name, icon, onboarding → itinerary flow) — see "Packaging decision" under Business model. Design and build accordingly (concept/wireframes should assume a complete app, not an embedded widget).
- **Three scope decisions that came from evidence rather than from this spec** — all three are in the v1 build:
  - **A thin in-trip layer, not planning only.** v1 ships two in-trip screens (today's leg + "what changed and what can still be done"). The mechanism is not notification-at-breakage but **lead time**: the signal must arrive while an alternative still exists. Consequence for the still-open tech-stack question: **offline and battery economy are stack-forcing requirements, not nice-to-haves** — Swedish hikers abandoned Lantmäteriet's own official app precisely because it lost offline on iOS, and DNT/NRK make offline-first mandatory.
  - **A community layer.** Field notes on *conditions* (trail state, actual waymarking, water, snow, on-site weather) as an explicitly separate, labelled source tier.
    **Ratings and reviews are in, under four explicit boundaries.** The argument against them was never "no need" — 11 ("is this realistic for someone like me") stands on exactly this — it was **risk of blurring source traceability**. The risk is real, so it is held by boundaries rather than by the absence of the entity: a rating never feeds the coherence verdict, never alters the official grading, **never sorts routes** (order comes from fit to the brief, not popularity), and a review (opinion) is a different object from a field note (condition). Photos are in for the same reason: the objection to them was **no source**, not harm — so every photo carries its source, licence and tier on the image itself, which turns it into evidence of traceability instead of a threat to it.
    The field-note half of this layer keeps its original justification, which is not the social job but a hole in our own main asset: official trail data diverges from the terrain in both directions, and no official dataset can close that by definition. Demo rule: notes are curated rather than invented — fabricated "user reviews" in a buyer demo would be exactly the antipattern we criticise competitors for. They are not labelled as illustrative inside the UI; that disclosure belongs to the pitch.
  - **An account exists in v1, but is not the entrance.** It is storage for a credential (membership, key), a gear inventory and the accumulating booking-completion state — not a preferences screen. The account is also the main source of **prefill for progressive profiling** — fitness, membership and gear inventory come from here, and that is what shrinks the cold-start question set to two fields. Registration still never stands in front of the generated plan: the product starts with the substance, not with a signup form.
- **Tech stack**: not yet decided — deferred to the research phase (`research/`), which should include a stack evaluation before it's locked in.
- **UI language**: **Ukrainian during design**, English at productisation. Pitch logic ("English, because the audience is an international acquisition target") is not a basis for product decisions. Wireframes and product copy are written in Ukrainian so the team writes them for real rather than translating them; the finished product gets translated when there is a finished product to translate. Source-language terms (`Selvbetjent`, `fjällstuga`, `betjeningsgrad`, place names) stay in the original either way.
- **Timeline**: no hard deadline — iterate phase by phase.

## Core user flow

**Input. There is no input *sequence*, because there is no form.** The product opens on the catalogue and collects what it needs in three ways at once:

1. **From the filters** — region, month, number of days, lodging regime. The person sets these to *browse*; we read them as the brief. Never asked a second time. This is what makes the rule "a filter exists only if it is simultaneously a plan parameter" enforceable.
2. **From the account** — fitness and pace, association membership, gear inventory. This is why the account exists (see Scope for v1).
3. **Asked, but only for the gap** — for a cold user with no account that is **group size and membership**, one line on the route card next to "make my plan". Those two are asked because they change the *answer*: a booking is N beds, gear is partly shared, and membership is variable #4 of the guarantee formula. Everything else defaults visibly rather than being asked.

**Exact dates are deliberately not asked up front.** Outside met.no's ~10-day horizon a date adds nothing a month does not already give (see the third honesty obligation below), and dates start to matter where booking deadlines do — so they are asked at "what still has to be locked in", not before the plan.

**The guard against becoming AllTrails is curation and order by fit to the brief** — not the absence of the object. The catalogue is the navigation root, so the boundary sits on the four explicit rules on it (`wireframes/sitemap.md`, entities 20 and 22). **Budget is an optional input**: no persona and no research documents a pain around it (jtbd.md H3), so it stays available but never blocks the path to a plan.

**Output**: multi-day itinerary — daily walking legs, matched overnight stays (DNT huts/campsites), a gear checklist, weather-driven adaptation per day, **transport legs to the trailhead and back (6)**, and **a list of what still has to be actually booked, in order, with deadlines and handoff to the official systems (7)** — we guide and hand off, we never run the transaction.

**One output surface is an obligation, not a feature** (`wireframes/sitemap.md`, entity 14): the ©Kartverket attribution string, legally required by CC BY 4.0. It stays compact and permanent in the chrome — the legal requirement is about presence, not prominence.

**The "illustrative data" label was a second obligation and is not one any more.** The screens are a prototype, and marking every field as mock made them read as a wireframe with annotations rather than as an app. The data dependency is still real and still has to be named — but in the pitch, on the slide, not on every bed-availability line. See the disclosure rule under Scope for v1.

**Difficulty has two different answers, and conflating them would break a hard constraint.** DNT is publicly on record that it wants the single national grading kept and no alternative systems, so we **surface the official grading and never compute our own** — personalise the *selection* of a route, never the *rating* of it. Two consequences that are easy to get wrong:

- **The official field is mostly empty.** `gradering` in Turrutebasen is filled for **1 of 92** foot routes in Jotunheimen, 28 of 59 on Hardangervidda, 64 of 137 between Narvik and Abisko. "Not graded" is the typical case, not an edge case, so any averaged 1–10 score would be computed from an absent field in most cases — invention, not interpretation. Where grading is missing we show the **measurements** (km, ascent, surface, exposure, fords) and let the person judge; those are commensurable across both countries, which the two national scales are not.
- **Load is a different object from terrain, and it is always computable.** "200 km in two days" is hard on flat ground, and that statement is about *the plan*, not about the trail — so it competes with no national system. Geometry and elevation are always present even when `gradering` is not, so this is the signal that fills the gap. It is computed with a **named published method, cited in the UI** — Naismith with Langmuir's descent correction, Tranter's fitness-and-load correction, or Munter — never with a formula of ours, which keeps it inside 5. Tranter takes pack weight, so **the gear checklist feeds the walking-time estimate**: two sources agreeing from the inside rather than by declaration. The load signal is the content of the coherence verdict, and "40 hours of walking in two days" is what makes the verdict a **conflict** with concrete exits.
  ⚠️ **The load signal must never use green / blue / red / black.** Those four are the official grading inside our UI; a load figure painted in them reads as terrain difficulty. Load is text and hours.

**A third honesty obligation, found the same day**: met.no's forecast horizon is ~10 days, and the primary persona plans months ahead. Outside that horizon the plan shows a **seasonal normal, explicitly labelled as a normal and excluded from the coherence verdict** — never a forecast-shaped number. The product then returns on its own with the real forecast ~10 days out, which turns the gap into the 3 lead-time mechanism rather than a hole.

## People & top jobs

Full detail, sourcing, and the second persona: [concept/personas.md](./concept/personas.md), [concept/jtbd.md](./concept/jtbd.md). Every claim behind them is audited against primary sources — the sourcing is inline in those two files.

**Structure: two personas, not four.** A Swedish/STF persona and a "novice" persona were considered and rejected — they were demographics and a psychographic state, not distinct behaviours, and neither had a job of its own. Two axes carry what they would have: *lodging regime* (country × object type × booking × arrival time) and *first multi-day trip vs. repeat*.

**Primary persona**: Kristin, 34, association member (DNT in Norway, STF in Sweden) — experienced, takes regular multi-day mountain trips. Even with full institutional knowledge of the system, she still has to be her own "integration layer" across the association's own disconnected tools (route planning vs. hut booking) — and DNT's own booking flow makes her do one transaction per hut in a chain. Proof this pain is structural, not a novice problem.

**Second persona**: Lukas, 29, foreign visitor planning a trip into a lodging system she doesn't know — genuinely different jobs (translate the system, fit the route into an already-booked travel window). Evidence base: an academic field study of DNT cabins and foreign visitors (Westskog/Leikanger, UiO + Aase, UiB, 2021) plus the first dated account of a foreigner who actually stayed in DNT huts (2022).

**Pitch-relevant finding from that study**: what a foreign visitor actually lacks is not the hut taxonomy but the **unwritten rules** (cleaning up, boots off, how sleeping space is divided, the honor-system premise) — plus the fact that self-service hut information exists only in Norwegian. None of that lives in any API, open or closed. It is a culture-and-language layer written by hand once — cheap for us, and DNT's own Secretary General is on record calling it their unsolved problem. That makes it an argument *for* the DNT pitch, not just a feature.

**Main job**: *When I plan a multi-day mountain trip, I want to be confident that route, lodging, gear, and weather agree with each other, so I'm not the one reconciling four disconnected sources myself.*

**Five jobs the demo has to show.** This is a *selection for the pitch*, not a ranking of needs — 1 and 4 are more fundamental but every competitor has them, so they prove nothing. Full list of eleven: [concept/jtbd.md](./concept/jtbd.md). **The number is not a priority**: 6 and 7 have the strongest evidence in the whole research and come last, because they were found from evidence rather than derived from this spec.

- **2 — what exactly each night's lodging needs.** The core differentiator against Komoot's and AllTrails' generic lodging, and the only one none of the five competitors can express. Verified against Norwegian- and Swedish-language primary sources; the English pages of both associations omit exactly what matters. Both countries share one principle: **booking buys a guaranteed bed; no booking still guarantees indoor space, possibly a floor mattress — nobody is turned away.** The answer for any given night is a function of **object type × booked or not × arrival time (18:00 in Sweden) × membership**. Also: not all beds are pre-bookable (some held for drop-ins), the DNT key is members-only (a 100 NOK deposit, not a walk-up price), and a logbook entry with membership number is required even after booking online. Full table: `concept/personas.md`, Ось A. **Rule: verify lodging rules in Norwegian and Swedish; treat the English pages as incomplete.**
- **3 — how a forecast change affects the plan already made.** The other differentiator named in the elevator pitch. ⚠️ Thinnest evidence of the five: no first-hand account of how anyone reacts to a forecast change mid-trip.
- **5 — why the plan makes each choice.** ⚠️ **Our bet, not a documented need.** There is no Scandinavian AI backlash: neither DNT, Røde Kors nor Sweden's Fjällsäkerhetsrådet has published any warning about AI-planned routes, and the AllTrails/SAR criticism we once built a defence against is a Canadian event with no Nordic counterpart. Keep the named-contributor mechanism — it is cheap, harmless, and we can set the standard first — but do not rest positioning on it.
- **6 — transport to and from the trailhead.** Three independent Swedish voices in a single week, including a documented case of a hiker *abandoning the region* over it, and a trailhead (Katterat) with no road access at all, so replacement buses are physically impossible. The strongest evidence in the entire research, and the best real-world illustration of the lead-time mechanism: what the hiker needed was not a cancellation notice but a signal a day or two earlier, while turning off toward Riksgränsen was still an option.
- **7 — getting the plan to actually-booked nights.** DNT's chain booking is N sequential transactions ("you must complete the booking and payment for one cabin before proceeding to the next"), and a logbook entry with a membership number is required even after paying online. Nestwood gives ordering, dependencies, deadlines and handoff — **it does not run the transaction** (research §2: orchestration layer, no legal liability for bed availability).

**Where the list came from, and why that matters.** Five of the eleven jobs map one-to-one onto the input/output fields of this spec (fitness→1, lodging→2, weather→3, gear→4, explanation→5) — i.e. they were derived from the product idea and evidence was fitted afterwards. Only **6 and 7 ran the other way**. That asymmetry is the reason we do not invent a job to justify a screen: when the Безпека tab needed one, it got **hypothesis H6** instead.

**The institutional argument, stated publicly by two of our four acquisition targets**: Røde Kors and DNT say foreign visitors *misjudge difficulty, distance, elevation gain, how fast the weather turns, and how much steeper/wetter/rougher Norwegian terrain is* — attributed partly to social-media images. DNT's own stated remedy is **"turveiledning og informasjon på flere språk"**, and Røde Kors is calling for joint *fjellvett-opplysning* with DNT and the police. That is close to a description of this product. Source: [NRK Vestland, 2026-08-01](https://www.nrk.no/vestland/turister-far-trobbel-pa-tur-i-fjellet-i-norge---rode-kors-og-dnt-vil-se-pa-fjellvett-tiltak-1.17970478). So the real hook is **preparedness and language, not AI transparency.**

**Hard constraint from the same source**: DNT wants the *single national difficulty grading* kept and explicitly does not want alternative systems. Nestwood therefore surfaces the official Norwegian grading and must not invent its own fitness→difficulty scale — personalise the *selection* of a route, never the *rating* of it. Also, per [NRK 2026-08-05](https://www.nrk.no/vestland/telenor-ut-mot-dnt-etter-redningsaksjonar-i-fjellet_-_-marknadsforer-omrade-utan-dekning-1.17973749): offline-first is mandatory, and "share your route and expected return time" is a feature DNT itself recommends.

## 🔴 Business-model risk — settle the pitch narrative before contacting DNT

Foreign tour operators are charging clients 20,000+ NOK while using DNT cabins **without booking, registration, or payment** (one Swedish operator arrived at Cunojávrihytta with 8 tourists and 50 sled dogs, unannounced). Jon Sommerseth, director of DNT Narvik: *"Det provoserer at vår frivillige innsats skal være grunnlag for kommersiell drift hos andre."* **From 2027 Troms Turlag bans all commercial use of its huts**, and DNT centrally calls this a growing problem. Source: [NRK Nordland, 2026-02-20](https://www.nrk.no/nordland/mener-dnt-hytter-misbrukes-av-turoperatorer_-_-det-provoserer-1.17771097).

A commercial AI layer that routes foreign visitors into DNT huts sits structurally next to exactly what is provoking DNT right now: outside parties monetising volunteer-maintained infrastructure. Pitching "we will bring you tourists" hits that nerve directly. The same fact supports a stronger framing: Nestwood as the layer that makes this traffic **register, book, and pay correctly** — an ally against the abuse rather than another instance of it. Choose this narrative deliberately, before the first DNT contact, not during it.

## Information architecture

Full detail: [wireframes/sitemap.md](./wireframes/sitemap.md) (entities, screen tree, navigation, traceability), [wireframes/flows.md](./wireframes/flows.md) (flows with decisions, states and dead ends), [wireframes/ia.html](./wireframes/ia.html) (rendered readout). **Five tabs, ~27 screens, 12 jobs, and the matrix closes in both directions** — no job without a surface, and every surface without a job has a named non-job reason.

**Top-level structure — five tabs.** The shape is deliberately ordinary: AllTrails, Komoot and Outdooractive all run Explore / Saved / Profile, and matching them is confirmation the frame is right, not a failure of imagination. The consequence has to be stated plainly, because it sets where the work goes:

> **Navigation will not differentiate us. Two screens will — the route card and the plan.** Everything that makes this Nestwood lives inside them: the guarantee formula, the official grading, dated conditions with a source, reachability of the trailhead, the coherence verdict, the chain of bookings. If those two are built like everyone else's, we are one more catalogue with tidy navigation.

- **Карта · Map** — the entrance and the catalogue. Map of Scandinavia plus a list ordered by **seasonal relevance**, not by proximity (a multi-day trek is never near anyone's geolocation; proximity is AllTrails' logic for day hikes and a meaningless sort for our object). Filters are the brief. Holds the **route card** ⭐, field notes on conditions, reviews as a separate list, the full-screen map surface, and the generative "assemble a route" entry.
- **Плани · Plans** — active / upcoming / past, with a badge for what still has to be locked in. **Opening this tab opens the active plan itself**, not a list, so "what is still missing" is at depth zero. The open plan is one multi-level object holding days, nights, transport (including stored tickets), gear, the offline pack, what changed, what to lock in, the shareable summary, and today's leg while in trip. Everything about the trip lives *inside* the plan rather than beside it — that is the orchestration thesis expressed as structure.
- **Довідник · Guide** — evergreen, searchable, filterable by country: how each lodging system actually works, the unwritten rules, fjellvett. This is 8's surface, and 8 is the second persona's job — previously this content sat inside the plan, i.e. reachable only by someone who had already generated one. Every article carries its source, for the same reason every photo does.
- **Безпека · Safety** — SOS, emergency numbers, my coordinates, the nearest bail-out point, avalanche danger, offline first aid. Half of it has a job (bail-out and change belong to 3/6, and entity 19 finally has a home); SOS and first aid do not — they are held as **hypothesis H6** with a named institutional basis, not as an invented job.
- **Профіль · Profile** — about me (fitness, weight, memberships, import from Strava/Garmin), gear inventory, membership and key, and app settings behind a gear icon. User data and app behaviour are different objects and are visibly separated, but settings do not earn a tab of their own — which is also what the competitors do.

**Home is contextual**: the plan when one is active or starting within a day or two, the map otherwise. A tab that appears and disappears is worse than a state inside a stable tab, so "today" is a state of the Plans tab rather than a sixth entry.

**Main flow**: map → route card → "make my plan" → **the plan, where route, lodging, gear and weather are visible together** → per-day drill-down → either lock it in or share it. **Three taps to a plan instead of four, and the value is visible at tap zero** — the catalogue is already content, not a form. Alternative entrances: a saved trip (0 taps), "nothing fits this brief" → assemble a route, and the profile for a repeat user. If a non-critical source is unavailable the plan is still generated and says what is missing; if a critical one is, the plan is not faked.

**Two things that must not be cut later**, because both are the whole differentiator arriving early: the **preview of the guarantee formula on the route card** (before a plan exists it is the only place 2 is visible at all) and the **source layer on every surface that asserts anything**.

## Non-goals for now

- Not building a standalone consumer venture or growth loop — the demo is a full app by packaging (see Packaging decision), but the business model stays acquisition-target, not an independent product with its own GTM.
- Not wiring up live third-party APIs yet (mock data shaped like real responses instead).
- Not covering regions outside Scandinavia.
- Not becoming a trail database or a discovery product. **The boundary sits on the object, not on a quantity** — a cap like "10–20 routes per country" does not survive a live catalogue: we catalogue **multi-day routes with overnight stays**, not trails. A 6 km morning loop is not our object by definition, which keeps us outside AllTrails by kind rather than by size. What is unchanged: nothing in the product is ordered by popularity, and a filter exists only if it is also a plan parameter.

## Repo / workflow structure

Repo was just cleared for this restart; the previous project's phase pipeline is being reused for this new product:

- `concept/` — problem framing, personas, scenarios
- `research/` — competitor audit, data source research, benchmarks, patterns
- `design-system/` + `tokens/` — visual language, design tokens
- `wireframes/` — low/mid-fidelity flows **and the drawn screens themselves**
- `components/` — built UI components
- `handoff/` — engineering handoff docs

## Wireframes

**56 pages — all 27 screens and their 29 states, drawn against the catalogue structure.** The main flow is complete — catalogue → route card → plan → day → night → transport — and the two screens that carry the differentiation are built out: the **route card** holds the guarantee-formula preview, the three difficulty blocks and trailhead reachability; the **plan** states the assumptions it ran on. The Довідник and Безпека surfaces are new and drawn. Nothing is left grey: every screen in the tree exists, and every named exit inside a mockup leads to a real page.

**The contract, not the pictures, is the artefact.** [`wireframes/_conventions.md`](./wireframes/_conventions.md) fixes the rules every screen obeys — detail level, semantic markup, file naming, the closed state vocabulary, and the three kinds of review chrome. It exists because the set was drawn partly by parallel subagents: with the contract they cloned one pattern instead of inventing six.

Four things worth knowing before touching this folder:

1. **A state is a separate page, never a variant appended at the end.** Same landmarks, same section order, same headings — only content differs. The states are `empty · error · loading · offline · degraded · conflict · seasonal · nooptions`, and the vocabulary is closed: a state outside it is a change to the sitemap, not a new filename.
2. **Every state has a named exit, and no link is broken.** A target that isn't drawn yet renders as inert text, never as a dead `href` — a 404 is exactly the dead end the flows forbid.
3. **Structure is regenerated, not copied by hand.** `_generate.py` holds `TREE` (sections → screens → states) as the single source; `_refresh.py` rewrites the navigation tree and the state row across all pages; `_audit.py` checks structure, zones, semantics, colour, attribution, broken links and dead ends, and must print zero.
4. **One obligation is visible on every page**: the ©Kartverket attribution in the footer — CC BY 4.0, a legal requirement, not a credit. The mock-data label used to be the second and was removed: the screens are a prototype and read as the product, not as an annotated wireframe.

**The main flow is also readable as one page.** [`wireframes/flow.html`](./wireframes/flow.html) lays the
happy path of the main job out in order — catalogue → route card → generation → plan → day → night → gear →
transport → lock-in → share — with the real mockups embedded, each one **extracted from its own file by
`_flow.py`** rather than redrawn, so the page cannot drift from the set. Every step carries its decision from
`flows.md` and the branches leaving it; a branch whose state is drawn is a link, one that isn't stays inert
text. It is the fifth entry in the documents navigation.

The audit trail is in `wireframes/_screens.md` (which states are real and why), `wireframes/_gaps.md` (what the framework was missing against five competitors) and `wireframes/_critique.md` (the final pass: four defects found and fixed, and why "deferred" only differs from "lost" if it is written down).

**UI language of the wireframes is Ukrainian** — see the note under Scope for v1.

## Voice

Full text: [design-system/voice.md](./design-system/voice.md). The audit trail of every string in the product: [wireframes/microcopy.md](./wireframes/microcopy.md) — 2 971 rows, one per interface line, regenerated from the pages by `_microcopy.py`.

**The voice was derived from the research, not chosen.** Each of the five principles cites a line in `research.md`, `personas.md`, `jtbd.md` or `competitors.md`; a sixth candidate — AI transparency — was written up and then **not taken**, because there is no Nordic evidence for it (the same finding that demoted job 5 to "our bet"). That rejection is kept in the file: a principle we declined for a stated reason is part of the artefact.

**What this product is actually about is preparedness, not convenience.** Every competitor's copy sells ease; ours sells knowing what you are walking into. That single sentence is what the five principles operationalise:

1. **Name the condition under which a statement holds.** Not "beds available" but "a booked bed is guaranteed; without a booking you still get indoor space, possibly a floor mattress". The guarantee formula is four variables, so the sentence has to carry them.
2. **Name the limit of our own knowledge on the field it applies to** — never as a banner, never in a separate "about the data" screen. Outside met.no's ~10-day horizon we say it is a seasonal normal, and the load figure says which published method computed it.
3. **Our numbers are about the consequence for this person, not about popularity.** No ratings in sort order, no "most popular route" — hours of walking, metres of ascent, kilometres to the next hut.
4. **Explain someone else's system as a property of that system, never as something the person should have known.** "DNT sells the key to members only" — not "don't forget your key". This is the second persona's whole job, and the tone that makes it land is the difference between a guide and a hall monitor.
5. **When something changes, say what can still be done and how much time is left.** The lead-time mechanism as a sentence pattern: the change, the remaining options, the deadline.

**Three enforced sub-systems**, which is what makes the principles checkable rather than aspirational:

- **Словник** — one concept, one word (a `перехід` is not a `день`; `нічліг` is not `житло`), the address fixed as **«ти»** on every screen, and an explicit allowed/banned anglicism list. It governs product text only — design documents are allowed their own vocabulary, and that boundary is written into the file because otherwise the dictionary starts editing the research.
- **Заборонене** — eight bans, each with a real було/треба pair: error clichés, greetings and celebration, the word «успішно», exclamation marks, emoji in system messages, promises of ease, popularity counts, and internal screen/format names leaking into the UI.
- **Мікрокопі** — a rule per element type (button, screen heading, form field, empty state, error, loading, success, destructive action), each with one Nestwood example. Buttons name the outcome, not the mechanism; an empty state always carries an exit; an error never jokes; success does not celebrate, it says what is now true.

**Screen names get a blunt test**, added after two invented ones shipped: if a person has never met the phrase in any app, the name is invented. «Останні кроки» and «Сказати, куди йду» replaced «Що лишилось закріпити» and «Підсумок для передачі» on exactly that ground.

The name of a screen lives in `_generate.py`'s `TREE` and nowhere else — `<title>`, the phone label, the header and the position line all read from it, and `_audit.py` fails if any of the four drifts. That check exists because a rename silently updated three places out of five and each of them looked correct on its own.

## Tech stack

Decided against the evidenced constraints, not against build convenience. Full evaluation: [research/research.md](./research/research.md) §7.

| Layer | Choice | Why this one |
|---|---|---|
| App shell | **Next.js (App Router) on Vercel**, TypeScript | The AI call needs a server side (the API key can't live in the browser) and met.no requires caching per its `Expires` header — both belong in route handlers next to the frontend, one repo, one deploy. A buyer opens the demo from their phone by link |
| Maps + offline | **MapLibre GL JS + PMTiles stored in OPFS** | PMTiles is one file per region served by byte range; OPFS gives near-native performance for large files in the browser. Explicitly suited to a bounded regional dataset on static hosting — which is exactly our scope |
| Packaging | **Native app from the start — Capacitor wrap, installed from the store** | The wrap is not an optimisation but a **condition for two jobs on iOS**: 3 and 6 are delivered by push with lead time, and web push on iOS works only for an installed PWA — so in the PWA phase our best-evidenced mechanism silently does not arrive, and the person is not told. Notification permission is asked when it means something (the plan is saved), not at first launch. Widgets and Live Activities also require the wrap; a Live Activity lasts hours, not days, so it fits a departure day or a single leg, never a whole trek |
| Data | **Adapter interfaces** (`LodgingSource`, `WeatherSource`, `TransportSource`, `RouteSource`) with mocks shaped like real NTB / met.no / Entur responses | This is the swap-without-rewrite requirement made concrete. After the source audit, three of the four adapters could be implemented for real today |
| Persistence | IndexedDB for plan, gear inventory and booking-completion state; Service Worker for the shell | These are exactly the things that must survive a closed tab (account decision) |
| AI | **`claude-opus-5`** — structured outputs to the plan schema, grounding via tool use over the adapters, prompt caching for the stable system prompt and reference tables, streaming generation | Structured outputs bound improvisation **by schema rather than by hoping the prompt holds** — which is what makes a live demo safe. Tool use over adapters is the orchestration layer we're actually selling |

**Four consequences to design around, not discover later:**

1. **Offline has a ceiling, and it must be designed rather than declared.** iOS evicts PWA storage under memory pressure; the seven-day script-writable cap does not apply to *installed* PWAs, and Safari 17+ offers the Persistent Storage API — but there is never a guarantee. So v1 promises **"an offline pack for this route"** — a screen, a state and a size in megabytes the person can see — not "offline everywhere". Anything stronger repeats the exact failure we cite as the pain (Swedish hikers left Lantmäteriet's own app when it lost iOS offline).
2. **Permission is asked where it is a means, never at the entrance.** This used to be about installing the PWA; with the store install (see Packaging) the install question disappears and the same rule now governs **notifications and location**: asked at the moment they do something — notifications when a plan is saved ("so we can warn you two days out"), location when the map or today's leg is opened — never on first launch, which is the same antipattern as putting registration in front of value. The offline pack keeps its own visible screen and size in megabytes.
3. **No continuous tracking, by design.** What drains a battery is continuous GPS, screen-on time and network polling — not the widget or the notification, which the system renders while the app is asleep. Our value in trip is a **signal with lead time**, i.e. a few pushes a day, which is nearly free; position on the map is **on demand**, when the person opens it. Building a tracker would contradict our own stack-forcing constraint rather than serve it.
4. **We must generate our own PMTiles from downloadable datasets.** Kartverket's zoom levels 12–20 come from the Geovekst cooperation and need the licensees' separate permission to copy, so packaging offline tiles by pulling their cache service is not open to us. Unplanned work that sits between us and the first offline demo.

**Demo rule**: generation is live (a real `claude-opus-5` call), with a pre-generated plan held in reserve against bad conference-room wifi. A scripted demo would collapse the moment a buyer asks to enter their own dates — and "a working prototype, not a mockup" is the whole pitch.

## Key external data sources

All verified by direct request on 2026-08-06 — licence, key requirement and liveness. Full detail, quoted terms and query results: [research/research.md](./research/research.md), "Решта джерел під продуктом".

| Need | Norway | Sweden |
|---|---|---|
| Maps, terrain | Kartverket — CC BY 4.0, ©Kartverket attribution **mandatory in the UI** | Lantmäteriet — CC0 |
| **Elevation models** — the load estimate depends on them, and they are present where `gradering` is not | Kartverket høydedata (DTM) | Lantmäteriet höjddata — CC0 |
| Trails **+ the official difficulty grading as a field** | Turrutebasen (Kartverket) — open, live WFS | Lantmäteriet / Naturvårdsverket |
| Weather | met.no Locationforecast 2.0 — CC BY 4.0, no key | SMHI `snow1g` v1 — CC BY 4.0 SE, no key |
| Transport to and from the trailhead (6) | Entur JourneyPlanner v3 — NLOD, **no key**, `ET-Client-Name` required | ResRobot v2.1 (CC0, key) + Trafikverket (CC0, key) |
| Road access to a trailhead / station (entity 19) | NVDB API Les v4 — NLOD, no auth, `X-Client` required since 2026-01-05 | Lantmäteriet CC0, but bulk download + account |
| Avalanche danger | NVE Varsom v6.3.0 — NLOD | lavinprognoser.se (Naturvårdsverket) — CC0, six areas only |
| Live bed availability | **DNT / NTB — closed.** Commercial agreement, not a technical blocker | STF — closed |
| Mobile coverage as a spatial layer | **Does not exist as reusable data** — Nkom publishes per-household XLSX | Same — PTS publishes per-municipality Excel |

**Three things to carry into the pitch and the build:**

1. **Exactly two classes are blocked**: live bed availability, and mobile coverage as a geographic layer. Everything else — weather, transport, road access, avalanche, trails with official grading — is open with commercial use permitted. Say "one blocked field in the hut data", not "one blocked field in the product".
2. **6 is now provable on the exact case it came from.** Katterat is in Entur as `NSR:StopPlace:58610` with a `cancellation` field, and NVDB returns **zero road segments** around it against fifteen at the neighbouring station — so "you can walk in but no bus can reach you" is computable from open data, with no key and no agreements.
3. **Sources move.** One audit turned up two switched-off APIs (SMHI `pmp3g`, killed 2026-03-31; NVDB v3 being decommissioned) and one new mandatory header. Multi-provider fallback is a response to a documented rate of change, not architectural taste.

## Open questions for the research phase

- **DNT's Nasjonal Turbase (NTB) API is closed — resolved as a working assumption.** Verified directly (uniform 404 across all documented endpoints; the root domain no longer resolves) and via DNT's own open-data page ("for economic, security, and strategic reasons"). **This is no longer treated as a blocker**: integration is deferred by decision, the schema is public (see Scope for v1), and only live availability is actually missing. It no longer blocks the tech-stack decision. What remains open is the *commercial* conversation, and it belongs to whoever acquires this — see the two disclosure rules under Scope for v1.
- Visual/brand direction. **A hard constraint rules out the obvious answer**: green, blue, red and black are already taken by the official Norwegian grading — verified verbatim on DNT's own support pages: **grønn = enkel · blå = middels · rød = krevende · svart = ekstra krevende**, plus a fifth marker, *Godt tilgjengelig*. We committed to surfacing that grading and never inventing our own, so those four colours **mean route difficulty inside our UI** and cannot simultaneously mean brand, success or error. This kills the default: light Scandinavian minimalism almost always lands on a muted green accent — as our own `design-system/docs/doc.css` does — and in the product a green accent would read as "easy route". The brand accent is **deferred by decision, not forgotten**; whatever it becomes, it comes from outside those four hues.
- **Deliberate consequence of the offline decision**: the in-trip screen is used outdoors in sunlight and must save battery. That is not the same layout in a light theme — it argues for a dedicated in-trip mode (dark, high contrast, large type, minimal repaint) rather than one aesthetic everywhere. Settle this with the visual direction. "Dark = saves battery" only holds on OLED at low-to-mid brightness; in sunlight a dark screen has to be driven brighter, and brightness costs more than dark pixels save. **The metric for the in-trip mode is seconds of screen-on, not the colour of the background** — which makes it a layout decision (everything needed visible at a glance, no scrolling) rather than a theme decision. The mode turns on by itself when the trip starts; a device-wide power saver cannot be set by a third-party app, so that is offered as a one-time Shortcuts/settings handoff, never promised as ours.
- **Two open questions on the route card's difficulty block:** what that block looks like when there is **no official grading** (the majority case — Jotunheimen 1 of 92) so it reads as "here are the facts, judge for yourself" rather than "no data"; and how we show that Norway and Sweden grade on **different systems** without inventing a common denominator.
- **11 has no content at launch.** "Is this realistic for someone like me" stands on reviews, and reviews start empty. Unlike field notes they cannot be seeded honestly — a hut warden can report a ford, not "if she could do it, so can I". Either accept 11 as unserved at launch, or substitute **curated third-party trip reports with attribution** (the same source 11 itself came from). Decide before drawing the route card.
- **Content sourcing for the Довідник is a licence question, not an editorial one.** DNT has already written what we planned to write — `dnt.no/turtips/turvett/artikler/` covers hut-to-hut, trip planning and fjellvett — **in Norwegian only**, and it is their copyright. Same class of problem as NTB: the content exists but is not ours. Three options: link out · agree · write our own from the primary rules with attribution to the rules. First-aid content is never authored by us and must be attributed (Røde Kors / Röda Korset) — check the licence before promising that screen offline. **Working assumption: agreements will be reached, and material will be bought if it has to be.**
- **Country parity in the Довідник** — the country filter promises material for both, and Norwegian sources are much richer than Swedish. **Working assumption**: collect as much as exists for every country and treat the filter as a convenience, not as a promise of parity.
- Concrete demo scenario and success criteria to use when pitching to acquisition targets.
- App identity for the standalone packaging — name (working assumption: Nestwood), icon, and onboarding tone — to settle during concept/design-system phases.
