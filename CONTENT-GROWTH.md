# Content growth — ExplorableLab

How we add quality explanations and put them on the public site.

## Two layers

| Layer | Location | Who sees it |
|-------|----------|-------------|
| **Workshop** | `content/**/*.md` (~5,500 files) | Contributors only |
| **Museum floor** | `site/src/data/canonical.json` (108 today) | Public site |

The site renders **only canonical slugs**. Bulk workshop pages stay in the repo for research and linking until promoted.

## Quality bar

Every public page should read like [`content/theories/complex-systems/schelling-segregation.md`](../content/theories/complex-systems/schelling-segregation.md):

- One-line essence (blockquote)
- Why this matters
- Core idea + mechanism
- Implications and misconceptions (where relevant)
- Related `[[wikilinks]]` within the canonical set
- Further reading with real citations

**Do not publish** boilerplate like *"understanding improves when learners manipulate the mechanism directly."*

Workshop-only sections (`## Discovery suggestions`) stay in markdown but are hidden on the public site.

## Add a new explanation

1. Copy a template from [`templates/`](../templates/) into the correct `content/` folder.
2. Write the body to the quality bar above.
3. Add the slug to [`meta/CANONICAL-REGISTRY.md`](../meta/CANONICAL-REGISTRY.md).
4. Add the slug to the export lists in [`scripts/canonical_promote.py`](../scripts/canonical_promote.py) (or extend `export_site_data()`).
5. Set `status: canonical` in frontmatter.
6. Regenerate site data:

```bash
cd scripts && python3 build_museum.py
```

7. Build and preview:

```bash
cd site && npm run dev
```

## Promote an existing workshop page

1. Find the markdown file (`content/theories/...`, etc.).
2. Rewrite the body — do not promote stubs unchanged.
3. Fix `related:` links to point at canonical slugs only.
4. Add slug to registry + `canonical_promote.py` if not already listed.
5. Run `build_museum.py` and verify `/exhibit/[slug]`.

## Growth targets (suggested batches)

| Batch | Focus | Target |
|-------|--------|--------|
| 1 | Core theories | 12 → 30 |
| 2 | Design patterns | 10 → 30 |
| 3 | Paradoxes + experiments | 22 → 50 |
| 4 | Simulation specs | 38 → 60 |

Promote in **batches of 10–20** with full rewrites, not mass auto-export.

## Site rendering

- Markdown path: `contentPath` in `canonical.json`
- Parser: [`site/src/lib/content.ts`](../site/src/lib/content.ts) — sections, TOC, callouts
- Layout: Notion-style doc page with properties, sidebar TOC, related links

## Status lifecycle

| Status | Meaning |
|--------|---------|
| `stub` | Placeholder — not for public site |
| `draft` | Work in progress |
| `mature` | Workshop complete — still needs curator review |
| `canonical` | On the museum floor |

See [`CONTRIBUTING.md`](../CONTRIBUTING.md) for full contributor rules.
