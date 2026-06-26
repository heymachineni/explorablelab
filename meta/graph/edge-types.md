# Edge Types Reference

See [schema.md](schema.md) for full graph model.

## Quick reference: what to link when

| You added… | Must link to… | Should suggest… |
|------------|---------------|-----------------|
| Paper | authors (SCI), theories (THY) | experiments, sim concepts |
| Theory | discipline (DIS), papers, people | patterns, metaphors, SIM, EXE check |
| Scientist | papers, theories, nobel | sim opportunities |
| Paradox | challenged theories | sim with choice/commit |
| Experiment | phenomenon, theory | interactive recreation SIM |
| Simulation concept | theories, patterns, metaphor | EXE differentiation |
| Existing explorable | theories taught, patterns used | gaps, extensions |
| Pattern | EXE examples, theories taught | |
| Discipline hub | top theories, top EXE, top SIM | MOC index |

## Bidirectional linking

If A lists B in `related.theories`, B should list A back in prose or related within 1 PR cycle.

## Coverage annotation

For EXE → THY links, note coverage in body:

```markdown
## Theories covered
| Theory | Coverage | Gap |
|--------|----------|-----|
| [[schelling-segregation]] | 85% | anti-bias desegregation |
```
