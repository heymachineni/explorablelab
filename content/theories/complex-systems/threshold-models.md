---
id: "THY-0003"
type: "theory"
slug: "threshold-models"
title: "Threshold Models"
summary: "People join when enough others have joined."
status: "canonical"
wing: "systems"
created: "2026-06-26"
updated: "2026-06-26"
related:
  theories: [standing-ovation, complex-contagion-protest, 1978-granovetter-threshold]
  simulations: {'existing': ['parable-of-polygons']}
explorable:
  verdict: "essential"
  best_medium: "web-simulation"
  best_medium_stars: 4
---

# Threshold Models

> **One-line essence:** Individual action often depends on how many others have already acted — and small threshold shifts can flip entire populations.

## Why this matters

Why does a lecture hall suddenly erupt in applause? Why do protests go from zero to massive? Why do technologies tip? Threshold models capture a simple social fact: **many behaviors require social proof before people participate**. The same population with slightly different thresholds can produce radically different collective outcomes — making these models central to riots, strikes, vaccination, and cultural fads.

## Core idea

Each person *i* has a **threshold** τᵢ: the minimum fraction (or count) of others who must adopt a behavior before *i* joins. Granovetter's formulation treats thresholds as heterogeneously distributed across a population. When early adopters with low thresholds act, they raise the observed adoption rate, triggering the next tier — a **cascade** through the threshold ladder.

The model is deliberately minimal: no explicit payoff matrix, just "I act when enough others have." That minimalism is its strength — it isolates **interdependent decision-making** from other motives like ideology or material incentive.

## Mechanism

1. **Population** with thresholds drawn from a distribution (often assumed known or estimated).
2. **Initial adopters** — people with τ = 0 or very low τ act first (or are seeded).
3. **Observed fraction** of adopters updates after each round.
4. **Activation rule:** agent *i* adopts when (adopters in *i*'s reference group) / (group size) ≥ τᵢ.
5. **Cascade** continues until no new activations occur or everyone has adopted.

On networks, **who observes whom** matters as much as thresholds. A hub with low threshold can ignite a wide cascade; clustered low-threshold agents can trigger local bursts that fail to globalize.

## Formal sketch

Population of size *N* with thresholds {τ₁, …, τ<sub>N</sub>}. At time *t*, fraction *p*<sub>t</sub> have adopted. Agent *i* activates at the smallest *t* such that *p*<sub>t</sub> ≥ τᵢ (global threshold model) or such that the fraction among *i*'s neighbors exceeds τᵢ (local threshold model). A **cascade** occurs when the final adopter set is much larger than the initial seed set. The **expected cascade size** depends on the threshold distribution's shape — uniform, normal, or bimodal — and on network degree distribution.

## Implications

- **The same preferences, different history.** Identical threshold distributions can yield full adoption or none depending on seeding and network structure.
- **Tipping points are real but not magic.** A "tip" is often a critical mass crossing the next rung of thresholds — not a mysterious phase change unrelated to micro-heterogeneity.
- **Interventions target seeds and visibility.** Influencers, early adopters, and public signals change observed fractions — shifting who crosses their threshold when.
- **Relation to other models.** Threshold models connect to [[schelling-segregation]] (move when unhappy fraction exceeds *T*), [[complex-contagion]] (multiple exposures), and [[information-cascades]] (inferring state from others' actions).

## Common misconceptions

| Wrong | Right |
|-------|-------|
| Threshold = personal preference strength | Threshold is *when* you act given others' actions, not *how much* you want the outcome |
| Cascades require irrationality | Perfectly rational agents with private uncertainty can behave like threshold actors |
| One rebel starts every revolution | Seed placement and network position determine whether low-threshold actors connect |
| Homogeneous thresholds predict smooth adoption | Identical τ can still tip sharply if adoption is all-or-nothing per person |

## Related

- [[1978-granovetter-threshold]] · [[standing-ovation]] · [[complex-contagion]]
- [[information-cascades]] · [[schelling-segregation]] · [[emergence]]
- [[complex-contagion-protest]] · [[wisdom-and-madness-of-crowds]]

## Further reading

- Granovetter, M. (1978). Threshold models of collective behavior. *American Journal of Sociology*, 83(6), 1420–1443.
- Watts, D. J. (2002). A simple model of global cascades on random networks. *PNAS*, 99(9), 5766–5771.
- Centola, D., & Macy, M. (2007). Complex contagions and the weakness of long ties. *American Journal of Sociology*, 113(3), 702–734.

## Discovery suggestions

### Missing pages to create
- [ ] [[1978-granovetter-threshold]] — PAP anchor
- [ ] [[standing-ovation-threshold]] — SIM cousin to Schelling

### Potential simulations
- **Threshold Cascade Lab** — tune distribution, seeds, network — priority: 9.0

### Cross-disciplinary links
- [[network-science]] — global cascades on random graphs
- [[political-science]] — protest mobilization
