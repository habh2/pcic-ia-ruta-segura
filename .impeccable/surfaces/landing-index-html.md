---
version: 1
slug: "landing-index-html"
primary_target: "landing/index.html"
related_targets: []
---

# Landing page (GoIA)

Scope: public pre-launch landing page, `landing/index.html`, served with a small Flask backend that stores emails. Visitor mode: Persuade.

Audience and action: anyone walking from A to B in CDMX who wants to weigh other people's safety reports (daily routes as much as unfamiliar areas; never framed as newcomers only). One action: pre-register for the free trial with an email.

Proof and content: demo only. A sample route in colonia Cuauhtémoc on the real street graph from app/index.html, labeled as a sample (stated decision after the hero: the comp said Juárez). No crime statistics, no invented users, testimonials or counters. No algorithm or technical vocabulary.

User-pinned requirements: prominent image and tagline first, customer needs, feature showcase, images throughout, one element that moves with the mouse, a working email-only pre-registration that stores emails, a map graphic, no university references.

Tone: daylight streets and safety, lamps as a detail. Not transit, not market or tourist, not night, not alarming, not technical, not generic startup.

## Direction contract

THESIS: Safety looks like an ordinary sunny sidewalk you would happily pick: shaded, kept up, with people walking on it. GoIA's yellow route walks you along it. The page refuses the category default (a phone mockup over a map with shield icons) and the night or crime register.

OWN-WORLD: Fresh off-white ground, deep forest-green ink, morning daylight photography with leaf shadows, and one sun-yellow route line as the only accent. A confident serif for headlines and a plain sans for copy. Square-shouldered controls in green ink. Leaf-shadow light is the texture.

STORY: The visitor sees a calm street they would happily walk, understands that GoIA picks that kind of sidewalk and says what it costs in minutes, sees how it works, plays with the sample map, and leaves an email.

FIRST VIEWPORT: Approved comp `.impeccable/mocks/decision/r2-pick.png`. A full-bleed eye-level photo of a tree-lined sidewalk in morning sun, washed to white on the left where the serif headline, one line of copy and the working email field sit. Headline, one line of copy and the working email field are all above the fold, and the yellow route starts in the hero and continues into the map below.

FORM: Banqueta con sombra, Impeccable's pick, position 1 of the grounded list (third hand, daylight steer). seed: ed7fafa4dad1ada1. Signature interaction: a leaf-shadow light lens (generated dappled-light texture, multiplied) that follows the cursor or finger over the map, enlarges streets, names them, and lifts the yellow route out of the street grid; with no pointer it drifts along the route. Motion: a walker dot travels the GoIA route continuously. No content starts hidden: an earlier scroll draw-on was removed because static captures showed missing routes. Reduced motion holds the lens and drops the walker.

FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance
