# ExplorableLab — Product Roadmap

**Companion to:** [`PRODUCT-SPEC.md`](PRODUCT-SPEC.md)  
**Horizon:** 0–90 days (launch) · 1 year (museum) · 10 years (legacy)

---

## Phase 0 — Freeze the warehouse (Week 1)

**Goal:** Stop being a generator. Become a museum project.

| # | Task | Output |
|---|------|--------|
| 0.1 | Freeze corpus generation | Document in README: no more `generate_to_target` runs |
| 0.2 | Adopt canonical registry | [`meta/CANONICAL-REGISTRY.md`](meta/CANONICAL-REGISTRY.md) is public surface definition |
| 0.3 | Update README | Point to PRODUCT-SPEC; remove "scale target" as primary message |
| 0.4 | Mark warehouse honestly | Note in EXPANSION.md: bulk pages are workshop, not floor |
| 0.5 | Brand | Use **ExplorableLab** in all new docs |

**Exit criteria:** Team agrees: next work is canonical + site, not markdown count.

---

## Phase 1 — Canonical 100 (Weeks 2–6)

**Goal:** 100 pages worthy of the museum floor.

| # | Task | Priority |
|---|------|----------|
| 1.1 | Promote 9 EXE pages | Fix bodies, autopsy summaries from research doc |
| 1.2 | Rewrite `schelling-segregation` tier peers | emergence, threshold-models, feedback-loops, percolation, goodharts-law, ostrom-commons-design |
| 1.3 | Merge Tier S research one-pagers into SIM corpus pages | 18 files — spec becomes exhibit card |
| 1.4 | Rewrite 15 design vocabulary pages from research | agent-placement, but-chain, etc. — delete slug/title mismatches |
| 1.5 | Curate 12 paradox + 10 experiment pages | Named slugs only; demote numeric stubs from any index |
| 1.6 | Curate 7 evidence anchors | Real citations, DOI where possible |
| 1.7 | Set `status: canonical` in frontmatter | Only registry slugs |
| 1.8 | Fix `related:` links within canonical set | No links to `hot-2`, `160-paradox`, etc. |

**Exit criteria:** All 100 registry slugs are `canonical` with non-boilerplate prose.

**Recommended order (weekly):**
1. EXE canon (9)  
2. Schelling cluster (7 THY)  
3. Tier S sims (18) — merge from research doc  
4. Design vocabulary (15)  
5. Paradox arcade set (12)  
6. Experiments (10)  
7. Evidence + discipline hubs (7 + 5 DIS)

---

## Phase 2 — Collections & paths (Weeks 4–8, parallel)

**Goal:** Navigation that feels like a museum, not a file tree.

| # | Task | Output |
|---|------|--------|
| 2.1 | Create 12 launch collections | [`indices/collections/`](indices/collections/) |
| 2.2 | Create 5 guided paths | [`indices/paths/`](indices/paths/) |
| 2.3 | Replace auto `awesome/*` with "canonical only" lists | Regenerate or hand-write |
| 2.4 | Build wing index pages | 7 wing landing markdown files |
| 2.5 | Write "Start Here" as single best entry | 5 stops, tested on 3 people |

**Exit criteria:** A new visitor can follow Start Here without hitting a generic stub.

---

## Phase 3 — Site v1 (Weeks 6–12)

**Goal:** Public ExplorableLab homepage — wonder, not GitHub.

| # | Task | Output |
|---|------|--------|
| 3.1 | Choose stack | Astro recommended (see PRODUCT-SPEC §11) |
| 3.2 | `site/` scaffold | Reads canonical registry + collections only |
| 3.3 | Homepage | Hero embed + three doors + collections rail |
| 3.4 | Exhibit template | Museum card layout for THY/PAR/SIM/EXE |
| 3.5 | Paradox Arcade page | 6–8 embeds or built minigames |
| 3.6 | Collection gallery | 12 collection pages |
| 3.7 | Surprise Me | Random canonical slug |
| 3.8 | You May Also Like | 3 related slugs from frontmatter |
| 3.9 | `/contribute` | Links to workshop docs (GitHub) |
| 3.10 | Deploy | Cloudflare Pages or GitHub Pages |

**Exit criteria:** Shareable URL; hero playable; no warehouse visible.

---

## Phase 4 — First native simulation (Weeks 10–16)

**Goal:** One Tier S built in-house — proof the museum builds, not just links.

| # | Task | Recommendation |
|---|------|----------------|
| 4.1 | Pick sim | **`petrie-multiplier`** — simple, viral, timely, low art burden |
| 4.2 | Spec lock | Merge research Phase 7 one-pager + E.C.H.O. |
| 4.3 | Build | Web (Canvas or DOM); predict-then-reveal; share card |
| 4.4 | Publish | Embed on homepage hero rotation |
| 4.5 | Catalog | `content/simulations/prototypes/petrie-multiplier/` → promote when done |

**Exit criteria:** Native sim on homepage; canonical SIM page links to live build.

**Second sim candidates:** `ergodicity-street`, `goodhart-school`, `braess-roads`

---

## Phase 5 — Graph & discovery v2 (Months 4–6)

| # | Task |
|---|------|
| 5.1 | Constellation graph view (canonical nodes only) |
| 5.2 | Rabbit hole mode (follow strongest edge) |
| 5.3 | Compare mode (two exhibits side-by-side) |
| 5.4 | Daily discovery editorial slot |
| 5.5 | Personal trail (localStorage) |

---

## Phase 6 — Studio & classroom (Months 6–12)

| # | Task |
|---|------|
| 6.1 | E.C.H.O. interactive worksheet |
| 6.2 | Nicky Case autopsy case studies (from research doc) |
| 6.3 | Teacher path templates (objectives + prompts) |
| 6.4 | Shareable single-exhibit URLs |
| 6.5 | Research Mode toggle (full corpus, dim UI) |

---

## Phase 7 — Scale the floor, not the warehouse (Year 2+)

| Milestone | Target |
|-----------|--------|
| Canonical exhibits | 100 → 250 → 500 |
| Built Tier S sims | 18 |
| Built Tier A sims | 20+ |
| Collections | 55 |
| Annotated graph edges | 1,000+ on canonical set |
| Languages | i18n for top 20 exhibits |

---

## What NOT to do (ever again)

- Run bulk generators to hit numeric targets
- Show `awesome/paradoxes.md` (800 links) to visitors
- Mark pages `essential` without curator review
- Lead with ARCHITECTURE.md or phases/
- Optimize for file count in README

---

## Immediate next 7 days (recommended sprint)

| Day | Focus |
|-----|-------|
| 1 | README + EXPANSION honesty pass; freeze generators |
| 2–3 | EXE canon (9) — rewrite bodies from research autopsies |
| 4 | Start Here collection + schelling cluster |
| 5 | Astro site scaffold + homepage wireframe in code |
| 6 | Embed Polygons + Trust on homepage |
| 7 | Ship static preview URL internally; test with 2 outsiders |

---

*Product roadmap ≠ [`ROADMAP.md`](ROADMAP.md) (graph seed files). That doc built the workshop. This doc builds the museum.*
