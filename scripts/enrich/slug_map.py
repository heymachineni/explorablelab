"""Map every corpus slug to its canonical title by replaying generation order."""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

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
    BOOK_TITLES,
    INTERACTION_PATTERNS,
    VISUAL_METAPHORS,
    STORY_STRUCTURES,
    SCIENTIST_NAMES,
    unique_slug,
)
from enrich.phrases import rebuild_phrases, title_case

THEORY_POOLS = [
    ("cognitive-science", PSYCH_EFFECTS),
    ("physics", PHYSICS_CONCEPTS),
    ("economics", ECON_CONCEPTS),
    ("evolution", BIO_CONCEPTS),
    ("probability", MATH_CONCEPTS),
    ("information-theory", CS_CONCEPTS),
    ("social-science", SOC_CONCEPTS),
]

PARADOX_WORDS = PARADOX_LIST.split()
MENTAL_WORDS = list(dict.fromkeys(MENTAL_MODELS))
EXPERIMENT_WORDS = list(dict.fromkeys(EXPERIMENT_NAMES.split()))
BOOK_WORDS = list(dict.fromkeys(BOOK_TITLES.split()))
PATTERN_WORDS = list(dict.fromkeys(INTERACTION_PATTERNS.split()))
METAPHOR_WORDS = list(dict.fromkeys(VISUAL_METAPHORS.split()))
STORY_WORDS = list(dict.fromkeys(STORY_STRUCTURES.split()))
SCIENTIST_WORDS = list(dict.fromkeys(SCIENTIST_NAMES.split()))

PHENOM_POOL = PSYCH_EFFECTS + PHYSICS_CONCEPTS + ECON_CONCEPTS + BIO_CONCEPTS


def _assign(existing: set[str], mapping: dict[str, str], raw: str) -> str:
    slug = unique_slug(raw, existing)
    existing.add(slug)
    mapping[slug] = title_case(raw)
    return slug


def build_generation_slug_map() -> dict[str, str]:
    existing: set[str] = set()
    m: dict[str, str] = {}

    for folder, words in THEORY_POOLS:
        for w in words:
            _assign(existing, m, w)

    fields = [f for f, _ in THEORY_POOLS]
    for idx in range(50000):
        f = fields[idx % len(fields)]
        raw = f"concept-{idx}"
        slug = unique_slug(f"{raw}-{f}", existing)
        if slug in m:
            break
        existing.add(slug)
        m[slug] = title_case(f"{raw} {f.replace('-', ' ')}")

    idx = 0
    while idx < 800:
        w = PARADOX_WORDS[idx % len(PARADOX_WORDS)] if idx < len(PARADOX_WORDS) else f"paradox-{idx}"
        raw = w if "paradox" in w else f"{w}-paradox"
        _assign(existing, m, raw)
        idx += 1

    for idx in range(600):
        w = MENTAL_WORDS[idx] if idx < len(MENTAL_WORDS) else f"mental-model-{idx}"
        _assign(existing, m, w)

    for idx in range(500):
        w = EXPERIMENT_WORDS[idx] if idx < len(EXPERIMENT_WORDS) else f"experiment-{idx}"
        _assign(existing, m, w)

    for year in range(1901, 2025):
        for cat in ["physics", "chemistry", "medicine", "literature", "peace", "economics"]:
            if cat == "economics" and year < 1969:
                continue
            raw = f"{year}-{cat}-nobel-prize"
            _assign(existing, m, raw.replace("-", " "))

    idx = 0
    pools = PSYCH_EFFECTS + PHYSICS_CONCEPTS + ECON_CONCEPTS + BIO_CONCEPTS + MATH_CONCEPTS
    while idx < 300:
        if idx < len(pools):
            topic = pools[idx]
            year = 1950 + (idx * 7) % 74
            raw = f"{year}-{topic}-paper"
            _assign(existing, m, f"On {title_case(topic)} ({year})")
        idx += 1

    idx = 0
    while idx < 300:
        name = SCIENTIST_WORDS[idx] if idx < len(SCIENTIST_WORDS) else f"scientist {idx}"
        _assign(existing, m, name)
        idx += 1

    for idx in range(250):
        t = BOOK_WORDS[idx] if idx < len(BOOK_WORDS) else f"explorable book {idx}"
        _assign(existing, m, t)

    for words, cap in ((PATTERN_WORDS, 200), (METAPHOR_WORDS, 150), (STORY_WORDS, 150)):
        for idx in range(cap):
            w = words[idx] if idx < len(words) else f"pattern-{idx}"
            _assign(existing, m, w)

    for idx in range(500):
        if idx < len(PHENOM_POOL) * 3:
            w = PHENOM_POOL[idx % len(PHENOM_POOL)]
            _assign(existing, m, f"{w}-phenomenon")
        else:
            _assign(existing, m, f"phenomenon-{idx}")

    return m


