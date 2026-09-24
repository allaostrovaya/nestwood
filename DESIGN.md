---
name: Nestwood
description: AI multi-day itinerary layer for Nordic trekking — the Прилад (Instrument) visual language, as built in the painted wireframes.
colors:
  glass: "#F4F5F5"
  surface: "#FFFFFF"
  hairline: "#D9DCDF"
  graphite: "#5E6368"
  ink: "#0F1113"
  signal-blue: "#2D5BFF"
  signal-blue-pressed: "#2149E0"
  signal-blue-soft: "#E8EEFF"
  hi-vis-yellow: "#F2E500"
  conflict: "#B42318"
  conflict-on-ink: "#FF7A6B"
  fixed: "#0B7A4B"
  fixed-soft: "#E7F4EC"
  disabled-fill: "#C9CDD1"
  map-land: "#E8ECE3"
  map-water: "#CFE0EA"
  map-contour: "#CDD5C4"
  dark-glass: "#0F1113"
  dark-surface: "#1C1E21"
  dark-hairline: "#34383C"
  dark-graphite: "#A3A9AE"
  dark-ink: "#F2F3F4"
  dark-signal-blue: "#3A66F5"
  dark-link: "#7C9BFF"
  dark-alert: "#26292D"
  dark-fixed: "#4CC38A"
  dark-fixed-soft: "#12301F"
typography:
  title:
    fontFamily: "Wix Madefor Display, system-ui, sans-serif"
    fontSize: "24px"
    fontWeight: 600
    lineHeight: 1.12
    letterSpacing: "-0.02em"
  headline:
    fontFamily: "Wix Madefor Display, system-ui, sans-serif"
    fontSize: "16px"
    fontWeight: 600
    lineHeight: 1.2
  body:
    fontFamily: "Wix Madefor Display, system-ui, sans-serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.45
  callout:
    fontFamily: "Wix Madefor Display, system-ui, sans-serif"
    fontSize: "14px"
    fontWeight: 400
    lineHeight: 1.4
  caption:
    fontFamily: "Wix Madefor Display, system-ui, sans-serif"
    fontSize: "12px"
    fontWeight: 400
    lineHeight: 1.4
  label:
    fontFamily: "Wix Madefor Display, system-ui, sans-serif"
    fontSize: "10px"
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: "0.06em"
  numeral:
    fontFamily: "Tektur, Wix Madefor Display, sans-serif"
    fontSize: "24px"
    fontWeight: 600
    lineHeight: 1
    letterSpacing: "-0.03em"
    fontFeature: "tnum"
  numeral-small:
    fontFamily: "Tektur, Wix Madefor Display, sans-serif"
    fontSize: "12px"
    fontWeight: 500
    lineHeight: 1.3
rounded:
  photo: "32px"
  panel: "24px"
  card: "20px"
  control: "16px"
  field: "12px"
  pill: "999px"
  row: "0px"
spacing:
  "1": "4px"
  "2": "8px"
  "3": "12px"
  "4": "16px"
  "5": "20px"
  "6": "24px"
  "8": "32px"
