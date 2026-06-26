# ExplorableLab Site

Static museum viewer for [ExplorableLab](../README.md). Reads canonical exhibit data from `src/data/canonical.json` and collections from `src/data/collections.json`.

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

## Pages

| Route | Purpose |
|-------|---------|
| `/` | Homepage — hero embed, three doors, collections rail, masters gallery |
| `/play` | Paradox Arcade — ncase.me embeds |
| `/discover` | Surprise Me — random canonical exhibit |
| `/learn` | Collection index |
| `/exhibit/[slug]` | Exhibit template |
| `/collection/[slug]` | Collection template |
| `/graph` | Constellation preview |
| `/contribute` | Workshop docs links |

## Data

- `src/data/canonical.json` — exhibit nodes (placeholder ~20 slugs; parent agent populates full set)
- `src/data/collections.json` — 12 launch collections

## Stack

- [Astro](https://astro.build) static site
- Scoped component styles — no external CSS frameworks
- Museum palette: `#1a1410` bg · `#f5ebe0` text · `#e07a5f` accent

## Deploy (Vercel)

**Recommended:** [Vercel](https://vercel.com) — free for personal projects. Full steps in [`DEPLOY.md`](../DEPLOY.md).

1. Import [github.com/heymachineni/explorablelab](https://github.com/heymachineni/explorablelab)
2. Set **Root Directory** → `site`
3. Deploy

Auto-redeploys on every push to `main`.

```bash
npm run build   # output in dist/
```

### Astro version

Pinned to **Astro 5.x** (`^5.18.2`). Astro 7.x is a major upgrade — stay on 5.x until a deliberate migration.
