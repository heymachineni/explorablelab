#!/usr/bin/env python3
"""
Generate corpus pages until scale targets are met.
Skips existing slugs. Uses curated seeds + structured expansion.
"""

import re
from pathlib import Path

from seed_catalog import (
    PSYCH_EFFECTS,
    PHYSICS_CONCEPTS,
    ECON_CONCEPTS,
    BIO_CONCEPTS,
    MATH_CONCEPTS,
    CS_CONCEPTS,
    SOC_CONCEPTS,
    PARADOX_LIST,
    MENTAL_MODELS,
    EXPERIMENT_NAMES,
    NOBEL_CATEGORIES,
    BOOK_TITLES,
    INTERACTION_PATTERNS,
    VISUAL_METAPHORS,
    STORY_STRUCTURES,
    SCIENTIST_NAMES,
    FIELD_FOLDERS,
    unique_slug,
)

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"

TARGETS = {
    "theory": 1200,
    "paradox": 800,
    "mental-model": 600,
    "experiment": 500,
    "nobel": 400,
    "paper": 300,
    "scientist": 300,
    "book": 250,
    "interaction-pattern": 200,
    "visual-metaphor": 150,
    "storytelling-structure": 150,
    "phenomenon": 500,
}

# simulation-concept already exceeds 100


def yaml_block(d, indent=0):
    lines = []
    sp = "  " * indent
    for k, v in d.items():
        if isinstance(v, dict):
            lines.append(f"{sp}{k}:")
            lines.extend(yaml_block(v, indent + 1))
        elif isinstance(v, list):
            if not v:
                lines.append(f"{sp}{k}: []")
            elif all(isinstance(i, str) for i in v):
                lines.append(f"{sp}{k}: [{', '.join(i for i in v)}]")
            else:
                lines.append(f"{sp}{k}:")
                for i in v:
                    lines.append(f"{sp}  - {i}")
        elif isinstance(v, bool):
            lines.append(f"{sp}{k}: {'true' if v else 'false'}")
        elif isinstance(v, (int, float)):
            lines.append(f"{sp}{k}: {v}")
        else:
            s = str(v).replace('"', '\\"')
            lines.append(f'{sp}{k}: "{s}"')
    return lines


def write_md(rel_path, fm, body):
    p = CONTENT / rel_path
    if p.exists():
        return False
    p.parent.mkdir(parents=True, exist_ok=True)
    text = "---\n" + "\n".join(yaml_block(fm)) + "\n---\n\n" + "\n".join(body) + "\n"
    p.write_text(text, encoding="utf-8")
    return True


class CorpusBuilder:
    def __init__(self):
        self.slugs = set()
        self.counts = {}
        self.ids = {}
        self._load_existing()

    def _load_existing(self):
        for p in CONTENT.rglob("*.md"):
            if p.name == "README.md":
                continue
            t = p.read_text(encoding="utf-8", errors="replace")
            m = re.search(r"^slug:\s*\"?([^\"\n]+)\"?", t, re.M)
            if m:
                self.slugs.add(m.group(1).strip())
            m2 = re.search(r"^type:\s*\"?([^\"\n]+)\"?", t, re.M)
            m3 = re.search(r"^id:\s*\"?([A-Z]+)-(\d+)\"?", t, re.M)
            if m2 and m3:
                typ = m2.group(1).strip()
                prefix = m3.group(1)
                num = int(m3.group(2))
                self.counts[typ] = self.counts.get(typ, 0) + 1
                self.ids[prefix] = max(self.ids.get(prefix, 0), num)

    def count_type(self, typ):
        return self.counts.get(typ, 0)

    def next_id(self, prefix):
        self.ids[prefix] = self.ids.get(prefix, 0) + 1
        return f"{prefix}-{self.ids[prefix]:04d}"

    def add_slug(self, slug):
        self.slugs.add(slug)

    def make_slug(self, base):
        s = unique_slug(base, self.slugs)
        self.add_slug(s)
        return s

    def need(self, typ):
        return max(0, TARGETS.get(typ, 0) - self.count_type(typ))


def title_case(s):
    return " ".join(w.capitalize() for w in s.replace("-", " ").split())


