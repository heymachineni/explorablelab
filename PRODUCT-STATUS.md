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
| **4 — Native sim** | ✅ Done | `site/public/sims/petrie-multiplier/` |
| **5 — Graph v2** | 🟡 Partial | Constellation + Rabbit Hole + local trail |
| **6 — Studio & classroom** | 🟡 Partial | E.C.H.O. worksheet page + teacher guide markdown |
| **7 — Scale floor** | 🟡 Started | Registry at 105; expand to 250+ over time |

---

## Run the museum

```bash
# Regenerate canonical content + site data
cd scripts && python3 build_museum.py

# Build static site
cd ../site && npm install && npm run dev
# or: npm run build
```

---

## Public surface

| Layer | Count | Visible to visitors |
|-------|-------|---------------------|
| Canonical exhibits | 105 | Yes |
| Workshop corpus | ~5,519 | No (Research Mode for contributors) |
| Collections | 12 | Yes |
| Native sims shipped | 1 | Petrie Multiplier |

---

## Next priorities

1. **Deploy** — GitHub Pages via `.github/workflows/deploy-pages.yml` → [live site](https://heymachineni.github.io/explorablelab/)
2. Build Tier S #2: `ergodicity-street` or `goodhart-school`
3. Compare mode on graph (two exhibits side-by-side)
4. Fix collection stops that reference sims not yet built (expected — cards show "coming soon" until built)
5. Expand annotated edges on canonical graph

---

## Quality bar

- All 105 registry slugs: `status: canonical`
- EXE pages: research autopsy bodies
- Reference theory: `schelling-segregation.md` (preserved, promoted)
- Generators: **frozen** — do not run `generate_to_target.py`
