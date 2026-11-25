---
name: GoIA
description: Daylight walking routes for CDMX, drawn as one sun-yellow line along a shaded sidewalk.
colors:
  route: "#f2c94c"
  route-deep: "#d9a92a"
  route-pill: "#f7d75c"
  forest-ink: "#144134"
  ink-soft: "#1b3525"
  ink-muted: "#4d6357"
  button-green: "#0f4535"
  button-green-deep: "#0a3327"
  button-edge: "#2d5e50"
  field-edge: "#4f6b5f"
  ink-mist: "#d5ded7"
  ground: "#f3f4ef"
  ground-deep: "#e9ebe3"
  paper-white: "#fbfbf7"
  map-ground: "#e4e3dc"
  map-street: "#f1f0ea"
  fast-gray: "#9c9d97"
  fast-pill: "#e6e5df"
  zone-violet: "#7b3294"
  error-brick: "#8a2c1f"
  fast-gray-deep: "#6f706a"
  ink-mist-dim: "#aebdb3"
typography:
  display-compact:
    fontFamily: "Noticia Text, Georgia, serif"
    fontSize: "clamp(2rem, 1.2rem + 4vw, 2.9rem)"
    fontWeight: 700
    lineHeight: 1.1
  ui-heading:
    fontFamily: "Noticia Text, Georgia, serif"
    fontSize: "clamp(1.5rem, 1.25rem + 0.8vw, 1.85rem)"
    fontWeight: 700
    lineHeight: 1.16
  ui-figure:
    fontFamily: "Noticia Text, Georgia, serif"
    fontSize: "2rem"
    fontWeight: 700
    lineHeight: 1
  ui-wordmark:
    fontFamily: "Noticia Text, Georgia, serif"
    fontSize: "1.6rem"
    fontWeight: 700
    lineHeight: 1
  ui-title-lg:
    fontFamily: "Noticia Text, Georgia, serif"
    fontSize: "1.25rem"
    fontWeight: 700
    lineHeight: 1.2
  ui-title:
    fontFamily: "Noticia Text, Georgia, serif"
    fontSize: "1.12rem"
    fontWeight: 700
    lineHeight: 1.25
  ui-lead:
    fontFamily: "Vend Sans, Segoe UI, system-ui, sans-serif"
    fontSize: "1.06rem"
    fontWeight: 300
    lineHeight: 1.55
  ui-body:
    fontFamily: "Vend Sans, Segoe UI, system-ui, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.5
  ui:
    fontFamily: "Vend Sans, Segoe UI, system-ui, sans-serif"
    fontSize: "0.95rem"
    fontWeight: 400
    lineHeight: 1.45
  ui-small:
    fontFamily: "Vend Sans, Segoe UI, system-ui, sans-serif"
    fontSize: "0.9rem"
    fontWeight: 400
    lineHeight: 1.4
  ui-caption:
    fontFamily: "Vend Sans, Segoe UI, system-ui, sans-serif"
    fontSize: "0.82rem"
    fontWeight: 500
    lineHeight: 1.3
  credit:
    fontFamily: "Vend Sans, Segoe UI, system-ui, sans-serif"
    fontSize: "0.75rem"
    fontWeight: 400
    lineHeight: 1.3
  display:
    fontFamily: "Noticia Text, Georgia, serif"
    fontSize: "clamp(2rem, 1.2rem + 4vw, 3.4rem)"
    fontWeight: 700
    lineHeight: 1.12
    letterSpacing: "-0.012em"
  headline:
    fontFamily: "Noticia Text, Georgia, serif"
    fontSize: "clamp(1.9rem, 1.2rem + 2.4vw, 3.25rem)"
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: "-0.015em"
  title:
    fontFamily: "Noticia Text, Georgia, serif"
    fontSize: "clamp(1.6rem, 1.2rem + 1.5vw, 2.5rem)"
    fontWeight: 700
    lineHeight: 1.12
  title-sm:
    fontFamily: "Noticia Text, Georgia, serif"
    fontSize: "clamp(1.3rem, 1.1rem + 0.7vw, 1.7rem)"
    fontWeight: 700
    lineHeight: 1.2
  lead:
    fontFamily: "Vend Sans, Segoe UI, system-ui, sans-serif"
    fontSize: "clamp(1.06rem, 0.98rem + 0.35vw, 1.28rem)"
    fontWeight: 300
    lineHeight: 1.55
  body:
    fontFamily: "Vend Sans, Segoe UI, system-ui, sans-serif"
    fontSize: "1.1rem"
    fontWeight: 300
    lineHeight: 1.6
  label:
    fontFamily: "Vend Sans, Segoe UI, system-ui, sans-serif"
    fontSize: "0.86rem"
    fontWeight: 500
    lineHeight: 1
    fontFeature: "tnum"
