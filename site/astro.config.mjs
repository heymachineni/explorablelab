import { defineConfig } from 'astro/config';

// Vercel: site at root (/). Set SITE_URL in Vercel env for production canonical URLs.
const site = process.env.SITE_URL ?? 'https://explorablelab.vercel.app';
const base = process.env.BASE_PATH ?? '/';

export default defineConfig({
  site,
  base,
  output: 'static',
});
