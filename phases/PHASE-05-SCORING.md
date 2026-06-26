# Phase 5 — Scoring Framework ✅

**Status:** Complete  
**Rubric:** [`meta/scoring/rubric.md`](../meta/scoring/rubric.md)  
**Examples:** [`meta/scoring/examples.md`](../meta/scoring/examples.md)

## 15 dimensions (1–10 each)

| # | Dimension | Build priority | Corpus quality |
|---|-----------|----------------|----------------|
| 1 | visual_potential | ✓ | |
| 2 | interaction_potential | ✓ | |
| 3 | educational_value | ✓ | ✓ |
| 4 | surprise | ✓ | |
| 5 | replayability | ✓ | |
| 6 | narrative_potential | ✓ | |
| 7 | beauty | ✓ | |
| 8 | novelty | ✓ (inverted with coverage) | |
| 9 | sandbox_potential | ✓ | |
| 10 | timelessness | ✓ | |
| 11 | virality | ✓ | |
| 12 | existing_coverage | ✓ (lower = build sooner) | |
| 13 | research_quality | | ✓ |
| 14 | citation_strength | | ✓ |
| 15 | cross_disciplinary | ✓ | ✓ |

## Priority formula

```
priority = 0.14×interaction + 0.12×educational + 0.12×surprise
         + 0.10×visual + 0.10×timelessness
         + 0.08×novelty×(1 - existing_coverage/10)
         + 0.08×sandbox + 0.08×cross_disciplinary
         + 0.06×virality + 0.06×narrative + 0.06×research_quality
```

Store as `scores.composite` in frontmatter.

## Tier buckets

| Tier | Composite | Index |
|------|-----------|-------|
| S | ≥ 8.5 | indices/by-score/tier-s.md |
| A | 7.5–8.4 | tier-a.md (create when >10 pages) |
| B | 6.5–7.4 | tier-b.md |
| C | < 6.5 | corpus only |

## Explorable verdict (gate)

| Verdict | Rule |
|---------|------|
| essential | interaction ≥ 8 AND educational ≥ 7 |
| strong | interaction ≥ 6 |
| moderate | visualization / classroom best |
| weak | graph-only stub |
| none | **reject page** |

## Worked example: Schelling segregation

See [`content/theories/complex-systems/schelling-segregation.md`](../content/theories/complex-systems/schelling-segregation.md)

- interaction_potential: **10**
- existing_coverage: **8** (Polygons exists → lower *build* priority, still canonical THY)
- composite: **8.7**
- verdict: **essential**

→ [Phase 6 — Knowledge Graph](PHASE-06-KNOWLEDGE-GRAPH.md)
