---
id: "PAT-0075"
type: "interaction-pattern"
slug: "undo"
title: "Leaderboard"
summary: "Leaderboard: understanding improves when learners manipulate the mechanism directly."
status: "mature"
created: "2026-06-26"
updated: "2026-06-26"
confidence: "medium"
tags: [complex-systems, leaderboard]
scores:
  visual_potential: 6
  interaction_potential: 8
  educational_value: 9
  surprise: 6
  replayability: 9
  narrative_potential: 5
  beauty: 6
  novelty: 4
  sandbox_potential: 8
  timelessness: 9
  virality: 5
  existing_coverage: 4
  research_quality: 6
  citation_strength: 5
  cross_disciplinary: 6
  composite: 7.0
explorable:
  verdict: "essential"
  why_interaction: "Patterns prove themselves when embedded in a live explorable demo."
  can_become:
    simulation: true
    interactive_game: false
    physical_toy: false
    classroom_activity: false
    visualization: true
    social_experiment: false
    mobile_app: false
    webgl_demo: false
    card_game: false
    board_game: false
    data_visualization: false
  best_medium: "web-simulation"
  best_medium_stars: 4
  best_medium_reason: "Patterns prove themselves when embedded in a live explorable demo."
  anti_patterns: [text-only lecture, animation without user agency]
related:
  theories: [linear-2, lm, load]
---

# Leaderboard

## What it is

**Interaction pattern:** Leaderboard gives authors a reusable move when building explorables. It encodes *when* to use interaction, not just *what* to animate.

## When to use

- Learner must feel consequence before naming the rule
- Parameter space is low-dimensional but insight is high
- Narrative and mechanics reinforce each other

## When to avoid

- Concept is purely definitional with no dynamic
- Interaction adds chrome without changing beliefs

## Implementation notes

| Element | Guidance |
|---------|----------|
| First screen | Minimal text; one manipulable |
| Reveal | After commit, show formal statement |
| Replay | Reset + randomize seed |

## Example explorables

- [[parable-of-polygons]] — reference implementation

## Pair with

- [[preface-paradox-kyburg]]
- [[rebound-paradox]]
- [[simpson-paradox]]

## Discovery suggestions

- [ ] Link to three THY nodes that use this pattern

## See also

- [[preface-paradox-kyburg]] · [[rebound-paradox]] · [[simpson-paradox]]
