---
id: "THY-0012"
type: "theory"
slug: "iterated-prisoners-dilemma"
title: "Iterated Prisoner's Dilemma"
summary: "One-shot defection; repeated cooperation."
status: "canonical"
wing: "systems"
created: "2026-06-26"
updated: "2026-06-26"
related:
  theories: [prisoners-dilemma, prisoners-dilemma-tournament, evolution-of-trust]
  simulations: {'existing': []}
explorable:
  verdict: "essential"
  best_medium: "web-simulation"
  best_medium_stars: 4
---

# Iterated Prisoner's Dilemma

> **One-line essence:** When the Prisoner's Dilemma is played repeatedly, cooperation can emerge from self-interest — but only under strategies that reward reciprocity and punish defection.

## Why this matters

The one-shot Prisoner's Dilemma says mutual defection is the rational outcome even when both players prefer mutual cooperation. Yet real relationships — business partnerships, international treaties, neighborhood norms, open-source communities — are **repeated**. The iterated game transforms the logic: today's defection costs tomorrow's trust. Robert Axelrod's tournaments showed that simple reciprocal strategies can outperform naive altruism and pure exploitation, offering a rigorous foundation for how cooperation evolves without central enforcement.

## Core idea

In the **Prisoner's Dilemma**, two players each choose Cooperate (C) or Defect (D). Payoffs satisfy: mutual cooperation beats mutual defection (R > P), but unilateral defection beats being exploited (T > R), and mutual defection beats being suckered (P > S). The one-shot Nash equilibrium is (D, D) — worse for both than (C, C).

**Iteration** changes the strategic space. Players can condition current moves on history. **Future shadow of the interaction** — the expected value of continued cooperation — can make C rational today. The Folk Theorem guarantees that if players are patient enough (discount factor δ high enough), **many outcomes including mutual cooperation** can be sustained as equilibria in infinitely repeated games.

## Mechanism

1. **Stage game** — each round, both choose C or D; payoffs follow the PD ordering T > R > P > S.
2. **History** — in round *t*, strategies can depend on all prior moves.
3. **Discounting** — future payoffs weighted by δ ∈ (0, 1]; cooperation requires δ above a threshold depending on payoffs.
4. **Reciprocity strategies** — e.g. **Tit-for-Tat** (TFT): start C, then copy opponent's last move.
5. **Tournament dynamics** — Axelrod (1980, 1984) ran open competitions; TFT won by being **nice**, **provokable**, **forgiving**, and **clear**.
6. **Evolution** — in populations with mutation and selection, cooperative strategies can invade and persist.

Key repeated-game strategies include Grim Trigger, Win-Stay Lose-Shift, and generous TFT.

## Formal sketch

Stage payoffs: *R* (both C), *T* (unilateral D), *S* (suckered), *P* (both D), with *T* > *R* > *P* > *S*. Discount factor δ. **Grim Trigger** sustains (C, C) if δ ≥ (*T* − *R*)/(*T* − *P*). **Folk Theorem:** for δ sufficiently close to 1, any feasible individually rational payoff vector can be a subgame-perfect equilibrium outcome.

## Implications

- **Cooperation does not require altruism.** Self-interested agents cooperate when reputation, retaliation, and repeated contact make it pay.
- **Shadow of the future is fragile.** Short horizons, anonymous interaction, or high temptation T collapse cooperation — relevant to [[ostrom-commons-design]].
- **Noise matters.** Overly punitive strategies can spiral into permanent defection; forgiveness helps.
- **Population structure.** Spatial and network structure shapes which strategies evolve.

## Common misconceptions

| Wrong | Right |
|-------|-------|
| TFT is always optimal | TFT succeeds in Axelrod's setup but loses to noise and to strategies that exploit its niceness |
| Repeated games always produce cooperation | Low δ, short horizons, or anonymous matching restore defection logic |
| Cooperation means players are friends | Reciprocal cooperation is equilibrium behavior among rational egoists |
| Defection in round 1 is always rational | If shadow of future is long enough, opening with C can be equilibrium |

## Related

- [[prisoners-dilemma]] · [[prisoners-dilemma-tournament]] · [[evolution-of-trust]]
- [[ostrom-commons-design]] · [[social-choice]] · [[feedback-loops]]

## Further reading

- Axelrod, R. (1984). *The Evolution of Cooperation*. Basic Books.
- Axelrod, R., & Hamilton, W. D. (1981). The evolution of cooperation. *Science*, 211(4489), 1390–1396.
- Rapoport, A., & Chammah, A. M. (1965). *Prisoner's Dilemma*. University of Michigan Press.
- Fudenberg, D., & Maskin, E. (1986). The Folk Theorem in repeated games with discounting or with incomplete information. *Econometrica*, 54(3), 533–554.

## Discovery suggestions

- [ ] [[prisoners-dilemma-tournament]] — SIM replicating Axelrod setup
- [ ] [[folk-theorem]] — formal anchor for repeated games
