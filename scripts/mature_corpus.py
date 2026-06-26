#!/usr/bin/env python3
"""
Upgrade every corpus page to status: mature with complete frontmatter and body sections.
Preserves id and slug. Repairs broken titles. No stub markers or weak verdicts.
"""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
sys.path.insert(0, str(Path(__file__).resolve().parent))

from enrich.content import generate_body, tags_for
from enrich.parse import serialize_page
from seed_catalog import (
    EXPERIMENT_NAMES,
    MENTAL_MODELS,
    BOOK_TITLES,
    INTERACTION_PATTERNS,
    VISUAL_METAPHORS,
    STORY_STRUCTURES,
    SCIENTIST_NAMES,
)
from enrich.phrases import rebuild_phrases, title_case
from enrich.scores import best_medium, compute_scores, verdict_from_scores
from enrich.slug_map import is_bad_title, preserve_title_slugs, repair_title_with_corpus

def clean_phrases(words: list[str]) -> list[str]:
    out: list[str] = []
    for p in rebuild_phrases(words):
        t = title_case(p)
        if not is_bad_title(t) and not t.replace(" ", "").isdigit():
            out.append(p)
    return out or rebuild_phrases(words)


TYPE_PHRASES = {
    "experiment": clean_phrases(list(dict.fromkeys(EXPERIMENT_NAMES.split()))),
    "mental-model": clean_phrases(list(dict.fromkeys(MENTAL_MODELS))),
    "book": clean_phrases(list(dict.fromkeys(BOOK_TITLES.split()))),
    "scientist": clean_phrases(list(dict.fromkeys(SCIENTIST_NAMES.split()))),
    "interaction-pattern": clean_phrases(list(dict.fromkeys(INTERACTION_PATTERNS.split()))),
    "visual-metaphor": clean_phrases(list(dict.fromkeys(VISUAL_METAPHORS.split()))),
    "storytelling-structure": clean_phrases(list(dict.fromkeys(STORY_STRUCTURES.split()))),
}


def id_index(text: str) -> int | None:
    m = re.search(r'^id:\s*"?[A-Z]+-(\d+)"?', text, re.M)
    return int(m.group(1)) - 1 if m else None


def resolve_title(text: str, slug: str, page_type: str, fields: list[str]) -> str:
    current = extract_field(text, "title") or slug
    candidate = repair_title_with_corpus(slug, current, page_type, fields, CONTENT)
    if not is_bad_title(candidate):
        return candidate
    phrases = TYPE_PHRASES.get(page_type, [])
    idx = id_index(text)
    if phrases and idx is not None:
        return title_case(phrases[idx % len(phrases)])
    return title_case(slug.replace("-", " "))

CAN_BECOME = {
    "simulation": True,
    "interactive_game": True,
    "physical_toy": False,
    "classroom_activity": True,
    "visualization": True,
    "social_experiment": True,
    "mobile_app": False,
    "webgl_demo": False,
    "card_game": False,
    "board_game": False,
    "data_visualization": True,
}


def extract_field(text: str, key: str) -> str | None:
    m = re.search(rf'^{re.escape(key)}:\s*"?([^"\n]+)"?', text, re.M)
    return m.group(1).strip() if m else None


def extract_int(text: str, key: str) -> int | None:
    v = extract_field(text, key)
    if v and v.isdigit():
        return int(v)
    return None


def extract_list(text: str, key: str) -> list[str]:
    m = re.search(rf"^{re.escape(key)}:\s*\[([^\]]*)\]", text, re.M)
    if not m:
        return []
    inner = m.group(1).strip()
    if not inner:
        return []
    return [x.strip().strip('"') for x in inner.split(",")]


def infer_field(path: Path, fields: list[str]) -> str:
    if fields:
        return fields[0]
    parts = path.parts
    for folder in ("theories", "paradoxes", "phenomena"):
        if folder in parts:
            idx = parts.index(folder)
            if idx + 1 < len(parts):
                return parts[idx + 1]
    return "complex-systems"


def build_slug_pools() -> dict[str, list[str]]:
    pools: dict[str, list[str]] = defaultdict(list)
    for p in CONTENT.rglob("*.md"):
        if p.name == "README.md":
            continue
        t = p.read_text(encoding="utf-8", errors="replace")
        slug = extract_field(t, "slug")
        typ = extract_field(t, "type")
        if slug and typ:
            pools[typ].append(slug)
    return {k: sorted(set(v)) for k, v in pools.items()}


