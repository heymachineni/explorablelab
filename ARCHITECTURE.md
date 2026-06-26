# Repository Architecture

*Design for 20,000+ markdown files · 20-year horizon · markdown-first · graph-native*

---

## 1. Folder Structure

### Design principles

1. **Shard before you choke** — no folder should exceed ~400 files; split by discipline, era, or prefix when approaching limit
2. **Stable slugs, mutable paths** — identity lives in frontmatter `id`, not folder location
3. **Three access paths** — browse by type, browse by discipline, browse by graph
4. **GitHub-native** — no build step required to read; indices are markdown, not generated DB
5. **Flat where possible, deep where meaningful** — type at L1, discipline at L2, subtopic at L3 max

### Root layout

```
/
├── README.md
├── ARCHITECTURE.md          ← this file
├── CONTRIBUTING.md
├── AGENT_GUIDE.md
├── ROADMAP.md
├── LICENSE
│
├── content/                 ← THE CORPUS (~20k nodes)
│   ├── theories/
│   ├── paradoxes/
│   ├── mental-models/
│   ├── phenomena/           ← observable effects, laws, empirical regularities
│   ├── people/
│   │   ├── scientists/
│   │   ├── designers/       ← Case, Victor, Hart, etc.
│   │   └── educators/
│   ├── publications/
│   │   ├── papers/
│   │   ├── books/
│   │   └── nobel/
│   ├── experiments/         ← named research experiments (Asch, Milgram, etc.)
│   ├── simulations/
│   │   ├── concepts/        ← not-yet-built interactive ideas
│   │   ├── prototypes/      ← in-progress builds
│   │   └── existing/        ← finished explorables (Polygons, Trust, etc.)
│   ├── design/
│   │   ├── interaction-patterns/
│   │   ├── visual-metaphors/
│   │   ├── storytelling-structures/
│   │   └── mediums/         ← simulation, board game, classroom activity, etc.
│   ├── disciplines/         ← discipline hub pages (not content duplicates)
│   ├── events/              ← historical events tied to ideas
│   └── organizations/       ← labs, prizes, institutions (optional)
│
├── templates/               ← one template per content type
│
├── meta/
│   ├── taxonomy/            ← controlled vocabularies
│   ├── scoring/             ← rubrics and score definitions
│   └── graph/               ← edge types, schema, validation rules
│
├── indices/                 ← human-curated maps (MOCs)
│   ├── by-discipline/
│   ├── by-score/
│   ├── by-medium/
│   ├── maps-of-content/
│   └── awesome/             ← themed lists (like awesome-* repos)
│
├── graph/                   ← optional explicit edge files
│   └── edges/               ← when wikilinks aren't enough
│
└── scripts/                 ← optional validation (no runtime dependency)
    └── validate-frontmatter.py
```

### Sharding strategy (per content type)

When a leaf folder exceeds **400 files**, split using **first letter** or **sub-discipline**:

```
content/theories/
├── complex-systems/           ← discipline shard (preferred)
│   ├── emergence.md
│   ├── schelling-segregation.md
│   └── self-organized-criticality.md
├── game-theory/
├── probability-statistics/
└── _archive/                  ← deprecated slugs (redirect notes)

# At 400+ in complex-systems/:
content/theories/complex-systems/
├── a-f/
├── g-m/
└── n-z/
```

### File naming

| Rule | Example |
|------|---------|
| Slug | `schelling-segregation.md` |
| Lowercase kebab-case | `prisoners-dilemma.md` |
| No dates in slug | ✗ `2024-bayes-theorem.md` |
| One concept per file | split don't merge |
| Stable ID in frontmatter | `id: THY-0042` |

### ID prefix registry

