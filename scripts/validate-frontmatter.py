#!/usr/bin/env python3
"""Validate markdown frontmatter across content/."""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"

REQUIRED = {
    "theory": ["id", "type", "slug", "title", "explorable"],
    "paper": ["id", "type", "slug", "title"],
    "discipline": ["id", "type", "slug", "title"],
}

def parse_frontmatter(text):
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    block = text[3:end]
    data = {}
    for line in block.splitlines():
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            data[k.strip()] = v.strip()
    return data

def collect_slugs():
    slugs = set()
    for p in CONTENT.rglob("*.md"):
        if p.name == "README.md":
            continue
        t = p.read_text(encoding="utf-8", errors="replace")
        fm = parse_frontmatter(t)
        if fm and "slug" in fm:
            slugs.add(fm["slug"])
    return slugs

def main():
    stats = args_stats = "--stats" in sys.argv
    slugs = collect_slugs()
    files = [p for p in CONTENT.rglob("*.md") if p.name != "README.md"]
    errors = []
    type_counts = {}

    for p in files:
        t = p.read_text(encoding="utf-8", errors="replace")
        fm = parse_frontmatter(t)
        if not fm:
            errors.append(f"{p}: no frontmatter")
            continue
        typ = fm.get("type", "unknown")
        type_counts[typ] = type_counts.get(typ, 0) + 1

    if stats:
        print(f"Content files: {len(files)}")
        print(f"Unique slugs: {len(slugs)}")
        for k, v in sorted(type_counts.items(), key=lambda x: -x[1]):
            print(f"  {k}: {v}")
        return 0

    print(f"Validated {len(files)} files, {len(slugs)} slugs")
    if errors:
        for e in errors[:20]:
            print("ERROR:", e)
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
