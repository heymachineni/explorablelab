---
id: "THY-0006"
type: "theory"
slug: "goodharts-law"
title: "Goodhart's Law"
summary: "When a measure becomes a target, it ceases to be a good measure."
status: "canonical"
wing: "systems"
created: "2026-06-26"
updated: "2026-06-26"
related:
  theories: [goodhart-school, metric-hydra, cobra-farm]
  simulations: {'existing': ['parable-of-polygons']}
explorable:
  verdict: "essential"
  best_medium: "web-simulation"
  best_medium_stars: 4
---

# Goodhart's Law

> **One-line essence:** Once a metric is used to control a system, people optimize the metric — and the metric stops tracking what you actually care about.

## Why this matters

Schools teach to the test. Hospitals avoid sick patients to improve mortality scores. Platforms maximize engagement while degrading well-being. **Goodhart's Law** names a structural failure mode of governance: any proxy pressed into service as a target becomes corrupted. Understanding it is prerequisite to designing metrics, incentives, and algorithmic objectives that do not backfire.

## Core idea

Charles Goodhart, a Bank of England economist, observed in 1975 that **any observed statistical regularity will tend to collapse once pressure is placed upon it for control purposes**. The logic is straightforward:

1. You care about goal *G* (learning, health, trust).
2. *G* is hard to measure, so you track proxy *M* (test scores, readmission rates, click-through).
3. *M* correlates with *G* when nobody is gaming it.
4. Rewards and penalties attach to *M*.
5. Agents optimize *M* through paths that weaken or invert the *M* → *G* link.

The law is not cynicism about measurement — it is a warning about **closed feedback loops** between measurement and behavior ([[feedback-loops]]).

## Mechanism

1. **Proxy selection** — choose *M* because it correlated with *G* historically.
2. **Incentive coupling** — budgets, careers, rankings, or algorithms weight *M*.
3. **Strategic response** — actors split effort between improving *G* and improving *M* cheaply.
4. **Goodhart collapse** — correlation breaks; *M* rises while *G* stagnates or falls.
5. **Campbell's Law variant** — social indicators used for social decision-making distort the processes they monitor (Campbell, 1979).

Multiple metrics (metric hydra) and rotating targets delay but rarely eliminate gaming. The deeper issue is **substitution**: proxies are never identical to goals.

## Formal sketch

Let true goal *G* and proxy *M*, historically correlated: Cov(*G*, *M*) > 0 under observational regime. After incentive π(*M*) attaches rewards to *M*, agents choose action *a* to maximize π(*M*(*a*)) + private benefit. **Goodhart collapse** occurs when ∂*G*/∂*M* changes sign or → 0 under optimization — the proxy decouples from the goal. Manheim & Garrabrant (2018) categorize variants: regressional, causal, and adversarial Goodhart.

## Implications

- **Measure outcomes, not only outputs** — but accept that even outcomes can be gamed at scale.
- **Use metrics for diagnosis, not sole judgment** — combine with audits, spot checks, and qualitative review.
- **Preserve slack and diversity** — homogenous optimization pressure on one *M* accelerates collapse.
- **Algorithmic alignment** — recommendation systems that optimize engagement inherit Goodhart dynamics at civilization scale ([[we-become-what-we-behold]]).
- **Historical caution** — the cobra effect ([[cobra-farm]]): bounties for dead cobras incentivized cobra breeding.

## Common misconceptions

| Wrong | Right |
|-------|-------|
| Goodhart means "never measure" | Measure carefully, with multiple signals and awareness of gaming |
| Only bad actors cause distortion | Rational agents respond to incentives; distortion is structural |
| Adding more metrics always helps | Multiple targets create [[metric-hydra]] — tradeoffs and new gaming surfaces |
| The law applies only to economics | Any institution with targets — schools, medicine, ML — is vulnerable |

## Related

- [[goodhart-school]] · [[metric-hydra]] · [[cobra-farm]]
- [[feedback-loops]] · [[p-hacking-lab]] · [[social-choice]]
- [[ostrom-commons-design]] · [[evolution-of-trust]]

## Further reading

- Goodhart, C. A. E. (1975). Problems of monetary management: The U.K. experience. In *Papers in Monetary Economics*. Reserve Bank of Australia.
- Campbell, D. T. (1979). Assessing the impact of planned social change. *Evaluation and Program Planning*, 2(2), 67–90.
- Manheim, D., & Garrabrant, S. (2018). Categorizing variants of Goodhart's Law. *arXiv:1803.04585*.
- Mullainathan, S., & Obermeyer, Z. (2022). Diagnosing physician error: A machine learning approach to low-value health care. *Quarterly Journal of Economics* (illustrative medical Goodhart).

## Discovery suggestions

### Missing pages to create
- [ ] [[campbells-law]] — social-science parallel citation
- [ ] [[cobra-farm]] — historical parable exhibit

### Potential simulations
- **Goodhart School** — raise test prep, watch learning flatline — priority: 9.0

### Cross-disciplinary links
- [[economics]] — monetary targeting
- [[machine-learning]] — reward hacking and specification gaming