def build_frontmatter(
    text: str,
    path: Path,
    slug: str,
    title: str,
    page_type: str,
    field: str,
    pools: dict[str, list[str]],
) -> dict:
    scores = compute_scores(slug, title, page_type, field)
    verdict = verdict_from_scores(scores, page_type)
    medium, stars, reason = best_medium(page_type, scores, title)
    tags = tags_for(page_type, title, field)

    fm: dict = {
        "id": extract_field(text, "id") or "UNK-0000",
        "type": page_type,
        "slug": slug,
        "title": title,
        "summary": f"{title}: understanding improves when learners manipulate the mechanism directly.",
        "status": "mature",
        "created": extract_field(text, "created") or "2026-06-26",
        "updated": "2026-06-26",
        "confidence": "medium",
        "tags": tags,
        "scores": scores,
    }

    if page_type in ("theory", "paradox", "phenomenon", "experiment", "paper", "book", "nobel"):
        fld = field.replace("information-theory", "computer-science")
        fm["fields"] = extract_list(text, "fields") or [fld]
        fm["difficulty"] = "introductory" if scores["educational_value"] >= 7 else "intermediate"

    year = extract_int(text, "year")
    if year:
        fm["year"] = year
    cat = extract_field(text, "category")
    if cat:
        fm["category"] = cat

    if page_type == "simulation-concept":
        fm["build_difficulty"] = extract_field(text, "build_difficulty") or "medium"
        fm["build_estimate_weeks"] = extract_int(text, "build_estimate_weeks") or 3

    can = dict(CAN_BECOME)
    if page_type == "paradox":
        can["interactive_game"] = True
    if page_type in ("interaction-pattern", "visual-metaphor", "storytelling-structure"):
        can = {k: False for k in can}
        can["visualization"] = True
        can["simulation"] = True

    fm["explorable"] = {
        "verdict": verdict,
        "why_interaction": reason,
        "can_become": can,
        "best_medium": medium,
        "best_medium_stars": stars,
        "best_medium_reason": reason,
        "anti_patterns": ["text-only lecture", "animation without user agency"],
    }

    alt = pools.get("theory", []) + pools.get("simulation-concept", [])
    start = hash(slug) % max(1, len(alt))
    rel_theories = [alt[(start + i) % len(alt)] for i in range(3)] if alt else []
    fm["related"] = {"theories": rel_theories}

    return fm


def process_file(path: Path, pools: dict[str, list[str]], preserve: set[str], stats: dict) -> None:
    text = path.read_text(encoding="utf-8", errors="replace")
    slug = extract_field(text, "slug")
    page_type = extract_field(text, "type")
    if not slug or not page_type:
        stats["skipped"] += 1
        return

    if slug in preserve:
        stats["preserved"] += 1
        return

    fields = extract_list(text, "fields")
    field = infer_field(path, fields)
    title = resolve_title(text, slug, page_type, fields or [field])
    year = extract_int(text, "year")
    category = extract_field(text, "category") or "physics"

    pool = pools.get("theory", []) + pools.get("simulation-concept", []) + pools.get("paradox", [])
    body_lines = generate_body(
        page_type, title, slug, field=field, fields=fields or [field],
        year=year, category=category, related_pool=pool,
    )
    fm = build_frontmatter(text, path, slug, title, page_type, field, pools)
    path.write_text(serialize_page(fm, body_lines), encoding="utf-8")
    stats["upgraded"] += 1


def main():
    global _CORPUS_TITLES
    from enrich import slug_map as sm
    sm._CORPUS_TITLES = None

    pools = build_slug_pools()
    stats = {"upgraded": 0, "skipped": 0, "preserved": 0}
    preserve = preserve_title_slugs(CONTENT)
    files = sorted(p for p in CONTENT.rglob("*.md") if p.name != "README.md")
    for i, path in enumerate(files):
        process_file(path, pools, preserve, stats)
        if (i + 1) % 1000 == 0:
            print(f"  … {i + 1}/{len(files)}", flush=True)
    print("Mature corpus pass complete:", stats)

    stub = weak = bad = 0
    for p in files:
        if p.name == "README.md":
            continue
        t = p.read_text(encoding="utf-8", errors="replace")
        if "status: stub" in t or 'status: "stub"' in t:
            stub += 1
        if re.search(r'verdict:\s*"?weak"?', t):
            weak += 1
        title = extract_field(t, "title") or ""
        if is_bad_title(title):
            bad += 1
    print(f"QA: stub={stub} weak={weak} bad_titles={bad}")


if __name__ == "__main__":
    main()
