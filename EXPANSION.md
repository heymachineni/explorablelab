# Expansion Log

## Product pivot — ExplorableLab museum ✅

**Date:** 2026-06-26

The project shifted from **scale-first** (5,519 markdown files) to **museum-first** (105 canonical exhibits + site + built sims).

| Doc | Role |
|-----|------|
| [`PRODUCT-SPEC.md`](PRODUCT-SPEC.md) | Product specification |
| [`PRODUCT-ROADMAP.md`](PRODUCT-ROADMAP.md) | Phased execution |
| [`meta/CANONICAL-REGISTRY.md`](meta/CANONICAL-REGISTRY.md) | Public museum floor |
| [`site/`](site/) | Astro viewer |
| [`scripts/FROZEN.md`](scripts/FROZEN.md) | Bulk generators frozen |

**Generators frozen:** `generate_to_target.py`, `mature_corpus.py`

---

## Warehouse history (workshop layer)

The bulk corpus exists for graph scaffolding — **not the visitor experience.**

| Batch | Script | Added |
|-------|--------|-------|
| Research | `generate_full_expansion.py` | ~354 curated seeds (SIM, hybrids) |
| Scale | `generate_to_target.py` | ~5,070 stubs |
| Maturation | `mature_corpus.py` | Template upgrade (superseded by canonical pass) |

Most workshop pages need curator review before museum promotion. See [`meta/CANONICAL-REGISTRY.md`](meta/CANONICAL-REGISTRY.md) for the public subset.

---

## Browse (workshop)

| Index | Path |
|-------|------|
| Tier S build queue | [`indices/by-score/tier-s.md`](indices/by-score/tier-s.md) |
| Research concepts | [`indices/awesome/simulation-concepts.md`](indices/awesome/simulation-concepts.md) |
| Canonical only (museum) | [`indices/awesome/canonical-exhibits.md`](indices/awesome/canonical-exhibits.md) |
