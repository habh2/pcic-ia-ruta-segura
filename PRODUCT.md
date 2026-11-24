# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

- One web application in `web/`, served by a small local Python (Flask) backend (`web/server.py`). Self-hosted by the team. Chosen by the user over a hosted Artifact database.
- Landing page at `/` (`web/index.html`): static HTML/CSS/JS. The backend writes pre-registration emails to a CSV. A secondary "Probar el demo" link leads to the app.
- Product app at `/app/` (`web/app/index.html`): single file, Leaflet 1.9.4 with OpenStreetMap tiles, Noticia Text and Vend Sans from the shared `web/assets/fonts/`. It must be served over http, because OpenStreetMap rejects tile requests without a referer.

## Users

Primary: people who move around Mexico City on foot or by public transport through areas they do not know. Typical cases are someone who just moved to the city, a visitor, or a local entering a part of the city they don't usually walk. Their job is getting from A to B without walking into a street where they could be robbed, while still arriving in reasonable time. Today they use Google Maps (which only minimizes time) and ask classmates or neighbors.

Reference archetype (fictional, from the business model): a graduate student new to CDMX who walks from the metro to campus through colonias she doesn't know yet.

Secondary (pays, not addressed by the landing page): businesses in safe zones that want more foot traffic.

## Product Purpose

Suggest walking routes from A to B that weigh the safety of each street, not only travel time, and let the user compare the safe route against the fastest one. Success is measured in platform visits, completed routes and submitted incident reports. The landing page exists to collect pre-registrations for the free trial version (hypothesis H6: at least 3% of visitors register in the first four weeks).

## Positioning

Mainstream planners (Google Maps, Waze) optimize time and are not built for pedestrians' safety. Safety-aware route planners exist abroad (Streetwise in Paris, Lyon and Brussels, RouteSafe in Turkey) but not for Mexico or Latin America. GoIA puts risk inside the route search itself (A* with a risk-weighted cost) for CDMX streets, with risk kept current by users' own incident reports.

## Operating Context

- Launch area: alcaldía Cuauhtémoc, CDMX (MVP). Pilot reasoning: about 63,215 economic units, the highest per-capita concentration in CDMX (2024), and first among alcaldías in robo a transeúnte at 390.8 per 100,000 inhabitants (sources in `reportes/ModeloDeNegocio/modelo_negocio.tex`).
- Used on a phone browser or a computer. Registration by email (or Google account, planned).
- Acquisition: LinkedIn teaser about the problem, student groups, CDMX community groups, short videos (`metricas_landing.csv`).

## Capabilities and Constraints

- Route planning with A* over a risk-weighted street graph, showing the recommended route's risk level and the fastest route for comparison.
- Collaborative incident and unsafe-zone reports (coordinates, date and time).
- Sponsored businesses appear as featured pins along the route (revenue side, 100 MXN per 1,000 impressions after a free 2,000-impression trial).
- The app is free for users, with no paywall on core features.
- Planned, not confirmed: government incident data at a higher update frequency (H9).

## Brand Commitments

- Display name: **GoIA** (current candidate, may change). Code name: **RutaSegura**, used for file names, folders and identifiers (`ruta-segura`).
- Public surfaces read as a real product: no university, course, assignment, author list or academic framing.
- Language: Spanish, for a CDMX audience (confirmed).
- Tone: streets, lamps, safety. Not a transit (Metro) app, and no market, tianguis, tourist or "come visit" angle. Calm and reassuring, never alarming (no crime-news imagery), never technical, never generic startup styling.
- Customer-facing surfaces talk about outcomes, not implementation. No algorithm names (A*), cost functions, graphs or other technical internals on the landing page. The visitor does not care how the route is computed.

## Evidence on Hand

- Business model, canvas and 12 hypotheses: `reportes/ModeloDeNegocio/` (all hypotheses still `pendiente`).
- One interview so far (E01, a business owner): "Estoy un poco escondido para los ojos del publico".
- Landing metrics: not collected yet (`metricas_landing.csv` is all `Pendiente`).
- Original proposal: `reportes/IA propuesta.docx-1.pdf`. Financial model: `reportes/modelo_financiero.xlsx`.
- Working app build: `web/app/index.html` (Colonia Cuauhtémoc, Paseo de la Reforma corridor).
- Absent, must not be fabricated: user counts, testimonials from users, ratings, press, partner logos, validated percentages, app store presence.

## Product Principles

1. Safety is part of the route, not a layer on top of it. Always show what the safer route costs in time compared to the fastest one.
2. Free for the person walking. Revenue comes from businesses, never from gating safety information.
3. The community keeps the map honest. Reports from people on the street are the core data source.
4. Local first. Built for CDMX streets and conditions, starting in Cuauhtémoc.
5. Claim only what is true. Show the mechanism and the real launch area, not invented traction.
