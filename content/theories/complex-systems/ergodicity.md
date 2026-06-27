---
id: "THY-0009"
type: "theory"
slug: "ergodicity"
title: "Ergodicity"
summary: "The ensemble average is not your average experience."
status: "canonical"
wing: "intuition"
created: "2026-06-26"
updated: "2026-06-26"
related:
  theories: [ergodicity-street, ergodic-inequality, st-petersburg-paradox]
  simulations: {'existing': ['parable-of-polygons']}
explorable:
  verdict: "essential"
  best_medium: "web-simulation"
  best_medium_stars: 4
---

# Ergodicity

> **One-line essence:** For many real-world processes, the average across many people at one moment differs from what one person experiences over time — and conflating the two leads to catastrophic misjudgment.

## Why this matters

Financial advisors cite "average returns." Doctors cite population survival rates. Policy models cite mean outcomes. But **you live one trajectory**, not an ensemble of parallel selves. When volatility compounds — wealth, infection risk, reputation — most individuals experience outcomes far below the arithmetic mean. Ergodicity economics (Peters, 2019) argues that much of economic theory silently assumes ergodicity when reality is **non-ergodic**, systematically mispricing risk and inequality.

## Core idea

A process is **ergodic** when its **time average** (one system evolving over time) equals its **ensemble average** (many copies at one instant). Flip a fair coin: your long-run heads fraction converges to 50%, and the average across many coins at once is 50%. Ergodic.

Now consider **multiplicative growth**: wealth *W*<sub>t+1</sub> = *W*<sub>t</sub> × (1 + *r*<sub>t</sub>), where returns *r*<sub>t</sub> fluctuate. The **ensemble average** *E*[*W*<sub>t</sub>] can grow even when each person's **time-average growth rate** is negative. Most individual trajectories go to zero; a few explode — the mean is pulled up by outliers. That is **non-ergodic**.

The intuitive failure: **"On average, people do well" does not mean "on average, you will do well over your life."**

## Mechanism

1. **Identify the random variable** — wealth, population, error rate.
2. **Ask: is the dynamic additive or multiplicative?** Additive processes (temperature sums) tend toward ergodicity; multiplicative ones (returns, populations, infection) often do not.
3. **Compute time-average growth rate** — geometric mean of per-period factors, not arithmetic mean of returns.
4. **Compare to ensemble average** — if they diverge, policy and intuition based on ensemble statistics mislead.
5. **Absorbing states** — bankruptcy, extinction, and irreversible loss make trajectories **path-dependent**; recovery from ensemble average is not available to the individual who failed.

The St. Petersburg paradox ([[st-petersburg-paradox]]) and Kelly criterion are cousins: expected value can recommend bets that almost surely ruin you.

## Formal sketch

Multiplicative process *W*<sub>t+1</sub> = *W*<sub>t</sub> · *X*<sub>t</sub> with i.i.d. factors *X*<sub>t</sub> > 0. **Ensemble average:** *E*[*W*<sub>t</sub>] = *W*<sub>0</sub> · *E*[*X*]<sup>t</sup>. **Time-average growth rate:** *g* = exp(*E*[ln *X*]) − 1 (by law of large numbers on log increments). Ergodicity requires *g* = *E*[*X*] − 1; for lognormal *X*, *E*[*X*] > exp(*E*[ln *X*]) — ensemble exceeds time average. Most trajectories follow *g*; the mean is dominated by rare explosive paths.

## Implications

- **Investment and insurance.** Arithmetic mean return overstates typical investor experience; log-utility and time-average frameworks differ systematically.
- **Inequality.** Non-ergodic wealth dynamics generate heavy tails even with identical ex-ante agents — luck compounds ([[ergodic-inequality]]).
- **Public health.** Population averages mask individual trajectories through repeated exposure (non-ergodic infection paths).
- **Policy evaluation.** GDP per capita can rise while median experienced welfare falls when volatility and multiplicative shocks dominate.
- **Survivorship bias.** Observing only ensemble survivors at time *t* hides the trajectories that already failed.

## Common misconceptions

| Wrong | Right |
|-------|-------|
| Expected value is what you'll probably get | Expected value weights all outcomes; multiplicative dynamics make the median trajectory differ from the mean |
| Ergodicity is a niche mathematical concept | It distinguishes "average person" from "person's average" — a practical distinction in finance and risk |
| High average return means a strategy is good for you | Negative time-average growth with positive ensemble mean is possible (volatility pumping) |
| Ergodicity only applies to physics | Peters and others apply it to economics; the logic applies wherever multiplicative noise meets path dependence |

## Related

- [[ergodicity-street]] · [[ergodic-inequality]] · [[st-petersburg-paradox]]
- [[fat-tail-farm]] · [[feedback-loops]] · [[goodharts-law]]
- [[percolation]] · [[emergence]]

## Further reading

- Peters, O. (2019). The ergodicity problem in economics. *Nature Physics*, 15(12), 1216–1221.
- von Neumann, J., & Morgenstern, O. (1944). *Theory of Games and Economic Behavior*. Princeton University Press.
- Ole Peters & M. Gell-Mann (2016). Evaluating gambles using dynamics. *Chaos*, 26(2), 023103.
- Bouchaud, J.-P. (2017). Wealth condensation in a simple model of economy. *Physica A* (illustrative multiplicative dynamics).

## Discovery suggestions

### Missing pages to create
- [ ] [[time-average-vs-ensemble-average]] — glossary anchor
- [ ] [[kelly-criterion]] — optimal sizing under multiplicative dynamics

### Potential simulations
- **Ergodicity Street** — parallel coins vs one coin over time — priority: 9.0

### Cross-disciplinary links
- [[probability]] — stochastic processes
- [[economics]] — expected utility critiques
