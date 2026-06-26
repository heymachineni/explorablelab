#!/usr/bin/env python3
"""Create Phase 7 discipline hub pages."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "content" / "disciplines"

DISCIPLINES = [
    ("DIS-0010", "cybernetics", "Cybernetics", "Feedback, control, communication in machines and living systems.", "complex-systems", ["requisite-variety", "feedback-loops"]),
    ("DIS-0011", "operations-research", "Operations Research", "Optimization, queueing, allocation under constraints.", "engineering", ["queueing-theory"]),
    ("DIS-0012", "information-theory-discipline", "Information Theory", "Entropy, compression, channel capacity, error correction.", "computer-science", ["shannon-entropy"]),
    ("DIS-0013", "decision-science", "Decision Science", "How individuals and groups choose under uncertainty.", "cognitive-science", ["loss-aversion", "bayes-theorem"]),
    ("DIS-0014", "human-computer-interaction", "Human-Computer Interaction", "Affordances, feedback, cognitive load in interactive systems.", "design", []),
    ("DIS-0015", "ecology-discipline", "Ecology", "Population dynamics, trophic cascades, carrying capacity.", "ecology", ["natural-selection", "red-queen"]),
    ("DIS-0016", "neuroscience-discipline", "Neuroscience", "Neural mechanisms of learning, perception, plasticity.", "neuroscience", ["hebbian-learning"]),
    ("DIS-0017", "linguistics-discipline", "Linguistics", "Language structure, meaning, pragmatics, evolution of language.", "social-science", []),
    ("DIS-0018", "anthropology-discipline", "Anthropology", "Culture, ritual, gift economies, cultural evolution.", "anthropology", []),
    ("DIS-0019", "political-philosophy", "Political Philosophy", "Social contract, veil of ignorance, collective action.", "philosophy", ["social-choice"]),
    ("DIS-0020", "game-design-discipline", "Game Design", "Mechanics, feedback, procedural rhetoric for play.", "design", ["explorable-explanations"]),
    ("DIS-0021", "architecture-urbanism", "Architecture & Urbanism", "Space, vitality, pattern language, Jacobs.", "architecture", ["jacobs-four-generators"]),
    ("DIS-0022", "music-theory-discipline", "Music Theory", "Consonance, rhythm, Fourier timbre, synchronization.", "music", ["coupled-oscillators"]),
    ("DIS-0023", "history-of-science-discipline", "History of Science", "Paradigm shifts, revolutions, replication.", "history-of-science", []),
    ("DIS-0024", "educational-psychology-discipline", "Educational Psychology", "Spacing, testing effect, cognitive load, productive failure.", "education", ["spaced-repetition"]),
    ("DIS-0025", "control-theory-discipline", "Control Theory", "Feedback control, stability, PID intuition.", "engineering", ["requisite-variety"]),
    ("DIS-0026", "queueing-theory-discipline", "Queueing Theory", "Waiting lines, utilization, Little's law.", "engineering", ["queueing-theory"]),
    ("DIS-0027", "semeiotics-discipline", "Semiotics", "Signs, symbols, icons, interpretation.", "semiotics", []),
    ("DIS-0028", "network-science-discipline", "Network Science", "Graph topology drives dynamics.", "complex-systems", ["percolation", "information-cascades", "preferential-attachment"]),
    ("DIS-0029", "behavioral-economics-discipline", "Behavioral Economics", "Psychology meets economic decision.", "economics", ["loss-aversion", "goodharts-law"]),
]

for did, slug, title, summary, field, theories in DISCIPLINES:
    p = ROOT / f"{slug}.md"
    if p.exists() and slug in ("game-theory", "probability-statistics", "cognitive-science", "complex-systems", "explorable-explanations"):
        continue
    theory_links = "\n".join(f"- [[{t}]]" for t in theories) or "- *(seed theories — expand)*"
    body = f"""---
id: {did}
type: discipline
slug: {slug}
title: "{title}"
summary: "{summary}"
status: mature
created: 2026-06-26
updated: 2026-06-26
fields: [{field}]
tags: []

related:
  disciplines: [complex-systems]
  theories: [{', '.join(theories)}]
---

# {title}

## Scope

{summary}

## Foundational theories

{theory_links}

## Explorable potential

High — systems in this discipline often require **running** models. See [`meta/taxonomy/visualizability.yaml`](../../meta/taxonomy/visualizability.yaml).

## Related disciplines

- [[complex-systems]]

## Discovery suggestions

### Missing pages
- [ ] Add top 5 THY for this discipline
- [ ] Link EXE if any exist

## See also

- [`phases/PHASE-07-DISCIPLINES.md`](../../phases/PHASE-07-DISCIPLINES.md)
"""
    p.write_text(body, encoding="utf-8")
    print(f"Wrote {slug}")