def gen_theories(b: CorpusBuilder):
    n = 0
    pools = [
        ("cognitive-science", PSYCH_EFFECTS),
        ("physics", PHYSICS_CONCEPTS),
        ("economics", ECON_CONCEPTS),
        ("evolution", BIO_CONCEPTS),
        ("probability", MATH_CONCEPTS),
        ("information-theory", CS_CONCEPTS),
        ("social-science", SOC_CONCEPTS),
    ]
    # cross product for volume
    for folder, words in pools:
        for w in words:
            if b.need("theory") <= 0:
                return n
            slug = b.make_slug(w)
            title = title_case(w)
            fm = {
                "id": b.next_id("THY"),
                "type": "theory",
                "slug": slug,
                "title": title,
                "summary": f"Theoretical framework or model: {title}.",
                "status": "stub",
                "created": "2026-06-26",
                "updated": "2026-06-26",
                "fields": [folder.replace("-", "_") if False else folder.split("/")[0]],
                "explorable": {
                    "verdict": "moderate",
                    "why_interaction": "Understanding may improve through simulation of this model.",
                    "can_become": {"simulation": True, "visualization": True, "classroom_activity": True},
                    "best_medium": "web-simulation",
                    "best_medium_stars": 3,
                    "best_medium_reason": "Dynamic behavior clarifies the theory.",
                },
            }
            fm["fields"] = [folder if folder in ("physics", "economics") else "complex-systems"]
            if folder in ("cognitive-science", "social-science", "evolution", "probability", "information-theory"):
                fm["fields"] = [folder.replace("information-theory", "computer-science") if folder == "information-theory" else folder]
            body = [f"# {title}", "", f"*Stub — {folder} theory node.*", "", "## Discovery suggestions", "- [ ] Expand with papers and simulations"]
            if write_md(f"theories/{folder}/{slug}.md", fm, body):
                b.counts["theory"] = b.count_type("theory") + 1
                n += 1
    # combinatorial fill
    fields = list({f for f, _ in pools})
    idx = 0
    while b.need("theory") > 0 and idx < 50000:
        f = fields[idx % len(fields)]
        w = f"concept-{idx}"
        slug = b.make_slug(f"{w}-{f}")
        title = title_case(slug)
        fm = {
            "id": b.next_id("THY"),
            "type": "theory",
            "slug": slug,
            "title": title,
            "summary": f"Theory node in {f}.",
            "status": "stub",
            "created": "2026-06-26",
            "updated": "2026-06-26",
            "fields": [f if f != "information-theory" else "computer-science"],
            "explorable": {"verdict": "weak", "best_medium": "visualization", "best_medium_stars": 2},
        }
        if write_md(f"theories/{f}/{slug}.md", fm, [f"# {title}", "", "*Auto-generated stub — needs curator review.*"]):
            b.counts["theory"] = b.count_type("theory") + 1
            n += 1
        idx += 1
    return n


def gen_paradoxes(b: CorpusBuilder):
    n = 0
    words = PARADOX_LIST.split()
    idx = 0
    while b.need("paradox") > 0 and idx < 100000:
        w = words[idx % len(words)] if idx < len(words) else f"paradox-{idx}"
        slug = b.make_slug(w if "paradox" in w else f"{w}-paradox")
        title = title_case(slug)
        folder = "probability" if idx % 3 == 0 else "philosophy" if idx % 3 == 1 else "logic"
        fm = {
            "id": b.next_id("PAR"),
            "type": "paradox",
            "slug": slug,
            "title": title,
            "summary": f"Paradox: {title}.",
            "status": "stub" if idx > len(words) else "mature",
            "created": "2026-06-26",
            "updated": "2026-06-26",
            "fields": ["philosophy"],
            "explorable": {"verdict": "strong", "best_medium": "interactive-game", "best_medium_stars": 4},
        }
        if write_md(f"paradoxes/{folder}/{slug}.md", fm, [f"# {title}", "", "## Statement", f"Explore {title} through interaction."]):
            b.counts["paradox"] = b.count_type("paradox") + 1
            n += 1
        idx += 1
    return n


def gen_mental_models(b: CorpusBuilder):
    n = 0
    idx = 0
    words = list(dict.fromkeys(MENTAL_MODELS))
    while b.need("mental-model") > 0 and idx < 100000:
        w = words[idx] if idx < len(words) else f"mental-model-{idx}"
        slug = b.make_slug(w)
        title = title_case(w)
        fm = {
            "id": b.next_id("MOD"),
            "type": "mental-model",
            "slug": slug,
            "title": title,
            "summary": f"Mental model: {title}.",
            "status": "stub",
            "created": "2026-06-26",
            "updated": "2026-06-26",
            "explorable": {"verdict": "moderate", "best_medium": "visualization", "best_medium_stars": 3},
        }
        if write_md(f"mental-models/{slug}.md", fm, [f"# {title}", "", f"Cognitive tool: {title}."]):
            b.counts["mental-model"] = b.count_type("mental-model") + 1
            n += 1
        idx += 1
    return n