rounded:
  focus: "4px"
  control: "6px"
  stage: "8px"
  pill: "999px"
spacing:
  gutter: "clamp(16px, 5vw, 64px)"
  container: "1180px"
  section: "clamp(80px, 11vw, 152px)"
  column-gap: "clamp(32px, 6vw, 96px)"
  feature-gap: "clamp(72px, 10vw, 136px)"
  field-gap: "10px"
components:
  button-primary:
    backgroundColor: "{colors.button-green}"
    textColor: "{colors.paper-white}"
    typography: "{typography.body}"
    rounded: "{rounded.control}"
    padding: "0 24px"
    height: "54px"
  button-primary-hover:
    backgroundColor: "{colors.button-green-deep}"
  nav-cta:
    backgroundColor: "{colors.button-green}"
    textColor: "{colors.paper-white}"
    rounded: "{rounded.control}"
    padding: "10px 16px"
  input-email:
    backgroundColor: "{colors.paper-white}"
    textColor: "{colors.forest-ink}"
    rounded: "{rounded.control}"
    padding: "0 18px"
    height: "54px"
  pill-route:
    backgroundColor: "{colors.route-pill}"
    textColor: "{colors.forest-ink}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
  pill-fast:
    backgroundColor: "{colors.fast-pill}"
    textColor: "{colors.forest-ink}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
  map-tag:
    backgroundColor: "{colors.paper-white}"
    textColor: "{colors.forest-ink}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: "6px 12px"
  photo-frame:
    backgroundColor: "{colors.ground-deep}"
    rounded: "{rounded.control}"
  map-stage:
    backgroundColor: "{colors.map-ground}"
    rounded: "{rounded.stage}"
  ink-band:
    backgroundColor: "{colors.forest-ink}"
    textColor: "{colors.paper-white}"
---

# Design System: GoIA

## Overview

**Creative North Star: "Banqueta con sombra"**

GoIA looks like an ordinary sunny sidewalk that a local would pick: shaded, kept up, with people walking on it. The ground is a fresh off-white, the ink is a deep forest green, and the only accent in the whole world is one sun-yellow route line that walks you along the street. Safety is told through daylight, trees and people, never through night, sirens or shield icons.

Density is calm and generous. Sections breathe with tall vertical padding, copy sits in short measures beside large eye-level photographs, and the yellow line threads the page as a continuous object: it starts in the hero photo, lands on the hero map, connects the three steps, and becomes the route on the sample map. Leaf-shadow light is the texture. It appears as dappled shade in the photography and, literally, as a multiplied leaf-light pattern inside the map lens.

The voice is a confident editorial serif for headlines over a light, plain sans for copy, with square-shouldered green controls. Nothing is glossy, nothing floats on shadows, and nothing reads as a tech product.

**Key Characteristics:**
- Off-white ground, forest-green ink, one sun-yellow accent reserved for the route.
- Bold slab-leaning serif (Noticia Text) headlines, light-weight sans (Vend Sans) copy.
- Morning daylight photography of tree-lined CDMX sidewalks with leaf shadows and people walking.
- Flat surfaces, small 6px corners, no drop shadows.
- The route line is the narrative thread and the only animated object.

## Colors

