---
id: "THY-0020"
type: "theory"
slug: "loss-aversion"
title: "Demand"
summary: "Demand: understanding improves when learners manipulate the mechanism directly."
status: "mature"
created: "2026-06-26"
updated: "2026-06-26"
confidence: "medium"
tags: [economics, demand]
scores:
  visual_potential: 6
  interaction_potential: 6
  educational_value: 9
  surprise: 5
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
  composite: 6.5
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
  theories: [wave-2, wave-3, weak]
---

# Demand

> **One-line essence:** Demand is a core framework for reasoning about economics.

## Why this matters

Without grasping demand, practitioners in economics overfit anecdotes to theory and under-specify the variables that actually drive outcomes.

## Core idea

Demand formalizes a relationship that practitioners already gesture at informally: which quantities matter, which feedback loops dominate, and where predictions break.

## Formal definition

Let **X** denote the primary state variable in demand. Under standard assumptions in economics, the relationship is written compactly as a mapping from initial conditions and parameters to observables. Exact notation varies by subfield; the explorable version should expose parameters, not hide them behind prose.

## Mechanism

1. Identify the units of analysis (agents, particles, beliefs, prices).
2. Specify update rules or conservation laws governing demand.
3. Iterate or integrate until equilibrium, steady state, or critical transition.
4. Compare aggregate statistics to baseline intuition.

## Parameters

| Parameter | Meaning | Typical range |
|-----------|---------|---------------|
| Primary rate | Controls speed of adjustment in demand | field-specific |
| Coupling strength | How strongly units influence neighbors | low → high |
| Noise / friction | Random shocks or transaction costs | 0 → substantial |
| Initial condition | Starting distribution of states | varied |

## Why interaction beats reading

**Verdict:** strong

Reading about demand invites hindsight bias: every outcome feels inevitable once labeled. An explorable lets users **set parameters, perturb initial conditions, and watch failure modes**—the only route to calibrated intuition.

## Surprising implications

- Small parameter shifts can flip demand from stable to explosive regimes.
- Mean outcomes can mislead when variance and tail risk dominate welfare.
- Interventions optimized on short horizons often reverse under demand dynamics.

## Common misconceptions

| Wrong | Right |
|-------|-------|
| It is only a metaphor | It makes falsifiable quantitative predictions |
| One counterexample refutes it entirely | Scope conditions define where it applies |
| More data alone fixes misunderstanding | Mechanism must be simulated or manipulated |

## Real-world applications

- **Education:** teach demand with sandbox labs before equations.
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

- [[newcomb-paradox]] · [[olbers-paradox-2]] · [[paradox-105]]

## Discovery suggestions

### Missing pages to create
- [ ] [[loss-aversion-paper]] — canonical citation anchor

### Potential simulations
- **Demand Sandbox** — web-simulation — priority: high

### Cross-disciplinary links
- [[newcomb-paradox]] — structural analogy
- [[olbers-paradox-2]] — structural analogy

## Further reading

- Standard references in economics (consult field bibliography).

## See also

- [[newcomb-paradox]] · [[olbers-paradox-2]] · [[paradox-105]]
