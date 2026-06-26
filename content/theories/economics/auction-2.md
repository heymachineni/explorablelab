---
id: "THY-0475"
type: "theory"
slug: "auction-2"
title: "Reputation"
summary: "Reputation: understanding improves when learners manipulate the mechanism directly."
status: "mature"
created: "2026-06-26"
updated: "2026-06-26"
confidence: "medium"
tags: [economics, reputation]
scores:
  visual_potential: 7
  interaction_potential: 7
  educational_value: 9
  surprise: 7
  replayability: 5
  narrative_potential: 4
  beauty: 5
  novelty: 4
  sandbox_potential: 6
  timelessness: 8
  virality: 6
  existing_coverage: 4
  research_quality: 7
  citation_strength: 6
  cross_disciplinary: 7
  composite: 7.0
fields: [economics]
difficulty: "introductory"
explorable:
  verdict: "strong"
  why_interaction: "Manipulation of variables makes the mechanism tangible."
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
  best_medium_stars: 4
  best_medium_reason: "Manipulation of variables makes the mechanism tangible."
  anti_patterns: [text-only lecture, animation without user agency]
related:
  theories: [translation, transparency, transport]
---

# Reputation

> **One-line essence:** Reputation links mechanism, prediction, and intervention in economics.

## Why this matters

Reputation sits at the fault line between intuition and evidence in economics; misunderstanding it propagates through textbooks, dashboards, and public debate.

## Core idea

The theory specifies conditions under which observed regularities hold, and—crucially—conditions under which they fail.

## Formal definition

Let **X** denote the primary state variable in reputation. Under standard assumptions in economics, the relationship is written compactly as a mapping from initial conditions and parameters to observables. Exact notation varies by subfield; the explorable version should expose parameters, not hide them behind prose.

## Mechanism

1. Identify the units of analysis (agents, particles, beliefs, prices).
2. Specify update rules or conservation laws governing reputation.
3. Iterate or integrate until equilibrium, steady state, or critical transition.
4. Compare aggregate statistics to baseline intuition.

## Parameters

| Parameter | Meaning | Typical range |
|-----------|---------|---------------|
| Primary rate | Controls speed of adjustment in reputation | field-specific |
| Coupling strength | How strongly units influence neighbors | low → high |
| Noise / friction | Random shocks or transaction costs | 0 → substantial |
| Initial condition | Starting distribution of states | varied |

## Why interaction beats reading

**Verdict:** strong

Reading about reputation invites hindsight bias: every outcome feels inevitable once labeled. An explorable lets users **set parameters, perturb initial conditions, and watch failure modes**—the only route to calibrated intuition.

## Surprising implications

- Small parameter shifts can flip reputation from stable to explosive regimes.
- Mean outcomes can mislead when variance and tail risk dominate welfare.
- Interventions optimized on short horizons often reverse under reputation dynamics.

## Common misconceptions

| Wrong | Right |
|-------|-------|
| It is only a metaphor | It makes falsifiable quantitative predictions |
| One counterexample refutes it entirely | Scope conditions define where it applies |
| More data alone fixes misunderstanding | Mechanism must be simulated or manipulated |

## Real-world applications

- **Education:** teach reputation with sandbox labs before equations.
- **Policy:** stress-test proposals against dynamic economics models, not static snapshots.
- **Design:** expose levers users can actually control; hide only complexity that does not change decisions.

## Can become

| Medium | Fit | Notes |
|--------|-----|-------|
| Simulation | ✓ | Primary medium |
| Interactive game | ✓ | Commit-reveal or role-play |
| Classroom activity | ✓ | Paper or token version |
| Visualization | ✓ | Parameter sweeps |

## Related

- [[queueing-theory]] · [[radiation-2]] · [[rational]]

## Discovery suggestions

### Missing pages to create
- [ ] [[auction-2-paper]] — canonical citation anchor

### Potential simulations
- **Reputation Sandbox** — web-simulation — priority: high

### Cross-disciplinary links
- [[queueing-theory]] — structural analogy
- [[radiation-2]] — structural analogy

## Further reading

- Standard references in economics (consult field bibliography).

## See also

- [[queueing-theory]] · [[radiation-2]] · [[rational]]