A daylight palette: pale paper ground, deep leaf-green ink, and a single warm yellow that means "the GoIA route" wherever it appears.

### Primary
- **Sun Route Yellow** (route): the GoIA route line in the hero, the hero map, the steps connector, the sample map, legend swatches, list markers, focus rings and text selection. It means "the way GoIA suggests" and nothing else.
- **Late-Sun Ochre** (route-deep): the outer casing of the route inside the map lens, list-marker rims and the nav-link hover underline. Always paired with Sun Route Yellow, never alone.
- **Pale Route Yellow** (route-pill): fill of the "Ruta GoIA · N min" time pill, so the label sits beside the line without competing with it.

### Secondary
- **Forest Ink** (forest-ink): headlines, primary text, the brand wordmark, map endpoints and walker rim, and the full-bleed ink bands (how-it-works section, footer).
- **Button Green** (button-green) and **Deep Button Green** (button-green-deep): the filled controls at rest and on hover. **Button Edge** (button-edge) is their 1px border.

### Neutral
- **Daylight Ground** (ground): page background and the color photo washes fade into.
- **Shade Ground** (ground-deep): placeholder behind photo frames.
- **Paper White** (paper-white): input fields, text on ink bands and buttons, map tag fill.
- **Soft Ink** (ink-soft) and **Muted Ink** (ink-muted): lead and body copy, then fine print and map notes.
- **Field Edge** (field-edge): 1.5px input borders.
- **Ink Mist** (ink-mist): secondary text on Forest Ink bands. **Dim Ink Mist** (ink-mist-dim) is the quieter fine print in the footer base row.
- **Map Ground** (map-ground) and **Map Street** (map-street): the sample map's blocks and streets, quiet so the routes carry it.
- **Fast Gray** (fast-gray) and **Fast Pill** (fast-pill): the "Más rápida" comparison route (dotted) and its time pill. The fastest route is always gray, never a second accent. **Deep Fast Gray** (fast-gray-deep) draws the dotted route when the person has selected it in the app, so the choice reads without a new hue.
- **Zone Violet** (zone-violet): dashed 2.5px outline of "zona con reportes" circles, filled at 18 to 28% alpha. Chosen over the earlier muted clay, which blended into the OpenStreetMap tiles. Violet stays distinct from the yellow route and the OSM tile colors under protanopia, deuteranopia and tritanopia, and it is never alarm red. It is 7.4:1 on paper, but it stays a shape and icon color: warning text stays in Forest Ink beside a violet icon.
- **Error Brick** (error-brick): form error messages only.

### Named Rules
**The One Line Rule.** Yellow belongs to the route. It may mark the route, its time, its stops, and keyboard focus. It never fills a button, a background band or a decorative shape.

**The Gray Alternative Rule.** The comparison route is shown in neutral gray (dotted on the map), so the choice reads as "the route" versus "just faster," not as two competing colors.

**The Daylight Rule.** No dark or night themes for brand surfaces. Dark green appears only as solid ink bands between daylight sections.

## Typography

**Display Font:** Noticia Text 700 (with Georgia, serif), self-hosted
**Body Font:** Vend Sans variable 300 to 700 (with Segoe UI, system-ui, sans-serif), self-hosted

**Character:** A sturdy newspaper serif speaks with local, editorial confidence. The light sans underneath keeps copy plain and quiet, like a neighbor's advice rather than a product pitch.

### Hierarchy
- **Display** (700, about 3.4rem on desktop, 1.12): the hero headline only, balanced wrap, slight negative tracking.
- **Headline** (700, clamp 1.9rem to 3.25rem, 1.1): section headings, max about 11 to 16em wide.
- **Title** (700, clamp 1.6rem to 2.5rem, 1.12): feature row headings.
- **Title Small** (700, clamp 1.3rem to 1.7rem, 1.2): step headings on the ink band.
- **Lead** (300, clamp 1.06rem to 1.28rem, 1.55): the one-paragraph intro under a heading, max 34em.
- **Body** (300 to 400, 1.04 to 1.1rem, 1.55 to 1.6): feature and step copy, max 28 to 34em. Bold lead-ins inside lists use 600 in Forest Ink.
- **Label** (500, 0.86 to 0.95rem, tabular numerals): pills, map tag, legend rows, map notes. Minutes and meters always use tabular figures.
- **Display Compact** (700, clamp 2rem to 2.9rem, 1.1): the hero headline below 900px.

