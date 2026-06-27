# ExplorableLab Site

Read-only museum for [ExplorableLab](../README.md). Renders markdown explanations from `content/` for each canonical exhibit in `src/data/canonical.json`.

## Quick start

```bash
cd site
npm install
npm run dev
```

Regenerate site data after corpus changes:

```bash
cd scripts && python3 build_museum.py
```

## Routes

| Route | Purpose |
|-------|---------|
| `/` | Home — stats, browse by type |
| `/learn` | Path index |
| `/collection/[slug]` | Path runner |
| `/exhibit/[slug]` | Read-only explanation (markdown from `content/`) |
| `/graph` | Atlas — search and filter by type |
| `/contribute` | Workshop docs |

Press **⌘K** to search anywhere.

## Stack

- Astro 5.x static site
- `marked` for markdown rendering
- `src/lib/content.ts` loads `contentPath` from repo root at build time

## Deploy

See [`DEPLOY.md`](../DEPLOY.md). Live: [explorablelab.vercel.app](https://explorablelab.vercel.app)
