# ExplorableLab — Product Status

**Updated:** 2026-06-26  
**Companion:** [`PRODUCT-SPEC.md`](PRODUCT-SPEC.md) · [`PRODUCT-ROADMAP.md`](PRODUCT-ROADMAP.md)

---

## Phase completion

| Phase | Status | Notes |
|-------|--------|-------|
| **0 — Freeze warehouse** | ✅ Done | `scripts/FROZEN.md`, README/EXPANSION updated |
| **1 — Canonical 100** | ✅ Done | 105 registry slugs promoted via `build_museum.py` |
| **2 — Collections & paths** | ✅ Done | 12 collections, 5 paths, 7 wings, `canonical-exhibits.md` |
| **3 — Site v1** | ✅ Done | Astro site builds; homepage, exhibits, collections, graph |
| **4 — Native sim** | ✅ Done | Petrie Multiplier + Ergodicity Street |
| **5 — Graph v2** | ✅ Done | Constellation, Rabbit Hole, trail, **Compare mode** |
| **6 — Studio & classroom** | 🟡 Partial | E.C.H.O. worksheet + teacher guide |
| **7 — Scale floor** | 🟡 Started | Registry at 105; expand to 250+ over time |

---

## Deploy (Vercel)

See [`DEPLOY.md`](DEPLOY.md). **Root Directory must be `site`.**

No paid GitHub plan required — Vercel free tier works for this static site.

---

## Run the museum

```bash
cd scripts && python3 build_museum.py
cd ../site && npm install && npm run dev
```

---

## Public surface

| Layer | Count | Visible to visitors |
|-------|-------|---------------------|
| Canonical exhibits | 105 | Yes |
| Workshop corpus | ~5,519 | No |
| Collections | 12 | Yes |
| Native sims shipped | 2 | Petrie Multiplier, Ergodicity Street |

---

## Next priorities

1. Connect Vercel to GitHub and deploy (see DEPLOY.md)
2. Build Tier S #3: `goodhart-school` or `braess-roads`
3. Expand annotated graph edges on canonical set
4. Ship remaining Tier S prototypes over time

---

## Quality bar

- All 105 registry slugs: `status: canonical`
- Generators: **frozen** — do not run `generate_to_target.py`
