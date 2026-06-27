---
id: "PAT-0001"
type: "interaction-pattern"
slug: "agent-placement"
title: "Agent Placement"
summary: "You move one piece; the system moves the rest."
status: "canonical"
wing: "design"
created: "2026-06-26"
updated: "2026-06-26"
related:
  design: {'patterns': ['parable-of-polygons', 'schelling-segregation']}
explorable:
  verdict: "essential"
  best_medium: "web-simulation"
  best_medium_stars: 4
---

# Agent Placement

> **One-line essence:** You move one piece; the system moves the rest — and the macro outcome becomes yours to own.

## What it is

Agent placement is the interaction pattern where the learner manually relocates one or a few agents in a simulation, then triggers automation so the remaining agents follow local rules. The user's hand initiates the cascade; the system completes it.

The pattern separates **intent** from **mechanism**. You choose where to put the unhappy triangle; the model decides who else moves, when, and why. The insight lands because the learner performed a reasonable local action and watched it produce an unreasonable global result.

## When to use it

Use agent placement when the theory depends on **emergence from micro-decisions** — segregation, diffusion, flocking, contagion, or any model where individual moves aggregate into structure nobody explicitly designed.

It works best when:

- The default state looks stable or fair until a small perturbation
- The learner's intuition says "this one move shouldn't matter much"
- Moral or political readings benefit from **complicity without accusation** — the user causes the outcome through benign choices, not villainous ones

Skip it when the phenomenon is purely aggregate (GDP curves, historical timelines) or when random initialization already tells the story.

## How it works in an explorable

A typical sequence:

1. **Show the grid** — integrated, calm, legible
2. **Highlight unhappy agents** — visual affordance for "this one wants to move"
3. **User drags one agent** — single move, no batch editing
4. **Run the rule** — neighbors react; clusters form or dissolve
5. **Pause on the surprise** — let the gap between expectation and outcome register

The first move should feel trivial. The second-order moves should feel inevitable in hindsight. That gap is the lesson.

## Design notes

- **One move first.** Batch placement turns complicity into configuration. Save bulk editing for sandbox mode later.
- **Make unhappiness visible.** Color, expression, or motion cues tell the user *which* agents are eligible without a tutorial paragraph.
- **Delay automation slightly.** A beat between the user's drop and the system's response builds causal attribution.
- **Pair with narration that stays local.** "This triangle wants more neighbors like itself" beats "society is racist."
- **Offer undo.** Letting users rewind one move reinforces that structure, not a single bad actor, drove the result.

## Anti-patterns

- **Video of the result without user placement** — the viewer watches segregation happen to someone else
- **Starting from an already segregated grid** — removes the shock of innocent first move (save reversed initial conditions for a later chapter)
- **Too many movable agents** — choice overload dilutes causal clarity
- **Hidden rules** — if the user cannot infer why agents move, placement feels like a slot machine
- **Lecture before touch** — explaining Schelling before the first drag front-loads abstraction and kills surprise

## Examples in our corpus

- [[parable-of-polygons]] — drag unhappy shapes; one reasonable relocation cracks an integrated neighborhood
- [[schelling-segregation]] — theory page documenting why manual placement precedes automation in the exhibit spine
- [[goodhart-school]] — placement of incentives and actors before metric-driven behavior runs
- [[jane-jacobs-corner]] — spatial agent decisions that reshape street-level dynamics

## Related

- [[ladder-of-abstraction]] — manual placement is usually the first rung
- [[parameter-slider]] — tolerance thresholds define who becomes "unhappy"
- [[sandbox-mode]] — free placement after the guided lesson
- [[neighborhood-grid]] — common visual metaphor for placement exhibits
- [[innocence-horror-hope]] — narrative arc that agent placement often opens

## Discovery suggestions

- [ ] Annotated GIF showing first-move → cascade → segregated clusters
- [ ] Side-by-side: same grid with automation-only vs user-initiated first move
- [ ] Classroom worksheet: "predict where one unhappy agent will move" before running simulation
- [ ] Anti-pattern gallery: static choropleth maps that skip placement entirely