components:
  button-primary:
    backgroundColor: "{colors.signal-blue}"
    textColor: "{colors.surface}"
    rounded: "{rounded.control}"
    padding: "0 20px"
    height: "52px"
  button-primary-pressed:
    backgroundColor: "{colors.signal-blue-pressed}"
    textColor: "{colors.surface}"
    rounded: "{rounded.control}"
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.control}"
    padding: "0 20px"
    height: "52px"
  button-disabled:
    backgroundColor: "{colors.disabled-fill}"
    textColor: "{colors.graphite}"
    rounded: "{rounded.control}"
    height: "52px"
  button-sos:
    backgroundColor: "{colors.conflict}"
    textColor: "{colors.surface}"
    rounded: "{rounded.pill}"
    padding: "0 20px"
    height: "56px"
  chip:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.pill}"
    padding: "0 12px"
    height: "32px"
  chip-selected:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.glass}"
    rounded: "{rounded.pill}"
    padding: "0 12px"
    height: "32px"
  pill-attention:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface}"
    typography: "{typography.callout}"
    rounded: "{rounded.pill}"
    padding: "8px 12px 8px 8px"
  pill-neutral:
    backgroundColor: "{colors.glass}"
    textColor: "{colors.ink}"
    rounded: "{rounded.pill}"
    padding: "8px 12px"
  pill-fixed:
    backgroundColor: "{colors.fixed-soft}"
    textColor: "{colors.fixed}"
    rounded: "{rounded.pill}"
    padding: "8px 12px 8px 8px"
  alert:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface}"
    rounded: "{rounded.card}"
    padding: "12px 16px 12px 24px"
  list-group:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.card}"
    padding: "0 16px"
  instrument-panel:
    textColor: "{colors.ink}"
    typography: "{typography.numeral}"
    rounded: "{rounded.panel}"
    padding: "16px"
  tab-bar:
    textColor: "{colors.graphite}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: "8px 8px 12px"
  search-pill:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.panel}"
    padding: "8px"
---

# Design System: Nestwood

## Overview

**Creative North Star: "Прилад" — the Instrument.**

A landscape photo carries the screen; on top of it, in the lower part of the frame, sits a frosted glass panel of measurements, read like a row of complications on a watch. Below the photo is a light, dense register that answers one question — does everything fit. Technology is the aesthetic, in deliberate contrast with the landscape: a precise modern tool that gets you to nature calmly. The product sells preparedness, not convenience, so the visual language carries measurements and conditions, never decoration.

The system is quiet by default and loud only when something needs a decision. There is one action colour (Signal blue) and one live-state colour (Hi-vis yellow, always paired with ink). An alert is an inverted ink panel with a hatched yellow edge, readable without colour and in direct sunlight. Everything that asserts something carries its source: every photo prints its author and licence on the image, every map prints ©Kartverket on the map.

Rejected, by the designer: PrivatBank-grade missing craft (dirty colours, a broken type scale, uneven spacing, no hierarchy, clutter); grey gradients in place of photos (a static placeholder — a loading skeleton is an animation and is allowed); screens without icons.

**Key Characteristics:**
- Photo-led hero with a frosted instrument panel; register below.
- One action colour, one live-state colour; state is a word, colour only reinforces it.
- Large radii on containers, flat rows inside them.
- Tektur digits for measurements, Wix Madefor Display for language.
- Solar icons; no Unicode glyph ever stands in for an icon.
- Light and dark are both first-class; a fixed toggle switches them.

## Colors

A closed, near-neutral palette with exactly two saturated voices — blue for doing, yellow for "live, look here".

