import workspaceData from '../data/workspace.json';
import type { DatabaseRow, Exhibit, Hub, WorkspaceData } from '../types';
import { iconForType } from './icons';
import type { IconName } from './icons';
import {
  displayTitle,
  exhibitBySlug,
  exhibits,
  typeLabel,
} from './museum';

export const workspace = workspaceData as WorkspaceData;

export const hubs = workspace.hubs;
export const hubBySlug = new Map(hubs.map((h) => [h.slug, h]));
export const pinnedHubs = workspace.pinnedHubs
  .map((slug) => hubBySlug.get(slug))
  .filter((h): h is Hub => !!h);

export function hubForPage(slug: string): Hub | undefined {
  const hubSlug = workspace.pageHub[slug];
  return hubSlug ? hubBySlug.get(hubSlug) : undefined;
}

export function pagesInHub(hubSlug: string): Exhibit[] {
  const members = workspace.hubMembers[hubSlug] ?? [];
  return members
    .map((slug) => exhibitBySlug(slug))
    .filter((e): e is Exhibit => !!e);
}

export function backlinksFor(slug: string): Exhibit[] {
  const sources = workspace.backlinks[slug] ?? [];
  return sources
    .map((s) => exhibitBySlug(s))
    .filter((e): e is Exhibit => !!e);
}

export function pageIcon(exhibit: Exhibit): IconName {
  return iconForType(exhibit.type);
}

export function toDatabaseRow(exhibit: Exhibit): DatabaseRow {
  const hub = hubForPage(exhibit.slug);
  const title = displayTitle(exhibit);
  const tl = typeLabel(exhibit);
  return {
    slug: exhibit.slug,
    title,
    summary: exhibit.summary,
    type: exhibit.type,
    typeLabel: tl,
    wing: exhibit.wing,
    hub: hub?.slug,
    hubTitle: hub?.title,
    difficulty: exhibit.difficulty,
    href: `/exhibit/${exhibit.slug}`,
    searchText: [
      title,
      exhibit.slug,
      tl,
      exhibit.wing,
      exhibit.summary,
      hub?.title,
      exhibit.difficulty,
      ...(exhibit.fields ?? []),
    ]
      .filter(Boolean)
      .join(' ')
      .toLowerCase(),
  };
}

export const databaseRows: DatabaseRow[] = exhibits.map(toDatabaseRow);

export function rowsForHub(hubSlug: string): DatabaseRow[] {
  return pagesInHub(hubSlug).map(toDatabaseRow);
}

export function rowsByType(type: string): DatabaseRow[] {
  return databaseRows.filter((row) => row.type === type);
}
