# Deploy ExplorableLab on Vercel

Vercel works with this Astro static site — **no paid GitHub plan required**.

## One-time setup

1. Sign in at [vercel.com](https://vercel.com) with your GitHub account.
2. **Add New Project** → import [heymachineni/explorablelab](https://github.com/heymachineni/explorablelab).
3. **Root Directory:** leave as **`.`** (repository root) — the root `vercel.json` builds `site/` automatically.
   - *Alternative:* set Root Directory to `site` and remove reliance on root config (either works).
4. **Environment variables:** set `SITE_URL` = `https://explorablelab.vercel.app` (optional).
   - **Do not set `BASE_PATH`** — it must stay unset so the site serves at `/`.
5. Click **Deploy**.

Your site will be live at `https://explorablelab.vercel.app` within ~2 minutes.

## Fix 404 after deploy

If you see **404 NOT FOUND**:

1. **Redeploy** after pulling latest `main` (root `vercel.json` fix).
2. In Vercel → Project → **Settings → Environment Variables**, **delete `BASE_PATH`** if it exists (old GitHub Pages value `/explorablelab/` breaks the root URL).
3. Confirm **Build & Development Settings**:
   - Output Directory: `site/dist` (if root is `.`) **or** `dist` (if root is `site`)
   - Build Command: `npm run build --prefix site` (root) **or** `npm run build` (site root)
4. Check **Deployments** tab — latest build must be **Ready**, not **Error**.

## Optional env vars

| Variable | Example | When |
|----------|---------|------|
| `SITE_URL` | `https://explorablelab.vercel.app` | Custom production URL (sitemap/canonical) |

No `BASE_PATH` needed on Vercel — the site runs at `/`, not a subpath.

## Custom domain

Project Settings → Domains → add your domain (e.g. `explorablelab.org`).

Then set `SITE_URL` to that domain and redeploy.

## Local preview (production-like)

```bash
cd site
npm run build
npm run preview
```

## GitHub Pages (not used)

The repo includes an optional GitHub Pages workflow. Vercel is the recommended host for this project.

## Regenerate exhibit data before deploy

If you changed canonical content:

```bash
cd scripts && python3 build_museum.py
git add -A && git commit -m "Update canonical data" && git push
```

Vercel redeploys automatically on push to `main`.
