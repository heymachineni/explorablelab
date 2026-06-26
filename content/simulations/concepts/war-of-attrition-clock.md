---
id: "SIM-0064"
type: "simulation-concept"
slug: "war-of-attrition-clock"
title: "The War of Attrition Clock"
summary: "The War of Attrition Clock: understanding improves when learners manipulate the mechanism directly."
status: "mature"
created: "2026-06-26"
updated: "2026-06-26"
confidence: "medium"
tags: [complex-systems, war, attrition, clock]
scores:
  visual_potential: 8
  interaction_potential: 9
  educational_value: 8
  surprise: 9
  replayability: 9
  narrative_potential: 7
  beauty: 6
  novelty: 5
  sandbox_potential: 9
  timelessness: 8
  virality: 7
  existing_coverage: 4
  research_quality: 7
  citation_strength: 6
  cross_disciplinary: 7
  composite: 8.1
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
  theories: [mechanics-2, mechanics-3, mechanics-4]
---

# The War of Attrition Clock

> **Tagline:** Interactive treatment of the war of attrition clock—behavior must be felt, not summarized.

## Theory

- [[berksons-paradox]]
- [[braess-paradox]]
- [[correlation-paradox]]

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

- [[berksons-paradox]] · [[braess-paradox]] · [[correlation-paradox]]
