import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { marked } from 'marked';

const REPO_ROOT = resolveRepoRoot();

const PUBLIC_HIDDEN_SECTIONS = new Set([
  'discovery suggestions',
  'play it',
  'see also',
]);

const COLLAPSIBLE_SECTIONS = new Set([
  'further reading',
  'formal definition',
  'parameters',
  'can become',
  'existing explorables',
]);

export interface DocMeta {
  difficulty?: string;
  confidence?: string;
  fields: string[];
  tags: string[];
  wing?: string;
}

export interface TocItem {
  id: string;
  title: string;
  level: 2 | 3;
}

export interface DocSection {
  id: string;
  title: string;
  level: 2 | 3;
  html: string;
  collapsible?: boolean;
  callout?: 'note' | 'tip' | 'warning';
}

export interface ParsedDocument {
  meta: DocMeta;
  essence?: string;
  sections: DocSection[];
  toc: TocItem[];
  fullHtml: string;
}

function resolveRepoRoot(): string {
  const cwd = process.cwd();
  if (fs.existsSync(path.join(cwd, 'content'))) return cwd;
  if (fs.existsSync(path.join(cwd, '..', 'content'))) return path.resolve(cwd, '..');
  return path.resolve(fileURLToPath(import.meta.url), '../../..');
}

function slugify(title: string): string {
  return title
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-|-$/g, '');
}

function parseYamlList(raw: string, key: string): string[] {
  const inline = raw.match(new RegExp(`${key}:\\s*\\[([^\\]]*)\\]`));
  if (inline) {
    return inline[1]
      .split(',')
      .map((s) => s.trim().replace(/^["']|["']$/g, ''))
      .filter(Boolean);
  }
  return [];
}

function parseYamlScalar(raw: string, key: string): string | undefined {
  const m = raw.match(new RegExp(`${key}:\\s*"?([^"\\n]+)"?`));
  return m?.[1]?.trim();
}

function parseFrontmatter(raw: string): { fm: string; body: string } {
  const match = raw.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n([\s\S]*)$/);
  if (!match) return { fm: '', body: raw.trim() };
  return { fm: match[1], body: match[2].trim() };
}

function parseMeta(fm: string): DocMeta {
  return {
    difficulty: parseYamlScalar(fm, 'difficulty'),
    confidence: parseYamlScalar(fm, 'confidence'),
    wing: parseYamlScalar(fm, 'wing'),
    fields: parseYamlList(fm, 'fields'),
    tags: parseYamlList(fm, 'tags'),
  };
}

function preprocessBlocks(body: string): string {
  const lines = body.split('\n');
  const out: string[] = [];
  let i = 0;

  while (i < lines.length) {
    const calloutMatch = lines[i].match(/^>\s*\[!(\w+)\]\s*$/i);
    if (calloutMatch) {
      const kind = calloutMatch[1].toLowerCase();
      const calloutLines: string[] = [];
      i += 1;
      while (i < lines.length && lines[i].startsWith('>')) {
        calloutLines.push(lines[i].replace(/^>\s?/, ''));
        i += 1;
      }
      out.push(`<div class="callout callout--${kind}">`);
      out.push(marked.parseInline(calloutLines.join(' ')) as string);
      out.push('</div>');
      continue;
    }

    if (/^---+\s*$/.test(lines[i])) {
      out.push('<div class="block-divider" role="separator"></div>');
      i += 1;
      continue;
    }

    out.push(lines[i]);
    i += 1;
  }

  return out.join('\n');
}

function sanitizeMarkdown(body: string): string {
  return body
    .split('\n')
    .filter((line) => !/ncase\.me/i.test(line))
    .filter((line) => !/^\s*>\s*\*\*Play:\*\*/i.test(line))
    .join('\n')
    .replace(/\[([^\]]+)\]\(https?:\/\/ncase\.me[^)]+\)/gi, '$1')
    .replace(/\[\[([a-z0-9-]+)\]\]/gi, (_, slug: string) => {
      const label = slug.replace(/-/g, ' ');
      return `[${label}](/exhibit/${slug})`;
    });
}

