# ExplorableLab — Product Specification

**Version:** 1.0 · **Date:** 2026-06-26  
**Status:** Approved direction — implementation not started  
**Audience:** Curators, designers, developers, contributors

---

## 1. Product definition

### What ExplorableLab is

**ExplorableLab is a digital museum for ideas that only make sense when you play with them.**

It is not:
- A wiki (definitions without manipulation)
- Documentation (how the repo works)
- A link farm (5,000 alphabetized pages)
- A MOOC (linear video + quiz)

It is:
- A place to **play**, **discover**, and **follow paths** through human knowledge
- A catalog of **exhibits** (canonical nodes + built simulations)
- A **studio** for explorable-explanation designers (hidden workshop layer)
- A **graph** of relationships between evidence, ideas, patterns, and canon

### One-sentence north star

> *"I spent an hour on ExplorableLab and I see the world differently."*

### Success metrics (decade horizon)

| Metric | Target |
|--------|--------|
| Canonical exhibits | ~500 deeply curated |
| Built simulations | 135 specs → prioritize Tier S (18) first |
| First-visit play rate | >60% interact with hero or arcade within 30s |
| Share rate | Every exhibit ends with a shareable "send this" moment |
| Return visits | Personal trail / discovery mode drives re-entry |
| Teacher use | Classroom paths with time estimates + prompts |
| Contributor quality | Promotions to `canonical`, not volume of new stubs |

---

## 2. Two-layer architecture

The repository already contains both layers. The product **separates them in the visitor experience.**

```
┌─────────────────────────────────────────────────────────────┐
│  MUSEUM FLOOR (public)                                      │
│  ~100–500 canonical exhibits · collections · built sims     │
│  Wonder-first UX · no file counts · no folder tree          │
└─────────────────────────────────────────────────────────────┘
                              │
                    promotion gate (curator)
                              │
┌─────────────────────────────────────────────────────────────┐
│  WORKSHOP (contributors)                                    │
│  Full corpus (~5,519 nodes) · templates · scripts · meta    │
│  Graph maintenance · research doc · agent workflows           │
└─────────────────────────────────────────────────────────────┘
```

| Layer | Git paths | Visitor sees |
|-------|-----------|--------------|
| **Museum floor** | [`meta/CANONICAL-REGISTRY.md`](meta/CANONICAL-REGISTRY.md), [`indices/collections/`](indices/collections/), built sims | Yes |
| **Workshop** | `content/` bulk, `scripts/`, `phases/`, `templates/` | No (except /contribute) |

**Rule:** Stop generating corpus volume. All new effort goes to **canonical promotion**, **collections**, and **built interactives**.

---

## 3. Brand & voice

| Element | Spec |
|---------|------|
| **Name** | ExplorableLab (public) · repo may stay `games/` internally until rename |
| **Tagline** | *Explore ideas that only make sense when you play with them.* |
| **Tone** | Warm, curious, complicity-without-blame (Nicky Case) · precise when needed (Distill) · wonder-first (Exploratorium) |
| **Avoid** | "Knowledge base", "5,519 pages", "documentation", Wikipedia infobox aesthetic |
| **Visual** | Warm palette · high data-ink on exhibits · minimal chrome · museum placards, not sidebar nav |

---

## 4. Information architecture

### 4.1 Primary navigation (visitor)

Three doors only on homepage:

| Door | Purpose | Default destination |
|------|---------|-------------------|
| **Play** | Immediate interaction | Paradox Arcade or hero sim |
| **Discover** | Serendipity | Random canonical exhibit + rabbit hole |
| **Learn** | Guided depth | Collections & paths |

Secondary (header, not hero):
- **Wings** (spatial zones)
- **Graph** (constellation view)
- **Collections**
- **Studio** → `/contribute` (workshop)

### 4.2 Museum wings (spatial, not folders)

| Wing | Slug | Contents |
|------|------|----------|
| Hall of Paradoxes | `wing-paradox` | Commit-reveal games |
| Systems Garden | `wing-systems` | Emergence, feedback, cascades, percolation |
| Street of Misconceptions | `wing-intuition` | Base rate, Simpson's, ergodicity, regression |
| City of Networks | `wing-networks` | Contagion, bridges, illusions |
| Studio of Design | `wing-design` | E.C.H.O., patterns, autopsies |
| Gallery of Masters | `wing-canon` | Nicky Case + descendants |
| Evidence Library | `wing-evidence` | Papers, experiments (curated only) — Research Mode |

### 4.3 Page types on the museum floor

| Surface type | Source in repo | Render as |
|--------------|----------------|-----------|
| **Exhibit** | Canonical THY/PAR/PHN/MOD | Museum card + long-form prose |
| **Simulation spec** | Tier S/A SIM | Build brief + "Play prototype" when built |
| **Playable** | EXE + built sims | Embedded interactive (iframe or native) |
| **Collection** | `indices/collections/*.md` | Curated gallery with narrative |
| **Path** | `indices/paths/*.md` | Step-by-step journey (5–9 stops) |
| **Pattern card** | Canonical PAT/MET/STR | Visual card deck, not 200-page list |
| **Autopsy** | Research doc sections | Interactive case study (future) |

