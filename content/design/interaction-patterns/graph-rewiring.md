---
id: "PAT-0008"
type: "interaction-pattern"
slug: "graph-rewiring"
title: "Graph Rewiring"
summary: "Drag edges; watch diffusion change."
status: "canonical"
wing: "design"
created: "2026-06-26"
updated: "2026-06-26"
related:
  design: {'patterns': ['wisdom-and-madness-of-crowds', 'weak-tie-bridge']}
explorable:
  verdict: "essential"
  best_medium: "web-simulation"
  best_medium_stars: 4
---

# Graph Rewiring

> **One-line essence:** Drag edges; watch diffusion change — topology beats content when information spreads.

## What it is

Graph rewiring lets the learner add, remove, or drag edges in a network visualization, then run diffusion, contagion, or consensus dynamics on the modified topology. The **same nodes, same initial beliefs, different wires** — and outcomes diverge sharply.

The pattern teaches that structure filters signal. Weak ties, echo chambers, bridge nodes, and majority illusions are not metaphors; they are edge layouts you can edit with a cursor.

## When to use it

Use graph rewiring when the theory claims **network structure causally matters** — Granovetter bridges, complex contagion thresholds, wisdom vs madness of crowds, filter bubbles.

Ideal when:

- Learners over-attribute outcomes to message quality instead of placement
- A small edge edit produces disproportionate macro change
- [[comparison-view]] can show before/after wiring with shared seeds

Less ideal for grid-based spatial models ([[agent-placement]]), continuous parameter sweeps alone ([[parameter-slider]]), or non-network domains.

## How it works in an explorable

1. **Render legible graph** — nodes as people or sites; edges as ties; avoid hairball layouts
2. **Seed identical node states** — one rumor, one innovation, one protest willingness
3. **Enable edge editing** — click-drag to connect, click to sever; optional edge weight
4. **Run diffusion** — animate spread; color nodes by adoption time or belief
5. **Prompt structural hypothesis** — "add one bridge"; "delete the weak tie"; compare reach
6. **Quantify** — reach, speed, polarization index; numbers anchor visual surprise

Rewiring should feel **surgical** — one edge, big effect — at least in the guided chapter.

## Design notes

- **Start sparse.** Dense random graphs make edge edits invisible in the noise.
- **Highlight bridges** after user discovery — vocabulary follows experience.
- **Snap or validate edges** — prevent accidental duplicate links or self-loops unless pedagogically intended.
- **Undo stack** — encourages experimentation without fear of breaking the layout.
- **Pair with [[weak-tie-bridge]]** and [[majority-illusion]] exhibits for canonical scenarios.
- **Layout stability** — nodes shouldn't jump unpredictably when one edge changes; preserve mental map.

## Anti-patterns

- **Hairball network** — too many nodes/edges; rewiring is needle-in-haystack
- **Content change coupled with rewire** — new message and new topology; confounded causality
- **Static graph with highlight only** — showing bridges without letting users create them
- **Rewire without run** — topology edit must connect to dynamics, not just pretty graphs
- **Misleading force layout** — physics simulation hides deliberate structure

## Examples in our corpus

- [[wisdom-and-madness-of-crowds]] — rewire crowd networks; wisdom collapses or emerges by topology
- [[weak-tie-bridge]] — add bridging tie; watch information reach new cluster
- [[majority-illusion]] — edge layout distorts perceived prevalence
- [[complex-contagion-protest]] — threshold contagion sensitive to local clustering
- [[information-cascade-falls]] — cascade paths depend on who listens to whom

## Related

- [[comparison-view]] — baseline vs rewired graph with synchronized runs
- [[parameter-slider]] — contagion threshold as dial; rewiring as spatial complement
- [[threshold-models]] — theory of when local density blocks or enables spread
- [[standing-ovation]] — audience topology and threshold interaction
- [[complex-contagion]] — theory hub for rewiring exhibits

## Discovery suggestions

- [ ] Annotated GIF: single edge add → diffusion reaches new component
- [ ] Challenge: connect two clusters with minimum edges for 90% reach
- [ ] Preset topologies: star, ring, small-world, random — same seed, compare
- [ ] Anti-pattern callout: social network viz with no interactive edges
