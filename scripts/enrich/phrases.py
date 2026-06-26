"""Rebuild canonical titles from slugs using seed catalogs and phrase heuristics."""

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

JOINERS = {
    "effect", "effects", "theory", "theories", "paradox", "paradoxes", "fallacy", "bias",
    "theorem", "law", "laws", "model", "models", "hypothesis", "principle", "principles",
    "dilemma", "problem", "game", "games", "distribution", "mechanics", "dynamics",
    "interpretation", "equilibrium", "equilibria", "cycle", "cycles", "process", "processes",
    "learning", "inference", "reasoning", "heuristic", "heuristics", "experiment",
    "phenomenon", "syndrome", "disorder", "test", "task", "method", "analysis",
    "optimization", "programming", "regression", "correlation", "selection", "mutation",
    "evolution", "transition", "transitions", "inequality", "identity", "formula",
    "function", "functions", "space", "spaces", "group", "groups", "graph", "graphs",
    "network", "networks", "system", "systems", "structure", "structures", "pattern",
    "patterns", "strategy", "strategies", "auction", "market", "markets", "trade",
    "growth", "decay", "diffusion", "cascade", "contagion", "threshold", "thresholds",
    "illusion", "anomaly", "puzzle", "puzzles", "kruger", "berg", "petersburg", "monty",
    "hall", "simpson", "goodman", "grue", "raven", "ravens", "curry", "berry", "liar",
    "zeno", "fermi", "maxwell", "gibbs", "braess", "friendship", "inspection", "waiting",
    "birthday", "sleeping", "beauty", "newcomb", "allais", "ellsberg", "moravec", "polanyi",
    "jevons", "petrie", "majority", "berkson", "hand", "fallacy", "paradox",
}


def rebuild_phrases(words: list[str]) -> list[str]:
    phrases: list[str] = []
    i = 0
    while i < len(words):
        if i + 1 < len(words) and words[i + 1] in JOINERS:
            phrases.append(f"{words[i]} {words[i + 1]}")
            i += 2
            continue
        if i + 2 < len(words) and words[i + 2] in JOINERS:
            phrases.append(f"{words[i]} {words[i + 1]} {words[i + 2]}")
            i += 3
            continue
        phrases.append(words[i])
        i += 1
    return phrases


def title_case(s: str) -> str:
    small = {"a", "an", "the", "of", "in", "on", "and", "or", "vs", "for", "to", "by", "via"}
    words = s.replace("-", " ").split()
    out = []
    for i, w in enumerate(words):
        lw = w.lower()
        if i > 0 and lw in small:
            out.append(lw)
        elif lw in ("b", "f", "p", "np", "tcp", "ip", "hci", "ml", "ai", "sir", "r0"):
            out.append(lw.upper())
        else:
            out.append(w.capitalize())
    return " ".join(out)


def _collect_phrases() -> list[str]:
    pools = [
        PSYCH_EFFECTS,
        PHYSICS_CONCEPTS,
        ECON_CONCEPTS,
        BIO_CONCEPTS,
        MATH_CONCEPTS,
        CS_CONCEPTS,
        SOC_CONCEPTS,
        list(dict.fromkeys(MENTAL_MODELS)),
        PARADOX_LIST.split(),
        EXPERIMENT_NAMES.split(),
        BOOK_TITLES.split(),
        INTERACTION_PATTERNS.split(),
        VISUAL_METAPHORS.split(),
        STORY_STRUCTURES.split(),
        SCIENTIST_NAMES.split(),
    ]
    seen: set[str] = set()
    phrases: list[str] = []
    for pool in pools:
        rebuilt = rebuild_phrases(list(pool))
        for p in rebuilt:
            key = p.lower().strip()
            if key and key not in seen:
                seen.add(key)
                phrases.append(p)
    return phrases


def build_slug_title_map() -> dict[str, str]:
    existing: set[str] = set()
    mapping: dict[str, str] = {}
    for phrase in _collect_phrases():
        slug = unique_slug(phrase, existing)
        existing.add(slug)
        mapping[slug] = title_case(phrase)
    return mapping


_SLUG_TITLES: dict[str, str] | None = None


def slug_titles() -> dict[str, str]:
    global _SLUG_TITLES
    if _SLUG_TITLES is None:
        _SLUG_TITLES = build_slug_title_map()
    return _SLUG_TITLES

BAD_TITLE_RE = re.compile(
    r"^(Effect|Theory|Principle|Hypothesis|Model|Problem|Process|System|Analysis|"
    r"Concept \d+ .+|Seminal Paper \d+|Nobel Discovery \d+|Scientist \d+|"
    r"Explorable Book \d+|Logical Paradox \d+|Replication Study \d+|"
    r"Researcher \d+|Pattern Variant \d+|Metaphor Motif \d+|Narrative Beat Template \d+|"
    r"Phenomenon \d+|Experiment \d+|Mental Model \d+|Paradox \d+|Theory Node .+)$"
)


def is_bad_title(title: str) -> bool:
    if not title or len(title) < 3:
        return True
    if BAD_TITLE_RE.match(title.strip()):
        return True
    if title.endswith(".") and "framework or model" in title.lower():
        return True
    if title.startswith("On ") and title.endswith(" Paper"):
        return False
    generic = {
        "Effect", "Theory", "Principle", "Hypothesis", "Model", "Problem",
        "Process", "System", "Analysis", "Method", "Approach", "Framework",
        "Concept", "Mechanism", "Structure", "Function", "Behavior", "Pattern",
    }
    return title.strip() in generic


def repair_title(slug: str, current: str, page_type: str, fields: list[str] | None = None) -> str:
    titles = slug_titles()
    if slug in titles and (is_bad_title(current) or current.lower() == slug.replace("-", " ")):
        return titles[slug]

    m = re.match(r"^concept-(\d+)-(.+)$", slug)
    if m:
        idx = int(m.group(1))
        field = m.group(2).replace("-", " ")
        field_phrases = [p for p in _collect_phrases() if True]
        if idx < len(field_phrases):
            return title_case(field_phrases[idx + hash(field) % 50])

    if slug in titles:
        return titles[slug]

    if not is_bad_title(current):
        return current

    cleaned = title_case(slug.replace("-2", "").replace("-3", ""))
    if not is_bad_title(cleaned):
        return cleaned

    if page_type == "nobel" and re.match(r"^\d{4}-", slug):
        parts = slug.split("-")
        year = parts[0]
        cat = parts[1] if len(parts) > 1 else "physics"
        return f"Nobel Prize in {title_case(cat)} ({year})"

    if page_type == "paper" and re.match(r"^\d{4}-", slug):
        topic = "-".join(slug.split("-")[1:-1]) if slug.endswith("-paper") else slug
        return f"On {title_case(topic)}"

    return title_case(slug)
