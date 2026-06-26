---
id: "PAT-0019"
type: "interaction-pattern"
slug: "predict"
title: "Abstraction Playable Game"
summary: "Abstraction Playable Game: understanding improves when learners manipulate the mechanism directly."
status: "mature"
created: "2026-06-26"
updated: "2026-06-26"
confidence: "medium"
tags: [complex-systems, abstraction, playable, game]
scores:
  visual_potential: 7
  interaction_potential: 9
  educational_value: 7
  surprise: 5
  replayability: 8
  narrative_potential: 5
  beauty: 6
  novelty: 4
  sandbox_potential: 9
  timelessness: 9
  virality: 5
  existing_coverage: 4
  research_quality: 6
  citation_strength: 5
  cross_disciplinary: 6
  composite: 7.0
explorable:
  verdict: "essential"
  why_interaction: "Commit-reveal mechanics force intuition to collide with formal resolution."
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
  best_medium: "interactive-game"
  best_medium_stars: 5
  best_medium_reason: "Commit-reveal mechanics force intuition to collide with formal resolution."
  anti_patterns: [text-only lecture, animation without user agency]
related:
  theories: [proof-2, proof-3, proofs]
---

# Abstraction Playable Game

## What it is

**Interaction pattern:** Abstraction Playable Game gives authors a reusable move when building explorables. It encodes *when* to use interaction, not just *what* to animate.

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

- [[diversity]]
- [[door-2]]
- [[dynamic]]

## Discovery suggestions

- [ ] Link to three THY nodes that use this pattern

## See also

- [[diversity]] · [[door-2]] · [[dynamic]]
