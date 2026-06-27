---
id: "PAT-0004"
type: "interaction-pattern"
slug: "but-chain"
title: "BUT-Chain"
summary: "Yes… but… therefore… narrative ladder."
status: "canonical"
wing: "design"
created: "2026-06-26"
updated: "2026-06-26"
related:
  design: {'patterns': ['evolution-of-trust', 'we-become-what-we-behold']}
explorable:
  verdict: "essential"
  best_medium: "web-simulation"
  best_medium_stars: 4
---

# BUT-Chain

> **One-line essence:** Yes… but… therefore… — each beat concedes a truth, adds a constraint, and forces the next conclusion.

## What it is

The BUT-chain is a narrative interaction pattern borrowed from improv comedy (the "Yes, And" inverted into structured argument). Each chapter of an explorable follows a rhetorical ladder:

- **Yes** — grant the learner's intuition or a plausible premise
- **But** — introduce a complication the intuition ignored
- **Therefore** — derive the next mechanism, simulation stage, or policy implication

The chain carries learners through counterintuitive territory without feeling lectured. Every "but" feels like a fair objection; every "therefore" feels earned.

## When to use it

Use BUT-chains when the target concept requires **sequential belief revision** — game theory, evolutionary dynamics, media feedback loops, any topic where the naive story is almost right and dangerously incomplete.

Ideal when:

- Stopping at the first intuitive answer would mislead (cooperation is rational → but repeated games → therefore tit-for-tat)
- Each simulation chapter maps to one link in the chain
- Emotional pacing matters — hope, setback, revised hope ([[innocence-horror-hope]])

Avoid when the idea is a single-shot paradox (use [[predict-then-reveal]]) or a spatial parameter sweep (use [[parameter-slider]]).

## How it works in an explorable

1. **Chapter opens with agreement** — "Trust seems fragile. One betrayal and it's over."
2. **Interactive beat tests the premise** — one-shot prisoner's dilemma; defection wins
3. **But pivot** — "Except people meet again."
4. **New simulation layer** — iterated game; different dominant strategy
5. **Therefore bridge** — "Reputation becomes valuable."
6. **Repeat** until the full model is assembled

Each link should be **playable**, not just readable. The "but" lands harder when the learner just experienced the previous "yes."

## Design notes

- **Name the structure lightly.** Learners don't need "BUT-chain" on screen — they need the rhythm.
- **One complication per chapter.** Stacking three "buts" before a "therefore" loses the thread.
- **Let interaction deliver the therefore.** The simulation outcome should feel like discovery, not caption.
- **End on open therefore when appropriate.** Not every chain resolves to comfort; some end on "therefore we still disagree."
- **Visual continuity** — same characters, grid, or payoff matrix across links so the chain feels like one world evolving.
- **See also [[but-chain-narrative]]** for the storytelling-structure variant with explicit beat labels.

## Anti-patterns

- **Strawman yes** — conceding a position nobody holds breaks trust in the narrator
- **But without play** — telling the complication instead of simulating it
- **Therefore as lecture** — paragraph of moralizing after the user already got the point
- **Broken chain** — chapter three resets the world without connecting to chapter two
- **Infinite regress** — chains without terminal insight feel like moving goalposts

## Examples in our corpus

- [[evolution-of-trust]] — one-shot → repeated → noise → population; each chapter revises the last conclusion
- [[we-become-what-we-behold]] — harmless photo → viral moment → mob dynamics; narrative therefores as headlines
- [[but-chain-narrative]] — design doc mapping yes/but/therefore beats to exhibit chapters
- [[innocence-horror-hope]] — emotional variant: fair world → consequence → possible repair
- [[krebs-cycle-of-outrage]] — each loop adds a "but social media changed the incentive"

## Related

- [[innocence-horror-hope]] — emotional pacing parallel to logical BUT-chain
- [[but-chain-narrative]] — explicit storytelling structure
- [[playable-game]] — games deliver therefores through felt stakes
- [[predict-then-reveal]] — single-beat version when one reversal suffices
- [[ladder-of-abstraction]] — orthogonal axis: power increases; BUT-chain adds belief revision

## Discovery suggestions

- [ ] Annotated storyboard: yes/but/therefore labels on [[evolution-of-trust]] chapter timeline
- [ ] Writer's template: blank BUT-chain worksheet for new exhibit pitches
- [ ] Anti-pattern reel: exhibits that skip "but" and jump straight to moral
- [ ] Classroom exercise: students write the chain before playing the sim
