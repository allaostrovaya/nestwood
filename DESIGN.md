---
name: Nestwood
description: AI multi-day itinerary layer for Nordic trekking — the Прилад (Instrument) visual language, as built across all 33 painted wireframe pages.
colors:
  glass: "#F4F5F5"
  surface: "#FFFFFF"
  hairline: "#D9DCDF"
  graphite: "#5E6368"
  ink: "#0F1113"
  dash: "#5E6368"
  signal-blue: "#2D5BFF"
  signal-blue-pressed: "#2149E0"
  signal-blue-soft: "#E8EEFF"
  link: "#2D5BFF"
  on-blue: "#FFFFFF"
  hi-vis-yellow: "#F2E500"
  yellow-ink: "#0F1113"
  conflict: "#B42318"
  conflict-on-ink: "#FF7A6B"
  on-conflict: "#FFFFFF"
  fixed: "#0B7A4B"
  fixed-soft: "#E7F4EC"
  disabled-fill: "#C9CDD1"
  on-disabled: "#5E6368"
  alert-bg: "#0F1113"
  alert-fg: "#FFFFFF"
  alert-sub: "rgba(255,255,255,.8)"
  on-photo: "#FFFFFF"
  on-photo-soft: "rgba(255,255,255,.94)"
  glass-btn: "rgba(15,17,19,.45)"
  glass-btn-strong: "rgba(15,17,19,.6)"
  panel-bg: "rgba(250,250,250,.9)"
  bar-bg: "rgba(255,255,255,.88)"
  chip-photo: "rgba(255,255,255,.92)"
  attrib-bg: "rgba(255,255,255,.7)"
  attrib-fg: "#5E6368"
  dim: "rgba(15,17,19,.5)"
  sos-bg: "#B42318"
  sos-fg: "#FFFFFF"
  map-land: "#E8ECE3"
  map-water: "#CFE0EA"
  map-contour: "#CDD5C4"
  dark-glass: "#0F1113"
  dark-surface: "#1C1E21"
  dark-hairline: "#34383C"
  dark-graphite: "#A3A9AE"
  dark-ink: "#F2F3F4"
  dark-signal-blue: "#3A66F5"
  dark-signal-blue-pressed: "#2E57E0"
  dark-signal-blue-soft: "#1D2A55"
  dark-link: "#7C9BFF"
  dark-conflict: "#FF7A6B"
  dark-on-conflict: "#0F1113"
  dark-fixed: "#4CC38A"
  dark-fixed-soft: "#12301F"
  dark-alert-bg: "#26292D"
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
  round: "50%"
spacing:
  "1": "4px"
  "2": "8px"
  "3": "12px"
  "4": "16px"
  "5": "20px"
  "6": "24px"
  "8": "32px"
  "10": "40px"
  "12": "48px"
  "14": "56px"
  "18": "72px"
components:
  button-primary:
    backgroundColor: "{colors.signal-blue}"
    textColor: "{colors.on-blue}"
    rounded: "{rounded.control}"
    padding: "0 20px"
    height: "52px"
  button-primary-pressed:
    backgroundColor: "{colors.signal-blue-pressed}"
    textColor: "{colors.on-blue}"
    rounded: "{rounded.control}"
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.control}"
    padding: "0 20px"
    height: "52px"
  button-text:
    textColor: "{colors.link}"
    typography: "{typography.body}"
    height: "44px"
  button-danger:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.conflict}"
    rounded: "{rounded.control}"
    height: "52px"
  button-danger-fill:
    backgroundColor: "{colors.conflict}"
    textColor: "{colors.on-conflict}"
    rounded: "{rounded.control}"
    height: "52px"
  button-disabled:
    backgroundColor: "{colors.disabled-fill}"
    textColor: "{colors.on-disabled}"
    rounded: "{rounded.control}"
    height: "52px"
  button-sos:
    backgroundColor: "{colors.sos-bg}"
    textColor: "{colors.sos-fg}"
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
    backgroundColor: "{colors.alert-bg}"
    textColor: "{colors.alert-fg}"
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
  field-input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.field}"
    height: "52px"
    padding: "0 16px"
  avatar:
    rounded: "{rounded.round}"
    size: "56px"
  card-photo:
    rounded: "{rounded.card}"
    textColor: "{colors.ink}"
  hero-short:
    rounded: "{rounded.row}"
    height: "190px"
