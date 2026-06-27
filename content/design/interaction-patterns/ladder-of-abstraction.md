---
id: "PAT-0009"
type: "interaction-pattern"
slug: "ladder-of-abstraction"
title: "Ladder of Abstraction"
summary: "Manual → automated → parameterized."
status: "canonical"
wing: "design"
created: "2026-06-26"
updated: "2026-06-26"
related:
  design: {'patterns': ['parable-of-polygons', 'to-build-a-better-ballot']}
explorable:
  verdict: "essential"
  best_medium: "web-simulation"
  best_medium_stars: 4
---

# Ladder of Abstraction

> **One-line essence:** Manual → automated → parameterized — each rung adds power and proves the rule generalizes.

## What it is

The ladder of abstraction is a sequencing pattern for explorable exhibits. The learner climbs through control modes of increasing generality:

1. **Manual** — move one agent, flip one switch, make one move ([[agent-placement]])
2. **Automated** — watch the full system run under fixed rules
3. **Parameterized** — tune coefficients with sliders ([[parameter-slider]])
4. **Sandbox** — unrestricted initial conditions and controls ([[sandbox-mode]])

Each rung answers a different skepticism. Manual proves complicity. Automation proves scale. Parameters prove the phenomenon is not tuned to one demo. Sandbox proves the author didn't cherry-pick.

## When to use it

Use the full ladder when the model is the argument — agent-based segregation, evolutionary game theory, electoral simulation — and the audience might dismiss a single curated scene.

Climb the ladder when:

- The default exhibit path needs **progressive trust-building**
- Different learners enter at different rungs (teachers may skip to sandbox)
- The same engine powers all chapters — one codebase, escalating affordances

Short-circuit when the concept is a single puzzle ([[predict-then-reveal]]) or a pairwise comparison ([[comparison-view]]) with no spatial model.

## How it works in an explorable

**Rung 1 — Manual:** User performs the smallest action with largest narrative weight. Pause for reflection.

**Rung 2 — Automated:** "Now let everyone follow the rule." Speed control; optional step-through.

**Rung 3 — Parameterized:** Expose tolerance, noise, or payoff. Sweep to find phase boundaries.

**Rung 4 — Initial-condition flip:** Optional middle rung — same rules, reversed starting state (integrated ↔ segregated).

**Rung 5 — Sandbox:** All controls unlocked; guided path remains accessible via menu.

Chapter transitions should name the escalation: "You moved one. Now everyone moves."

## Design notes

- **Same visual world throughout** — continuity signals one model, more power
- **Do not skip rung 1 for impatience** — the visceral hook lives in manual control
- **Allow chapter select** — experts replay sandbox; novices need the climb
- **Document the ladder in exhibit metadata** — helps museum curation and classroom planning
- **Pair with [[innocence-horror-hope]]** on emotional axis while ladder handles control axis
- **Reverse ladder rarely** — starting sandbox then constraining feels punitive

## Anti-patterns

- **Sandbox-only exhibit** — power without story; most users stop at noise
- **Manual without automation** — anecdote without proof of scale
- **Automation without parameters** — "trust me, it always happens" without sensitivity analysis
- **Disjoint engines per rung** — different sims per chapter break the generalization claim
- **Hidden rungs** — users don't know more depth exists

## Examples in our corpus

- [[parable-of-polygons]] — canonical four-beat ladder: placement → automate → slider → segregated start → sandbox
- [[schelling-segregation]] — theory page explicitly maps exhibit spine to ladder rungs
- [[to-build-a-better-ballot]] — guided election scenarios → open electorate editor
- [[evolution-of-trust]] — narrative chapters escalate from one-shot to population tournament
- [[goodhart-school]] — manual metric choice → automated school response → parameter sweep

## Related

- [[agent-placement]] — first rung for spatial ABMs
- [[parameter-slider]] — third rung for continuous models
- [[sandbox-mode]] — top rung
- [[but-chain]] — orthogonal narrative structure; often interleaved with ladder rungs
- [[neighborhood-grid]] — visual metaphor that persists across rungs

## Discovery suggestions

- [ ] Exhibit audit checklist: which rungs exist, which are missing
- [ ] Annotated spine diagram for [[parable-of-polygons]] with rung labels
- [ ] Classroom pacing guide: one rung per session for multi-day units
- [ ] Anti-pattern callout: video essay masquerading as explorable (no rungs at all)
