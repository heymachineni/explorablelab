---
id: "THY-0011"
type: "theory"
slug: "information-cascades"
title: "Information Cascades"
summary: "Follow the crowd; ignore private signal."
status: "canonical"
wing: "networks"
created: "2026-06-26"
updated: "2026-06-26"
related:
  theories: [information-cascade-falls, wisdom-and-madness-of-crowds, majority-illusion]
  simulations: {'existing': ['parable-of-polygons']}
explorable:
  verdict: "essential"
  best_medium: "web-simulation"
  best_medium_stars: 4
---

# Information Cascades

> **One-line essence:** Rational observers can ignore their own private information and follow earlier actors — producing herds that may be wrong yet self-reinforcing.

## Why this matters

Restaurant lines, stock bubbles, academic bandwagons, and viral misinformation share a pattern: people choose based on what others chose, not only on private evidence. **Information cascades** show this herding can be **Bayesian-rational** — not stupidity, but inference under uncertainty when others' actions embed information you lack. Once a cascade starts, later actors add no new information; the crowd looks unanimous while being fragile.

## Core idea

Agents decide in sequence. Each receives a **private signal** about which option is better (say, restaurant *A* or *B*), plus observes all prior choices. Early movers reveal their signals through action. Later movers, whose private signals are weak or ambiguous, rationally **follow the majority** — their small private doubt is outweighed by accumulated public history.

At some point, **everyone ignores private information**. The cascade is **informationally inefficient**: social learning stops even though many agents still hold contrary private signals. Bikhchandani, Hirshleifer, and Welch (1992) formalized this; Banerjee (1992) independently developed related herding models.

## Mechanism

1. **Sequential decision** — agents act one at a time (or in visible order).
2. **Private signal** — each agent gets imperfect information about state *θ* (good vs bad restaurant).
3. **Public history** — all prior choices are observable.
4. **Bayesian update** — combine private signal with inferred information from history.
5. **Cascade trigger** — when public history is strong enough, private signal is never pivotal; agent follows herd.
6. **Information blockage** — subsequent agents add no new data; cascade persists even if *θ* is opposite.

**Reverse cascades** are hard: one dissenter rarely overturns a long public record because their deviation looks like noise. **Breakdown** requires visible private signals strong enough, or exogenous shocks to public beliefs.

## Formal sketch

Agents *i* = 1, …, *n* decide in order. True state *θ* ∈ {0, 1} with prior *P*(*θ* = 1) = ½. Private signal *s*<sub>i</sub> ∈ {0, 1} with *P*(*s*<sub>i</sub> = *θ*) = *q* > ½. Agent *i* observes history *H*<sub>i</sub> = (*a*<sub>1</sub>, …, *a*<sub>i−1</sub>) and chooses *a*<sub>i</sub> to maximize *P*(*θ* | *s*<sub>i</sub>, *H*<sub>i</sub>). A **cascade** on action 1 begins at *i*<sup>*</sup> when *a*<sub>i</sub> = 1 for all *i* ≥ *i*<sup>*</sup> regardless of *s*<sub>i</sub> — private information is thereafter unused.

## Implications

- **Unanimity ≠ correctness.** Long queues and consensus forecasts may reflect cascades, not wisdom ([[wisdom-and-madness-of-crowds]]).
- **First movers matter disproportionately.** Early choices carry outsize weight — seeding and launch dynamics shape equilibria.
- **Silence is informative.** In many settings, not acting also signals; cascades can form around inaction.
- **Social media amplifies visibility.** Algorithmic ranking makes public history salient, lowering the threshold to cascade ([[majority-illusion]]).
- **Contrast with complex contagion.** [[complex-contagion]] requires multiple exposures for *willingness*; cascades require sequential inference about *hidden quality*.

## Common misconceptions

| Wrong | Right |
|-------|-------|
| Herding is always irrational | Cascades can be fully rational given others' actions contain information |
| Cascades mean people have no private info | Agents often retain contrary signals but rationally override them |
| More participants improve accuracy | After cascade onset, additional participants add no information |
| Only fads and finance cascade | Hiring, publishing, technology adoption, and medical practice all show herding |

## Related

- [[information-cascade-falls]] · [[wisdom-and-madness-of-crowds]] · [[majority-illusion]]
- [[complex-contagion]] · [[threshold-models]] · [[we-become-what-we-behold]]
- [[social-choice]] · [[goodharts-law]] · [[feedback-loops]]

## Further reading

- Bikhchandani, S., Hirshleifer, D., & Welch, I. (1992). A theory of fads, fashion, custom, and cultural change as informational cascades. *Journal of Political Economy*, 100(5), 992–1026.
- Banerjee, A. V. (1992). A simple model of herd behavior. *Quarterly Journal of Economics*, 107(3), 797–817.
- Anderson, L. R., & Holt, C. A. (1997). Information cascades in the laboratory. *American Economic Review*, 87(5), 847–862.
- Surowiecki, J. (2004). *The Wisdom of Crowds*. Doubleday. (conditions when crowds aggregate well vs cascade)

## Discovery suggestions

### Missing pages to create
- [ ] [[1992-bikhchandani-cascade]] — PAP anchor
- [ ] [[herd-behavior-banerjee]] — parallel formalization

### Potential simulations
- **Information Cascade Falls** — watch rational agents walk off the cliff — priority: 9.0

### Cross-disciplinary links
- [[economics]] — financial herding
- [[network-science]] — visibility and majority illusion
