---
id: "SIM-0116"
type: "simulation-concept"
slug: "byzantine-generals-camp"
title: "The Byzantine Generals Camp"
summary: "The Byzantine Generals Camp: understanding improves when learners manipulate the mechanism directly."
status: "mature"
created: "2026-06-26"
updated: "2026-06-26"
confidence: "medium"
tags: [complex-systems, byzantine, generals, camp]
scores:
  visual_potential: 9
  interaction_potential: 9
  educational_value: 8
  surprise: 8
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
  theories: [nash, nash-2, natural]
---

# The Byzantine Generals Camp

> **Tagline:** Interactive treatment of the byzantine generals camp—behavior must be felt, not summarized.

## Theory

- [[logical-paradox-89]]
- [[logical-paradox-95]]
- [[lottery-paradox-2]]

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

- [[logical-paradox-89]] · [[logical-paradox-95]] · [[lottery-paradox-2]]
