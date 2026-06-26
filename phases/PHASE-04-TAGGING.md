# Phase 4 — Tagging System ✅

**Status:** Complete  
**Location:** [`meta/taxonomy/`](../meta/taxonomy/)

## Taxonomy layers

| Layer | File | Usage in frontmatter |
|-------|------|---------------------|
| **Field** | fields.yaml | `fields: [complex-systems]` max 3 |
| **Subfield** | subfields.yaml | `subfields: [agent-based-modeling]` |
| **Difficulty** | difficulty.yaml | `difficulty: introductory` |
| **Era** | eras.yaml | `era: [1960s, 1970s]` |
| **Application** | applications.yaml | `applications: [urban-planning]` |
| **Simulation type** | simulation-types.yaml | `simulation_type: agent-based` |
| **Math foundation** | math-foundations.yaml | `math: [probability, graph-theory]` |
| **Visualizability** | visualizability.yaml | `visualizability: high` |
| **Free tags** | tag-registry.md | `tags: [emergence]` registered only |

## Anti-duplication rules

1. **Register before use** — PR must update tag-registry.md  
2. **Singular nouns** — `network` not `networks`  
3. **US spelling** — `behavior`, `modeling`  
4. **Prefer field over vague tag** — use subfield `bayesian-inference` not `hard`  
5. **Deprecated table** — old → new mapping in tag-registry.md  
6. **Max 12 tags** per page  
7. **Max 3 fields** per page  

## Difficulty enum

| Value | Audience |
|-------|----------|
| introductory | Curious 14+; no prereqs |
| intermediate | Some math or prior concepts |
| advanced | Undergraduate major level |
| research | Graduate / specialist |

## Visualizability enum

| Value | Meaning |
|-------|---------|
| none | Purely abstract |
| low | Static diagram only |
| medium | Animated or simple interact |
| high | Dynamic simulation natural |
| essential | Meaningless without visual |

## Interaction pattern tags

Link to PAT pages — do **not** duplicate as free tags:

- ✗ `tag: sandbox`
- ✓ `related.design.patterns: [sandbox-mode]`

## Scaling

When tag-registry exceeds **500 entries**, shard:

```
meta/taxonomy/tags/
├── core.md
├── a-f.md
└── ...
```

→ [Phase 5 — Scoring](PHASE-05-SCORING.md)
