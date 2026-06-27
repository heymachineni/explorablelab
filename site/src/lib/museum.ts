import canonicalData from '../data/canonical.json';
import collectionsData from '../data/collections.json';
import type { Collection, Exhibit } from '../types';

export const exhibits = canonicalData.exhibits as Exhibit[];

/** Public paths only — hide internal build queue from visitor IA */
export const collections = (collectionsData.collections as Collection[]).filter(
  (c) => c.slug !== 'build-these-next-tier-s',
);

const PUBLIC_COLLECTION_SLUGS = new Set(collections.map((c) => c.slug));

export const DISPLAY_TITLES: Record<string, string> = {
  'parable-of-polygons': 'Parable of the Polygons',
  'evolution-of-trust': 'Evolution of Trust',
  'we-become-what-we-behold': 'We Become What We Behold',
  'to-build-a-better-ballot': 'To Build a Better Ballot',
  'loopy': 'Loopy',
  'fireflies': 'Fireflies',
  'wisdom-and-madness-of-crowds': 'Wisdom and/or Madness of Crowds',
  'adventures-with-anxiety': 'Adventures with Anxiety',
  'how-to-remember-anything-forever-ish': 'How to Remember Anything Forever-ish',
  'petrie-multiplier': 'Petrie Multiplier',
  'ergodicity-street': 'Ergodicity Street',
  'schelling-segregation': 'Schelling Segregation Model',
  'start-here-first-visit': 'Start Here: First Visit',
};

export function isPlayable(exhibit: Exhibit | undefined): boolean {
  if (!exhibit) return false;
  return !!(exhibit.embedUrl || exhibit.playUrl);
}

export function playableExhibits(): Exhibit[] {
  return exhibits.filter(isPlayable);
}

export function exhibitBySlug(slug: string): Exhibit | undefined {
  return exhibits.find((e) => e.slug === slug);
}

export function collectionBySlug(slug: string): Collection | undefined {
  if (!PUBLIC_COLLECTION_SLUGS.has(slug)) return undefined;
  return collections.find((c) => c.slug === slug);
}

export function displayTitle(exhibit: Exhibit): string {
  return DISPLAY_TITLES[exhibit.slug] ?? exhibit.title;
}

export function displaySummary(exhibit: Exhibit): string {
  if (exhibit.hook && exhibit.hook !== exhibit.summary) return exhibit.hook;
  return exhibit.summary;
}

export function playerSrc(exhibit: Exhibit, embed = false): string | undefined {
  const src = exhibit.playUrl ?? exhibit.embedUrl;
  if (!src) return undefined;
  if (exhibit.playUrl && embed) {
    return `${exhibit.playUrl}${exhibit.playUrl.includes('?') ? '&' : '?'}embed=1`;
  }
  return src;
}

export function pathPlayableCount(collection: Collection): number {
  return collection.stops.filter((slug) => isPlayable(exhibitBySlug(slug))).length;
}

export function exhibitInPathUrl(
  exhibitSlug: string,
  pathSlug: string,
  stepIndex: number,
): string {
  return `/exhibit/${exhibitSlug}?path=${pathSlug}&step=${stepIndex}`;
}

export function pathStepMeta(pathSlug: string, stepIndex: number) {
  const path = collectionBySlug(pathSlug);
  if (!path || stepIndex < 0 || stepIndex >= path.stops.length) return null;
  const slug = path.stops[stepIndex];
  const exhibit = exhibitBySlug(slug);
  if (!exhibit) return null;
  return { path, stepIndex, slug, exhibit, total: path.stops.length };
}

export function relatedPlayable(exhibit: Exhibit, limit = 3): Exhibit[] {
  const out: Exhibit[] = [];
  for (const slug of exhibit.related) {
    const rel = exhibitBySlug(slug);
    if (rel && isPlayable(rel) && rel.slug !== exhibit.slug) {
      out.push(rel);
    }
    if (out.length >= limit) break;
  }
  return out;
}

export const stats = {
  total: exhibits.length,
  playable: playableExhibits().length,
  paths: collections.length,
};