| Prefix | Type | Folder |
|--------|------|--------|
| `THY` | Theory | `content/theories/` |
| `PAR` | Paradox | `content/paradoxes/` |
| `MOD` | Mental model | `content/mental-models/` |
| `PHN` | Phenomenon | `content/phenomena/` |
| `SCI` | Scientist | `content/people/scientists/` |
| `DSN` | Designer/educator | `content/people/designers/` |
| `PAP` | Paper | `content/publications/papers/` |
| `BOK` | Book | `content/publications/books/` |
| `NOB` | Nobel discovery | `content/publications/nobel/` |
| `EXP` | Experiment | `content/experiments/` |
| `SIM` | Simulation concept | `content/simulations/concepts/` |
| `PRO` | Prototype | `content/simulations/prototypes/` |
| `EXE` | Existing explorable | `content/simulations/existing/` |
| `PAT` | Interaction pattern | `content/design/interaction-patterns/` |
| `MET` | Visual metaphor | `content/design/visual-metaphors/` |
| `STR` | Storytelling structure | `content/design/storytelling-structures/` |
| `MED` | Medium | `content/design/mediums/` |
| `DIS` | Discipline hub | `content/disciplines/` |
| `EVT` | Historical event | `content/events/` |
| `ORG` | Organization | `content/organizations/` |

IDs are **immutable**. Slugs can redirect via `supersedes` / `merged_into` frontmatter.

---

## 2. Markdown Templates

All templates live in `templates/`. Every content file uses YAML frontmatter + standardized sections.

### Universal frontmatter (all types)

```yaml
---
id: THY-0042
type: theory
slug: schelling-segregation
title: "Schelling Segregation Model"
summary: "One-sentence description."
status: draft | stub | mature | canonical
created: 2026-06-26
updated: 2026-06-26
authors: []                    # who wrote this page
confidence: low | medium | high  # editorial confidence

# Taxonomy (controlled tags — see meta/taxonomy/)
fields: [social-science, complex-systems]
subfields: [agent-based-modeling, urban-sociology]
difficulty: introductory | intermediate | advanced | research
era: [1960s, 1970s]
tags: [segregation, emergence, tolerance-threshold]

# Graph edges (wikilink slugs)
related:
  people: [thomas-schelling]
  theories: [emergence, threshold-models]
  papers: [schelling-1971-dynamic-models]
  books: []
  paradoxes: []
  experiments: []
  mental_models: [tipping-point]
  simulations:
    concepts: [standing-ovation-threshold]
    existing: [parable-of-polygons]
  design:
    patterns: [agent-placement, parameter-slider]
    metaphors: [neighborhood-grid]
    structures: [but-chain, sandbox-ending]

# Scores (1-10, see meta/scoring/rubric.md)
scores:
  visual_potential: 9
  interaction_potential: 10
  educational_value: 9
  surprise: 9
  replayability: 9
  narrative_potential: 8
  beauty: 7
  novelty: 6                    # as explorable (not as theory)
  sandbox_potential: 10
  timelessness: 10
  virality: 9
  existing_coverage: 8          # high = already many explorables
  research_quality: 10
  citation_strength: 10
  cross_disciplinary: 9
  composite: 8.9                # optional pre-computed

# Explorable assessment (REQUIRED for theories, paradoxes, phenomena)
explorable:
  verdict: essential | strong | moderate | weak | none
  why_interaction: "One paragraph."
  can_become:
    simulation: true
    interactive_game: true
    physical_toy: true
    classroom_activity: true
    visualization: true
    social_experiment: true
    mobile_app: false
    webgl_demo: true
    card_game: false
    board_game: true
    data_visualization: true
  best_medium: web-simulation
  best_medium_stars: 5
  best_medium_reason: "Behavior only clicks when users move agents themselves."
  anti_patterns: ["static heatmap only", "lecture then quiz"]

# Provenance
sources:
  - type: paper
    id: PAP-0128
  - type: url
    url: https://...
---
```

### Required body sections by type

See individual templates in `templates/`. Summary:

| Type | Required sections |
|------|-------------------|
| **Theory** | Why it matters · Core idea · Formal definition · Mechanism · Why interaction · Surprising implications · Real-world applications · Common misconceptions · Can become · Related graph · Further reading |
| **Paradox** | Statement · Why paradoxical · Resolution paths · Why interaction · Famous variants · Related |
| **Paper** | Abstract · Key contribution · Methods · Findings · Why explorable · Citations · Related |
| **Scientist** | Bio · Key contributions · Major works · Influence graph · Explorable opportunities |
| **Book** | Thesis · Key chapters · Models introduced · Why explorable · Related |
| **Mental model** | Definition · When to use · Failure modes · Visual/interactive form · Related |
| **Experiment** | Setup · Procedure · Results · Replications · Interactive recreation · Ethics |
| **Nobel** | Discovery · Laureates · Why it matters · Explorable angle · Related |
| **Simulation concept** | Theory link · Interaction model · Visual metaphor · Controls · Emergence · Build estimate · Related |
| **Interaction pattern** | Description · When to use · Examples · Anti-patterns · Related |
| **Visual metaphor** | Mapping · Strengths · Breaks down when · Related |
| **Storytelling structure** | Beat sheet · Used in · Related |
| **Historical event** | Context · Ideas born from it · Related |
| **Existing explorable** | URL · What it teaches · Patterns used · Gaps · Related |
| **Prototype idea** | Status · Spec · Open questions · Related |
| **Discipline hub** | Scope · Subfields · Key figures · Top explorables · Related |
| **Phenomenon** | Observation · Mechanism · Theories explaining it · Explorable angle · Related |

