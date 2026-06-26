# Graph Schema

## Node types (17)

| type | prefix | folder |
|------|--------|--------|
| theory | THY | content/theories/ |
| paradox | PAR | content/paradoxes/ |
| phenomenon | PHN | content/phenomena/ |
| mental-model | MOD | content/mental-models/ |
| scientist | SCI | content/people/scientists/ |
| designer | DSN | content/people/designers/ |
| paper | PAP | content/publications/papers/ |
| book | BOK | content/publications/books/ |
| nobel | NOB | content/publications/nobel/ |
| experiment | EXP | content/experiments/ |
| simulation-concept | SIM | content/simulations/concepts/ |
| prototype | PRO | content/simulations/prototypes/ |
| existing-explorable | EXE | content/simulations/existing/ |
| interaction-pattern | PAT | content/design/interaction-patterns/ |
| visual-metaphor | MET | content/design/visual-metaphors/ |
| storytelling-structure | STR | content/design/storytelling-structures/ |
| medium | MED | content/design/mediums/ |
| discipline | DIS | content/disciplines/ |
| event | EVT | content/events/ |

## Edge types (22)

Stored in frontmatter `related:` (typed) or `graph/edges/` (annotated).

| Edge | From | To | Required metadata |
|------|------|-----|-------------------|
| developed | SCI, DSN | THY, PAP | year optional |
| published | SCI | PAP, BOK | role: author |
| introduced | PAP | THY | |
| extends | THY | THY | |
| contradicts | THY | THY | |
| explains | THY | PHN | |
| instantiates | PAT | THY | |
| visualizes | MET | THY | aspect |
| demonstrates | EXE | THY | coverage: 0-100 |
| proposes | SIM | THY | |
| inspired_by | SIM, EXE | EXE, PAP | |
| replicates | EXP | PHN | |
| documents | BOK | THY | chapter optional |
| awarded_for | NOB | THY, PHN | year |
| part_of | THY, PHN | DIS | |
| applies_to | THY | application tag | |
| generalizes | MOD | THY | |
| paradox_of | PAR | THY | |
| cites | PAP | PAP | |
| co_occurs | * | * | weak link |
| uses_pattern | EXE, SIM | PAT | |
| uses_structure | EXE, SIM | STR | |
| uses_metaphor | EXE, SIM | MET | |
| suitable_medium | THY, SIM | MED | stars |

## Layer model

```
L0 Evidence     PAP · EXP · NOB · EVT
L1 People       SCI · DSN · ORG
L2 Ideas        THY · PAR · PHN · MOD
L3 Design vocab PAT · MET · STR · MED
L4 Applied      SIM · PRO
L5 Canon        EXE
L6 Navigation   DIS · indices
```

## Integrity rules

1. **No orphans** — ≥2 inbound links within 90 days of `status: mature`
2. **SIM** → ≥1 THY, ≥1 PAT
3. **EXE** → ≥1 THY, ≥1 PAT listed
4. **PAP** → ≥1 SCI, ≥1 THY or PHN
5. **THY mature** → ≥1 PAP or BOK, ≥1 explorable section filled
6. **Stubs** — allowed with `status: stub` + backlinks only; promote within 180 days or delete

## Wikilink convention

```markdown
[[slug]]                    # link by slug
[[slug|Display text]]       # alias
[[theory/schelling-segregation]]  # optional path hint (slug is canonical)
```

Slug is globally unique across all types.

## Explicit edge files (optional)

Path: `graph/edges/{from-id}--{edge-type}--{to-id}.md`

```yaml
---
from: THY-0042
to: PAT-0008
type: instantiates
note: "Agent placement in opening chapter"
weight: 1.0
---
```

Use when edge has metadata that clutters frontmatter.

## Graph queries (future viewer)

Viewer may parse all frontmatter `related:` blocks. No database — static site generator or client-side index from JSON export optional.

Export script (future): `scripts/export-graph.json`
