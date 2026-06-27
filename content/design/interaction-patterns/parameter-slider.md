---
id: "PAT-0002"
type: "interaction-pattern"
slug: "parameter-slider"
title: "Parameter Slider"
summary: "One dial, many worlds."
status: "canonical"
wing: "design"
created: "2026-06-26"
updated: "2026-06-26"
related:
  design: {'patterns': ['fireflies', 'evolution-of-trust']}
explorable:
  verdict: "essential"
  best_medium: "web-simulation"
  best_medium_stars: 4
---

# Parameter Slider

> **One-line essence:** One dial, many worlds — sweep a single variable and watch the entire system reorganize.

## What it is

A parameter slider exposes one model variable as a continuous control — tolerance, noise, coupling strength, mutation rate, discount factor — and updates the simulation in real time as the learner drags. The learner explores **parameter space** by feel rather than by reading equations.

Sliders translate abstract coefficients into physical intuition. "33% same-neighbor preference" becomes a thumb moving left and right while clusters appear and dissolve. The pattern makes models **legible** without making them **simplified**.

## When to use it

Use sliders when the theory's punchline is **threshold behavior**, **phase transitions**, or **comparative statics** — small parameter shifts that flip outcomes qualitatively.

Strong fits:

- Bifurcations (integrated ↔ segregated, synchronized ↔ chaotic)
- Sensitivity analysis ("which assumption matters most?")
- Debunking false precision ("any tolerance above X produces Y")

Weak fits:

- Models where parameters are categorical, not continuous (voting rules → use [[comparison-view]] instead)
- Concepts with no natural ordering on the control
- First exposure before the learner understands what the variable means

## How it works in an explorable

1. **Establish baseline** — run at a default value; narrate what the learner sees
2. **Label the dial in plain language** — "How picky are agents about neighbors?" not "T"
3. **Live update** — simulation responds while dragging; no "apply" button
4. **Mark critical thresholds** — subtle tick or color shift at bifurcation points
5. **Invite sweep** — "drag slowly across the middle; notice when it breaks"

The learner builds a mental map: left side = one regime, right side = another, middle = unstable or transitional zone.

## Design notes

- **One slider at a time** for first contact. Multi-dimensional parameter space needs [[sandbox-mode]] or staged unlocks.
- **Bind visible outcomes.** If the slider moves but nothing obvious changes, the control feels broken.
- **Use logarithmic scales** for parameters that span orders of magnitude (infection rate, learning rate).
- **Show the number** alongside the label — some learners want the symbol; others want the story.
- **Reset button** — lets users re-run the sweep without reloading the page.
- **Couple with animation speed control** when transitions are slow — fast-forward through equilibration.

## Anti-patterns

- **Ten sliders on first screen** — instant cognitive collapse; no variable feels causal
- **Discrete jumps disguised as continuous** — if the model only supports three values, use stepped buttons
- **Slider before story** — tuning a dial you don't understand is fiddling, not learning
- **No default anchor** — users need a known starting point to compare against
- **Silent failure at extremes** — if high values crash the sim, clamp and explain rather than freezing

## Examples in our corpus

- [[parable-of-polygons]] — tolerance threshold slider after manual and automated chapters
- [[fireflies]] — coupling strength between oscillators; watch sync emerge and collapse
- [[evolution-of-trust]] — noise, simulation speed, and payoff matrix assumptions exposed as controls
- [[standing-ovation]] — threshold for standing; small shifts flip audience behavior
- [[deffuant-polarization]] — opinion tolerance and interaction radius as sweepable parameters

## Related

- [[ladder-of-abstraction]] — sliders typically arrive after manual and automated phases
- [[sandbox-mode]] — unrestricted slider play after the guided path
- [[comparison-view]] — when the variable is discrete (voting systems), side-by-side beats a dial
- [[agent-placement]] — often precedes sliders in segregation exhibits
- [[schelling-segregation]] — canonical theory pairing for tolerance-threshold sliders

## Discovery suggestions

- [ ] Annotated GIF: slow sweep across bifurcation with cluster count overlay
- [ ] "Which assumption matters?" exercise — hide slider labels, ask users to guess which dial they moved
- [ ] Heatmap mode: two sliders simultaneously in sandbox (advanced)
- [ ] Anti-pattern callout: dashboard with twelve unlabeled dials