def build_phrase_slug_map() -> dict[str, str]:
    existing: set[str] = set()
    m: dict[str, str] = {}
    all_pools = [
        PSYCH_EFFECTS,
        PHYSICS_CONCEPTS,
        ECON_CONCEPTS,
        BIO_CONCEPTS,
        MATH_CONCEPTS,
        CS_CONCEPTS,
        SOC_CONCEPTS,
    ]
    for pool in all_pools:
        for phrase in rebuild_phrases(list(pool)):
            slug = unique_slug(phrase, existing)
            existing.add(slug)
            m[slug] = title_case(phrase)
    return m


_GEN_MAP: dict[str, str] | None = None
_PHRASE_MAP: dict[str, str] | None = None


def all_title_maps() -> dict[str, str]:
    global _GEN_MAP, _PHRASE_MAP
    if _GEN_MAP is None:
        _GEN_MAP = build_generation_slug_map()
    if _PHRASE_MAP is None:
        _PHRASE_MAP = build_phrase_slug_map()
    merged = dict(_PHRASE_MAP)
    merged.update(_GEN_MAP)
    return merged


BAD_TITLE_RE = re.compile(
    r"^(Effect\d*|Theory\d*|Concept \d+ .+|Seminal Paper \d+|Nobel Discovery \d+|"
    r"Scientist \d+|Explorable Book \d+|Logical Paradox \d+|Replication Study \d+|"
    r"Researcher \d+|Pattern Variant \d+|Metaphor Motif \d+|Narrative Beat Template \d+|"
    r"Phenomenon \d+|Experiment \d+|Mental Model \d+|Paradox \d+)$",
    re.I,
)


def is_bad_title(title: str) -> bool:
    if not title or len(title.strip()) < 3:
        return True
    t = title.strip()
    if t.isdigit() or (len(t) <= 2 and t.upper() == t and slug not in SPECIAL_SLUG_TITLES):
        return True
    if re.search(r"\([a-z-]+ [Ss]cience\)", title):
        return True
    if BAD_TITLE_RE.match(t):
        return True
    generic = {
        "Effect", "Theory", "Principle", "Hypothesis", "Model", "Problem",
        "Process", "System", "Analysis", "Method", "Framework", "Concept",
    }
    return t in generic


def preserve_title_slugs(content_root: Path) -> set[str]:
    keep = {
        "schelling-segregation", "parable-of-polygons", "standing-ovation",
        "agent-placement", "neighborhood-grid",
    }
    sim_dir = content_root / "simulations" / "concepts"
    if sim_dir.exists():
        for p in sim_dir.glob("*.md"):
            keep.add(p.stem)
    exe_dir = content_root / "simulations" / "existing"
    if exe_dir.exists():
        for p in exe_dir.glob("*.md"):
            keep.add(p.stem)
    return keep


SPECIAL_SLUG_TITLES = {
    "np": "NP-Completeness",
    "p": "P Versus NP",
    "o": "Big O Notation",
    "tcp": "TCP/IP",
    "ip": "TCP/IP Networking",
    "ml": "Machine Learning",
    "ai": "Artificial Intelligence",
    "hci": "Human-Computer Interaction",
}


def repair_title(slug: str, current: str, page_type: str, fields: list[str] | None = None) -> str:
    if slug in SPECIAL_SLUG_TITLES:
        return SPECIAL_SLUG_TITLES[slug]
    if not is_bad_title(current):
        return current
    maps = all_title_maps()
    if slug in maps and not is_bad_title(maps[slug]):
        return maps[slug]
    cleaned = title_case(slug.replace("-", " "))
    if not is_bad_title(cleaned):
        return cleaned
    if page_type == "nobel" and re.match(r"^\d{4}-", slug):
        parts = slug.split("-")
        year, cat = parts[0], parts[1]
        return f"Nobel Prize in {title_case(cat)} ({year})"
    return cleaned


