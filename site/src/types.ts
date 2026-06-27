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
}

export interface Collection {
  slug: string;
  title: string;
  summary: string;
  time_minutes: number;
  emotional_arc: string;
  stops: string[];
}

export interface CanonicalData {
  exhibits: Exhibit[];
}

export interface CollectionsData {
  collections: Collection[];
}