### 4.4 What stays hidden by default

- Bulk `awesome/*` alphabetical dumps (replace with editorial collections)
- Numeric slugs (`1`, `160-paradox`)
- Year-matrix Nobel (400 pages)
- Synthetic paper stubs
- Combinatorial theories (`concept-N-field`)
- `phases/`, raw `templates/`, generator scripts

Accessible via **Research Mode** toggle for researchers only.

---

## 5. Canonical surface

The public product is defined by [`meta/CANONICAL-REGISTRY.md`](meta/CANONICAL-REGISTRY.md) — **100 slugs** for v1, expanding to ~500 over years.

### Lifecycle

```
stub → draft → mature → canonical
                              ↑
                    curator promotion only
                    (see PRODUCT-ROADMAP Phase 1)
```

### Promotion criteria (all required)

1. **Explorable thesis** — clear answer to "why interaction?"
2. **Accurate title** — slug matches human-readable name
3. **No boilerplate** — no generic mature_corpus paragraphs
4. **Min graph edges** — per AGENT_GUIDE (THY: 3 related ideas or 1 THY + 2 PAP + 1 PAT)
5. **Collection membership** — at least one wing or collection
6. **Discovery block** — filled with real suggestions, not placeholders
7. **Optional:** built sim or EXE link with coverage %

### v1 public face (100 nodes)

See registry file for full list. Summary:

| Tier | Count | Role |
|------|-------|------|
| Existing explorables | 9 | Play today |
| Tier S simulations | 18 | Brand + build queue |
| Foundational theories | 12 | Graph hubs |
| Hybrids + Tier A sims | 17 | Novelty |
| Design vocabulary | 15 | Author studio |
| Paradoxes | 12 | Paradox Arcade |
| Experiments | 10 | Playable history |
| Evidence | 7 | Research spine |

---

## 6. Collections (v1 launch set)

Launch with **12 collections**; expand to 55 over time ([`indices/collections/README.md`](indices/collections/README.md)).

| # | Collection | Stops | Time |
|---|------------|-------|------|
| 1 | **Start Here: First Visit** | 5 | 15 min |
| 2 | **Paradoxes Everyone Should Play Once** | 8 | 25 min |
| 3 | **Innocence → Horror → Hope** | 5 | 20 min |
| 4 | **Why Groups Act Weird** | 6 | 20 min |
| 5 | **Math That Lies to You** | 7 | 30 min |
| 6 | **Systems That Shape Society** | 8 | 35 min |
| 7 | **Steal From Nicky Case** | 7 | 40 min |
| 8 | **Trust, Betrayal, Forgiveness** | 5 | 20 min |
| 9 | **Networks You're Inside Of** | 6 | 25 min |
| 10 | **Ideas Every Designer Should Understand** | 10 | 45 min |
| 11 | **Under 5 Minutes** | 6 | 5 min each |
| 12 | **Build These Next** (Tier S) | 18 | reference |

Each collection file format:

```yaml
---
id: COL-0001
slug: start-here-first-visit
title: "Start Here: First Visit"
summary: "Five exhibits. One sitting. See the world differently."
status: canonical
wing: null
stops: [parable-of-polygons, monty-hall, petrie-multiplier, schelling-segregation, evolution-of-trust]
time_minutes: 15
emotional_arc: "curiosity → surprise → complicity → hope"
audience: [everyone]
---
```

---

## 7. Homepage specification

### 5-second comprehension

User understands: **things move here · I can play · I'll be surprised**

### Layout (top → bottom)

1. **Hero exhibit** — one live interactive (weekly rotation). Caption from E.C.H.O. hook.
2. **Three doors** — Play · Discover · Learn (see §4.1)
3. **Exhibit of the week** — editorial card, large, poster aesthetic
4. **Collections rail** — 6–8 horizontal scroll cards
5. **Graph preview** — constellation teaser (canonical nodes only, bright)
6. **Gallery of Masters** — 9 canon tiles, playable
7. **Quiet lineage** — "Inspired by Bret Victor, Nicky Case, Distill, the Exploratorium"
8. **Footer** — About · Contribute · Research Mode · CC0

### Anti-patterns

No page counts · no folder tree · no GitHub aesthetic · no sidebar documentation nav

### Hero rotation (v1)

| Week | Hero | Hook line |
|------|------|-----------|
| 1 | Parable of Polygons (embed) | *You just segregated a society with one reasonable move.* |
| 2 | Petrie Multiplier (when built) | *Equal rules. Unequal harm. Count it.* |
| 3 | Monty Hall (when built) | *Your intuition is wrong. Bet on it.* |
| 4 | Evolution of Trust (embed) | *Cooperation works—until it doesn't.* |

Until Tier S sims exist, rotate canon embeds.

---

## 8. Key user journeys (summary)