### Primary
- **Signal Blue** (#2D5BFF): the only action colour — primary buttons, text actions ("book", "buy", "change"), links, focus. White on it is 5.2:1. Close to the iOS system blue, one step darker so white text passes AA. Pressed state and text on the soft blue background use **Signal Blue Pressed** (#2149E0, 5.85:1 on #E8EEFF).

### Secondary
- **Hi-vis Yellow** (#F2E500): live state on the instrument only — the alert's hatched edge, the alert's deadline tag, the day node that needs attention, the tab-bar badge, the attention icon. Never a button fill, never text on a light background; always paired with Instrument Ink (#0F1113), in both themes.

### Neutral
- **Glass** (#F4F5F5): screen background, neutral pill background, pressed secondary button.
- **Surface** (#FFFFFF): cards, grouped lists, sheets, the action bar, secondary buttons.
- **Hairline** (#D9DCDF): 1px inset outlines of cards and pills, dividers inside lists and the panel.
- **Graphite** (#5E6368): secondary text, units next to numbers, panel labels, icons in rows, the dashed "knowledge limit" border. 5.56:1 on Glass.
- **Instrument Ink** (#0F1113): primary text, the alert and attention-pill background, the selected chip, the active tab.

### Semantic
- **Conflict** (#B42318): SOS, destructive text ("Change and reset"). On ink and in dark mode: **Conflict on Ink** (#FF7A6B) — the red edge of a verdict.
- **Fixed** (#0B7A4B on #E7F4EC): "Everything fits." — the only green, 4.76:1.
- **Disabled** (#C9CDD1 fill, Graphite text, 3.8:1 — WCAG does not require contrast for inactive controls; the system never goes below 3).
- **Map**: land #E8ECE3, water #CFE0EA, contours #CDD5C4.

### Dark theme
Glass #0F1113 · Surface #1C1E21 · Hairline #34383C · Graphite #A3A9AE · Ink #F2F3F4 · action #3A66F5, links #7C9BFF · alert panel #26292D · fixed #4CC38A on #12301F · conflict #FF7A6B. Yellow keeps its ink partner. Maps invert with `filter: invert(.88) hue-rotate(180deg) saturate(.7)`.

### Named Rules
**The One Voice Rule.** Blue appears only on things that are pressed. A tab is navigation, not action, so the active tab is ink, not blue.
**The Word First Rule.** No state is carried by colour alone: "Everything fits.", "walk-in only", "1 missing" are words; the colour and the icon only reinforce them.
**The Closed Palette Rule.** A colour not listed here is a defect.

## Typography

**Display / UI Font:** Wix Madefor Display (with system-ui)
**Numeral Font:** Tektur — digits and Latin only; its Cyrillic reads д/г as g/r, so Ukrainian labels and units always fall back to Wix.

**Character:** a precise, warm grotesque for language next to an instrument-panel face for measurements; numbers are the content and are set like readings.

**Scale** (designer, 2026-09-24): **10 · 12 · 14 · 16 · 18 · 24 · 28 · 32**. In the painted screens 10, 12, 14, 16 and 24 are used; 18, 28 and 32 are reserved.

### Hierarchy
- **Title** (600, 24px, 1.12, −0.02em): the screen name (h1) — "Kungsleden · Abisko → Nikkaluokta".
- **Headline** (600, 16px, 1.2): section headers ("Needs attention", "Route", "Days") and sheet headers ("Best in Sweden in August").
- **Body** (400–600, 16px, 1.3–1.45): row titles (600), buttons (600), card titles (600), running text.
- **Callout** (400–600, 14px, 1.4): status pills, the alert's body line, the brief ("17–22 August · 2 people · 1 STF member"), chips (500), footer.
- **Caption** (400, 12px, 1.4, Graphite): the secondary line of a row or card, the unit next to a number on the photo panel, the search-pill field label, photo credits.
- **Label** (500, 10px, +0.06em, UPPERCASE, Graphite): the label under a measurement ("DISTANCE"), and the tab bar (500 / 600 active, sentence case).
- **Numeral** (Tektur 600, 24px, 1, −0.02 to −0.04em): measurements on the panel and in the day card. Units sit next to the number at 12–14px Graphite, so the number reads first.
- **Numeral small** (Tektur 500–600, 12px): the alert's deadline tag, the preset duration pill, the HUD on the photo (uppercase, +0.07em).

### Named Rules
**The Floor Rule.** Text is 12px or larger. 10px exists only for the tab bar, the badge and the uppercase measurement label — as iOS itself sets its tab labels at 10pt.
**The Number First Rule.** A unit is never the same size as its number.

## Layout

A single 375-wide mobile column (the device frame renders a 355px screen). Content gutter 16px; everything that lies on a photo — the glass back button, share, the photo credit, the instrument panel — sits 12px from the photo edges. Spacing runs on a 4px step: 4 · 8 · 12 · 16 · 20 · 24 · 32. Sections are separated by 20px, a heading sits 8px above its content, rows are 12px top and bottom with a 56px minimum height, pills breathe 8/12px.

Screen skeletons:
- **Plan / New plan:** full-bleed 300px photo under the status bar (bottom corners 32) → instrument panel on the photo → title → brief → status → sections. New plan is modal: no tab bar, a sticky action bar at the bottom.
- **Catalogue:** the map is the surface and stays put; the search pill is pinned on top; the preset sheet scrolls over the map with two snap heights (half — map visible; full — just under the search pill).
- **Day:** standard nav bar, title, map, elevation profile, one measurement card, rows with icons.
- **Sheet (another hut):** lies over the dimmed screen it came from, top corners 24 with a 36×4 handle, covers the tab bar.

A floating glass tab bar sits 10px from the screen edges; screens pad 96px at the bottom to clear it.

## Elevation & Depth

Flat with glass. Surfaces are defined by a 1px inset hairline, not by lift — lift reads as promotional. Depth appears only where something floats over content or photography.

### Shadow Vocabulary
- **Float** (`box-shadow: 0 12px 32px -16px rgba(15,17,19,.38)`): the tab bar, the search pill, the own-route card and unselected chips lying on the map.
- **Sheet edge** (`box-shadow: 0 -8px 24px -18px rgba(15,17,19,.35)`): the top edge of the preset sheet over the map.
- **Photo floor** (`box-shadow: inset 0 -90px 60px -40px rgba(0,0,0,.35)` plus a 110px top scrim `rgba(0,0,0,.42)→0`): keeps white text on photos at AA.

### Glass
- **Instrument panel:** `rgba(250,250,250,.9)` + `blur(16px) saturate(1.2)`; dark `rgba(28,30,33,.88)`.
- **Bars** (tab bar, action bar, nav bar over content): `rgba(255,255,255,.88)` + `blur(18px) saturate(1.3)`.
- **Buttons on photos:** `rgba(15,17,19,.45)` + `blur(12px)` — never lighter, so white text holds 7.7:1 over the top scrim.

### Named Rules
**The Flat-By-Default Rule.** Cards and lists never cast shadows. Only floating layers do.

## Shapes

Big radii on containers, flat inside them — the resolution of the designer's "large radii" (Raiffeisen) with the flat measurement row (19–86).

- **32** — the hero photo's bottom corners.
- **24** — the instrument panel, the sheet's top corners, the search pill.
- **20** — cards, grouped lists, alerts, map and profile frames, preset photos.
- **16** — buttons.
- **12** — form fields (none in the painted screens).
- **999** — pills, chips, the tab bar, the badge, the SOS capsule, the attribution chip, round icon buttons.
- **0** — rows inside a card.

The alert's 8px hatched edge (`repeating-linear-gradient(135deg, #F2E500 0 5px, #0F1113 5px 10px)`) is the system's one signature mark.

## Components

### Buttons
- **Shape:** 16px radius, 52px tall, 600 16px.
- **Primary:** Signal Blue, white text; one per screen (Save plan, Make a plan, Plan again from this trip). Pressed #2149E0, scale .985.
- **Secondary:** Surface with a 1.5px inset Hairline, ink text (Cancel, Clear points, Try again); pressed Glass.
- **Tertiary / text action:** Signal Blue text, no frame ("book", "buy", "change"); destructive text in Conflict ("Change and reset").
- **On a photo:** round 44px glass buttons (back, share) or a glass capsule ("My trips"), Solar icon 18–22px, white.
- **Disabled:** #C9CDD1 fill, Graphite text, and it says what is missing ("Choose one of the options").
- **SOS:** Conflict capsule, 56px, Tektur 700.
- **Focus:** 3px ink outline, 3px offset.

### Chips
- **Style:** 32px, 14/500, pill; unselected Surface with 1.5px Hairline, selected Ink with Glass text. The 44px tap target comes from an invisible ::after, not from a bigger chip.

### Status pills
- **Attention:** Ink pill, white 14/600 text, yellow Solar danger-triangle icon ("1 missing", "flood", "by 18:00").
- **Neutral:** Glass pill with Hairline, ink 14/600 ("bookable", "walk-in only").
- **Fixed:** Fixed-soft pill, Fixed text and check icon ("Everything fits.").
- **Preset duration:** white 92% pill on the photo's top-left corner, Tektur 12 ("6 days").

### Alert and verdict
- **Alert (attention):** Ink panel, radius 20, 8px hatched yellow edge; title 16/600 white, body 14 at 80% white, deadline tag Tektur 12 yellow; opens the place where it is fixed.
- **Verdict (conflict):** the same panel with a Conflict-on-Ink edge; options below it are an ordinary grouped list.
- **Knowledge limit:** Graphite text in a 1.5px dashed Graphite frame, radius 20, padding 16 with 48 on the icon side, a 20px Solar cloud icon — used when data is kept but not fresh (offline, couldn't update).
- **Loading skeleton:** Hairline blocks with a shimmer (1.4s, off under reduced motion); the hero skeleton takes the photo's place and shape for the seconds it takes to generate — an animation, not a photo substitute.

### Cards / Containers
- **Grouped list:** Surface, radius 20, 1px inset Hairline, 16px side padding, Hairline dividers; rows 12px vertical, 56px minimum, title 16/600, secondary 12 Graphite, chevron 16px Graphite; rows in "About the trip" carry a 22px Solar icon.
- **Preset card:** no container — a 4:3 photo (radius 20) with the credit on its bottom edge over a darkening gradient, then title 16/600 and a 12 Graphite line.

### Signature: Instrument panel
Three measurements on glass over the photo — distance, ascent, longest day — in three equal columns with Hairline dividers. Numeral Tektur 24, unit 12 Graphite, label 10 uppercase Graphite below. 16px padding, radius 24, 12px from the photo edges. Plan and New plan use the identical panel. The day card is the same component on a white card.

### Signature: Day chain
Days as a chain: a 2px Hairline thread, 24px numbered nodes (Tektur 12); a day that needs attention gets a yellow node with an ink ring; getting there / back use train and bus Solar icons in place of a node.

### Navigation
- **Tab bar:** floating glass capsule, 5 Solar icons 22px (linear; bold for the active tab), labels 10px; active tab Ink 600, inactive Graphite; badge yellow with ink digits and a 2px surface ring.
- **Nav bar (no photo):** glass bar, back link in Signal Blue with a Solar chevron, title 16/600 centred on a three-column grid.
- **Search pill:** Surface, radius 24, Float shadow; three fields Where · When · Who, field label 12 Graphite, value 14/600 up to two lines.

### Map
Map frames are radius 20 with ©Kartverket · Lantmäteriet on a white-70% capsule inside the map; the catalogue map is full-bleed and stays put under the sheet.

## Do's and Don'ts

### Do:
- **Do** put the three key measurements on the photo in the instrument panel, and put a unit at 12–14px Graphite next to every number.
- **Do** print the photo's author and licence on the photo, and ©Kartverket on every map.
- **Do** say a state in words; let colour and icon reinforce it.
- **Do** keep white text on photos on glass no lighter than `rgba(15,17,19,.45)`.
- **Do** use Solar icons (linear 1.5; bold only for the active tab).
- **Do** keep everything on a photo 12px from its edges and content 16px from the screen edge.

### Don't:
- **Don't** use Signal Blue for anything that isn't pressed, and don't use yellow as a fill or as text on light.
- **Don't** set a unit the same size as its number, or box each measurement separately.
- **Don't** use a Unicode glyph (‹ › ✕ ✓ ↗) as an icon.
- **Don't** use text below 12px outside the tab bar, the badge and the uppercase measurement label.
- **Don't** cast shadows on cards or lists; only floating layers get one.
- **Don't** add prev/next day buttons — days are switched from the plan.

## Джерела

- [concept.md](./concept.md) — смак дизайнера, п'ять атрибутів, обраний напрям «Прилад» і кожне правило з причиною; розділ «Прилад у макетах» звіряє concept.md із цим файлом.
- [concept/references.md](./concept/references.md) — запозичені прийоми (N26, 19–86, Airbnb Trips, Komoot, World App) і що з них свідомо не взято.
- Живий стенд мови — [concept.html](./concept.html); код макетів — [wireframes/_prylad.css](./wireframes/_prylad.css).
