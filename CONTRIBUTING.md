# Contributing

## The curator's gate

Every page must answer:

> **Why does this deserve an explorable explanation?**

If `explorable.verdict` is `weak` or `none`, do not add the page. Link to Wikipedia instead.

## Adding a page

1. **Find or assign ID** — check [`meta/id-registry.md`](meta/id-registry.md)
2. **Copy template** from [`templates/`](templates/)
3. **Place file** in correct `content/` folder (see [`ARCHITECTURE.md`](ARCHITECTURE.md))
4. **Fill frontmatter** — all required fields
5. **Score** — use [`meta/scoring/rubric.md`](meta/scoring/rubric.md)
6. **Link** — add `related:` edges; update hub pages and indices
7. **Discovery block** — fill suggestions section
8. **Create stubs** for broken links you introduce

## Status lifecycle

| Status | Meaning |
|--------|---------|
| `stub` | Placeholder; slug + one-line summary + backlinks only |
| `draft` | Work in progress |
| `mature` | Complete enough for public use |
| `canonical` | Reference quality; rarely change |

Promote `stub → draft → mature` within 180 days or remove.

## Pull request checklist

- [ ] Unique `id` and `slug`
- [ ] Tags registered in [`meta/taxonomy/tag-registry.md`](meta/taxonomy/tag-registry.md)
- [ ] `explorable` block complete (theories, paradoxes, phenomena)
- [ ] ≥2 inbound links from existing pages OR noted in PR for follow-up
- [ ] Discovery suggestions filled
- [ ] No duplicate of existing EXE without differentiation note
- [ ] Scores justified in prose if any dimension ≥ 9 or ≤ 3

## Linking rules

- Use `[[slug]]` wikilinks in body
- Use typed `related:` in frontmatter
- Prefer linking to **ideas** over linking to **people** alone

## What not to add

- Pure biographies without explorable angle
- News-cycle topics with no timelessness
- Duplicates of Wikipedia without interaction thesis
- Proprietary explorables without permission note

## ID assignment

Reserve blocks in PR description:

```
THY-0100–THY-0149: complex systems batch
```

Update `meta/id-registry.md` in same PR.

## For AI agents

Read [`AGENT_GUIDE.md`](AGENT_GUIDE.md) before batch additions.

## License

Contributions are CC0. You agree to dedicate your contribution to the public domain.
