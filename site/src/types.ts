export interface Exhibit {
  slug: string;
  title: string;
  summary: string;
  type: string;
  wing: string;
  status: string;
  hook?: string;
  related: string[];
  contentPath?: string;
  hub?: string;
  fields?: string[];
  difficulty?: string;
  confidence?: string;
}

export interface Collection {
  slug: string;
  title: string;
  summary: string;
  time_minutes: number;
  emotional_arc: string;
  stops: string[];
}

export interface Hub {
  slug: string;
  title: string;
  summary: string;
  memberCount: number;
  href: string;
}

export interface WorkspaceData {
  pinnedHubs: string[];
  hubs: Hub[];
  hubMembers: Record<string, string[]>;
  pageHub: Record<string, string>;
  backlinks: Record<string, string[]>;
}

export interface CanonicalData {
  exhibits: Exhibit[];
}

export interface CollectionsData {
  collections: Collection[];
}

export interface DatabaseRow {
  slug: string;
  title: string;
  summary: string;
  type: string;
  typeLabel: string;
  wing: string;
  hub?: string;
  hubTitle?: string;
  difficulty?: string;
  href: string;
  searchText: string;
}
