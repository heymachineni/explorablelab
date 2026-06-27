# ExplorableLab Site

Static museum for [ExplorableLab](../README.md). Playable exhibits and curated paths are driven by `src/data/canonical.json` and `src/data/collections.json`.

## Quick start

```bash
cd site
npm install
npm run dev
```

Open [http://localhost:4321](http://localhost:4321).

## Scripts

| Command | Description |
|---------|-------------|
| `npm run dev` | Start dev server |
| `npm run build` | Type-check and build static site to `dist/` |
| `npm run preview` | Preview production build |

## Information architecture

| Route | Purpose |
|-------|---------|
| `/` | Home — stats, featured sim, begin first visit |
| `/play` | All **playable** exhibits (native + embeds) |
| `/learn` | Path index with playable counts |
| `/collection/[slug]` | Path runner — stops link to exhibit or catalog |
| `/exhibit/[slug]` | **Playable only** — player + path prev/next |
| `/catalog/[slug]` | Non-playable entries — honest “not built yet” + skip |
| `/discover` | Random from playable pool only |
| `/graph` | Atlas — searchable/filterable catalog |
| `/contribute` | Workshop docs |

Press **⌘K** (or click Search) anywhere to open the command palette.

## Data layer

`src/lib/museum.ts` — `isPlayable()`, path URLs, display titles, stats.

## Stack

- [Astro](https://astro.build) 5.x static site
- `src/styles/design-system.css` — Notion clarity × Linear density (flat, no shadows)

## Deploy

See [`DEPLOY.md`](../DEPLOY.md). Live: [explorablelab.vercel.app](https://explorablelab.vercel.app)
