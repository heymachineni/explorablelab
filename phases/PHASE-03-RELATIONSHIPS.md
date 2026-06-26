# Phase 3 — Relationships ✅

**Status:** Complete  
**Spec:** [`meta/graph/schema.md`](../meta/graph/schema.md) · [`meta/graph/edge-types.md`](../meta/graph/edge-types.md) · [`meta/graph/relationships.md`](../meta/graph/relationships.md)

## Three linking layers

| Layer | Mechanism | Machine-readable |
|-------|-----------|------------------|
| 1 | `related:` in YAML frontmatter | ✅ |
| 2 | `[[wikilinks]]` in markdown body | Partial |
| 3 | `graph/edges/*.md` annotated edges | ✅ |

## Canonical chain (implemented in corpus)

```
[[thomas-schelling]]           SCI-0001
        │ developed
        ▼
[[schelling-segregation]]      THY-0001
        │ part_of · explains
        ▼
[[emergence]]                  THY-0002
        │ part_of
        ▼
[[complex-systems]]            DIS-0001
        │ instantiates
        ▼
[[agent-placement]]            PAT-0001
        │ uses_metaphor
        ▼
[[neighborhood-grid]]          MET-0001
        │ demonstrates
        ▼
[[parable-of-polygons]]        EXE-0001
        │ proposes (gap)
        ▼
[[standing-ovation-threshold]]   SIM (stub — create next)
```

## Frontmatter `related:` schema

```yaml
related:
  people: [slug]
  theories: [slug]
  papers: [slug]
  books: [slug]
  paradoxes: [slug]
  experiments: [slug]
  mental_models: [slug]
  phenomena: [slug]
  simulations:
    concepts: [slug]
    existing: [slug]
    prototypes: [slug]
  design:
    patterns: [slug]
    metaphors: [slug]
    structures: [slug]
    mediums: [slug]
  disciplines: [slug]
  events: [slug]
```

## Integrity rules

| Rule | Enforcement |
|------|-------------|
| No orphans | ≥2 inbound links before `mature` |
| SIM → THY + PAT | Required |
| EXE → THY + PAT | Required |
| PAP → SCI + (THY or PHN) | Required |
| Broken link | Create `status: stub` same PR |

## Example explicit edge

See [`graph/edges/THY-0001--demonstrates--EXE-0001.md`](../graph/edges/THY-0001--demonstrates--EXE-0001.md)

→ [Phase 4 — Tagging](PHASE-04-TAGGING.md)