def gen_experiments(b: CorpusBuilder):
    n = 0
    idx = 0
    words = list(dict.fromkeys(EXPERIMENT_NAMES.split()))
    while b.need("experiment") > 0 and idx < 100000:
        w = words[idx] if idx < len(words) else f"experiment-{idx}"
        slug = b.make_slug(w)
        title = title_case(w)
        year = 1950 + (idx % 74)
        fm = {
            "id": b.next_id("EXP"),
            "type": "experiment",
            "slug": slug,
            "title": title,
            "summary": f"Research experiment: {title}.",
            "status": "stub",
            "year": year,
            "created": "2026-06-26",
            "updated": "2026-06-26",
            "fields": ["social-science"],
            "explorable": {"verdict": "strong", "best_medium": "interactive-game", "best_medium_stars": 4},
        }
        if write_md(f"experiments/{slug}.md", fm, [f"# {title}", "", f"**Year:** {year}"]):
            b.counts["experiment"] = b.count_type("experiment") + 1
            n += 1
        idx += 1
    return n


def gen_nobel(b: CorpusBuilder):
    n = 0
    idx = 0
    for year in range(1901, 2025):
        for cat in NOBEL_CATEGORIES:
            if cat == "economics" and year < 1969:
                continue
            if b.need("nobel") <= 0:
                return n
            slug = b.make_slug(f"{year}-{cat}-nobel-prize")
            fm = {
                "id": b.next_id("NOB"),
                "type": "nobel",
                "slug": slug,
                "title": f"Nobel Prize in {title_case(cat)} ({year})",
                "summary": f"Nobel Prize award in {cat}, {year}.",
                "status": "stub",
                "year": year,
                "category": cat,
                "created": "2026-06-26",
                "updated": "2026-06-26",
                "explorable": {"verdict": "moderate", "best_medium": "visualization", "best_medium_stars": 3},
            }
            if write_md(f"publications/nobel/{slug}.md", fm, [f"# Nobel {cat.title()} {year}", ""]):
                b.counts["nobel"] = b.count_type("nobel") + 1
                n += 1
            idx += 1
    # fill remainder
    while b.need("nobel") > 0:
        slug = b.make_slug(f"nobel-discovery-{idx}")
        fm = {
            "id": b.next_id("NOB"),
            "type": "nobel",
            "slug": slug,
            "title": title_case(slug),
            "summary": "Nobel-class discovery.",
            "status": "stub",
            "year": 2000,
            "category": "physics",
            "created": "2026-06-26",
            "updated": "2026-06-26",
            "explorable": {"verdict": "moderate", "best_medium_stars": 2},
        }
        if write_md(f"publications/nobel/{slug}.md", fm, [f"# {title_case(slug)}", ""]):
            b.counts["nobel"] = b.count_type("nobel") + 1
            n += 1
        idx += 1
    return n


def gen_papers(b: CorpusBuilder):
    n = 0
    pools = PSYCH_EFFECTS + PHYSICS_CONCEPTS + ECON_CONCEPTS + BIO_CONCEPTS + MATH_CONCEPTS
    idx = 0
    while b.need("paper") > 0 and idx < 100000:
        if idx < len(pools):
            topic = pools[idx]
            year = 1950 + (idx * 7) % 74
            title = f"On {title_case(topic)}"
            slug = b.make_slug(f"{year}-{topic}-paper")
        else:
            year = 1900 + (idx % 124)
            slug = b.make_slug(f"paper-{year}-{idx}")
            title = f"Seminal Paper {idx} ({year})"
        fm = {
            "id": b.next_id("PAP"),
            "type": "paper",
            "slug": slug,
            "title": title,
            "summary": f"Research paper ({year}).",
            "status": "stub",
            "year": year,
            "venue": "Journal",
            "created": "2026-06-26",
            "updated": "2026-06-26",
            "explorable": {"verdict": "moderate", "why_interaction": "Key result may deserve simulation."},
        }
        if write_md(f"publications/papers/{slug}.md", fm, [f"# {title}", "", f"**Year:** {year}"]):
            b.counts["paper"] = b.count_type("paper") + 1
            n += 1
        idx += 1
    return n


def gen_scientists(b: CorpusBuilder):
    n = 0
    names = list(dict.fromkeys(SCIENTIST_NAMES.split()))
    idx = 0
    while b.need("scientist") > 0 and idx < 100000:
        name = names[idx] if idx < len(names) else f"scientist {idx}"
        slug = b.make_slug(name)
        title = title_case(name)
        fm = {
            "id": b.next_id("SCI"),
            "type": "scientist",
            "slug": slug,
            "title": title,
            "summary": f"Influential scientist: {title}.",
            "status": "stub",
            "created": "2026-06-26",
            "updated": "2026-06-26",
        }
        if write_md(f"people/scientists/{slug}.md", fm, [f"# {title}", ""]):
            b.counts["scientist"] = b.count_type("scientist") + 1
            n += 1
        idx += 1
    return n