---

# Design System: Nestwood

## Overview

**Creative North Star: "Прилад" — the Instrument.**

A landscape photo carries the screen; on top of it, in the lower part of the frame, sits a frosted glass panel of measurements, read like a row of complications on a watch. Below the photo is a light, dense register that answers one question — does everything fit. Technology is the aesthetic, in deliberate contrast with the landscape: a precise modern tool that gets you to nature calmly. The product sells preparedness, not convenience, so the visual language carries measurements and conditions, never decoration.

The system is quiet by default and loud only when something needs a decision. There is one action colour (Signal blue) and one live-state colour (Hi-vis yellow, always paired with ink). An alert is an inverted ink panel with a hatched yellow edge, readable without colour and in direct sunlight. Everything that asserts something carries its source: every photo prints its author and licence on the image, every map prints ©Kartverket on the map.

**Since the last recording** (2026-09-24 → 2026-09-25 onward), the system was consolidated into a single token layer, `ui/kit.css`, and painted across all 33 wireframe pages / 20 screens instead of the original 16 main-flow pages. What was previously scattered across `wireframes/_prylad.css` inline rules is now one `:root` (and one `[data-theme="dark"]` override of the same names) that every component class consumes through `var()`. The language did not change; its reach and its reusable-component vocabulary did — hub screens (Guide, Safety), evergreen content (Article), and account/settings screens (Profile, My gear, Membership and key, Settings, Sign in) are now built in the same instrument grammar, not left as grey wireframes.

Rejected, by the designer: PrivatBank-grade missing craft (dirty colours, a broken type scale, uneven spacing, no hierarchy, clutter); grey gradients in place of photos (a static placeholder — a loading skeleton is an animation and is allowed); screens without icons.

**Key Characteristics:**
- Photo-led hero with a frosted instrument panel; register below.
- One action colour, one live-state colour; state is a word, colour only reinforces it.
- Large radii on containers, flat rows inside them.
- Tektur digits for measurements, Wix Madefor Display for language.
- Solar icons (inlined as CSS mask data-URIs in `ui/kit.css`); no Unicode glyph ever stands in for an icon.
- Light and dark are both first-class; a fixed toggle switches them.
- A short hero photo with the screen title printed directly on it opens hub screens (Guide, Safety) that have no separate `.shell__head` — the photo carries the h1.

## Colors

A closed, near-neutral palette with exactly two saturated voices — blue for doing, yellow for "live, look here". Every token below is defined once in `ui/kit.css`'s `:root` and re-pointed, name for name, in `[data-theme="dark"]` — there is no second token namespace for dark mode.

