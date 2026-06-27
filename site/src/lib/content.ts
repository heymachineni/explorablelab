import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { marked } from 'marked';

const REPO_ROOT = resolveRepoRoot();

function resolveRepoRoot(): string {
  const cwd = process.cwd();
  if (fs.existsSync(path.join(cwd, 'content'))) return cwd;
  if (fs.existsSync(path.join(cwd, '..', 'content'))) return path.resolve(cwd, '..');
  return path.resolve(fileURLToPath(import.meta.url), '../../..');
}

marked.setOptions({ gfm: true, breaks: false });

function splitFrontmatter(raw: string): { body: string } {
  const match = raw.match(/^---\r?\n[\s\S]*?\r?\n---\r?\n([\s\S]*)$/);
  return { body: match ? match[1].trim() : raw.trim() };
}

function sanitizeMarkdown(body: string): string {
  return body
    .split('\n')
    .filter((line) => !/ncase\.me/i.test(line))
    .filter((line) => !/^\s*>\s*\*\*Play:\*\*/i.test(line))
    .join('\n')
    .replace(/\[([^\]]+)\]\(https?:\/\/ncase\.me[^)]+\)/gi, '$1')
    .replace(/\[\[([a-z0-9-]+)\]\]/gi, (_, slug: string) => `[${slug.replace(/-/g, ' ')}](/exhibit/${slug})`);
}

export function loadExhibitMarkdown(contentPath: string | undefined): string | null {
  if (!contentPath) return null;
  const filePath = path.join(REPO_ROOT, contentPath);
  if (!fs.existsSync(filePath)) return null;
  const raw = fs.readFileSync(filePath, 'utf-8');
  const { body } = splitFrontmatter(raw);
  const cleaned = sanitizeMarkdown(body);
  if (!cleaned) return null;
  return marked.parse(cleaned) as string;
}
