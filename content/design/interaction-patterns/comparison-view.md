---
id: "PAT-0006"
type: "interaction-pattern"
slug: "comparison-view"
title: "Comparison View"
summary: "Same inputs, side by side."
status: "canonical"
wing: "design"
created: "2026-06-26"
updated: "2026-06-26"
related:
  design: {'patterns': ['to-build-a-better-ballot', 'wisdom-and-madness-of-crowds']}
explorable:
  verdict: "essential"
  best_medium: "web-simulation"
  best_medium_stars: 4
---

# Comparison View

> **One-line essence:** Same inputs, side by side — difference must be visible simultaneously, not remembered sequentially.

## What it is

Comparison view places two or more variants of a model — voting rules, network topologies, policy regimes, initial conditions — on screen at once, fed by **identical inputs**. The learner sees divergent outputs emerge in parallel without toggling tabs or relying on memory of the last run.

The pattern answers questions of the form: "Does the mechanism matter, or just the story we tell about it?" When only one panel is visible, authors can smuggle conclusions. Side-by-side denies that smuggle.

## When to use it

Use comparison view when the lesson is **relative** — which system is more fair, more stable, more contagious — not absolute.

Strong fits:

- Electoral systems applied to the same preference profile ([[to-build-a-better-ballot]])
- Network structures with identical seed content ([[graph-rewiring]] exhibits often pair with comparison)
- Simpson's paradox partitions shown together ([[simpsons-paradox-university]])
- Treatment vs control in social simulations

Weaker fits:

- Single-threshold emergence (use [[agent-placement]] + [[parameter-slider]])
- Narratives requiring sequential surprise ([[but-chain]])
- Concepts with one correct answer ([[predict-then-reveal]])

## How it works in an explorable

1. **Define shared input** — one electorate, one rumor, one dataset, one agent population
2. **Instantiate variants** — left panel: rule A; right panel: rule B (labels in plain language)
3. **Synchronize time** — shared play/pause; linked scrubber when histories matter
4. **Highlight divergence** — color, annotation, or metric readout when paths split
5. **Invite swap** — optional: flip which variant is "yours" to test fairness of framing

Synchronization is non-negotiable. Async runs let users attribute differences to randomness rather than structure.

## Design notes

- **Two panels first.** Three-plus comparisons belong in sandbox or expert mode.
- **Identical random seeds** when stochasticity matters — otherwise noise masquerades as mechanism.
- **Shared legend and scale** — mismatched axes make one side look "more dramatic" by design cheat.
- **Input editor upstream** — let users edit the shared preference profile and watch both panels update.
- **Name mechanisms, not outcomes.** "Instant runoff" vs "plurality" — not "good result" vs "bad result."
- **Mobile: stack vertically** with sticky shared controls; side-by-side may not fit narrow viewports.

## Anti-patterns

- **Sequential toggle** — showing A, then B, then asking "which was fairer?" tests memory, not judgment
- **Different inputs per panel** — apples-to-oranges comparison proves nothing
- **Unlabeled panels** — users compare vibes, not rules
- **Desynced animation** — one side finishes early; causality feels rigged
- **Winner badge** — declaring a victor before users inspect tradeoffs short-circuits reasoning

## Examples in our corpus

- [[to-build-a-better-ballot]] — same votes, different electoral systems, divergent winners
- [[wisdom-and-madness-of-crowds]] — network topology comparison with identical information seeds
- [[simpsons-paradox-university]] — aggregate vs partitioned views side by side
- [[majority-illusion]] — perceived vs actual prevalence under different graph wiring
- [[commons-garden]] — cooperative vs defecting strategies on matched resource pools

## Related

- [[parameter-slider]] — continuous sweep when variants are numeric, not categorical
- [[graph-rewiring]] — often paired: rewire one graph, compare diffusion to baseline
- [[sandbox-mode]] — advanced users compose their own comparison sets
- [[predict-then-reveal]] — sometimes precedes comparison ("guess which system wins")
- [[social-choice]] — theory hub for voting comparison exhibits

## Discovery suggestions

- [ ] Annotated GIF: shared input edit → both panels update → divergence highlight
- [ ] Classroom worksheet: same data, predict both outcomes before reveal
- [ ] Diff mode: single chart overlaying both result metrics
- [ ] Anti-pattern callout: before/after screenshots instead of live dual panels
