---
id: "THY-0010"
type: "theory"
slug: "complex-contagion"
title: "Complex Contagion"
summary: "Some behaviors need multiple exposures to spread."
status: "canonical"
wing: "networks"
created: "2026-06-26"
updated: "2026-06-26"
related:
  theories: [complex-contagion-protest, contagion-of-courage, 2007-centola-complex-contagion]
  simulations: {'existing': ['parable-of-polygons']}
explorable:
  verdict: "essential"
  best_medium: "web-simulation"
  best_medium_stars: 4
---

# Complex Contagion

> **One-line essence:** Unlike simple contagions, many social behaviors require reinforcement from multiple contacts before a person adopts — which makes weak ties and network structure matter in unexpected ways.

## Why this matters

A flu virus spreads from one sneeze. Joining a protest, quitting smoking, or adopting a political identity usually does not. **Complex contagion** captures behaviors where adoption risk increases with the number — or diversity — of adopting neighbors. This distinction explains why some campaigns fizzle despite viral reach, why clustered networks amplify norms, and why Granovetter's "strength of weak ties" fails for behaviors that need social proof.

## Core idea

**Simple contagion:** infection probability from a single exposure is sufficient; more contacts add redundant paths. Models like independent cascade or SIR often assume this.

**Complex contagion:** the probability of adoption is a **nonlinear function** of exposure count. One friend using a product may not convince you; three might. Threshold models ([[threshold-models]]) are one formalization: adopt when adopters in your neighborhood ≥ τ.

Centola and Macy (2007) argue complex contagions arise when behaviors are **costly, risky, or coordination-sensitive** — joining a riot, buying a new technology, coming out, changing pronouns. Multiple exposures provide **social reinforcement**, **credibility**, and **coordination assurance**.

## Mechanism

1. **Agent** observes adopting neighbors in their local network.
2. **Adoption function** *f(k)* maps number of adopting neighbors *k* to adoption probability.
3. **Simple case:** *f*(1) > 0 — one adopter suffices (like a virus).
4. **Complex case:** *f*(1) ≈ 0 but *f*(3) >> 0 — need critical mass locally.
5. **Spread dynamics** differ: complex contagions favor **wide bridges** (clusters connected by multiple ties) over single weak ties; homophilous clusters amplify before global spread.

Experimental work (Centola, 2010) showed health behaviors spreading faster in clustered-lattice topologies than in random networks — opposite to simple contagion predictions.

## Formal sketch

Let *f*(*k*) be adoption probability given *k* adopting neighbors. **Simple contagion:** *f*(1) ≈ *p* > 0 and *f* is concave — redundant exposures add little. **Complex contagion:** *f*(1) ≈ 0, *f* is convex on [0, *k*<sup>*</sup>], then saturates — sub-threshold exposures fail, supra-threshold exposures tip locally. On networks, define **wide bridge** as two nodes connected by ≥ 2 independent paths; complex contagions require wide bridges to cross communities, not single edges.

## Implications

- **Weak ties are not universal bridges.** For complex contagions, a single acquaintance is insufficient; redundant paths across groups matter.
- **Seeding strategy changes.** Target clustered communities with enough density to reach local thresholds, not just high-degree hubs.
- **Visibility and pluralistic ignorance.** If adoption is hidden, neighbors cannot reinforce — behaviors stall despite latent support ([[contagion-of-courage]]).
- **Platform design.** Social proof widgets ("3 friends bought this") exploit complex contagion mechanics — for better or worse.
- **Relation to cascades.** [[information-cascades]] involve inferring hidden states; complex contagion involves **willingness** requiring multiple signals.

## Common misconceptions

| Wrong | Right |
|-------|-------|
| Viral marketing always works like epidemics | Many products and ideas need reinforcement, not one impression |
| More links always speed spread | For complex contagions, topology and cluster density dominate |
| Complex contagion means "complicated topic" | It refers to the adoption *function*, not cognitive difficulty |
| Threshold and complex contagion are unrelated | Threshold models are a standard formalization of complex contagion |

## Related

- [[2007-centola-complex-contagion]] · [[complex-contagion-protest]] · [[contagion-of-courage]]
- [[threshold-models]] · [[information-cascades]] · [[wisdom-and-madness-of-crowds]]
- [[percolation]] · [[emergence]] · [[schelling-segregation]]

## Further reading

- Centola, D., & Macy, M. (2007). Complex contagions and the weakness of long ties. *American Journal of Sociology*, 113(3), 702–734.
- Centola, D. (2010). The spread of behavior in an online social network experiment. *Science*, 329(5996), 1194–1197.
- Granovetter, M. (1973). The strength of weak ties. *American Journal of Sociology*, 78(6), 1360–1380. (contrast case)
- Dodds, P. S., & Watts, D. J. (2004). Universal behavior in a generalized model of contagion. *Physical Review Letters*, 92(21), 218701.

## Discovery suggestions

### Missing pages to create
- [ ] [[2007-centola-complex-contagion]] — PAP anchor
- [ ] [[simple-vs-complex-contagion]] — comparison exhibit

### Potential simulations
- **Complex Contagion Protest** — toggle topology, watch spread stall or tip — priority: 9.0

### Cross-disciplinary links
- [[network-science]] — topology-dependent diffusion
- [[social-psychology]] — pluralistic ignorance
