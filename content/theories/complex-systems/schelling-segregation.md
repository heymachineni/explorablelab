---
id: THY-0001
type: theory
slug: schelling-segregation
title: "Schelling Segregation Model"
summary: "Mild individual preference for similar neighbors produces dramatic macro-segregation."
status: canonical
created: 2026-06-26
updated: 2026-06-26
confidence: high

fields: [social-science, complex-systems]
subfields: [agent-based-modeling, urban-sociology]
difficulty: introductory
era: [1960s, 1970s]
tags: [segregation, emergence, threshold, collective-behavior]

related:
  people: [thomas-schelling]
  theories: [emergence, threshold-models]
  papers: [schelling-1971-dynamic-models]
  books: [micromotives-and-macrobehavior]
  paradoxes: []
  experiments: []
  mental_models: []
  phenomena: [residential-segregation]
  simulations:
    concepts: [standing-ovation-threshold]
    existing: [parable-of-polygons]
  design:
    patterns: [agent-placement, parameter-slider, sandbox-mode, innocence-horror-hope]
    metaphors: [neighborhood-grid]
    structures: [innocence-horror-hope, but-chain-narrative]
    mediums: [web-simulation, board-game]
  disciplines: [complex-systems, social-science]
  events: []

scores:
  visual_potential: 9
  interaction_potential: 10
  educational_value: 9
  surprise: 9
  replayability: 9
  narrative_potential: 8
  beauty: 7
  novelty: 4
  sandbox_potential: 10
  timelessness: 10
  virality: 9
  existing_coverage: 8
  research_quality: 10
  citation_strength: 10
  cross_disciplinary: 9
  composite: 8.7

explorable:
  verdict: essential
  why_interaction: "Reading '33% tolerance threshold' does not produce the visceral shock of watching an integrated grid segregate after a few benign moves. The user must cause segregation through reasonable local choices."
  can_become:
    simulation: true
    interactive_game: true
    physical_toy: true
    classroom_activity: true
    visualization: true
    social_experiment: true
    mobile_app: true
    webgl_demo: true
    card_game: false
    board_game: true
    data_visualization: true
  best_medium: web-simulation
  best_medium_stars: 5
  best_medium_reason: "Behavior only becomes intuitive when users drag unhappy agents themselves, then automate, then tune bias — the full ladder."
  anti_patterns: ["static choropleth map only", "video of result without user placement", "quiz after lecture"]

sources:
  - type: paper
    id: PAP-0001
  - type: book
    id: BOK-0001
---

# Schelling Segregation Model

> **One-line essence:** Local tolerance thresholds can produce global segregation without individual malice.

## Why this matters

Explains residential segregation, school lunch tables, conference cliques, and online echo chambers — without requiring racist intent. Policy debates often assume bad actors; Schelling shows **structure from micro-preferences**.

## Core idea

Agents on a grid move if fewer than fraction *T* of neighbors share their type. With *T* ≈ 0.33 and two equal groups, integrated starting states often converge to highly segregated patterns.

## Formal definition

For agent *i* with type *cᵢ*, let *N(i)* be neighbor set. Agent is **unhappy** if:

```
|{ j ∈ N(i) : cⱼ = cᵢ }| / |N(i)| < T
```

Unhappy agents move to random empty cells. Repeat until equilibrium or max steps.

## Mechanism

1. Start integrated (or random)
2. Identify unhappy agents
3. Relocate to empty cells
4. Repeat — clusters form, making more agents unhappy
5. Segregation deepens from benign moves

## Parameters

| Parameter | Meaning | Typical range |
|-----------|---------|---------------|
| T | Tolerance threshold | 0.25–0.50 |
| % empty | Vacancy rate | 5–15% |
| Initial mix | Starting integration | 50/50 |
| Anti-bias | Demand diversity (Polygons extension) | T_diversity |

## Why interaction beats reading

**Verdict:** essential

The aha requires **complicity**: user moves one unhappy triangle to an "empty spot" and watches society crack. Automation + slider + "world starts segregated" chapters complete the ladder ([[ladder-of-abstraction]]).

## Surprising implications

- **Zero bias doesn't undo history** — integrated start with T=0 still may not unmix a segregated start
- **Anti-bias can desegregate** — demanding minimum diversity (Polygons extension) reverses trend
- **Equality is unstable** — integrated equilibrium is fragile; slight bias tips system

## Common misconceptions

| Wrong | Right |
|-------|-------|
| Agents are racist | Agents prefer *some* similar neighbors |
| Model proves people want segregation | Model shows emergent structure from weak preferences |
| Real segregation is only preference-based | Model is one mechanism among many (institutions, history) |

## Can become

| Medium | Fit | Notes |
|--------|-----|-------|
| Simulation | ✓ | Definitive |
| Interactive game | ✓ | Drag phase |
| Physical toy | ✓ | Grid + two colored tokens |
| Classroom activity | ✓ | Paper grid exercise |
| Board game | ✓ | Neighborhood builder |

**Best medium:** ★★★★★ web-simulation

**Reason:** Parameter exploration (T, initial conditions, anti-bias) requires sandbox.

## Existing explorables

| Explorable | Coverage | Gap |
|------------|----------|-----|
| [[parable-of-polygons]] | 90% | Real-world data layer; 3+ groups |

## Related

- [[thomas-schelling]] · [[emergence]] · [[threshold-models]]
- [[parable-of-polygons]] · [[agent-placement]] · [[neighborhood-grid]]

## Discovery suggestions

### Missing pages to create
- [ ] [[residential-segregation]] — PHN stub
- [ ] [[standing-ovation-threshold]] — SIM (Granovetter cousin)
- [ ] [[schelling-1971-dynamic-models]] — PAP
- [ ] [[micromotives-and-macrobehavior]] — BOK

### Potential simulations
- **Urban Percolation Equity** — segregation × service access — priority: 9.0

### Cross-disciplinary links
- [[network-science]] — spatial vs network segregation
- [[game-theory]] — nonequilibrium dynamics

## Further reading

- Schelling, T. C. (1971). Dynamic Models of Segregation. *Journal of Mathematical Sociology*.
- Case & Hart — [[parable-of-polygons]]

## See also

- [[emergence]] · [[threshold-models]] · [[ostrom-commons-design]]
