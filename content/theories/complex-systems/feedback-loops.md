---
id: "THY-0004"
type: "theory"
slug: "feedback-loops"
title: "Feedback Loops"
summary: "Output becomes input. Circles close."
status: "canonical"
wing: "systems"
created: "2026-06-26"
updated: "2026-06-26"
related:
  theories: [loopy, we-become-what-we-behold, krebs-cycle-of-outrage]
  simulations: {'existing': ['parable-of-polygons']}
explorable:
  verdict: "essential"
  best_medium: "web-simulation"
  best_medium_stars: 4
---

# Feedback Loops

> **One-line essence:** When a system's output feeds back into its input, small changes can amplify into runaway growth or settle into stable balance.

## Why this matters

Feedback loops are the grammar of dynamics. Anxiety spirals, wealth compounds, thermostats stabilize, outrage cycles accelerate — all share the same structural pattern: **output becomes input**. Without recognizing loop sign (reinforcing vs balancing) and delay, policy makers chase symptoms, platforms optimize metrics that degrade experience, and individuals misread temporary stability for permanent safety.

## Core idea

A **feedback loop** is a causal cycle in which variable *A* affects *B*, and *B* eventually affects *A* again. Two families dominate:

- **Reinforcing (positive) loops** amplify deviation. More of *A* produces more of *B*, which produces more of *A*. Examples: compound interest, viral growth, arms races, panic selling.
- **Balancing (negative) loops** resist deviation. The system pushes back toward a goal or equilibrium. Examples: thermostats, hunger regulation, supply meeting demand at a market price.

Most real systems contain **multiple nested loops** operating at different speeds. What looks like chaos is often competing loops — one reinforcing, one balancing — with delays that cause overshoot and oscillation.

## Mechanism

1. **Identify stocks** — quantities that accumulate (trust, debt, temperature, outrage).
2. **Identify flows** — rates that change stocks (deposits, posts, heat transfer).
3. **Trace causality** — does an increase in the stock increase or decrease the flow that feeds it?
4. **Classify loop sign** — even number of negative links → reinforcing; odd → balancing.
5. **Add delays** — perception, reporting, and physical lag turn smooth curves into oscillations.

System dynamics (Forrester, Meadows) formalizes this with differential equations and stock-flow diagrams. The insight transfers without the math: **structure drives behavior**, not isolated events.

## Formal sketch

For stock *X* with inflow *I*(*X*, *Y*) and outflow *O*(*X*, *Y*), the governing equation is d*X*/d*t* = *I* − *O*. A reinforcing loop appears when ∂*I*/∂*X* > ∂*O*/∂*X* over the operating range — more *X* accelerates net accumulation. Delays τ in information or physical response turn monotonic approaches into oscillation: the system overshoots before the balancing loop engages.

## Implications

- **Reinforcing loops dominate until a limit.** Exponential growth always hits constraints — another loop, a resource ceiling, or collapse.
- **Balancing loops hide leverage points.** Changing a delay or gain in a balancing loop often beats direct intervention on symptoms.
- **Metrics create loops.** When a measured output becomes a target, the loop reconnects measurement to behavior — see [[goodharts-law]].
- **Emergence lives in loops.** Local rules that feed global patterns back to agents produce [[emergence]] without central design.

## Common misconceptions

| Wrong | Right |
|-------|-------|
| "Positive feedback" means good | Reinforcing loops amplify whatever direction they're pointed — growth or collapse |
| Balance means static | Balancing loops produce dynamic equilibrium — oscillation around a set point is common |
| Loops are always visible | Hidden delays and indirect paths make loops hard to see without explicit mapping |
| Breaking one link fixes the system | Compensating loops often activate; whack-a-mole is multiple loops fighting |

## Related

- [[goodharts-law]] · [[emergence]] · [[ergodicity]]
- [[loopy]] · [[krebs-cycle-of-outrage]] · [[we-become-what-we-behold]]
- [[feedback-loop-circle]] · [[schelling-segregation]]

## Further reading

- Meadows, D. H. (2008). *Thinking in Systems: A Primer*. Chelsea Green.
- Richardson, G. P. (1991). *Feedback Thought in Social Science and Systems Theory*. University of Pennsylvania Press.
- Sterman, J. D. (2000). *Business Dynamics: Systems Thinking and Modeling for a Complex World*. McGraw-Hill.

## Discovery suggestions

### Missing pages to create
- [ ] [[stock-flow-diagram]] — design pattern for exhibits
- [ ] [[delay-overshoot]] — oscillation without external shocks

### Potential simulations
- **Loop Builder** — draw nodes, auto-classify R/B loops — priority: 8.0

### Cross-disciplinary links
- [[economics]] — multiplier-accelerator models
- [[climate-science]] — ice-albedo and carbon feedbacks
