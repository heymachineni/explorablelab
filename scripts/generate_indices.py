#!/usr/bin/env python3
"""Regenerate index pages from corpus frontmatter."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"


def parse_fm(path):
    t = path.read_text(encoding="utf-8", errors="replace")
    if not t.startswith("---"):
        return None
    end = t.find("\n---", 3)
    if end < 0:
        return None
    block = t[3:end]
    d = {}
    for line in block.splitlines():
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            d[k.strip()] = v.strip().strip('"')
    return d


def collect(type_filter=None):
    items = []
    for p in CONTENT.rglob("*.md"):
        if p.name == "README.md":
            continue
        fm = parse_fm(p)
        if not fm or "slug" not in fm:
            continue
        if type_filter and fm.get("type") != type_filter:
            continue
        items.append(fm)
    return items


def write_index(path, title, intro, sections):
    lines = [f"# {title}", "", intro, ""]
    for heading, slugs in sections:
        lines.append(f"## {heading}")
        lines.append("")
        for s in sorted(slugs):
            lines.append(f"- [[{s}]]")
        lines.append("")
    (ROOT / path).parent.mkdir(parents=True, exist_ok=True)
    (ROOT / path).write_text("\n".join(lines), encoding="utf-8")


def main():
    sims = collect("simulation-concept")
    pars = collect("paradox")
    exps = collect("experiment")
    paps = collect("paper")
    nobs = collect("nobel")
    mods = collect("mental-model")
    phns = collect("phenomenon")
    hybrids = [s for s in sims if s.get("hybrid") == "true" or "hybrid" in str(s)]

    # Tier S sims (from research top scores)
    tier_s = [
        "ergodicity-street", "petrie-multiplier", "percolation-city", "majority-illusion",
        "parrondos-paradox", "complex-contagion-protest", "base-rate-hospital",
        "braess-roads", "goodhart-school", "simpsons-paradox-university",
        "sandpile-avalanche", "commons-garden", "pluralistic-ignorance-pool",
        "maxwells-demon-box", "jane-jacobs-corner", "urban-percolation-equity",
        "contagion-of-courage", "ergodic-inequality", "krebs-cycle-of-outrage",
    ]

    tier_s_existing = [s for s in tier_s if any(x.get("slug") == s for x in sims)]

    write_index(
        "indices/by-score/tier-s.md",
        "Tier S — Priority Simulations",
        "Composite ≥ 8.5 · low existing coverage · essential verdict. Build these first.",
        [("Simulation concepts", tier_s_existing)],
    )

    write_index(
        "indices/by-score/tier-a.md",
        "Tier A — High Priority Simulations",
        "Strong explorable potential; build after Tier S.",
        [("All simulation concepts (sample)", [s["slug"] for s in sims[:40]])],
    )

    write_index(
        "indices/awesome/paradoxes.md",
        "Awesome Paradoxes",
        f"{len(pars)} paradoxes worth interactive treatment.",
        [("All paradoxes", [p["slug"] for p in pars])],
    )

    write_index(
        "indices/awesome/experiments.md",
        "Awesome Experiments",
        f"{len(exps)} classic experiments recreate-able as interactives.",
        [("All experiments", [e["slug"] for e in exps])],
    )

    write_index(
        "indices/awesome/simulation-concepts.md",
        "Awesome Simulation Concepts",
        f"{len(sims)} concepts from research + hybrids.",
        [
            ("Hybrid concepts (novel combinations)", [s["slug"] for s in sims if s.get("slug", "").startswith(("bayesian", "urban-percolation", "metric-hydra", "ergodic-inequality", "contagion-of", "krebs", "polya-culture", "thermodynamic", "ostrom-network", "paradox-traffic", "sleeping-beauty-portfolio", "stochastic-resonance-democracy", "forecasting-market", "memory-channel", "evolutionary-trust"))]),
            ("Society & institutions (1–15)", [s["slug"] for s in sims if s["slug"] in ("standing-ovation", "veil-room", "petrie-multiplier", "overton-window", "commons-garden", "cobra-farm", "goodhart-school", "campbell-scoreboard", "majority-illusion", "weak-tie-bridge", "focal-point", "pygmalion-class", "matthew-effect", "institutional-ratchet", "pluralistic-ignorance-pool")]),
            ("Full catalog", [s["slug"] for s in sims]),
        ],
    )

    write_index(
        "indices/awesome/papers.md",
        "Awesome Papers",
        f"{len(paps)} canonical papers with explorable angles.",
        [("All papers", [p["slug"] for p in paps])],
    )

    write_index(
        "indices/awesome/mental-models.md",
        "Awesome Mental Models",
        f"{len(mods)} mental models with interactive potential.",
        [("All mental models", [m["slug"] for m in mods])],
    )

    write_index(
        "indices/awesome/phenomena.md",
        "Awesome Phenomena",
        f"{len(phns)} observable phenomena.",
        [("All phenomena", [p["slug"] for p in phns])],
    )

    write_index(
        "indices/awesome/nobel-discoveries.md",
        "Awesome Nobel Discoveries",
        f"{len(nobs)} Nobel-linked discoveries.",
        [("All Nobel pages", [n["slug"] for n in nobs])],
    )

    # Stats file
    stats = {
        "theory": len(collect("theory")),
        "paradox": len(pars),
        "mental-model": len(mods),
        "experiment": len(exps),
        "phenomenon": len(phns),
        "nobel": len(nobs),
        "paper": len(paps),
        "scientist": len(collect("scientist")),
        "book": len(collect("book")),
        "interaction-pattern": len(collect("interaction-pattern")),
        "visual-metaphor": len(collect("visual-metaphor")),
        "storytelling-structure": len(collect("storytelling-structure")),
        "simulation-concept": len(sims),
        "discipline": len(collect("discipline")),
        "existing-explorable": len(collect("existing-explorable")),
    }
    lines = ["# Corpus Statistics", "", "| Type | Count |", "|------|-------|"]
    for k, v in sorted(stats.items(), key=lambda x: -x[1]):
        lines.append(f"| {k} | {v} |")
    lines.append("")
    lines.append(f"**Total content pages:** {sum(stats.values())}")
    (ROOT / "indices" / "CORPUS-STATS.md").write_text("\n".join(lines), encoding="utf-8")
    print("Indices updated. Stats:", stats)


if __name__ == "__main__":
    main()