### App UI scale
The app at `/app/` is an Operate surface, so its steps are fixed and smaller than the landing's editorial ramp. They live as `--fs-*` custom properties in `web/app/index.html`.
- **UI Heading** (Noticia 700, clamp 1.5rem to 1.85rem): one per view, a plain sentence ending in a period.
- **UI Figure** (Noticia 700, 2rem): minutes left while walking.
- **UI Wordmark** (Noticia 700, 1.6rem) and **UI Title Large** (Noticia 700, 1.25rem): the app header and the walking instruction or dialog title.
- **UI Title** (Noticia 700, 1.12rem): section openers and route names.
- **UI Lead** (Vend Sans 300, 1.06rem) and **UI Body** (400, 1rem): the intro line under a heading, then controls and running text.
- **UI** (0.95rem), **UI Small** (0.9rem) and **UI Caption** (500, 0.82rem): secondary lines, notes and errors, then badges and the map tag.
- **Credit** (0.75rem): map attribution only. Nothing a person reads to act goes below UI Caption.

### Named Rules
**The Serif Speaks First Rule.** Every section opens with a serif sentence, written as a plain statement ending in a period. Sans text never takes the heading role.

**The Light Copy Rule.** Running copy is Vend Sans at weight 300 to 400. Weight 600 is reserved for short bold lead-ins and legend names.

## Layout

A single centered container (max 1180px, side gutter clamp(16px, 5vw, 64px)) with tall section padding (clamp(80px, 11vw, 152px)). Content sections are two-column splits of photo and text (gap clamp(32px, 6vw, 96px)), and feature rows alternate photo side down the page with large gaps between rows. Full-bleed moments break the container: the hero photo, the Forest Ink how-it-works band, the closing photo section and the footer.

The hero is a full-bleed photo washed to the ground color on the left, where headline, one line of copy and the email field sit above the fold. Below 1024px all splits collapse to one column and the steps stack vertically with the connector hidden. Below 900px the hero becomes a stacked flow: header, headline, copy, form, then the photo and the hero map. The closing wash turns from a left-to-right gradient into a top-to-bottom one.

## Elevation & Depth

Flat. There are no box shadows anywhere. Depth comes from three things: photographic light (morning sun and leaf shadow), translucent ground-colored washes that let copy sit on a photo (a 90deg gradient from 94% ground to transparent at 72%), and tonal bands of Forest Ink against Daylight Ground. Inside the sample map, the lens is a brighter disc with a multiplied leaf-light texture and a thin Forest Ink rim, which reads as a pool of light rather than a raised card.

### Named Rules
**The Light Not Shadow Rule.** Depth is sunlight and shade, never drop shadows. A surface that needs separation gets a tonal change or a photo wash.

## Shapes

Small, square-shouldered corners: 6px on buttons, inputs and photo frames, 8px on the map stage, 4px on focus outlines. Pills (time labels, map tag) are fully rounded. Circles are reserved for route semantics: list markers (yellow with ochre rim), step stops (ring or filled), map endpoints and the walker dot. Lines are round-capped. Photos sit in clean rectangles (4:5 for the needs column, 3:2 for feature rows) with no borders.

## Components

### Buttons
Square-shouldered and solid, in green ink.
- **Shape:** gently squared corners (6px).
- **Primary:** Button Green fill, Paper White text, 1px Button Edge border, 54px tall with 24px side padding, weight 500.
- **Hover / Active:** fill darkens to Deep Button Green over 160ms ease-out. Press nudges down 1px over 120ms.
- **Focus:** 3px Sun Route Yellow outline, 3px offset.
- **Disabled:** 70% opacity with a progress cursor while the email submits.
- **Nav CTA:** the same button, compact (10px 16px), in the header.