---

## 3. Relationships (The Graph)

### Linking mechanisms (use all three)

1. **Frontmatter `related:`** — typed edges, machine-parseable
2. **Wikilinks in body** — `[[schelling-segregation|Schelling model]]`
3. **Explicit edge files** — `graph/edges/THY-0042--instantiates--PAT-0012.md` for complex metadata

### Edge type taxonomy

| Edge | From → To | Meaning |
|------|-----------|---------|
| `developed` | Person → Theory/Paper | Creator |
| `published` | Person → Paper | Authorship |
| `introduced` | Paper → Theory | First articulation |
| `extends` | Theory → Theory | Builds on |
| `contradicts` | Theory → Theory | In tension |
| `explains` | Theory → Phenomenon | Mechanism |
| `instantiates` | Pattern → Theory | Teaching pattern for theory |
| `visualizes` | Metaphor → Theory | Visual mapping |
| `demonstrates` | Existing → Theory | Finished explorable |
| `proposes` | Simulation → Theory | Not-yet-built idea |
| `inspired_by` | Simulation → Existing | Derivative |
| `replicates` | Experiment → Phenomenon | Empirical demo |
| `documents` | Book → Theory | Popularization |
| `awarded_for` | Nobel → Discovery | Prize link |
| `part_of` | Theory → Discipline | Classification |
| `applies_to` | Theory → Application domain | Use case |
| `generalizes` | Mental model → Theory | Abstraction |
| `paradox_of` | Paradox → Theory | Challenge to |
| `cites` | Paper → Paper | Citation |
| `co_occurs` | Any → Any | Weak association |

### Example chain (target density per canonical theory page)

```
Thomas Schelling (SCI)
  ↓ developed
Schelling Segregation (THY)
  ↓ part_of
Emergence (THY) · Complex Systems (DIS)
  ↓ instantiates
Agent-Based Modeling (THY)
  ↓ related
Network Science (DIS)
  ↓ published
Dynamic Models of Segregation (PAP)
  ↓ documents
Micromotives and Macrobehavior (BOK)
  ↓ demonstrates
Parable of the Polygons (EXE)
  ↓ proposes
Standing Ovation Threshold (SIM)
  ↓ visualizes
Neighborhood Grid (MET)
  ↓ instantiates
Agent Placement Pattern (PAT)
```

Every **mature** theory page should have ≥3 related theories, ≥1 paper, ≥1 person, ≥1 design artifact (pattern/metaphor/simulation), and explicit **Why interaction** section.

---

## 4. Tagging System

**Rule: tags are registered, not invented.** New tags via PR to `meta/taxonomy/tag-registry.md`.

### Taxonomy layers

| Layer | Controlled file | Example |
|-------|-----------------|---------|
| **Field** | `fields.yaml` | `social-science`, `physics`, `mathematics` |
| **Subfield** | `subfields.yaml` | `game-theory`, `thermodynamics` |
| **Difficulty** | enum | `introductory` … `research` |
| **Era** | `eras.yaml` | `ancient`, `1960s`, `2010s` |
| **Interaction pattern** | link to PAT nodes | `parameter-slider`, `sandbox` |
| **Simulation type** | `simulation-types.yaml` | `agent-based`, `cellular-automaton`, `system-dynamics` |
| **Mathematical foundation** | `math-foundations.yaml` | `probability`, `differential-equations`, `graph-theory` |
| **Application** | `applications.yaml` | `urban-planning`, `public-health`, `education` |
| **Medium** | link to MED nodes | `web-simulation`, `classroom-activity` |
| **Free tags** | `tag-registry.md` | max 12 per page; must be registered |