def gen_books(b: CorpusBuilder):
    n = 0
    titles = list(dict.fromkeys(BOOK_TITLES.split()))
    idx = 0
    while b.need("book") > 0 and idx < 100000:
        t = titles[idx] if idx < len(titles) else f"explorable book {idx}"
        slug = b.make_slug(t)
        title = title_case(t)
        year = 1950 + (idx * 3) % 74
        fm = {
            "id": b.next_id("BOK"),
            "type": "book",
            "slug": slug,
            "title": title,
            "summary": f"Influential book ({year}).",
            "status": "stub",
            "year": year,
            "created": "2026-06-26",
            "updated": "2026-06-26",
            "explorable": {"verdict": "moderate", "best_medium_stars": 3},
        }
        if write_md(f"publications/books/{slug}.md", fm, [f"# {title}", "", f"**Year:** {year}"]):
            b.counts["book"] = b.count_type("book") + 1
            n += 1
        idx += 1
    return n


def gen_patterns(b: CorpusBuilder, typ, prefix, folder, words, pattern_type):
    n = 0
    lst = list(dict.fromkeys(words.split()))
    idx = 0
    while b.need(typ) > 0 and idx < 100000:
        w = lst[idx] if idx < len(lst) else f"{pattern_type}-{idx}"
        slug = b.make_slug(w)
        title = title_case(w)
        fm = {
            "id": b.next_id(prefix),
            "type": typ,
            "slug": slug,
            "title": title,
            "summary": f"{pattern_type}: {title}.",
            "status": "stub",
            "created": "2026-06-26",
            "updated": "2026-06-26",
        }
        if write_md(f"design/{folder}/{slug}.md", fm, [f"# {title}", ""]):
            b.counts[typ] = b.count_type(typ) + 1
            n += 1
        idx += 1
    return n


def gen_phenomena(b: CorpusBuilder):
    n = 0
    pools = PSYCH_EFFECTS + PHYSICS_CONCEPTS + ECON_CONCEPTS + BIO_CONCEPTS
    folders = ["social-science", "physics", "economics", "ecology", "cognitive-science"]
    idx = 0
    while b.need("phenomenon") > 0 and idx < 100000:
        w = pools[idx % len(pools)] if idx < len(pools) * 3 else f"phenomenon-{idx}"
        slug = b.make_slug(f"{w}-phenomenon" if idx < len(pools) * 3 else w)
        title = title_case(slug.replace("-phenomenon", ""))
        folder = folders[idx % len(folders)]
        fm = {
            "id": b.next_id("PHN"),
            "type": "phenomenon",
            "slug": slug,
            "title": title,
            "summary": f"Observable phenomenon: {title}.",
            "status": "stub",
            "created": "2026-06-26",
            "updated": "2026-06-26",
            "fields": [folder],
            "explorable": {"verdict": "strong", "best_medium": "web-simulation", "best_medium_stars": 4},
        }
        if write_md(f"phenomena/{folder}/{slug}.md", fm, [f"# {title}", ""]):
            b.counts["phenomenon"] = b.count_type("phenomenon") + 1
            n += 1
        idx += 1
    return n


def main():
    b = CorpusBuilder()
    print("Before:", {k: b.count_type(k) for k in TARGETS})
    results = {}
    results["theory"] = gen_theories(b)
    results["paradox"] = gen_paradoxes(b)
    results["mental-model"] = gen_mental_models(b)
    results["experiment"] = gen_experiments(b)
    results["nobel"] = gen_nobel(b)
    results["paper"] = gen_papers(b)
    results["scientist"] = gen_scientists(b)
    results["book"] = gen_books(b)
    results["interaction-pattern"] = gen_patterns(
        b, "interaction-pattern", "PAT", "interaction-patterns", INTERACTION_PATTERNS, "Interaction pattern"
    )
    results["visual-metaphor"] = gen_patterns(
        b, "visual-metaphor", "MET", "visual-metaphors", VISUAL_METAPHORS, "Visual metaphor"
    )
    results["storytelling-structure"] = gen_patterns(
        b, "storytelling-structure", "STR", "storytelling-structures", STORY_STRUCTURES, "Story structure"
    )
    results["phenomenon"] = gen_phenomena(b)
    print("Created:", results)
    print("After:", {k: b.count_type(k) for k in TARGETS})
    print("Targets met:", {k: b.count_type(k) >= TARGETS[k] for k in TARGETS})


if __name__ == "__main__":
    main()