### Inputs / Fields
- **Style:** Paper White fill, 1.5px Field Edge border, 6px corners, 54px tall, 18px side padding. Always paired side by side with the primary button (stacked full width on mobile).
- **Hover:** border shifts to Forest Ink.
- **Focus:** the shared yellow focus ring.
- **Status:** a polite live region under the form. Success in Forest Ink, errors in Error Brick, worded as plain Spanish instructions.

### Chips (time pills)
- **Style:** fully rounded pills with tabular numerals. "Ruta GoIA · N min" on Pale Route Yellow, "Más rápida · N min" on Fast Pill gray. Always shown as a pair so the time cost is explicit.

### Navigation
- **Style:** the GoIA wordmark in Noticia Text 700 at left, two plain text links (weight 500) and the compact CTA at right. Link hover is a 2px Late-Sun Ochre underline offset 0.3em. On mobile the text links hide and the wordmark plus CTA remain.

### Steps on the route
Three steps on a Forest Ink band, joined by a 4px round-capped yellow line. Each step has a 26px stop: Forest Ink fill with a 4px yellow ring, and the last stop filled yellow as the destination. On narrow screens the line is hidden and steps stack.

### Needs list
A list of short needs, each led by a 14px yellow dot with an ochre rim, a bold Forest Ink lead-in sentence and a light follow-up line.

### Feature rows
Photo plus serif title plus one short paragraph, alternating sides. Photos ease to scale 1.025 on hover over 900ms (cubic-bezier(0.16, 1, 0.3, 1)) inside their 6px frame.

### Map stage and leaf-light lens (signature)
A real-street sample map on Map Ground, 16:7 (4:3 on mobile), 8px corners, with a "Datos de ejemplo" tag at top left and a legend beside the heading. The GoIA route is solid yellow, the fastest route dotted gray, report zones are dashed violet circles. A circular lens follows the pointer or finger (eased at 0.14 per frame): inside it the streets widen to white, a leaf-light texture is multiplied in, street names appear in small sans with a paper halo, and the route is drawn with an ochre casing so it lifts out of the grid. With no pointer, the lens drifts slowly along the route. A paper-white walker dot with a Forest Ink rim travels the route on a 9 second loop. Reduced motion holds the lens still at mid-route and removes the walker.

### Hero route
The yellow route enters as a tapered band painted over the hero sidewalk, then continues as the line on a clipped hero map strip with the two time pills, so the route visibly starts in the photo and continues into the map.

### Footer
A Forest Ink band with the serif wordmark, a one-line tagline in Ink Mist, plain Paper White links with a yellow hover underline, and a base row separated by a 20% Ink Mist rule.

## Do's and Don'ts

### Do:
- **Do** keep Sun Route Yellow (route) for the route, its stops, its time pill and focus, and nothing else.
- **Do** pair every safe-route time with the fastest-route time, in a yellow pill and a gray pill.
- **Do** use morning daylight photography of tree-lined CDMX sidewalks with people walking calmly, and fade it into Daylight Ground where copy sits on it.
- **Do** open sections with a Noticia Text 700 sentence and follow with a light Vend Sans lead (weight 300, max 34em).
- **Do** keep controls square-shouldered (6px) in Button Green with a 1px Button Edge border.
- **Do** honor reduced motion: hold the lens, drop the walker, keep every route fully drawn.
- **Do** label sample data on the map ("Datos de ejemplo") and keep zones illustrative.

### Don't:
- **Don't** use drop shadows or floating cards. Depth is light, washes and ink bands.
- **Don't** show night streets, crime-news imagery, sirens, shields or alarm red. Report zones are violet.
- **Don't** introduce a second accent color. The fast route stays gray.
- **Don't** start content hidden or draw routes in on scroll. Static views must show every route complete.
- **Don't** put a phone mockup over a map as the hero.
- **Don't** use small uppercase eyebrow labels above headings. Uppercase tracked text belongs only to place names printed on a map.