### Anti-duplication rules

- Singular nouns: `network` not `networks`
- US spelling in tags: `behavior` not `behaviour`
- Prefer discipline tag over vague tag: use `bayesian-inference` not `hard-math`
- Merge synonyms in registry: `prisoners-dilemma` absorbs `prisoner-dilemma`
- Deprecated tags list with redirect: `old-tag → new-tag`

---

## 5. Scoring Framework

Full rubric: [`meta/scoring/rubric.md`](meta/scoring/rubric.md)

### Dimensions (1–10 each)

| Score | Meaning |
|-------|---------|
| **visual_potential** | Can the idea be *seen*? |
| **interaction_potential** | Must users *do* something to get it? |
| **educational_value** | Does misunderstanding cause real harm? |
| **surprise** | Gap between intuition and truth |
| **replayability** | Sandbox / parameter exploration |
| **narrative_potential** | Story, complicity, emotional arc |
| **beauty** | Aesthetic simulation potential |
| **novelty** | Unexplored as explorable (10 = empty field) |
| **sandbox_potential** | Open-ended play after lesson |
| **timelessness** | Will matter in 2036? |
| **virality** | Shareable "aha" moment |
| **existing_coverage** | 10 = many explorables exist (lower priority) |
| **research_quality** | Empirical / theoretical rigor |
| **citation_strength** | Canonical citations |
| **cross_disciplinary** | Bridges fields |

### Priority formula (for simulation backlog)

```
priority = (
  0.14 * interaction_potential +
  0.12 * educational_value +
  0.12 * surprise +
  0.10 * visual_potential +
  0.10 * timelessness +
  0.08 * novelty * (1 - existing_coverage/10) +
  0.08 * sandbox_potential +
  0.08 * cross_disciplinary +
  0.06 * virality +
  0.06 * narrative_potential +
  0.06 * research_quality
)
```

**Note:** `existing_coverage` inverts — well-explored ideas score lower *for new build priority* but remain in corpus as canonical references.

---

## 6. Knowledge Graph Structure

### Layer model (bottom → top)

```
Layer 0: Evidence
  Papers · Experiments · Nobel · Events

Layer 1: People & Institutions
  Scientists · Designers · Organizations

Layer 2: Ideas
  Theories · Paradoxes · Phenomena · Mental Models

Layer 3: Design vocabulary
  Interaction Patterns · Visual Metaphors · Storytelling · Mediums

Layer 4: Applied creativity
  Simulation Concepts · Prototypes

Layer 5: Canon
  Existing Explorables

Layer 6: Navigation
  Disciplines · Indices · MOCs
```

### Hub nodes (high PageRank targets)

- Discipline pages (`content/disciplines/`)
- Pattern pages (`agent-placement`, `but-chain`, `sandbox`)
- Era MOCs (`indices/maps-of-content/1960s-systems-revolution.md`)
- Score MOCs (`indices/by-score/priority-tier-1.md`)

### Graph integrity rules

1. No orphan pages — every node ≥2 inbound links within 90 days of creation
2. Every `SIM` must link to ≥1 `THY` and ≥1 `PAT`
3. Every `EXE` must link to ≥1 `THY` and list patterns used
4. Every `PAP` must link to ≥1 `SCI` and ≥1 `THY` or `PHN`
5. Bidirectional links encouraged in prose: "See also" sections

---

## 7. Missing Categories (Discipline Expansion)

Beyond Nicky Case's usual domains, the corpus must include:

### Tier A — High explorable density (prioritize)

