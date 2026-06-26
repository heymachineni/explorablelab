# Graph

Optional **annotated edges** supplement frontmatter `related:`.

## Structure

```
graph/
└── edges/
    └── {FROM-ID}--{edge-type}--{TO-ID}.md
```

## When to add an edge file

- Coverage percentage (EXE → THY)
- Weighted or disputed relationships
- Notes too long for frontmatter

## Schema

See [`meta/graph/schema.md`](../meta/graph/schema.md)

## Example

[`edges/THY-0001--demonstrates--EXE-0001.md`](edges/THY-0001--demonstrates--EXE-0001.md)

## Future export

`scripts/export-graph.py` → JSON for website viewer (optional).