function stripPageChrome(body: string): { body: string; essence?: string } {
  let text = body.replace(/^#\s+.+\n+/, '');
  const essenceMatch = text.match(/^>\s*\*\*([^*]+):\*\*\s*(.+)$/m);
  let essence: string | undefined;
  if (essenceMatch) {
    essence = essenceMatch[2].replace(/^\*|\*$/g, '').trim();
    text = text.replace(essenceMatch[0], '').trim();
  }
  return { body: text, essence };
}

marked.use({ gfm: true, breaks: false });

function postProcessHtml(html: string): string {
  return html
    .replace(/<table>/g, '<div class="table-wrap"><table class="notion-table">')
    .replace(/<\/table>/g, '</table></div>')
    .replace(/<blockquote>/g, '<div class="callout callout--quote">')
    .replace(/<\/blockquote>/g, '</div>')
    .replace(/<pre>/g, '<pre class="code-block">')
    .replace(/<hr\s*\/?>/g, '<div class="block-divider" role="separator"></div>');
}

function splitSections(body: string): DocSection[] {
  const lines = body.split('\n');
  const sections: DocSection[] = [];
  let currentTitle = 'Overview';
  let currentLevel: 2 | 3 = 2;
  let currentLines: string[] = [];
  let started = false;

  const flush = () => {
    const md = currentLines.join('\n').trim();
    if (!md) return;
    const titleKey = currentTitle.toLowerCase();
    if (PUBLIC_HIDDEN_SECTIONS.has(titleKey)) {
      currentLines = [];
      return;
    }
    sections.push({
      id: slugify(currentTitle),
      title: currentTitle,
      level: currentLevel,
      collapsible: COLLAPSIBLE_SECTIONS.has(titleKey),
      html: postProcessHtml(marked.parse(preprocessBlocks(md)) as string),
    });
    currentLines = [];
  };

  for (const line of lines) {
    const h2 = line.match(/^##\s+(.+)/);
    const h3 = line.match(/^###\s+(.+)/);
    if (h2 || h3) {
      if (started) flush();
      started = true;
      currentTitle = (h2 ?? h3)![1].trim();
      currentLevel = h2 ? 2 : 3;
      continue;
    }
    if (started || !line.match(/^#\s+/)) {
      started = true;
      currentLines.push(line);
    }
  }
  flush();

  if (!sections.length && body.trim()) {
    sections.push({
      id: 'overview',
      title: 'Overview',
      level: 2,
      html: postProcessHtml(marked.parse(preprocessBlocks(body)) as string),
    });
  }

  return sections;
}

export function loadExhibitDocument(contentPath: string | undefined): ParsedDocument | null {
  if (!contentPath) return null;
  const filePath = path.join(REPO_ROOT, contentPath);
  if (!fs.existsSync(filePath)) return null;

  const raw = fs.readFileSync(filePath, 'utf-8');
  const { fm, body } = parseFrontmatter(raw);
  const meta = parseMeta(fm);
  const cleaned = sanitizeMarkdown(body);
  if (!cleaned) return null;

  const { body: trimmed, essence } = stripPageChrome(cleaned);
  const sections = splitSections(trimmed);
  const toc: TocItem[] = sections
    .filter((s) => s.level === 2)
    .map(({ id, title, level }) => ({ id, title, level }));

  return {
    meta,
    essence,
    sections,
    toc,
    fullHtml: sections.map((s) => s.html).join('\n'),
  };
}

/** @deprecated Use loadExhibitDocument */
export function loadExhibitMarkdown(contentPath: string | undefined): string | null {
  const doc = loadExhibitDocument(contentPath);
  return doc?.fullHtml ?? null;
}
