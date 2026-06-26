# Deploy ExplorableLab on Vercel

Vercel works with this Astro static site — **no paid GitHub plan required**.

## One-time setup

1. Sign in at [vercel.com](https://vercel.com) with your GitHub account.
2. **Add New Project** → import [heymachineni/explorablelab](https://github.com/heymachineni/explorablelab).
3. Set **Root Directory** to `site` (important — the Astro app lives in `/site`).
4. Vercel auto-detects Astro. Confirm:
   - **Build Command:** `npm run build`
   - **Output Directory:** `dist`
   - **Install Command:** `npm install`
5. Click **Deploy**.

Your site will be live at a URL like `https://explorablelab.vercel.app` within ~2 minutes.

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
