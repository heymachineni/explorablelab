import type { IconNode } from 'lucide';
import {
  ArrowLeft,
  ArrowRight,
  BookOpen,
  Brain,
  ChevronRight,
  CircleDot,
  FileText,
  FlaskConical,
  Home,
  Layers,
  Library,
  Link2,
  Map,
  Plus,
  Route,
  Search,
  Sparkles,
  X,
  Zap,
  ExternalLink,
} from 'lucide';

export type IconName =
  | 'home'
  | 'browse'
  | 'paths'
  | 'search'
  | 'hub'
  | 'contribute'
  | 'chevron-right'
  | 'arrow-left'
  | 'arrow-right'
  | 'page'
  | 'theory'
  | 'pattern'
  | 'topic'
  | 'experiment'
  | 'paradox'
  | 'simulation'
  | 'explorable'
  | 'link'
  | 'close'
  | 'external';

const ICONS: Record<IconName, IconNode> = {
  home: Home,
  browse: Library,
  paths: Route,
  search: Search,
  hub: CircleDot,
  contribute: Plus,
  'chevron-right': ChevronRight,
  'arrow-left': ArrowLeft,
  'arrow-right': ArrowRight,
  page: FileText,
  theory: Brain,
  pattern: Layers,
  topic: Map,
  experiment: FlaskConical,
  paradox: Zap,
  simulation: Sparkles,
  explorable: BookOpen,
  link: Link2,
  close: X,
  external: ExternalLink,
};

/** Map exhibit type codes to Lucide icon names. */
export const TYPE_ICON: Record<string, IconName> = {
  THY: 'theory',
  PAT: 'pattern',
  DIS: 'topic',
  EXE: 'explorable',
  PAR: 'paradox',
  EXP: 'experiment',
  SIM: 'simulation',
  MOD: 'theory',
  MET: 'pattern',
  STR: 'pattern',
  PAP: 'page',
  BOK: 'page',
  DSN: 'page',
};

export function iconForType(type: string): IconName {
  return TYPE_ICON[type] ?? 'page';
}

export function iconToSvg(
  nodes: IconNode,
  size = 20,
  strokeWidth = 1.75,
  className = '',
): string {
  const children = nodes
    .map(([tag, attrs]) => {
      const attrStr = Object.entries(attrs)
        .map(([key, value]) => `${key}="${String(value)}"`)
        .join(' ');
      return `<${tag} ${attrStr}/>`;
    })
    .join('');
  return `<svg xmlns="http://www.w3.org/2000/svg" width="${size}" height="${size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="${strokeWidth}" stroke-linecap="round" stroke-linejoin="round"${className ? ` class="${className}"` : ''} aria-hidden="true">${children}</svg>`;
}

export function getIcon(name: IconName): IconNode {
  return ICONS[name];
}
