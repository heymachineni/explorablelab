---
id: "SIM-0097"
type: "simulation-concept"
slug: "littles-law-queue"
title: "The Little's Law Queue"
summary: "The Little's Law Queue: understanding improves when learners manipulate the mechanism directly."
status: "mature"
created: "2026-06-26"
updated: "2026-06-26"
confidence: "medium"
tags: [complex-systems, little, law, queue]
scores:
  visual_potential: 9
  interaction_potential: 9
  educational_value: 8
  surprise: 9
  replayability: 8
  narrative_potential: 7
  beauty: 6
  novelty: 5
  sandbox_potential: 9
  timelessness: 8
  virality: 7
  existing_coverage: 4
  research_quality: 9
  citation_strength: 7
  cross_disciplinary: 7
  composite: 8.3
build_difficulty: "medium"
build_estimate_weeks: 3
explorable:
  verdict: "essential"
  why_interaction: "Parameter exploration reveals behavior invisible in static prose."
  can_become:
    simulation: true
    interactive_game: true
    physical_toy: false
    classroom_activity: true
    visualization: true
    social_experiment: true
    mobile_app: false
    webgl_demo: false
    card_game: false
    board_game: false
    data_visualization: true
  best_medium: "web-simulation"
  best_medium_stars: 5
  best_medium_reason: "Parameter exploration reveals behavior invisible in static prose."
  anti_patterns: [text-only lecture, animation without user agency]
related:
  theories: [proof-2, proof-3, proofs]
---

# The Little's Law Queue

> **Tagline:** Interactive treatment of the little's law queue—behavior must be felt, not summarized.

## Theory

- [[in-5]]
- [[inference]]
- [[information-cascades]]

## Core interaction

Users manipulate the smallest set of parameters that produces surprise. Default path: naive play → contradiction → named rule → sandbox.

## Build spec

| Layer | Requirement |
|-------|-------------|
| Model | Transparent update rules |
| UI | One dominant control per act |
| Narrative | BUT-chain between acts |

## Anti-patterns

- Text wall before first interaction
- Animation without user agency

## Discovery suggestions

- [ ] Prototype stub (PRT) when composite ≥ 8.5

## See also

- [[in-5]] · [[inference]] · [[information-cascades]]