| Domain | Example entries |
|--------|-----------------|
| **Cybernetics & control** | Ashby requisite variety, PID, homeostasis, feedback control |
| **Operations research** | Queuing (Little's law, Kingman), inventory, linear programming intuition |
| **Information theory** | Shannon entropy, channel capacity, error correction, Kolmogorov complexity |
| **Decision science** | Prospect theory, ambiguity aversion, multi-criteria decision |
| **Systems engineering** | Requirements cascade, failure modes, redundancy |
| **HCI & design theory** | Affordances, feedback, gulf of execution, cognitive load |
| **Educational psychology** | Spacing, testing effect, cognitive load, productive failure |
| **Ecology** | Trophic cascades, carrying capacity, island biogeography |
| **Neuroscience** | Hebbian learning, predictive processing, plasticity |
| **Semiotics** | Signifier/signified, icons/index/symbols |
| **Political philosophy** | Veil of ignorance, social contract, collective action |
| **Anthropology** | Gift economy, ritual, cultural evolution |
| **Linguistics** | Sapir-Whorf (weak), pragmatics, speech acts |
| **Music theory** | Consonance, rhythm sync, Fourier timbre |
| **Architecture & urbanism** | Jacobs, pattern language, space syntax |
| **History of science** | Paradigm shifts, replication crisis, scientific revolutions |

### Tier B — Essential but harder interactively

| Domain | Approach |
|--------|----------|
| **Pure mathematics** | Visual proofs, interactive proofs where possible |
| **Law & jurisprudence** | Scenario branching, precedent graphs |
| **Theology & philosophy** | Thought experiments, dialogue trees |
| **Chemistry** | Molecular sims, reaction kinetics |
| **Geology** | Deep time sliders, plate tectonics |

### Tier C — Meta corpus (about explorables themselves)

| Category | Purpose |
|----------|---------|
| **Interaction patterns** | Reusable design vocabulary |
| **Storytelling structures** | BUT-chain, ladder of abstraction |
| **Mediums** | When simulation beats essay |
| **Designers/educators** | Case, Victor, Hart, Bogost, Resnick |
| **Existing explorables** | Canon reference, avoid duplication |

### New content types considered

| Type | Verdict | Location |
|------|---------|----------|
| **Dataset** | Add as `content/publications/datasets/` when theory requires real data | Optional phase 2 |
| **Course** | Link out; don't host | External only |
| **Tool** | Loopy-like; tag as `EXE` or external | `simulations/existing/` |
| **Law/Policy** | Tag under `applications` | No separate type |

---

## 8. Roadmap: First 100 Files

See [`ROADMAP.md`](ROADMAP.md) — ranked by foundational importance, not popularity.

**Phase 0 (infrastructure):** 15 files — architecture, templates, taxonomy, indices  
**Phase 1 (vocabulary):** 25 files — design patterns, disciplines, mediums  
**Phase 2 (canon):** 20 files — existing explorables + key scientists  
**Phase 3 (foundations):** 40 files — highest-priority theories + papers  

---

## 9. Auto-Suggestion Protocol (Agents & Contributors)

When adding any page, complete the **Discovery Block** (in every template) and run the checklist in [`AGENT_GUIDE.md`](AGENT_GUIDE.md):

### Automatic suggestions required

| Trigger | Suggest |
|---------|---------|
| New **paper** | Authors (SCI), theories introduced (THY), experiments (EXP), citation graph |
| New **theory** | Parent discipline, related paradoxes, patterns, metaphors, SIM concepts, EXE coverage check |
| New **scientist** | Papers, theories, Nobel, designers influenced |
| New **simulation concept** | THY, PAT, MET, STR, medium, build priority score |
| New **existing explorable** | THY taught, patterns used, gaps, extensions |
| Missing link detected | Stub page creation PR or `status: stub` suggestion |

### Stub creation rule

If a `related:` link points to non-existent slug → create `status: stub` page with minimum frontmatter + one-line summary + backlinks.

### Discovery Block template

```markdown
## Discovery suggestions

<!-- AUTO-GENERATED SECTION: expand when editing -->

### Missing pages to create
- [ ] [[slug]] — reason

### Potential simulations
- [[sim-slug]] — medium: web-simulation — priority: high

### Visual metaphors
- [[met-slug]] — mapping

### Cross-disciplinary links
- [[discipline/slug]] — connection

### Existing coverage
- [[exe-slug]] — covers 60% — gap: sandbox for parameter X
```

---

## Validation (optional scripts)

`scripts/validate-frontmatter.py` checks:

- Required fields present
- Tags registered in taxonomy
- Related slugs exist (or marked stub)
- Scores 1–10
- `explorable.verdict` present for THY/PAR/PHN
- No duplicate IDs

No CI required for reading; recommended for PRs at scale.

---

*This architecture is version 1.0. Propose changes via PR to this file with `meta/` updates.*
