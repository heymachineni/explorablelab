import canonicalData from '../data/canonical.json';
import collectionsData from '../data/collections.json';
import type { Collection, Exhibit } from '../types';

export const exhibits = canonicalData.exhibits as Exhibit[];

export const collections = (collectionsData.collections as Collection[]).filter(
  (c) => c.slug !== 'build-these-next-tier-s',
);

const PUBLIC_COLLECTION_SLUGS = new Set(collections.map((c) => c.slug));

export const TYPE_LABELS: Record<string, string> = {
  THY: 'Theory',
  PAT: 'Pattern',
  MET: 'Metaphor',
  STR: 'Structure',
  SIM: 'Simulation',
  EXE: 'Explorable',
  PAR: 'Paradox',
  EXP: 'Experiment',
  PAP: 'Paper',
  BOK: 'Book',
  DIS: 'Discipline',
  DSN: 'Designer',
};

export function exhibitBySlug(slug: string): Exhibit | undefined {
  return exhibits.find((e) => e.slug === slug);
}

export function collectionBySlug(slug: string): Collection | undefined {
  if (!PUBLIC_COLLECTION_SLUGS.has(slug)) return undefined;
  return collections.find((c) => c.slug === slug);
}

export function displayTitle(exhibit: Exhibit): string {
  return exhibit.title;
}

export function displaySummary(exhibit: Exhibit): string {
  if (exhibit.hook && exhibit.hook !== exhibit.summary) return exhibit.hook;
  return exhibit.summary;
}

export function typeLabel(exhibit: Exhibit): string {
  return TYPE_LABELS[exhibit.type] ?? exhibit.type;
}

export function exhibitUrl(slug: string, pathSlug?: string | null, stepIndex?: number): string {
  const base = `/exhibit/${slug}`;
  if (pathSlug != null && stepIndex != null && stepIndex >= 0) {
    return `${base}?path=${pathSlug}&step=${stepIndex}`;
  }
  return base;
}

export function pathStepMeta(pathSlug: string, stepIndex: number) {
  const path = collectionBySlug(pathSlug);
  if (!path || stepIndex < 0 || stepIndex >= path.stops.length) return null;
  const slug = path.stops[stepIndex];
  const exhibit = exhibitBySlug(slug);
  if (!exhibit) return null;
  return { path, stepIndex, slug, exhibit, total: path.stops.length };
}

export function relatedExhibits(exhibit: Exhibit, limit = 6): Exhibit[] {
  const out: Exhibit[] = [];
  for (const slug of exhibit.related) {
    const rel = exhibitBySlug(slug);
    if (rel && rel.slug !== exhibit.slug) out.push(rel);
    if (out.length >= limit) break;
  }
  return out;
}

export function exhibitsByType(type: string): Exhibit[] {
  return exhibits.filter((e) => e.type === type);
}

export const stats = {
  total: exhibits.length,
  paths: collections.length,
  theories: exhibitsByType('THY').length,
  patterns: exhibitsByType('PAT').length,
  simulations: exhibitsByType('SIM').length,
  paradoxes: exhibitsByType('PAR').length,
  experiments: exhibitsByType('EXP').length,
};
