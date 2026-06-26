import { defineConfig } from 'astro/config';

// GitHub Pages project site: https://heymachineni.github.io/explorablelab/
// Override with SITE_URL / BASE_PATH env vars for custom domain later.
const site = process.env.SITE_URL ?? 'https://heymachineni.github.io';
const base = process.env.BASE_PATH ?? '/explorablelab/';

export default defineConfig({
  site,
  base,
  output: 'static',
});
