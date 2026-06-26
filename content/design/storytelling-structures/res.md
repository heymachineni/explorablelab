---
id: "STR-0017"
type: "storytelling-structure"
slug: "res"
title: "Within"
summary: "Within: understanding improves when learners manipulate the mechanism directly."
status: "mature"
created: "2026-06-26"
updated: "2026-06-26"
confidence: "medium"
tags: [complex-systems, within]
scores:
  visual_potential: 6
  interaction_potential: 8
  educational_value: 6
  surprise: 5
  replayability: 7
  narrative_potential: 8
  beauty: 5
  novelty: 4
  sandbox_potential: 4
  timelessness: 9
  virality: 5
  existing_coverage: 4
  research_quality: 5
  citation_strength: 4
  cross_disciplinary: 5
  composite: 6.3
explorable:
  verdict: "strong"
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
  theories: [sunk-cost-tunnel, thermodynamic-attention, tragedy-lake]
---

# Within

## What it is

**Story structure:** Within gives authors a reusable move when building explorables. It encodes *when* to use interaction, not just *what* to animate.

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

- [[84-paradox]]
- [[90-paradox]]
- [[97-paradox]]

## Discovery suggestions

- [ ] Link to three THY nodes that use this pattern

## See also

- [[84-paradox]] · [[90-paradox]] · [[97-paradox]]
