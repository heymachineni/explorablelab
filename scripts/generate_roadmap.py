#!/usr/bin/env python3
"""Generate roadmap markdown files #16-100 with consistent frontmatter."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# (path_relative_to_content_or_indices, frontmatter_dict, body_lines)
# Paths starting with indices/ go to indices/

ENTRIES = []

def add(path, fm, body):
    ENTRIES.append((path, fm, body))

# --- P1: Design vocabulary #16-45 (skip agent-placement #16 exists) ---

PATTERNS = [
    ("parameter-slider", "PAT-0002", "Parameter Slider", "User adjusts continuous or discrete parameters; system responds live.", ["schelling-segregation", "feedback-loops"], ["parable-of-polygons"]),
    ("sandbox-mode", "PAT-0003", "Sandbox Mode", "Open-ended playground after guided lesson; user explores own questions.", ["emergence"], ["parable-of-polygons", "evolution-of-trust"]),
    ("but-chain", "PAT-0004", "BUT-Chain", "Each answer contains the seed of its destruction; plot twists as pedagogy.", ["iterated-prisoners-dilemma"], ["evolution-of-trust"]),
    ("predict-then-reveal", "PAT-0005", "Predict-Then-Reveal", "User bets on outcome before simulation runs; gap creates aha.", ["regression-to-mean", "monty-hall-paradox"], []),
    ("comparison-view", "PAT-0006", "Comparison View", "Same input, side-by-side rule or system variants.", ["social-choice", "mechanism-design"], ["to-build-a-better-ballot"]),
    ("role-as-system", "PAT-0007", "Role-as-System", "Player embodies part of the system (camera, anxiety voice).", ["feedback-loops"], ["we-become-what-we-behold"]),
    ("graph-rewiring", "PAT-0008", "Graph Rewiring", "User adds/removes edges; topology changes outcome.", ["information-cascades", "complex-contagion"], ["wisdom-and-madness-of-crowds"]),
    ("ladder-of-abstraction", "PAT-0009", "Ladder of Abstraction", "Concrete experience first, then scale up step by step.", ["emergence"], ["to-build-a-better-ballot"]),
    ("playable-game", "PAT-0010", "Playable Game", "User plays rounds against strategies or opponents.", ["iterated-prisoners-dilemma"], ["evolution-of-trust"]),
]

for slug, pid, title, summary, theories, exe in PATTERNS:
    add(f"design/interaction-patterns/{slug}.md", {
        "id": pid, "type": "interaction-pattern", "slug": slug, "title": title,
        "summary": summary, "status": "mature", "origin": "nicky-case",
        "tags": ["explorable-explanations"],
        "related": {"theories": theories, "simulations": {"existing": exe}},
    }, [f"# {title}", "", "## Description", summary, "", "## See also", "- [[agent-placement]]"])

STRUCTURES = [
    ("echo-start-sandbox-end", "STR-0001", "Echo Start, Sandbox End", "Open with author question; close with user questions in sandbox."),
    ("innocence-horror-hope", "STR-0002", "Innocence → Horror → Hope", "Cute start, systemic horror, actionable hope."),
    ("but-chain-narrative", "STR-0003", "BUT-Chain Narrative", "Therefore/but chain through counter-intuitive beats."),
]

for slug, sid, title, summary in STRUCTURES:
    add(f"design/storytelling-structures/{slug}.md", {
        "id": sid, "type": "storytelling-structure", "slug": slug, "title": title,
        "summary": summary, "status": "mature", "origin": "nicky-case",
    }, [f"# {title}", "", summary])

METAPHORS = [
    ("neighborhood-grid", "MET-0001", "Neighborhood Grid", "Spatial grid of agents; local neighborhoods define behavior.", ["schelling-segregation"]),
    ("feedback-loop-circle", "MET-0002", "Feedback Loop Circle", "Circular causal arrows; reinforcing vs balancing.", ["feedback-loops"]),
    ("double-well-potential", "MET-0003", "Double-Well Potential", "Ball in two valleys; tipping between equilibria.", ["entropy"]),
    ("network-graph", "MET-0004", "Network Graph", "Nodes and edges; topology drives dynamics.", ["information-cascades", "percolation"]),
    ("phase-space", "MET-0005", "Phase Space", "State space trajectories; attractors as regions.", ["emergence"]),
]

for slug, mid, title, summary, theories in METAPHORS:
    add(f"design/visual-metaphors/{slug}.md", {
        "id": mid, "type": "visual-metaphor", "slug": slug, "title": title,
        "summary": summary, "status": "mature",
        "related": {"theories": theories},
    }, [f"# {title}", "", "## Mapping", f"Visualizes: {', '.join(theories)}"])

MEDIUMS = [
    ("web-simulation", "MED-0001", "Web Simulation", "Browser-based interactive simulation."),
    ("classroom-activity", "MED-0002", "Classroom Activity", "Paper, tokens, or group exercise."),
    ("interactive-game", "MED-0003", "Interactive Game", "Goal-directed play with feedback."),
    ("physical-toy", "MED-0004", "Physical Toy", "Manipulable physical model."),
]

for slug, mid, title, summary in MEDIUMS:
    add(f"design/mediums/{slug}.md", {
        "id": mid, "type": "medium", "slug": slug, "title": title,
        "summary": summary, "status": "mature",
    }, [f"# {title}", "", summary])

DISCIPLINES = [
    ("game-theory", "DIS-0002", "Game Theory", "Strategic interaction among rational or evolving agents."),
    ("probability-statistics", "DIS-0003", "Probability & Statistics", "Uncertainty, inference, and aggregate regularity."),
    ("cognitive-science", "DIS-0004", "Cognitive Science", "Mind, bias, learning, perception."),
]

for slug, did, title, summary in DISCIPLINES:
    add(f"disciplines/{slug}.md", {
        "id": did, "type": "discipline", "slug": slug, "title": title,
        "summary": summary, "status": "mature", "fields": [slug.replace("-", "_").replace("_statistics", "-statistics") if "probability" not in slug else "mathematics"],
    }, [f"# {title}", "", summary])

# --- P2: Canon #46-65 ---

DESIGNERS = [
    ("bret-victor", "DSN-0002", "Bret Victor", "Coined explorable explanations; ladder of abstraction; inventing on principle."),
    ("vi-hart", "DSN-0003", "Vi Hart", "Mathematical play; co-created Parable of the Polygons."),
]

for slug, did, title, summary in DESIGNERS:
    add(f"people/designers/{slug}.md", {
        "id": did, "type": "designer", "slug": slug, "title": title,
        "summary": summary, "status": "mature", "fields": ["design"],
    }, [f"# {title}", "", summary])

EXISTING = [
    ("evolution-of-trust", "EXE-0002", "The Evolution of Trust", "Iterated prisoner's dilemma, noise, forgiveness, evolution.", "https://ncase.me/trust/", 2017, ["iterated-prisoners-dilemma", "evolution-of-cooperation"], ["playable-game", "but-chain-narrative", "sandbox-mode"]),
    ("we-become-what-we-behold", "EXE-0003", "We Become What We Behold", "Media feedback loops; player as camera.", "https://ncase.me/wbwwb/", 2016, ["feedback-loops"], ["role-as-system"]),
    ("to-build-a-better-ballot", "EXE-0004", "To Build a Better Ballot", "Voting systems compared on same electorate.", "https://ncase.me/ballot/", 2016, ["social-choice", "mechanism-design"], ["comparison-view", "ladder-of-abstraction"]),
    ("loopy", "EXE-0005", "Loopy", "Draw and simulate feedback loop diagrams.", "https://ncase.me/loopy/", 2017, ["feedback-loops"], []),
    ("fireflies", "EXE-0006", "Fireflies", "Coupled oscillators self-synchronize.", "https://ncase.me/fireflies/", 2017, ["coupled-oscillators"], ["parameter-slider"]),
    ("wisdom-and-madness-of-crowds", "EXE-0007", "The Wisdom and/or Madness of Crowds", "Network topology changes message spread.", "https://ncase.me/crowds/", 2018, ["information-cascades"], ["graph-rewiring"]),
    ("adventures-with-anxiety", "EXE-0008", "Adventures with Anxiety", "Play as the anxiety voice.", "https://ncase.me/anxiety/", 2019, ["feedback-loops"], ["role-as-system"]),
    ("how-to-remember-anything-forever-ish", "EXE-0009", "How to Remember Anything Forever-ish", "Spaced repetition embedded in explorable.", "https://ncase.me/remember/", 2018, ["spaced-repetition"], []),
]

for slug, eid, title, summary, url, year, theories, patterns in EXISTING:
    add(f"simulations/existing/{slug}.md", {
        "id": eid, "type": "existing-explorable", "slug": slug, "title": title,
        "summary": summary, "status": "mature", "url": url, "year": year,
        "creator": ["nicky-case"], "license": "CC0",
        "related": {"theories": theories, "design": {"patterns": patterns}},
    }, [f"# {title}", "", f"**URL:** {url}", "", "## Theories", ", ".join(f"[[{t}]]" for t in theories)])

BOOKS = [
    ("micromotives-and-macrobehavior", "BOK-0001", "Micromotives and Macrobehavior", "Thomas Schelling", 1978, ["schelling-segregation", "threshold-models"]),
    ("evolution-of-cooperation", "BOK-0002", "The Evolution of Cooperation", "Robert Axelrod", 1984, ["evolution-of-cooperation", "iterated-prisoners-dilemma"]),
    ("thinking-fast-and-slow", "BOK-0003", "Thinking, Fast and Slow", "Daniel Kahneman", 2011, ["loss-aversion", "cognitive-biases-overview"]),
    ("the-selfish-gene", "BOK-0004", "The Selfish Gene", "Richard Dawkins", 1976, ["natural-selection"]),
    ("governing-the-commons", "BOK-0005", "Governing the Commons", "Elinor Ostrom", 1990, ["ostrom-commons-design", "tragedy-of-commons"]),
]

for slug, bid, title, author, year, theories in BOOKS:
    add(f"publications/books/{slug}.md", {
        "id": bid, "type": "book", "slug": slug, "title": title,
        "summary": f"By {author}.", "status": "mature", "year": year,
        "authors": [author.lower().replace(" ", "-").replace(".", "")[:20]],
        "related": {"theories": theories},
    }, [f"# {title}", "", f"**Author:** {author} · **Year:** {year}"])

SCIENTISTS = [
    ("robert-axelrod", "SCI-0002", "Robert Axelrod", "Evolution of cooperation; iterated PD tournaments."),
    ("elinor-ostrom", "SCI-0003", "Elinor Ostrom", "Commons governance; Nobel 2009."),
]

for slug, sid, title, summary in SCIENTISTS:
    add(f"people/scientists/{slug}.md", {
        "id": sid, "type": "scientist", "slug": slug, "title": title,
        "summary": summary, "status": "mature",
    }, [f"# {title}", "", summary])

# --- P3: Theories #66-100 ---

THEORIES = [
    ("complex-systems/self-organized-criticality", "THY-0003", "self-organized-criticality", "Self-Organized Criticality", "Systems naturally evolve to critical states; power-law avalanches.", 8, 9, 9),
    ("complex-systems/feedback-loops", "THY-0004", "feedback-loops", "Feedback Loops", "Reinforcing and balancing causal loops drive system behavior.", 9, 9, 10),
    ("complex-systems/threshold-models", "THY-0005", "threshold-models", "Threshold Models", "Heterogeneous activation thresholds produce cascades.", 8, 9, 9),
    ("game-theory/iterated-prisoners-dilemma", "THY-0006", "iterated-prisoners-dilemma", "Iterated Prisoner's Dilemma", "Repeated play enables cooperation despite one-shot defection incentive.", 8, 10, 10),
    ("game-theory/evolution-of-cooperation", "THY-0007", "evolution-of-cooperation", "Evolution of Cooperation", "Cooperative strategies evolve under repetition, clustering, and noise.", 8, 9, 9),
    ("game-theory/mechanism-design", "THY-0008", "mechanism-design", "Mechanism Design", "Design rules so truthful or social behavior is equilibrium.", 7, 9, 9),
    ("game-theory/signaling-games", "THY-0009", "signaling-games", "Signaling Games", "Costly signals convey information in equilibrium.", 8, 8, 8),
    ("network-science/percolation", "THY-0010", "percolation", "Percolation Theory", "Random removal of links/nodes; giant component collapse at p_c.", 9, 10, 9),
    ("network-science/information-cascades", "THY-0011", "information-cascades", "Information Cascades", "Sequential decisions; people ignore private signal, follow predecessors.", 8, 9, 9),
    ("network-science/complex-contagion", "THY-0012", "complex-contagion", "Complex Contagion", "Some behaviors require multiple exposures to spread.", 8, 9, 9),
    ("network-science/preferential-attachment", "THY-0013", "preferential-attachment", "Preferential Attachment", "New nodes link to hubs; scale-free networks emerge.", 8, 8, 8),
    ("probability/bayes-theorem", "THY-0014", "bayes-theorem", "Bayes' Theorem", "Update beliefs from evidence; base rates matter.", 7, 9, 10),
    ("probability/ergodicity", "THY-0015", "ergodicity", "Ergodicity Economics", "Ensemble average ≠ time average for individuals; ruin vs growth.", 8, 10, 10),
    ("probability/central-limit-theorem", "THY-0016", "central-limit-theorem", "Central Limit Theorem", "Sums of random variables tend toward normal distribution.", 9, 8, 8),
    ("probability/regression-to-mean", "THY-0017", "regression-to-mean", "Regression to the Mean", "Extreme observations followed by less extreme; not always causation.", 8, 8, 9),
    ("economics/tragedy-of-commons", "THY-0018", "tragedy-of-commons", "Tragedy of the Commons", "Individual incentive depletes shared resource.", 8, 8, 9),
    ("economics/goodharts-law", "THY-0019", "goodharts-law", "Goodhart's Law", "When measure becomes target, it ceases to be good measure.", 8, 9, 9),
    ("economics/loss-aversion", "THY-0020", "loss-aversion", "Loss Aversion", "Losses loom larger than equivalent gains.", 7, 8, 8),
    ("economics/comparative-advantage", "THY-0021", "comparative-advantage", "Comparative Advantage", "Trade benefits even when one party is better at everything.", 7, 8, 8),
    ("cognitive-science/hebbian-learning", "THY-0022", "hebbian-learning", "Hebbian Learning", "Neurons that fire together wire together.", 9, 9, 8),
    ("cognitive-science/spaced-repetition", "THY-0023", "spaced-repetition", "Spaced Repetition", "Distributed practice beats massed practice for retention.", 7, 9, 9),
    ("cognitive-science/cognitive-biases-overview", "THY-0024", "cognitive-biases-overview", "Cognitive Biases (Overview)", "Systematic deviations from normative judgment.", 7, 8, 9),
    ("physics/entropy", "THY-0025", "entropy", "Entropy", "Disorder and multiplicity; thermodynamic arrow of time.", 8, 8, 9),
    ("physics/coupled-oscillators", "THY-0026", "coupled-oscillators", "Coupled Oscillators", "Local coupling produces global synchronization.", 9, 9, 8),
    ("evolution/natural-selection", "THY-0027", "natural-selection", "Natural Selection", "Variation, selection, inheritance drive adaptation.", 8, 8, 10),
    ("evolution/red-queen", "THY-0028", "red-queen", "Red Queen Hypothesis", "Running to stay in place in coevolutionary arms races.", 8, 8, 8),
    ("engineering/queueing-theory", "THY-0029", "queueing-theory", "Queueing Theory", "Waiting lines; utilization drives delay nonlinearly.", 7, 9, 8),
    ("engineering/requisite-variety", "THY-0030", "requisite-variety", "Law of Requisite Variety", "Controller must match system complexity to regulate.", 6, 8, 8),
    ("information-theory/shannon-entropy", "THY-0031", "shannon-entropy", "Shannon Entropy", "Information content and compressibility.", 6, 7, 9),
    ("social-science/pluralistic-ignorance", "THY-0032", "pluralistic-ignorance", "Pluralistic Ignorance", "Private rejection, public conformity.", 8, 9, 9),
    ("social-science/ostrom-commons-design", "THY-0033", "ostrom-commons-design", "Ostrom's Commons Design Principles", "Institutional rules enable sustainable commons.", 8, 9, 10),
    ("urbanism/jacobs-four-generators", "THY-0034", "jacobs-four-generators", "Jacobs' Four Generators of Diversity", "Mixed use, short blocks, old buildings, density create vitality.", 9, 8, 8),
    ("political-science/social-choice", "THY-0035", "social-choice", "Social Choice Theory", "Voting rules; impossibility theorems; aggregation paradoxes.", 7, 9, 9),
]

for path, tid, slug, title, summary, vis, inter, edu in THEORIES:
    add(f"theories/{path}.md", {
        "id": tid, "type": "theory", "slug": slug, "title": title,
        "summary": summary, "status": "mature" if slug not in ("ergodicity",) else "mature",
        "confidence": "high",
        "explorable": {
            "verdict": "essential" if inter >= 9 else "strong",
            "why_interaction": f"Understanding {title} requires manipulating the system, not reading equations alone.",
            "can_become": {"simulation": True, "interactive_game": inter >= 9, "classroom_activity": True, "visualization": True},
            "best_medium": "web-simulation" if inter >= 9 else "visualization",
            "best_medium_stars": 5 if inter >= 9 else 4,
            "best_medium_reason": "Behavior becomes intuitive when users manipulate parameters.",
        },
        "scores": {
            "visual_potential": vis, "interaction_potential": inter, "educational_value": edu,
            "surprise": 8, "replayability": 8, "timelessness": 9, "research_quality": 9,
        },
    }, [f"# {title}", "", "> **Summary:** " + summary, "", "## Why interaction beats reading", f"See frontmatter `explorable.verdict`.", "", "## Discovery suggestions", "- [ ] Link related papers and experiments"])

# Index files
add("indices/by-discipline/complex-systems.md", {"type": "index", "title": "Complex Systems Index"}, [
    "# Complex Systems", "",
    "## Theories", "- [[emergence]]", "- [[schelling-segregation]]", "- [[feedback-loops]]", "",
    "## Explorables", "- [[parable-of-polygons]]", "- [[loopy]]", "- [[fireflies]]",
])

def yaml_dump(d, indent=0):
    lines = []
    sp = "  " * indent
    for k, v in d.items():
        if isinstance(v, dict):
            lines.append(f"{sp}{k}:")
            lines.extend(yaml_dump(v, indent+1))
        elif isinstance(v, list):
            if not v:
                lines.append(f"{sp}{k}: []")
            elif all(isinstance(i, str) for i in v):
                lines.append(f"{sp}{k}: [{', '.join(v)}]")
            else:
                lines.append(f"{sp}{k}:")
                for item in v:
                    lines.append(f"{sp}  - {item}")
        elif isinstance(v, bool):
            lines.append(f"{sp}{k}: {'true' if v else 'false'}")
        elif v is None:
            lines.append(f"{sp}{k}: null")
        else:
            s = str(v)
            if any(c in s for c in [':', '#', '{', '[', '"']):
                lines.append(f'{sp}{k}: "{s}"')
            else:
                lines.append(f"{sp}{k}: {s}")
    return lines

def write_entry(path, fm, body):
    full = ROOT / "content" / path if not path.startswith("indices/") else ROOT / path
    if full.exists() and path == "design/interaction-patterns/agent-placement.md":
        return False
    full.parent.mkdir(parents=True, exist_ok=True)
    fm_lines = ["---"] + yaml_dump(fm) + ["---", ""]
    full.write_text("\n".join(fm_lines) + "\n".join(body) + "\n", encoding="utf-8")
    return True

if __name__ == "__main__":
    n = 0
    for path, fm, body in ENTRIES:
        fm.setdefault("created", "2026-06-26")
        fm.setdefault("updated", "2026-06-26")
        if write_entry(path, fm, body):
            n += 1
    print(f"Wrote {n} files")
