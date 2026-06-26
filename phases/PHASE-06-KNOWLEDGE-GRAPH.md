# Phase 6 — Knowledge Graph ✅

**Status:** Complete  
**Schema:** [`meta/graph/schema.md`](../meta/graph/schema.md)  
**Master MOC:** [`indices/maps-of-content/master-graph.md`](../indices/maps-of-content/master-graph.md)

## Layer model

```
L6  Navigation     DIS · indices · MOCs
L5  Canon          EXE (finished explorables)
L4  Applied        SIM · PRO
L3  Design vocab   PAT · MET · STR · MED
L2  Ideas          THY · PAR · PHN · MOD
L1  People         SCI · DSN · ORG
L0  Evidence       PAP · BOK · NOB · EXP · EVT
```

## Edge flow (primary)

```
People → Papers → Theories → Paradoxes
                    ↓
              Experiments → Phenomena
                    ↓
              Books (popularize)
                    ↓
         Visual Metaphors · Interaction Patterns · Story Structures
                    ↓
              Simulation Concepts → Prototypes
                    ↓
              Existing Explorables (EXE)
```

## Hub nodes (high connectivity)

| Hub | Type | Purpose |
|-----|------|---------|
| complex-systems | DIS | ABM, emergence |
| game-theory | DIS | Cooperation, mechanism design |
| probability-statistics | DIS | Bayes, ergodicity |
| explorable-explanations | DIS | Meta discipline |
| agent-placement | PAT | Pattern vocabulary |
| sandbox-mode | PAT | Pattern vocabulary |
| schelling-segregation | THY | Most linked social THY |
| parable-of-polygons | EXE | Canon reference |

## Graph statistics (seed corpus)

Run: `python3 scripts/validate-frontmatter.py --stats`

## Viewer implementation (future)

1. Parse all YAML frontmatter `related:`
2. Parse `graph/edges/*.md`
3. Build adjacency list
4. Render force-directed or layered (D3, sigma.js)

No database — build index at static site compile time.

→ [Phase 7 — Missing Categories](PHASE-07-DISCIPLINES.md)