| Persona | Entry | Success exit |
|---------|-------|--------------|
| **Curious student** | Paradox Arcade | "One more" → optional 15-min path |
| **Designer** | Steal From Nicky Case collection | E.C.H.O. worksheet + gap map |
| **Teacher** | Classroom-ready collection | Shareable single-exhibit link |
| **Researcher** | Research Mode → evidence wing | Citation + graph chain export |
| **Developer** | Build These Next (Tier S) | Spec + starter kit |
| **Random visitor** | Hero or Discover | Share card + bookmark Surprise Me |

Full journey detail: prior product architecture report (Tasks 2–3).

---

## 9. Navigation systems (product features)

| Feature | v1 | v2 | v3 |
|---------|----|----|-----|
| Three doors homepage | ✓ | | |
| 12 collections | ✓ | | |
| Paradox Arcade (embeds) | ✓ | | |
| Canonical-only browse | ✓ | | |
| Surprise Me (random canonical) | ✓ | | |
| You May Also Like (max 3 edges) | ✓ | | |
| Guided paths (5–9 stops) | | ✓ | |
| Constellation graph view | | ✓ | |
| Compare mode (side-by-side) | | ✓ | |
| Personal trail (local) | | ✓ | |
| Built Tier S sims (native) | | ✓ (rolling) | |
| Full Research Mode corpus | | | ✓ |
| Author studio (submit specs) | | | ✓ |
| Classroom assign links | | | ✓ |

---

## 10. Content strategy (stop / start)

### STOP

- Running `generate_to_target.py` for scale
- Running `mature_corpus.py` on the full corpus
- Treating `awesome/*` dumps as visitor navigation
- Adding bulk PAT/MET/THY/PAR without curator review
- Showing warehouse stats on homepage

### START

- Promoting registry slugs to `status: canonical` with real editorial prose
- Merging research one-pagers into canonical SIM/THY pages
- Writing collection files in `indices/collections/`
- Fixing slug/title/links on canonical 100 only
- Building **one** Tier S simulation end-to-end as reference (recommend: `petrie-multiplier`)
- Embedding 9 canon EXEs on homepage and arcade

---

## 11. Technical approach (high level)

**Principle:** Markdown remains source of truth. Site is a viewer.

| Option | Fit | Notes |
|--------|-----|-------|
| **Quartz / Obsidian Publish** | Fast v1 | Graph-native, markdown-first |
| **Astro + MDX** | Best long-term | Museum UX control, embed iframes |
| **Vite + custom** | Max control | Higher build cost |

### v1 recommendation: **Astro static site**

- `site/` reads only `meta/CANONICAL-REGISTRY.md` + collections + canonical content paths
- Canon EXEs embedded via iframe to ncase.me / itch.io
- No backend; CC0; deploy to Cloudflare Pages or GitHub Pages
- Research Mode: optional second build or `/research` route indexing full corpus

### Data flow

```
meta/CANONICAL-REGISTRY.md  ──┐
indices/collections/*.md    ──┼──► site build ──► ExplorableLab (public)
content/{canonical slugs}   ──┘
EXPLORABLE_EXPLANATIONS_RESEARCH.md ──► autopsy pages (Phase 3)
```

---

## 12. Governance

| Role | Responsibility |
|------|----------------|
| **Curator** | Promote/demote canonical; approve collections; hero rotation |
| **Exhibit author** | Rewrite canonical prose; fix links |
| **Simulation builder** | Tier S builds; prototype → EXE or new SIM |
| **Designer** | Wings, collections, homepage, graph aesthetic |
| **Agent (AI)** | Discovery reports on canonical edits only; no bulk gen |

**Weekly rhythm:** 1 canonical promotion · 1 collection touch-up · graph link fixes on canonical set only

---

## 13. Related documents

| Doc | Purpose |
|-----|---------|
| [`PRODUCT-ROADMAP.md`](PRODUCT-ROADMAP.md) | Phased execution plan |
| [`meta/CANONICAL-REGISTRY.md`](meta/CANONICAL-REGISTRY.md) | The 100 public slugs |
| [`indices/collections/README.md`](indices/collections/README.md) | Collection format |
| [`EXPLORABLE_EXPLANATIONS_RESEARCH.md`](EXPLORABLE_EXPLANATIONS_RESEARCH.md) | Design bible |
| [`ARCHITECTURE.md`](ARCHITECTURE.md) | Workshop / graph schema |
| [`indices/by-score/tier-s.md`](indices/by-score/tier-s.md) | Build queue |

---

## 14. Open decisions

| Decision | Options | Recommendation |
|----------|---------|----------------|
| Repo rename | Keep `games/` vs rename to `explorable-lab` | Rename when site launches |
| Domain | explorablelab.org / .com | Register before public launch |
| First built sim | Any Tier S | **petrie-multiplier** (viral, simple, timely) |
| Site stack | Quartz vs Astro | **Astro** for museum UX |
| Research Mode | Same site vs separate | Same site, toggle, dim non-canonical |

---

*This spec supersedes scale-first expansion goals in README for **visitor-facing product**. The workshop corpus remains valuable as graph scaffolding— invisible until curated.*
