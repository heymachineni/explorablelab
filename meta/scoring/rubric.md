# Scoring Rubric

Every theory, paradox, phenomenon, and simulation concept should be scored **1–10** per dimension.

## Dimensions

### Explorable potential (prioritize builds)

| Dimension | 1 | 5 | 10 |
|-----------|---|---|-----|
| **visual_potential** | Purely abstract | Diagrammable | Inherently visual dynamic system |
| **interaction_potential** | Reading suffices | Helps to interact | Meaningless without manipulation |
| **surprise** | Obvious | Mildly counter-intuitive | Mind-bending gap vs intuition |
| **replayability** | One-shot | Few variations | Rich sandbox |
| **narrative_potential** | No story | Some arc | Complicity, emotion, BUT-chain |
| **beauty** | Ugly or dry | Clean | Aesthetic experience aids memory |
| **novelty** | Many explorables exist | Some coverage | Empty field |
| **sandbox_potential** | Closed lesson | Limited params | Open-ended user questions |
| **timelessness** | Trendy | decade relevance | Will matter in 20 years |
| **virality** | Niche | Shareable | "Send this to your uncle" |

### Corpus quality (prioritize pages)

| Dimension | 1 | 5 | 10 |
|-----------|---|---|-----|
| **educational_value** | Trivial | Useful | Misunderstanding causes real harm |
| **research_quality** | Pseudoscience | Mixed | Rigorous consensus |
| **citation_strength** | Obscure | Known in field | Canonical textbook/paper |
| **cross_disciplinary** | Siloed | Two fields | Bridges many domains |
| **existing_coverage** | No explorables | Some | Overdone (lower build priority) |

## Priority formula (simulation backlog)

```
priority =
  0.14 * interaction_potential +
  0.12 * educational_value +
  0.12 * surprise +
  0.10 * visual_potential +
  0.10 * timelessness +
  0.08 * novelty * (1 - existing_coverage/10) +
  0.08 * sandbox_potential +
  0.08 * cross_disciplinary +
  0.06 * virality +
  0.06 * narrative_potential +
  0.06 * research_quality
```

Store in frontmatter as `scores.composite` (rounded to 1 decimal) or compute in validation script.

## Explorable verdict

| Verdict | Criteria |
|---------|----------|
| **essential** | interaction_potential ≥ 8 AND educational_value ≥ 7 |
| **strong** | interaction_potential ≥ 6 AND clear sim concept |
| **moderate** | Visualization or classroom activity best |
| **weak** | Mostly text; include only if foundational for graph |
| **none** | Do not add to corpus — belongs on Wikipedia |

## Best medium stars

| Stars | Meaning |
|-------|---------|
| ★★★★★ | Definitive medium; others are inferior |
| ★★★★ | Excellent fit |
| ★★★ | Good fit |
| ★★ | Possible but compromised |
| ★ | Poor fit |
| ☆ | Do not use this medium |

Always pair stars with `best_medium_reason`.

## Tier buckets (for indices)

| Tier | Composite | Action |
|------|-----------|--------|
| **S** | ≥ 8.5 | Flag for simulation studio |
| **A** | 7.5–8.4 | High-priority concept page + SIM stub |
| **B** | 6.5–7.4 | Corpus page; sim when capacity |
| **C** | < 6.5 | Corpus only if graph-critical |

Update [`indices/by-score/`](../indices/by-score/) manually or via script.