### Primary
- **Signal Blue** (`--blue` #2D5BFF): the only action colour — primary buttons, text actions ("book", "buy", "change"), links, the field focus ring, the checked switch/checkbox fill. White on it is 5.2:1. Close to the iOS system blue, one step darker so white text passes AA. Pressed state and text on the soft blue background use **Signal Blue Pressed** (`--blue-pressed` #2149E0, 5.85:1 on `--blue-soft` #E8EEFF).

### Secondary
- **Hi-vis Yellow** (`--yellow` #F2E500): live state on the instrument only — the alert's hatched edge, the alert's deadline tag (`--alert__tag`), the day node that needs attention, the tab-bar badge, the attention-pill's danger icon, the active step on the avalanche-danger scale. Never a button fill, never text on a light background; always paired with Instrument Ink (`--yellow-ink` #0F1113), in both themes.

### Neutral
- **Glass** (`--glass` #F4F5F5): screen background (`.nw`), neutral pill background, pressed secondary button, the bare-list background under an alert.
- **Surface** (`--surface` #FFFFFF): cards, grouped lists, sheets, the action bar, secondary buttons, the switch knob, chip default fill.
- **Hairline** (`--hairline` #D9DCDF): 1px inset outlines of cards and pills (`--e-hair`, `--e-stroke`), dividers inside lists, the day-chain thread, the unchecked switch track.
- **Graphite** (`--graphite` / `--dash` #5E6368): secondary text, units next to numbers, panel labels, icons in rows and content-icon lists, the dashed "knowledge limit" border, search-pill field labels. 5.56:1 on Glass.
- **Instrument Ink** (`--ink` #0F1113): primary text, the alert and attention-pill background, the selected chip, the active tab, the day-chain node ring.

### Semantic
- **Conflict** (`--conflict` #B42318): SOS button fill, destructive text ("Change and reset", "Delete account"), the verdict panel's edge, error-field outline. On ink and in dark mode: **Conflict on Ink** (`--conflict-on-ink` #FF7A6B) — the red hatched edge of a verdict.
- **Fixed** (`--fixed` #0B7A4B on `--fixed-soft` #E7F4EC): "Everything fits.", ok-field outline — the only green, 4.76:1.
- **Disabled** (`--disabled` #C9CDD1 fill, `--on-disabled` #5E6368 text, 3.8:1 — WCAG does not require contrast for inactive controls; the system never goes below 3).
- **Map**: land `--map-land` #E8ECE3, water `--map-water` #CFE0EA, contours #CDD5C4.

### Dark theme
Glass #0F1113 · Surface #1C1E21 · Hairline #34383C · Graphite #A3A9AE · Ink #F2F3F4 · action `--blue` #3A66F5 (pressed #2E57E0, soft #1D2A55), links #7C9BFF · alert panel #26292D · fixed #4CC38A on #12301F · conflict #FF7A6B (on-conflict #0F1113). Yellow keeps its ink partner in both themes — it is never redefined for dark. Maps and elevation profiles invert with `filter: invert(.88) hue-rotate(180deg) saturate(.7)` (`--map-dark`) and a lighter `invert(.9) hue-rotate(180deg)` (`--profile-dark`) respectively.

### Named Rules
**The One Voice Rule.** Blue appears only on things that are pressed or actionable. A tab is navigation, not action, so the active tab is ink, not blue.
**The Word First Rule.** No state is carried by colour alone: "Everything fits.", "walk-in only", "1 missing" are words; the colour and the icon only reinforce them. This extends to the avalanche-danger `.scale`: the active step is yellow, but the number/word ("2 · moderate") is what a colour-blind reading depends on, never the fill alone.
**The Closed Palette Rule.** A colour not listed here is a defect. Every colour in the product traces to a name in `ui/kit.css`'s `:root`.

## Typography

**Display / UI Font:** Wix Madefor Display (with system-ui)
**Numeral Font:** Tektur — digits and Latin only; its Cyrillic reads д/г as g/r, so Ukrainian labels and units always fall back to Wix.

**Character:** a precise, warm grotesque for language next to an instrument-panel face for measurements; numbers are the content and are set like readings.

**Scale** (designer, 2026-09-24): **10 · 12 · 14 · 16 · 18 · 24 · 28 · 32**. In the now-fully-painted set, 10, 12, 14, 16, 24 and **28** are in active use (28 appears in `.hero__title`, the title printed directly on the short hero photo of hub screens); 18 and 32 remain reserved.

### Hierarchy
- **Title** (600, 24px, 1.12, −0.02em): the screen name (h1) — "Kungsleden · Abisko → Nikkaluokta".
- **Hero title** (600, 28px, 1.12): the h1-equivalent printed directly on a short hero photo (`.hero__title`) on hub screens that have no separate head block — "Guide", "Safety" — white with a `--shadow-title` text shadow.
- **Headline** (600, 16px, 1.2): section headers ("Needs attention", "Route", "Days") and sheet headers ("Best in Sweden in August").
- **Body** (400–600, 16px, 1.3–1.45): row titles (600), buttons (600), card titles (600), running text, field inputs.
- **Callout** (400–600, 14px, 1.4): status pills, the alert's body line, the brief ("17–22 August · 2 people · 1 STF member"), chips (500), footer, field labels, avatar row subtitle.
- **Caption** (400, 12px, 1.4, Graphite): the secondary line of a row or card, the unit next to a number on the photo panel, the search-pill field label, photo credits, card-photo subtitle.
- **Label** (500, 10px, +0.06em, UPPERCASE, Graphite): the label under a measurement ("DISTANCE"), and the tab bar (500 / 600 active, sentence case).
- **Numeral** (Tektur 600, 24px, 1, −0.02 to −0.04em): measurements on the panel and in the day card. Units sit next to the number at 12–14px Graphite, so the number reads first.
- **Numeral small** (Tektur 500–600, 12px): the alert's deadline tag, the preset duration pill, the HUD on the photo (uppercase, +0.07em), the tab-bar badge digit, the day-chain node number.

### Named Rules
**The Floor Rule.** Text is 12px or larger. 10px exists only for the tab bar, the badge and the uppercase measurement label — as iOS itself sets its tab labels at 10pt.
**The Number First Rule.** A unit is never the same size as its number.

## Layout

A single 375-wide mobile column (the device frame renders a 355px screen). Content gutter 16px; everything that lies on a photo — the glass back button, share, the photo credit, the instrument panel — sits 12px from the photo edges. Spacing runs on a 4px step: 4 · 8 · 12 · 16 · 20 · 24 · 32, plus 40/48/56 for larger blocks (the avatar row, the panel's icon offset, list row height). Sections are separated by 20px, a heading sits 8px above its content, rows are 12px top and bottom with a 56px minimum height, pills breathe 8/12px.

Screen skeletons (four `.shell` variants, all defined once and shared across all 20 screens — `ui/shell.html` is the reference):
- **Plain** (`.shell`): sticky glass bar with a back link, `.shell__head` (h1 + optional brief), then section slots and the attribution footer. Used by Day, Gear, Share my route, Article, First aid, Settings, and most non-photo screens.
- **On a photo** (`.shell--photo`): full-bleed 300px photo hero under the status bar (bottom corners 32) → instrument panel on the photo → h1 + brief below the photo. Plan and New plan use this.
- **Modal** (`.shell--photo.shell--modal`): the photo variant with no tab bar and a sticky `.actionbar` at the bottom instead — New plan.
- **Sheet** (`.shell--sheet`): lies over the dimmed screen it came from (`.shell__backdrop` + a `.dim` overlay), top corners 24 with a 36×4 handle, "Close" instead of "back", covers the tab bar — Another hut, Hut, Notes and reviews, Book, Membership and key, My gear, Sign in.
- **Map surface** (`.shell--map`): bar and head are visually hidden (the map is the entrance) — Catalogue.
- **Hub, short hero** (`.hero--short`): a 190px photo with the screen title (`.hero__title`, 28px) printed on it via a bottom scrim, no separate `.shell__head` — Guide, Safety. Guide additionally floats a search field (`.search-float`) half-overlapping the photo's bottom edge.

A floating glass tab bar sits 10px from the screen edges; screens pad 96px at the bottom to clear it (hidden on modal and sheet variants).


## Elevation & Depth

Flat with glass. Surfaces are defined by a 1px inset hairline, not by lift — lift reads as promotional. Depth appears only where something floats over content or photography.

### Shadow Vocabulary
- **Float** (`--e-float`: `0 12px 32px -16px rgba(15,17,19,.38)`): the tab bar, the search pill, the switch knob, the own-route card and unselected chips lying on the map, any `.list--float` floating on a map surface.
- **Sheet edge** (`--e-sheet`: `0 -8px 24px -18px rgba(15,17,19,.35)`): the top edge of the preset sheet over the map.
- **Photo floor** (`--e-photo-floor`: `inset 0 -90px 60px -40px rgba(0,0,0,.35)`) plus a 110px top scrim (`--scrim-top`) and, on short heroes and photo cards, a bottom scrim (`--scrim-bottom`): keeps white text on photos at AA.
- **Text shadow** (`--shadow-text` / `--shadow-title` / `--shadow-card`): a soft `0 1px 3px rgba(0,0,0,.35–.6)` behind white text directly on a photo (hero credit, hero HUD, hero title, card-photo credit) — a second, cheaper mechanism than the glass buttons, used where a full glass chip would be too heavy.

### Glass
- **Instrument panel** (`--panel-bg`): `rgba(250,250,250,.9)` + `blur(16px) saturate(1.2)` (`--blur-glass`); dark `rgba(28,30,33,.88)`.
- **Bars** (`--bar-bg`, tab bar, action bar, nav bar over content): `rgba(255,255,255,.88)` + `blur(18px) saturate(1.3)` (`--blur-bar`).
- **Buttons on photos** (`--glass-btn` / `--glass-btn-strong`): `rgba(15,17,19,.45–.6)` + `blur(12px)` (`--blur-btn`) — never lighter, so white text holds 7.7:1 over the top scrim.

### Named Rules
**The Flat-By-Default Rule.** Cards and lists never cast shadows (`--e-hair` is an inset outline, not a shadow). Only floating layers get one.

## Shapes

Big radii on containers, flat inside them — the resolution of the designer's "large radii" (Raiffeisen) with the flat measurement row (19–86).

- **32** (`--r-photo`) — the hero photo's bottom corners on Plan, New plan and Hut. The short hub hero (Guide, Safety) is the exception: `.hero--short` overrides this to **0** — it is the screen's own top-level identity photo, edge to edge, not a photo sitting inside a scrolling register.
- **24** (`--r-panel`) — the instrument panel, the sheet's top corners, the search pill.
- **20** (`--r-card`) — cards, grouped lists, alerts, map and profile frames, preset/card-photo images, the disclosure block.
- **16** (`--r-control`) — buttons.
- **12** (`--r-field`) — form fields (Booking number, field notes text, sign-in email — now painted, previously "none in the painted screens").
- **999** (`--r-pill`) — pills, chips, the tab bar, the badge, the SOS capsule, the attribution chip, round icon buttons, switch track, the avalanche-scale steps.
- **50%** (`--r-round`) — the avatar, round glass icon buttons, the day-chain node, the spinner.
- **0** (`--r-0`) — rows inside a card.

The alert's 8px hatched edge (`--hatch`: `repeating-linear-gradient(135deg, #F2E500 0 5px, #0F1113 5px 10px)`) is the system's one signature mark.

## Components

Component coverage below is organised the way `ui/inventory.md` groups it — by how many of the 20 screens a pattern actually repeats on — rather than by which screen it was first drawn on. Only patterns confirmed on 2+ screens, or genuinely signature, are documented; one-offs (the Where·When·Who search, the full-bleed catalogue map, the trip-level "Needs attention" alert copy, the booking chain-order indicator, the settings gear icon, the segmented Field notes/Reviews switch, the elevation profile, and others listed under "Разове" in `ui/inventory.md`) are deliberately left undocumented here — see the closing note.

### Navigation (on all 20 screens)
- **Tab bar** (`.tabbar`): floating glass capsule, 5 Solar icons 22px (linear; bold mask swapped in for the active Map/Plans tab only — Guide/Safety/Profile share one icon active or not), labels 10px; active tab Ink 600, inactive Graphite; badge (`.tabbar__badge`) yellow with ink digits and a 2px surface ring, hidden wherever no plan exists yet.
- **Two-layer header** (`.shell__bar` + `.shell__head`): layer 1 is navigation only (back/close · title · one optional action icon); layer 2 is content (h1 + brief). On a photo, layer 1 becomes glass buttons with no visible title (the title lives in the h1); in a sheet, layer 1 gains the drag handle and "Close".
- **Attribution footer** (`.shell__footer`, all 20 screens): the ©Kartverket / Lantmäteriet / met.no / Trafikverket line, a `disclosure--quiet` "Where this comes from", and a "Last checked" timestamp — legally required (CC BY 4.0), present without exception.

### Cards / Lists (near-universal)
- **Section** (`.section` + `.section__title`, all 20 screens): an h2 and its content, 20px top padding, 8px under the title.
- **Grouped list / row** (`.list` / `.row`, 19 of 20 screens — absent only on Sign in): Surface, radius 20, 1px inset Hairline, 16px side padding, Hairline dividers; rows 12px vertical, 56px minimum, title 16/600, secondary 12 Graphite, chevron 16px Graphite. `.list--icons` prefixes each row with a 22px content icon (`.i-*` classes select the mask). A row can carry a neutral state word, an attention pill, a switch, or checkbox at its trailing edge instead of a chevron.
- **Profile identity** (`.profile-id`, Profile): superseded the earlier boxed avatar row — a card built from the ordinary grouped-list row read as a cramped, generic settings item, not the one identity header of the whole screen. Sits directly on the screen background, no Surface fill or Hairline border: a 72px round photo (`--s-18`, added to the spacing scale for this) next to the name at Title scale (24/600, the same size as the screen's own h1) with the subtitle in Callout Graphite below. Not a `.list` row, so it never gets a chevron or a card outline — nothing to navigate to here, it just states who you are.
- **Disclosure** (`.disclosure` / `.disclosure--quiet`, present on all 20 screens as the footer's "Where this comes from", plus standalone on Plan as "Change plan"): Surface card or quiet inline, chevron rotates open.
- **Empty state** (`.empty`, 4 screens: Another hut, New plan error, Notes and reviews, My trips): dashed Graphite border, centred sentence, always paired with an exit (a list of alternatives or a primary button) — never a dead end.

### Signature: Instrument panel (`.panel`)
Three (or, on the day card, unevenly-weighted via `--day-cols`) measurements on glass over a photo — distance, ascent, longest day — in equal columns with Hairline dividers. Numeral Tektur 24, unit 12 Graphite, label 10 uppercase Graphite below. 16px padding, radius 24, 12px from the photo edges. `.panel--card` is the identical component off the photo, on a white card with a hairline outline (the day card). Plan and New plan use the photo variant identically.

### Signature: Day chain (`.days` / `.day`)
Days as a chain: a 2px Hairline thread (`::before` on each `<li>`), 24px round numbered nodes (Tektur 12, CSS counter); a day that needs attention gets a yellow node with an ink ring (`.day--warn`); getting there/back use transport Solar icons (`.day--transport`) in place of a numbered node.

### Signature: Avalanche danger scale (`.scale`)
Five equal pill segments in a row; the active step alone is filled Hi-vis Yellow, the rest Hairline. Position on the scale, not fill amount, carries the meaning — explicitly **not** the official four-colour trail grading (green/blue/red/black), which stays reserved for Turrutebasen's own difficulty field and is never reused for anything else in the product. New since the last recording (Safety).

### Signature: Card-photo (`.card-photo`, `.cards`)
A 4:3 (`--ratio-card`) photo, radius 20, with the credit printed on the image over a bottom scrim, an optional country/category pill top-left, then a plain title (16/600) and a Graphite 12px subtitle below the image — no card container of its own. Used for catalogue presets, the nearest-trip card on My trips, and now the Guide/Safety article grid (`guide.html`'s "STF huts" / "DNT huts" / "Fjellvett" cards) — confirmed as a system component, not a one-off, because it now repeats identically across three distinct screens with the same markup.

### Signature: Short hero + floated search (Guide, Safety)
`.hero--short` (190px, bottom scrim, no top scrim, **square corners — no `--r-photo` rounding**) prints the screen name directly on the photo as `.hero__title` (28px), replacing the two-layer header's usual h1 — a hub screen has no brief to show, so the head layer collapses into the photo. Unlike the rounded hero on Plan/New plan/Hut, this photo is the screen's own top identity image, not a card floating over a register, so it runs edge to edge with sharp corners. Guide additionally floats a pill-shaped search field (`.search-float`) half-overlapping the photo's lower edge, a distinct pattern from the pinned `.search` used on the catalogue map.

### Buttons
- **Shape:** 16px radius, 52px tall, 600 16px.
- **Primary** (`.btn--primary`): Signal Blue, white text; one per screen (Save plan, Make a plan, Plan again from this trip). Pressed #2149E0, scale .985.
- **Secondary** (`.btn--secondary`): Surface with a 1.5px inset Hairline, ink text (Cancel, Clear points, Try again); pressed Glass.
- **Tertiary / text action** (`.btn--text` / `.action-text`): Signal Blue text, no frame ("book", "buy", "change"); destructive text in Conflict (`.btn--danger`, "Change and reset", "Delete account").
- **On a photo** (`.btn--glass`, `.btn--round`): round 44px glass buttons (back, share) or a glass capsule ("My trips"), Solar icon 18–22px, white.
- **Disabled** (`:disabled` / `[aria-disabled="true"]`): #C9CDD1 fill, Graphite text, and it says what is missing ("Choose one of the options").
- **SOS, urgent/floating** (`.btn--sos`): Conflict capsule, 56px, Tektur 700, floats absolutely over a photo/map (`.actions--sos`) on Day (in-trip).
- **SOS, static** (`.btn--danger-fill`): the ordinary primary button shape (16px radius, 52px, Wix Madefor 600) filled Conflict instead of Signal Blue — used where SOS sits in the page flow next to a secondary action rather than floating alone, e.g. Safety's "If it's happening now" paired with "Share my route" (`.actions--split`).
- **Focus:** 3px ink outline, 3px offset (`:focus-visible`).
- **Third-party sign-in / connect** (`.btn--apple`, `.btn--google`, `.btn--strava`): the one deliberate hole in the Closed Palette Rule. Apple, Google and Strava each require their own button colour and logo mark, so these are hardcoded outside `ui/kit.css`'s `:root` — same reasoning as the mandatory ©Kartverket attribution string. `.btn--apple`: solid black (`#000`), white text and Apple glyph. `.btn--google`: white fill, `#1F1F1F` text, `#747775` 1px border, the official four-colour "G" mark — Google's own light-button spec, not our Signal Blue. `.btn--strava`: solid Strava orange (`#FC4C02`), white text and the Strava mark — used for "Import from Strava" on Profile. All three keep the ordinary 16px/52px button shape and stay fixed in dark mode (brand identity, not a themed surface). **Garmin has no equivalent codified consumer-facing button the way Apple/Google/Strava do** — "Import from Garmin" deliberately stays `.btn--secondary`, our own style, rather than guessing at a brand treatment; confirm against Garmin's own developer brand guidelines before this ships.

### Chips (`.chip`)
32px, 14/500, pill; unselected Surface with 1.5px Hairline, selected Ink with Glass text (`[aria-pressed="true"]`). The 44px tap target comes from an invisible `::after`, not from a bigger chip. `.chips--on-map` variant floats chips over the catalogue map with the Float shadow on the unselected state.

### Status pills
- **Attention** (`.pill--attention`): Ink pill, white 14/600 text, yellow Solar danger-triangle icon ("1 missing", "flood", "by 18:00").
- **Neutral** (`.pill`): Glass pill with Hairline, ink 14/600 ("bookable", "walk-in only").
- **Fixed** (`.pill--fixed`): Fixed-soft pill, Fixed text and check icon ("Everything fits.").
- **On-photo** (`.pill--photo`): white-92% pill on a photo's top-left corner (preset duration "6 days", country tag on Guide's article cards), Tektur 12 for numerals.

### Alert and verdict
- **Alert (attention)** (`.alert`): Ink panel, radius 20, 8px hatched yellow edge; title 16/600 white, body 14 at 80% white, deadline tag Tektur 12 yellow; opens the place where it is fixed.
- **Verdict (conflict)** (`.alert--conflict`): the same panel with a Conflict-on-Ink hatched edge instead of yellow; options below it are an ordinary grouped list.
- **Static alert** (`.alert--static`): the same ink panel with no chevron/link affordance, for a statement rather than a navigable alert.
- **Knowledge limit** (`.limit`): Graphite text in a 1.5px dashed Graphite frame, radius 20, padding 16 with 48 on the icon side, a 20px Solar cloud-cross icon — used when data is kept but not fresh (offline, couldn't update). `.limit--done` swaps the icon for a check and drops the border for a closed-trip summary line.
- **Loading skeleton** (`.skeleton`, `.skeleton--hero`, `.skeleton--block`): Hairline blocks with a shimmer (1.4s, off under reduced motion); the hero skeleton takes the photo's place and shape for the seconds it takes to generate — an animation, not a photo substitute.

### Forms
- **Field** (`.field` / `.field__input`): label 14/600 above a 52px input, radius 12, 1.5px inset Hairline; focus is a 2px Signal Blue inset ring plus a 4px soft-blue halo (`--e-focus-ring`); error state swaps the ring and hint text to Conflict, a confirmed-ok state to Fixed. Carries its own 16px top margin so it never sits flush against whatever precedes it (a button, another field, a chip row) — reset by nothing, since the base reset zeroes every native margin. Used on Booking number, field notes, sign-in email.
- **Switch** (`.switch`, Settings): 52×28px pill track, Hairline when off, Signal Blue when on; a Surface knob with the Float shadow slides on a 0.2s ease transition.
- **Checkbox** (`.check`, Gear checklist): 22px round, Hairline stroke off, Signal Blue fill with a white check mask when checked.
- **Segmented control** (`.seg`, Notes and reviews): two-way toggle sharing the chip's ink-inversion principle, on a Surface track.

## Do's and Don'ts

### Do:
- **Do** put the three key measurements on the photo in the instrument panel, and put a unit at 12–14px Graphite next to every number.
- **Do** print the photo's author and licence on the photo, and ©Kartverket on every map.
- **Do** say a state in words; let colour and icon reinforce it — including the avalanche scale, which is read by its number/word, never by yellow alone.
- **Do** keep white text on photos on glass no lighter than `rgba(15,17,19,.45)`, or behind the `--shadow-text` text shadow where a glass chip would be too heavy (hero credits, card-photo credits).
- **Do** use Solar icons (linear 1.5; bold only for the active tab's Map/Plans icon).
- **Do** keep everything on a photo 12px from its edges and content 16px from the screen edge.
- **Do** reuse `.card-photo` for any future photo-led catalogue-like grid (it is now confirmed across presets, My trips, and the Guide/Safety article grid) rather than inventing a new card shape.

### Don't:
- **Don't** use Signal Blue for anything that isn't pressed or actionable, and don't use yellow as a fill or as text on light.
- **Don't** set a unit the same size as its number, or box each measurement separately.
- **Don't** use a Unicode glyph (‹ › ✕ ✓ ↗) as an icon.
- **Don't** use text below 12px outside the tab bar, the badge, the day-chain node number, and the uppercase measurement label.
- **Don't** cast shadows on cards or lists; only floating layers get one.
- **Don't** add prev/next day buttons — days are switched from the plan.
- **Don't** reuse the official difficulty grading's colours (green/blue/red/black) for anything else — the avalanche `.scale` deliberately uses yellow-on-hairline instead, precisely so it is never mistaken for Turrutebasen's own grading.
- **Don't** treat a kicker/eyebrow label as a system component: none of the 20 screens use one (headings go straight from photo or icon into the h1/h2), and none should be added — a kicker is not evidenced anywhere in `ui/kit.css` or the painted pages.

## Джерела

- [concept.md](./concept.md) — смак дизайнера, п'ять атрибутів, обраний напрям «Прилад» і кожне правило з причиною; розділ «Прилад у макетах» звіряє concept.md із цим файлом.
- [concept/references.md](./concept/references.md) — запозичені прийоми (N26, 19–86, Airbnb Trips, Komoot, World App) і що з них свідомо не взято.
- Живий стенд мови — [concept.html](./concept.html); канонічний код токенів і компонентів — [ui/kit.css](./ui/kit.css) (вітрина станів — [ui/kit.html](./ui/kit.html), розмітка оболонки — [ui/shell.html](./ui/shell.html)); наскрізний інвентар компонентів по всіх 20 екранах — [ui/inventory.md](./ui/inventory.md).
