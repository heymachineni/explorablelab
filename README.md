# ExplorableLab

**A digital museum for ideas that only make sense when you play with them.**

> Explore ideas that only make sense when you play with them.

This repository powers **ExplorableLab** — not a wiki, not documentation, a museum.

---

## Two layers

| Layer | What | Who sees it |
|-------|------|-------------|
| **Museum floor** | ~105 canonical exhibits · collections · built sims | Everyone |
| **Workshop** | Full markdown corpus · templates · scripts | Contributors |

Public surface: [`meta/CANONICAL-REGISTRY.md`](meta/CANONICAL-REGISTRY.md)

---

## Start here

| I want to… | Go to |
|------------|-------|
| **Product vision** | [`PRODUCT-SPEC.md`](PRODUCT-SPEC.md) |
| **Execution roadmap** | [`PRODUCT-ROADMAP.md`](PRODUCT-ROADMAP.md) |
| **Museum floor (105 slugs)** | [`meta/CANONICAL-REGISTRY.md`](meta/CANONICAL-REGISTRY.md) |
| **Collections** | [`indices/collections/`](indices/collections/) |
| **Run the site (local)** | [`site/README.md`](site/README.md) |
| **Live site** | [heymachineni.github.io/explorablelab](https://heymachineni.github.io/explorablelab/) |
| **Design bible** | [`EXPLORABLE_EXPLANATIONS_RESEARCH.md`](EXPLORABLE_EXPLANATIONS_RESEARCH.md) |
| **Build Tier S sims** | [`indices/by-score/tier-s.md`](indices/by-score/tier-s.md) |
| **Contribute (workshop)** | [`CONTRIBUTING.md`](CONTRIBUTING.md) · [`AGENT_GUIDE.md`](AGENT_GUIDE.md) |
| **Architecture (workshop)** | [`ARCHITECTURE.md`](ARCHITECTURE.md) |

---

## Principles

- **Curator's gate** — every exhibit answers: *Why does this deserve an explorable?*
- **Markdown-first** — corpus is source of truth; site is the viewer
- **Graph-native** — ideas connect; visitors wander, not search folders
- **CC0** — public domain ([`LICENSE`](LICENSE))

---

## Workshop corpus (contributors only)

~5,519 markdown nodes exist for graph maintenance. **Not shown to museum visitors by default.**

| Doc | Purpose |
|-----|---------|
| [`EXPANSION.md`](EXPANSION.md) | How the warehouse was built |
| [`indices/CORPUS-STATS.md`](indices/CORPUS-STATS.md) | Type counts |
| [`scripts/FROZEN.md`](scripts/FROZEN.md) | Generators frozen — do not re-run bulk scripts |

---

## Layout

```
content/          ← workshop corpus (all nodes)
site/             ← ExplorableLab public viewer (canonical only)
indices/          ← collections, paths, wings
meta/             ← canonical registry, taxonomy, scoring
templates/        ← page templates for contributors
EXPLORABLE_EXPLANATIONS_RESEARCH.md  ← design bible
```
