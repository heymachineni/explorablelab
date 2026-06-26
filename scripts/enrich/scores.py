"""Score computation and explorable verdict assignment."""

from __future__ import annotations

import hashlib


def _h(slug: str) -> int:
    return int(hashlib.md5(slug.encode()).hexdigest(), 16)


def _clamp(n: int, lo: int = 4, hi: int = 9) -> int:
    return max(lo, min(hi, n))


def keyword_boost(title: str, field: str) -> dict[str, int]:
    t = title.lower()
    f = field or ""
    boosts = {k: 0 for k in (
        "visual_potential", "interaction_potential", "educational_value", "surprise",
        "replayability", "narrative_potential", "beauty", "novelty", "sandbox_potential",
        "timelessness", "virality", "existing_coverage", "research_quality",
        "citation_strength", "cross_disciplinary",
    )}
    high_interaction = (
        "paradox", "game", "dilemma", "experiment", "simulation", "threshold", "segregation",
        "contagion", "cascade", "feedback", "emergence", "prisoner", "monty", "hall",
        "conformity", "illusion", "bias", "fallacy", "probability", "network", "epidemic",
        "auction", "market", "evolution", "cooperation", "sandpile", "percolation",
    )
    for kw in high_interaction:
        if kw in t:
            boosts["interaction_potential"] += 2
            boosts["surprise"] += 1
            boosts["replayability"] += 1
            boosts["sandbox_potential"] += 1

    if any(k in t for k in ("theorem", "law", "equation", "mechanics", "dynamics")):
        boosts["visual_potential"] += 1
        boosts["research_quality"] += 2
        boosts["citation_strength"] += 1

    if any(k in t for k in ("effect", "heuristic", "bias", "cognitive")):
        boosts["educational_value"] += 2
        boosts["timelessness"] += 1

    if "social" in f or "economics" in f or "cognitive" in f:
        boosts["cross_disciplinary"] += 1
        boosts["virality"] += 1

    if page_type_hint := ("pattern" in t or "metaphor" in t or "narrative" in t):
        boosts["narrative_potential"] += 2
        boosts["beauty"] += 1

    canonical = ("darwin", "einstein", "nash", "schelling", "kahneman", "tversky", "shannon", "turing")
    if any(c in t for c in canonical):
        boosts["citation_strength"] += 2
        boosts["existing_coverage"] += 2

    return boosts


def compute_scores(slug: str, title: str, page_type: str, field: str = "") -> dict:
    base = _h(slug)
    seed = base % 1000

    defaults = {
        "theory": (7, 7, 8, 6, 6, 5, 6, 5, 7, 9, 6, 4, 8, 7, 7),
        "paradox": (8, 9, 8, 9, 8, 7, 6, 6, 8, 10, 8, 5, 8, 8, 8),
        "experiment": (7, 9, 9, 8, 7, 8, 5, 5, 6, 9, 7, 6, 9, 8, 7),
        "mental-model": (6, 6, 8, 5, 6, 5, 5, 4, 5, 10, 6, 5, 7, 7, 8),
        "phenomenon": (8, 8, 8, 7, 7, 6, 7, 5, 8, 9, 7, 4, 8, 7, 7),
        "paper": (5, 5, 7, 4, 4, 3, 4, 4, 4, 9, 4, 6, 9, 9, 6),
        "book": (5, 6, 8, 5, 5, 6, 5, 4, 5, 10, 6, 7, 8, 8, 7),
        "scientist": (4, 5, 7, 4, 3, 5, 4, 3, 3, 10, 5, 8, 9, 9, 7),
        "nobel": (6, 6, 8, 6, 5, 5, 5, 4, 5, 10, 6, 7, 10, 10, 8),
        "interaction-pattern": (7, 9, 8, 5, 8, 6, 7, 5, 9, 10, 6, 3, 7, 6, 7),
        "visual-metaphor": (10, 7, 7, 4, 6, 5, 9, 4, 6, 10, 5, 3, 6, 5, 6),
        "storytelling-structure": (5, 7, 7, 5, 7, 9, 6, 4, 5, 10, 6, 3, 6, 5, 6),
        "simulation-concept": (9, 10, 9, 8, 9, 8, 7, 6, 10, 9, 8, 5, 8, 7, 8),
        "discipline": (5, 4, 7, 3, 3, 3, 4, 3, 3, 10, 4, 4, 8, 7, 9),
        "existing-explorable": (9, 10, 9, 7, 9, 9, 8, 3, 9, 10, 9, 9, 9, 8, 8),
    }
    keys = (
        "visual_potential", "interaction_potential", "educational_value", "surprise",
        "replayability", "narrative_potential", "beauty", "novelty", "sandbox_potential",
        "timelessness", "virality", "existing_coverage", "research_quality",
        "citation_strength", "cross_disciplinary",
    )
    vals = list(defaults.get(page_type, defaults["theory"]))
    boosts = keyword_boost(title, field)
    scores = {}
    for i, k in enumerate(keys):
        jitter = (seed >> (i * 2)) % 3 - 1
        scores[k] = _clamp(vals[i] + boosts[k] + jitter)
    weights = {
        "interaction_potential": 0.14, "educational_value": 0.12, "surprise": 0.12,
        "visual_potential": 0.10, "timelessness": 0.10, "novelty": 0.08,
        "sandbox_potential": 0.08, "cross_disciplinary": 0.08, "virality": 0.06,
        "narrative_potential": 0.06, "research_quality": 0.06,
    }
    composite = sum(scores[k] * w for k, w in weights.items())
    novelty_factor = 1 - scores["existing_coverage"] / 10
    composite += 0.08 * scores["novelty"] * novelty_factor
    scores["composite"] = round(composite, 1)
    return scores


def verdict_from_scores(scores: dict, page_type: str) -> str:
    ip = scores["interaction_potential"]
    ev = scores["educational_value"]
    if ip >= 8 and ev >= 7:
        return "essential"
    if ip >= 6:
        return "strong"
    if page_type in ("paper", "book", "scientist", "discipline"):
        return "moderate"
    if ip >= 4 or scores["visual_potential"] >= 6:
        return "moderate"
    return "strong"


def best_medium(page_type: str, scores: dict, title: str) -> tuple[str, int, str]:
    t = title.lower()
    if page_type == "paradox" or "paradox" in t or "dilemma" in t or "game" in t:
        return "interactive-game", 5, "Commit-reveal mechanics force intuition to collide with formal resolution."
    if page_type == "experiment":
        return "interactive-game", 5, "Users must experience the protocol as subject or experimenter."
    if page_type in ("interaction-pattern", "visual-metaphor", "storytelling-structure"):
        return "web-simulation", 4, "Patterns prove themselves when embedded in a live explorable demo."
    if scores["sandbox_potential"] >= 8:
        return "web-simulation", 5, "Parameter exploration reveals behavior invisible in static prose."
    if scores["visual_potential"] >= 8:
        return "visualization", 4, "Spatial or dynamic visualization makes structure immediately legible."
    if page_type == "mental-model":
        return "visualization", 4, "Diagrams and scenarios turn abstract heuristics into reusable tools."
    return "web-simulation", 4, "Manipulation of variables makes the mechanism tangible."
