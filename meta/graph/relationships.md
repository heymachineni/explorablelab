# Relationships — Full Specification

How every page connects in the knowledge graph.

## Design goal

Every page feels like an **Obsidian node**: typed neighbors, not isolated articles.

## Linking priority (when editing any page)

1. **Upward** — discipline hub (`DIS`), parent theory
2. **Sideways** — related theories, paradoxes, mental models
3. **Evidence** — papers, books, experiments, Nobel
4. **People** — scientists, designers
5. **Design** — patterns, metaphors, structures, mediums
6. **Applied** — simulation concepts, existing explorables
7. **Downward** — stubs you expose as missing

## Minimum link counts (`status: mature`)

| Type | Minimum |
|------|---------|
| THY | 3 theories OR 1 theory + 2 papers; 1 PAT or MET; 1 DIS |
| PAP | 1 SCI; 1 THY or PHN |
| SCI | 2 PAP or THY |
| EXE | 1 THY; 2 PAT |
| SIM | 1 THY; 1 PAT; 1 MET |
| PAT | 2 EXE or THY examples |
| DIS | 5 THY; 2 EXE |

## Bidirectional maintenance

If `schelling-segregation` lists `emergence`, then `emergence` must mention `schelling-segregation` in body or related within one PR cycle.

## Coverage annotation (EXE → THY)

```markdown
| Theory | Coverage | Gap |
|--------|----------|-----|
| [[schelling-segregation]] | 85% | real-world data |
```

## Full example: Thomas Schelling node

```yaml
related:
  theories: [schelling-segregation, threshold-models]
  papers: [schelling-1971-dynamic-models]
  books: [micromotives-and-macrobehavior]
  simulations:
    existing: [parable-of-polygons]
  disciplines: [complex-systems, game-theory]
```

Downstream from Schelling — see chain in [`phases/PHASE-03-RELATIONSHIPS.md`](../phases/PHASE-03-RELATIONSHIPS.md).

## Wikilink conventions

```markdown
[[schelling-segregation]]              # slug only
[[schelling-segregation|Schelling model]]  # alias
```

**Slug is globally unique** — no type prefix in wikilink.

## When to use graph/edges/

Use explicit edge file when edge has metadata:

- `coverage: 85`
- `note: "opening chapter only"`
- `weight: 0.9`

Otherwise frontmatter `related:` is enough.

## Traversal paths for humans

| Start at | Follow |
|----------|--------|
| Scientist | papers → theories → SIM/EXE |
| Theory | patterns → EXE → gaps → SIM |
| EXE | patterns → theories → papers → people |
| Discipline | top THY by score → EXE canon |

## Traversal paths for agents

See [`AGENT_GUIDE.md`](../AGENT_GUIDE.md) Discovery Report.
