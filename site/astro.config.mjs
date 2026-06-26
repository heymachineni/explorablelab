import { defineConfig } from 'astro/config';

// Always serve from /. (Do not set BASE_PATH on Vercel — it breaks the homepage.)
const site = process.env.SITE_URL ?? 'https://explorablelab.vercel.app';

export default defineConfig({
  site,
  base: '/',
  output: 'static',
});