FIELD_PHRASES = {
    "cognitive-science": rebuild_phrases(list(PSYCH_EFFECTS)),
    "physics": rebuild_phrases(list(PHYSICS_CONCEPTS)),
    "economics": rebuild_phrases(list(ECON_CONCEPTS)),
    "evolution": rebuild_phrases(list(BIO_CONCEPTS)),
    "probability": rebuild_phrases(list(MATH_CONCEPTS)),
    "information-theory": rebuild_phrases(list(CS_CONCEPTS)),
    "social-science": rebuild_phrases(list(SOC_CONCEPTS)),
}


def build_index_title_map(content_root: Path) -> dict[str, str]:
    """Assign canonical titles by sorted ID within each content group."""
    mapping: dict[str, str] = {}

    preserve = preserve_title_slugs(content_root)

    def assign_from_folder(folder: Path, phrases: list[str]) -> None:
        if not folder.exists() or not phrases:
            return
        file_data = []
        for p in sorted(folder.glob("*.md")):
            text = p.read_text(encoding="utf-8", errors="replace")
            mid = re.search(r'^id:\s*"?([A-Z]+)-(\d+)"?', text, re.M)
            sid = int(mid.group(2)) if mid else 0
            slug_m = re.search(r'^slug:\s*"?([^"\n]+)"?', text, re.M)
            slug = slug_m.group(1).strip() if slug_m else p.stem
            title_m = re.search(r'^title:\s*"?([^"\n]+)"?', text, re.M)
            current = title_m.group(1).strip() if title_m else ""
            file_data.append((sid, slug, current))
        file_data.sort(key=lambda x: x[0])
        for i, (_, slug, current) in enumerate(file_data):
            if slug in preserve and not is_bad_title(current):
                mapping[slug] = current
            elif i < len(phrases):
                mapping[slug] = title_case(phrases[i])
            else:
                extra = i - len(phrases) + 1
                a, b = phrases[i % len(phrases)], phrases[(i + 11) % len(phrases)]
                mapping[slug] = title_case(f"{a} × {b} ({extra})")

    theories = content_root / "theories"
    if theories.exists():
        for folder in sorted(theories.iterdir()):
            if folder.is_dir():
                assign_from_folder(folder, FIELD_PHRASES.get(folder.name, []))

    paradox_root = content_root / "paradoxes"
    if paradox_root.exists():
        px = rebuild_phrases(PARADOX_WORDS[:300])
        for folder in sorted(paradox_root.iterdir()):
            if folder.is_dir():
                assign_from_folder(folder, px)

    assign_from_folder(content_root / "mental-models", rebuild_phrases(list(MENTAL_WORDS)))
    assign_from_folder(content_root / "experiments", rebuild_phrases(EXPERIMENT_WORDS[:300]))
    assign_from_folder(content_root / "design" / "interaction-patterns", rebuild_phrases(PATTERN_WORDS[:200]))
    assign_from_folder(content_root / "design" / "visual-metaphors", rebuild_phrases(METAPHOR_WORDS[:150]))
    assign_from_folder(content_root / "design" / "storytelling-structures", rebuild_phrases(STORY_WORDS[:150]))
    assign_from_folder(content_root / "people" / "scientists", rebuild_phrases(SCIENTIST_WORDS))
    assign_from_folder(content_root / "publications" / "books", rebuild_phrases(BOOK_WORDS))

    phenom_root = content_root / "phenomena"
    if phenom_root.exists():
        ph = rebuild_phrases(list(PHENOM_POOL[:300]))
        for folder in sorted(phenom_root.iterdir()):
            if folder.is_dir():
                assign_from_folder(folder, ph)

    return mapping


_CORPUS_TITLES: dict[str, str] | None = None


def corpus_title_map(content_root: Path | None = None) -> dict[str, str]:
    global _CORPUS_TITLES
    if _CORPUS_TITLES is None:
        root = content_root or Path(__file__).resolve().parent.parent.parent / "content"
        _CORPUS_TITLES = build_index_title_map(root)
    return _CORPUS_TITLES


def repair_title_with_corpus(
    slug: str, current: str, page_type: str, fields: list[str] | None = None,
    content_root: Path | None = None,
) -> str:
    root = content_root or Path(__file__).resolve().parent.parent.parent / "content"
    corp = corpus_title_map(root)
    if slug in corp and not is_bad_title(corp[slug]):
        return corp[slug]
    if not is_bad_title(current):
        return current
    return repair_title(slug, current, page_type, fields)
