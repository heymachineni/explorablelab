---
id: "PAT-0010"
type: "interaction-pattern"
slug: "playable-game"
title: "Playable Game"
summary: "Real stakes in a toy world."
status: "canonical"
wing: "design"
created: "2026-06-26"
updated: "2026-06-26"
related:
  design: {'patterns': ['evolution-of-trust', 'ultimatum-game']}
explorable:
  verdict: "essential"
  best_medium: "web-simulation"
  best_medium_stars: 4
---

# Playable Game

> **One-line essence:** Real stakes in a toy world — games are arguments you feel in your gut before you articulate them.

## What it is

Playable game embeds genuine game mechanics — repeated decisions, scoring, opponent modeling, resource exhaustion — inside an explorable whose purpose is understanding, not entertainment alone. The learner **invests rounds**; betrayal, cooperation, or miscalculation carries felt cost.

Toy payoffs stand in for real incentives. The mapping is explicit enough to transfer, abstract enough to avoid trauma or partisan trigger. You don't read that defection dominates one-shot interactions; you defect, win once, and watch trust collapse over ten rounds.

## When to use it

Use playable games when the concept is **strategic** — game theory, negotiation, trust, fairness norms, mechanism design — and prose cannot convey the incentive bite.

Strong fits:

- Prisoner's dilemma and iterated variants
- Ultimatum and dictator games
- Newcomb-style prediction contests
- Resource commons with harvest pressure

Weaker fits:

- Pure visualization of static data
- Phenomena with no agent choice ([[galton-board]]-style physics)
- Topics where scoring trivializes harm without [[role-as-system]] care

## How it works in an explorable

1. **Minimal rules tutorial** — one interactive round, not a rulebook page
2. **Clear payoff visibility** — matrix, coin counter, or trust bar always on screen
3. **Repeated rounds** — single play is anecdote; series reveals structure
4. **Opponent with legible behavior** — tit-for-tat, random, grim trigger; label the strategy
5. **Debrief bridge** — connect felt outcome to named concept (Nash equilibrium, folk theorem)
6. **Optional tournament** — pit strategies; user discovers which wins population ([[evolution-of-trust]])

Stakes should be **recoverable** — lost points, not lost dignity. Reset restores trust for another hypothesis.

## Design notes

- **Short rounds** — ten clicks beat hundred-turn grind for classroom time budgets
- **Name strategies after behavior** — "Copycat" not "strategy 7"
- **Show history** — round-by-round grid makes pattern recognition possible
- **Let users pick opponent** — agency over who they learn against
- **Separate score from moral judgment** — high score ≠ endorsement; debrief makes normative layer explicit
- **Accessibility** — keyboard playable; color not sole payoff indicator

## Anti-patterns

- **Skinner box without debrief** — addictive clicks, no conceptual landing
- **Hidden payoffs** — users can't learn incentives they can't see
- **Real money or social punishment** — breaks toy-world contract; ethical review required
- **Unbeatable opponent** — learned helplessness, not game theory
- **Game so fun the argument disappears** — entertainment eclipses transfer

## Examples in our corpus

- [[evolution-of-trust]] — flagship iterated game plus population tournament
- [[ultimatum-game]] — accept/reject offers; fairness vs rationality tension
- [[newcomb-predictor]] — prediction game with transparent opponent model
- [[commons-garden]] — harvest game with tragedy and Ostrom-style variants
- [[prisoners-dilemma-tournament]] — experiment page linking classroom play to pattern
- [[iterated-prisoners-dilemma]] — theory companion for repeated playable exhibits

## Related

- [[but-chain]] — narrative spine for multi-chapter game expositions
- [[predict-then-reveal]] — commit-before-opponent-move variant
- [[sandbox-mode]] — tournament sandbox after guided play
- [[role-as-system]] — when the player embodies a mechanism, not a strategist
- [[game-theory]] — discipline hub for playable exhibits

## Discovery suggestions

- [ ] Annotated GIF: round history filling → strategy recognition moment
- [ ] Strategy card deck for offline classroom prisoner's dilemma
- [ ] Opponent gallery with win-rate stats after user tournament
- [ ] Anti-pattern callout: quiz labeled "game" with no repeated decisions
