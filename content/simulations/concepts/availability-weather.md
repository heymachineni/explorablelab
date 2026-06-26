---
id: "SIM-0019"
type: "simulation-concept"
slug: "availability-weather"
title: "The Availability Weather"
summary: "The Availability Weather: understanding improves when learners manipulate the mechanism directly."
status: "mature"
created: "2026-06-26"
updated: "2026-06-26"
confidence: "medium"
tags: [complex-systems, availability, weather]
scores:
  visual_potential: 8
  interaction_potential: 9
  educational_value: 8
  surprise: 7
  replayability: 8
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
  composite: 7.8
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
  theories: [theory-32, theory-33, theory-34]
---

# The Availability Weather

> **Tagline:** Interactive treatment of the availability weather—behavior must be felt, not summarized.

## Theory

- [[paradox-232]]
- [[paradox-239]]
- [[paradox-245]]

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

- [[paradox-232]] · [[paradox-239]] · [[paradox-245]]
