---
id: "THY-0005"
type: "theory"
slug: "percolation"
title: "Percolation"
summary: "Connectivity jumps at a critical point."
status: "canonical"
wing: "systems"
created: "2026-06-26"
updated: "2026-06-26"
related:
  theories: [percolation-city, urban-percolation-equity, braess-roads]
  simulations: {'existing': ['parable-of-polygons']}
explorable:
  verdict: "essential"
  best_medium: "web-simulation"
  best_medium_stars: 4
---

# Percolation

> **One-line essence:** Randomly opening or closing links in a network produces a sharp transition — below a critical point, fragments; above it, a giant connected component spans the system.

## Why this matters

When does an epidemic become a pandemic? When does a city become navigable by car? When does misinformation cross from fringe to mainstream? **Percolation theory** shows that connectivity often does not grow smoothly — it **jumps** at a critical threshold. Near that threshold, the system is fragile: removing a few bridges or adding a few shortcuts can flip global reachability.

## Core idea

Consider a lattice or network where each edge (or site) is **open** with probability *p* and **closed** with probability 1 − *p*, independently. For low *p*, open clusters are small and isolated. As *p* increases, clusters merge. At a **critical probability** *p*<sub>c</sub>, a **giant component** — spanning a fraction of the system — appears abruptly. This is a **phase transition**, analogous to water freezing: quantitative change in *p* produces qualitative change in connectivity.

Bond percolation opens edges; site percolation opens nodes. Both exhibit universal features near *p*<sub>c</sub>: fractal clusters, power-law size distributions, and extreme sensitivity to local defects.

## Mechanism

1. **Start** with a graph (grid, random graph, road network).
2. **Randomly activate** edges or nodes with probability *p*.
3. **Identify connected components** among open elements.
4. **Track** the size *S*<sub>max</sub> of the largest component as *p* varies.
5. **Observe** that *S*<sub>max</sub>/N (fraction of nodes in the giant cluster) goes from ~0 to ~1 around *p*<sub>c</sub>.

On a 2D square lattice, bond percolation has *p*<sub>c</sub> ≈ 0.593. On Erdős–Rényi random graphs with *N* nodes, the threshold occurs near average degree 1: when *p* ≈ 1/*N*, the giant component emerges.

## Formal sketch

Let *G* = (*V*, *E*) be a graph. Each edge is open independently with probability *p*. Define *C*<sub>max</sub>(*p*) as the size of the largest connected component of open edges. The **percolation threshold** *p*<sub>c</sub> satisfies: for *p* < *p*<sub>c</sub>, *C*<sub>max</sub>/*N* → 0 as *N* → ∞; for *p* > *p*<sub>c</sub>, *C*<sub>max</sub>/*N* → *θ* > 0. Near *p*<sub>c</sub>, cluster sizes follow a power law — the hallmark of a second-order phase transition.

## Implications

- **Infrastructure fragility.** Road networks, power grids, and supply chains near *p*<sub>c</sub> lose global function from localized failures — relevant to [[braess-roads]] paradox and urban access ([[urban-percolation-equity]]).
- **Epidemic thresholds.** Disease spread on networks has a percolation-like threshold: below critical transmissibility, outbreaks die; above it, they reach macroscopic scale.
- **Segregation and isolation.** [[schelling-segregation]] can reduce effective *p* across group boundaries, fragmenting social percolation even when local density seems adequate.
- **Criticality is double-edged.** At *p*<sub>c</sub>, both connectivity and vulnerability peak — small additions or deletions have outsized effects.

## Common misconceptions

| Wrong | Right |
|-------|-------|
| Connectivity grows linearly with links added | The giant component often appears suddenly near *p*<sub>c</sub> |
| Removing random roads always degrades traffic smoothly | Near criticality, targeted or random cuts can disconnect abruptly |
| Percolation is only about physical lattices | Any graph with random activation — social ties, hyperlinks, neurons — percolates |
| Above *p*<sub>c</sub>, the network is uniform | A giant component coexists with many small clusters; structure is heterogeneous |

## Related

- [[percolation-city]] · [[urban-percolation-equity]] · [[braess-roads]]
- [[schelling-segregation]] · [[complex-contagion]] · [[emergence]]
- [[network-science]] · [[sandpile-avalanche]]

## Further reading

- Stauffer, D., & Aharony, A. (1994). *Introduction to Percolation Theory* (2nd ed.). Taylor & Francis.
- Broadbent, S. R., & Hammersley, J. M. (1957). Percolation processes I. *Mathematical Proceedings of the Cambridge Philosophical Society*, 53(3), 629–641.
- Newman, M. E. J. (2010). *Networks: An Introduction*. Oxford University Press, Ch. 8.

## Discovery suggestions

### Missing pages to create
- [ ] [[urban-percolation-equity]] — PHN linking segregation × access
- [ ] [[epidemic-threshold]] — SIR on networks bridge

### Potential simulations
- **Percolation City** — toggle roads, watch giant component — priority: 9.0

### Cross-disciplinary links
- [[network-science]] — giant component in random graphs
- [[epidemiology]] — outbreak thresholds
