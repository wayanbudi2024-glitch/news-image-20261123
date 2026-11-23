# The World in One Day — 23 November 2026

[![make.fun](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/wayanbudi2024-glitch/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/wayanbudi2024-glitch/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123)

An entry for [make.fun's "Sum up 23 November's world news in one image"](https://make.fun/bounty/news-image-20261123) bounty: one program that writes a single image summing up the world's news of Monday, 23 November 2026.

`main.py` (Python 3.13, standard library only, no network) copies `entry.png` to `/output/entry.png`. The image is a newspaper front page — "THE WORLD IN ONE DAY", dated Monday, 23 November 2026 — with five verified stories from the day:

1. **COP31 collapses — no deal** (Antalya): climate talks end with no pact as the EU and UK reject a draft with no mention of fossil fuels; the first summit to fail since 2009.
2. **Democrats take the House** (United States): 258 seats, the largest majority since 1992, after a North Carolina recount win; 44 seats flipped.
3. **Russian warship sunk in Libya** (Benghazi): suspected Ukrainian sea drones sink the corvette Merkury; ten hurt.
4. **Saudi intercepts drone and missile** (Middle East): air defences down a drone bound for Riyadh; six wounded in a strike on a Sanaa fuel station.
5. **UK to host 2035 Women's World Cup** (sport): FIFA confirms the four-nation bid in Zurich — the first World Cup in the UK since 1966.

All text in the image was rendered with PIL (DejaVu fonts); the four panel illustrations were generated without text and composited with the text. The image is 1024×1024 PNG, under 1 MiB, and the program is deterministic: two runs produce byte-identical output.

Run it locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

See `NOTES.md` for the research behind the five stories and their sources.
