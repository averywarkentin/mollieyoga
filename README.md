# Mollie Yoga — Brand Concepts

Three brand directions for **Mollie Yoga**, built for the next check-in: an aligning
conversation on overall colour, palette and design/brand concept.

📄 **The deliverable:** [`deck/MollieYoga-Brand-Concepts.pdf`](deck/MollieYoga-Brand-Concepts.pdf) — a 15-page deck.

## What's inside

1. **Cover**
2. **The brief** — what we're aligning on (pulled from the likes/dislikes + call) and the three directions at a glance
3–6. **Direction 01 · In Flow** — aurora gradients + kinetic type · *Fraunces / Space Grotesk*
7–10. **Direction 02 · Earth & Ember** — bold, grounded, lit by fire · *Bricolage Grotesque / Spectral*
11–14. **Direction 03 · Talisman** — folk-modern symbols + flat colour · *Syne / DM Sans*
15. **Next step** — questions to react to

Each direction is a complete world: **colour palette · typography · a small brand mark
("little tag") · Instagram system (grid + stories + reel cover) · website mockup (on Wix)**.

## Direction principles (from Mollie's references)

- Typography with **movement**; bold, confident use of text + photo
- Gradient / watercolour / abstract photography
- Green · blue · violet, warmed with amber/orange highlights — **no beige & sage**
- Symbol & spirit: prayer hands, yin-yang, sun, the elements — drawn modern, never whimsical
- Earthy and grounded with a bit of fire; approachable, "anyone can do yoga"
- Never looks like a Canva template

> Photography is represented by abstract gradient fields throughout — they hold the space
> until Mollie's shoot, and double as a real on-brand treatment.

## Regenerating the deck

```bash
python3 deck/build.py            # writes deck/index.html
node deck/render.mjs pdf         # writes deck/MollieYoga-Brand-Concepts.pdf
node deck/render.mjs shot 1,4,5  # optional: PNG previews of given pages
```

- `deck/build.py` — generator (palettes, type, marks, mockups live here as data/SVG)
- `deck/css/deck.css` — page system (1280×720), device mockups, swatches, grain
- `assets/fonts/` — self-hosted web fonts (woff2) so rendering is deterministic offline
- `assets/grain.png` — tileable film-grain texture

Rendering uses the pre-installed Chromium via Playwright
(`executablePath: /opt/pw-browsers/chromium`).
