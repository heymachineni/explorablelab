"""Canonical promotion data and writers for ExplorableLab museum floor."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"


def fm_block(d: dict) -> str:
    lines = ["---"]
    for k, v in d.items():
        if isinstance(v, dict):
            lines.append(f"{k}:")
            for sk, sv in v.items():
                if isinstance(sv, bool):
                    lines.append(f"  {sk}: {'true' if sv else 'false'}")
                elif isinstance(sv, list):
                    lines.append(f"  {sk}: [{', '.join(sv)}]")
                else:
                    lines.append(f'  {sk}: "{sv}"' if isinstance(sv, str) else f"  {sk}: {sv}")
        elif isinstance(v, list):
            lines.append(f"{k}: [{', '.join(v)}]")
        elif isinstance(v, bool):
            lines.append(f"{k}: {'true' if v else 'false'}")
        elif isinstance(v, (int, float)):
            lines.append(f"{k}: {v}")
        else:
            lines.append(f'{k}: "{v}"')
    lines.append("---")
    return "\n".join(lines)


def default_path(slug: str, typ: str) -> Path:
    mapping = {
        "theory": CONTENT / "theories/complex-systems" / f"{slug}.md",
        "interaction-pattern": CONTENT / "design/interaction-patterns" / f"{slug}.md",
        "visual-metaphor": CONTENT / "design/visual-metaphors" / f"{slug}.md",
        "storytelling-structure": CONTENT / "design/storytelling-structures" / f"{slug}.md",
        "simulation-concept": CONTENT / "simulations/concepts" / f"{slug}.md",
        "paradox": CONTENT / "paradoxes/probability" / f"{slug}.md",
        "experiment": CONTENT / "experiments" / f"{slug}.md",
        "paper": CONTENT / "papers" / f"{slug}.md",
        "book": CONTENT / "books" / f"{slug}.md",
        "discipline": CONTENT / "disciplines" / f"{slug}.md",
        "designer": CONTENT / "designers" / f"{slug}.md",
    }
    return mapping.get(typ, CONTENT / "disciplines" / f"{slug}.md")


def write_page(slug: str, typ: str, fm: dict, body: str, path: Path | None = None) -> None:
    path = path or default_path(slug, typ)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(fm_block(fm) + "\n\n" + body + "\n", encoding="utf-8")


def promote_schelling():
    path = CONTENT / "theories/complex-systems/schelling-segregation.md"
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"^status:\s*mature\s*$", "status: canonical", text, flags=re.M)
    path.write_text(text, encoding="utf-8")


THY = [
    ("emergence", "Emergence", "systems", "Local rules produce global patterns nobody designed.",
     "Watch ants, markets, or fireflies: no central planner, yet order appears. Emergence is the bridge from micro-motives to macro-behavior.",
     ["schelling-segregation", "fireflies", "sandpile-avalanche", "agent-placement"]),
    ("threshold-models", "Threshold Models", "systems", "People join when enough others have joined.",
     "Granovetter's threshold model: individual action depends on observed group behavior. Small threshold shifts can flip entire populations.",
     ["standing-ovation", "complex-contagion-protest", "1978-granovetter-threshold", "schelling-segregation"]),
    ("feedback-loops", "Feedback Loops", "systems", "Output becomes input. Circles close.",
     "Reinforcing loops amplify; balancing loops stabilize. Loopy made this drawable — but the concept governs anxiety, outrage, and climate.",
     ["loopy", "we-become-what-we-behold", "krebs-cycle-of-outrage", "feedback-loop-circle"]),
    ("percolation", "Percolation", "systems", "Connectivity jumps at a critical point.",
     "Remove random edges; suddenly the network fragments. p_c is a phase transition — roads, infections, and equity all percolate.",
     ["percolation-city", "urban-percolation-equity", "braess-roads", "schelling-segregation"]),
    ("goodharts-law", "Goodhart's Law", "systems", "When a measure becomes a target, it ceases to be a good measure.",
     "Optimize the metric, lose the goal. Schools teach to the test; platforms chase engagement. The gap between proxy and purpose is playable.",
     ["goodhart-school", "metric-hydra", "cobra-farm", "p-hacking-lab"]),
    ("ostrom-commons-design", "Ostrom Commons Design", "systems", "Communities can govern shared resources without tragedy.",
     "Elinor Ostrom's design principles: boundaries, monitoring, graduated sanctions. The commons isn't doomed — but it needs institutions.",
     ["commons-garden", "2009-ostrom-commons", "tragedy-of-the-commons", "evolution-of-trust"]),
    ("social-choice", "Social Choice", "systems", "No voting system is perfect — Arrow proved it.",
     "Same voters, different rules, different winners. To Build a Better Ballot makes impossibility tangible.",
     ["to-build-a-better-ballot", "stochastic-resonance-democracy", "prisoners-dilemma", "evolution-of-trust"]),
    ("ergodicity", "Ergodicity", "intuition", "The ensemble average is not your average experience.",
     "Time averages and ensemble averages diverge for non-ergodic processes. Most people experience the losing path, not the mean.",
     ["ergodicity-street", "ergodic-inequality", "st-petersburg-paradox", "fat-tail-farm"]),
    ("complex-contagion", "Complex Contagion", "networks", "Some behaviors need multiple exposures to spread.",
     "Simple contagion: one contact suffices. Complex contagion: you need social proof. Protests, norms, and courage work this way.",
     ["complex-contagion-protest", "contagion-of-courage", "2007-centola-complex-contagion", "wisdom-and-madness-of-crowds"]),
    ("information-cascades", "Information Cascades", "networks", "Follow the crowd; ignore private signal.",
     "Rational agents can cascade on weak evidence when others act first. Herding isn't stupidity — it's inference under uncertainty.",
     ["information-cascade-falls", "wisdom-and-madness-of-crowds", "majority-illusion", "we-become-what-we-behold"]),
    ("iterated-prisoners-dilemma", "Iterated Prisoner's Dilemma", "systems", "One-shot defection; repeated cooperation.",
     "Shadow of the future changes strategy. Tit-for-tat, forgiveness, noise — Evolution of Trust is the textbook you play.",
     ["evolution-of-trust", "prisoners-dilemma", "prisoners-dilemma-tournament", "commons-garden"]),
]

DESIGN = [
    ("agent-placement", "interaction-pattern", "Agent Placement", "You move one piece; the system moves the rest.", "Place unhappy agents by hand before automation — complicity without accusation.", ["parable-of-polygons", "schelling-segregation", "sandbox-mode"]),
    ("parameter-slider", "interaction-pattern", "Parameter Slider", "One dial, many worlds.", "Tolerance, coupling, noise — sliders make parameter space explorable.", ["fireflies", "evolution-of-trust", "parable-of-polygons"]),
    ("sandbox-mode", "interaction-pattern", "Sandbox Mode", "Prove generality after the lesson.", "After the guided path, free play confirms the rule wasn't a trick.", ["evolution-of-trust", "to-build-a-better-ballot", "loopy"]),
    ("but-chain", "interaction-pattern", "BUT-Chain", "Yes… but… therefore… narrative ladder.", "Each beat adds a constraint; the chain carries the learner through counterintuitive truth.", ["evolution-of-trust", "we-become-what-we-behold", "but-chain-narrative"]),
    ("predict-then-reveal", "interaction-pattern", "Predict-Then-Reveal", "Commit before the simulation runs.", "Prediction creates stakes; reveal creates memory. Monty Hall only works if you guess first.", ["monty-hall-carnival", "petrie-multiplier", "how-to-remember-anything-forever-ish"]),
    ("comparison-view", "interaction-pattern", "Comparison View", "Same inputs, side by side.", "Voting systems, network topologies — difference must be visible simultaneously.", ["to-build-a-better-ballot", "wisdom-and-madness-of-crowds", "simpsons-paradox-university"]),
    ("role-as-system", "interaction-pattern", "Role-as-System", "Play the antagonist, not the hero.", "Anxiety voice, news camera — role reversal creates insight pamphlets can't.", ["adventures-with-anxiety", "we-become-what-we-behold", "innocence-horror-hope"]),
    ("graph-rewiring", "interaction-pattern", "Graph Rewiring", "Drag edges; watch diffusion change.", "Topology beats content. Rewire and compare.", ["wisdom-and-madness-of-crowds", "weak-tie-bridge", "majority-illusion"]),
    ("ladder-of-abstraction", "interaction-pattern", "Ladder of Abstraction", "Manual → automated → parameterized.", "Climb from hand placement to full simulation — each rung adds power.", ["parable-of-polygons", "to-build-a-better-ballot", "agent-placement"]),
    ("playable-game", "interaction-pattern", "Playable Game", "Real stakes in a toy world.", "Betrayal hurts because you invested rounds. Games are arguments you feel.", ["evolution-of-trust", "ultimatum-game", "newcomb-predictor"]),
    ("innocence-horror-hope", "storytelling-structure", "Innocence → Horror → Hope", "Warm start, dread middle, agency end.", "Polygons and WBWWB arc: comfort, complicity, possibility of repair.", ["parable-of-polygons", "we-become-what-we-behold", "goodhart-school"]),
    ("echo-start-sandbox-end", "storytelling-structure", "Echo Start, Sandbox End", "Guided hook, open finish.", "Teach the pattern, then release control — Remember Forever-ish ends in free SR.", ["how-to-remember-anything-forever-ish", "sandbox-mode", "predict-then-reveal"]),
    ("neighborhood-grid", "visual-metaphor", "Neighborhood Grid", "Cells and local vision.", "Schelling's chessboard made tactile — only see neighbors, act locally.", ["parable-of-polygons", "schelling-segregation", "urban-percolation-equity"]),
    ("feedback-loop-circle", "visual-metaphor", "Feedback Loop Circle", "Arrows that bite their tail.", "Loopy's circles — stock, flow, delay made drawable.", ["loopy", "feedback-loops", "krebs-cycle-of-outrage"]),
    ("but-chain-narrative", "storytelling-structure", "BUT-Chain Narrative", "Structured counterintuitive beats.", "Nicky Case's therefore/but rhythm — each twist earns the next.", ["but-chain", "evolution-of-trust", "innocence-horror-hope"]),
]

TIER_D = [
    ("monty-hall-carnival", "Three doors. One car. Switch or stay?", "Monty Hall — switching wins 2/3 of the time.", "paradox", ["monty-hall", "predict-then-reveal", "base-rate-hospital"]),
    ("newcomb-predictor", "The box knows what you'll do.", "Newcomb's problem — one-boxers vs two-boxers.", "paradox", ["newcomb-paradox", "predict-then-reveal", "evolution-of-trust"]),
    ("simpsons-paradox-university", "Every department improved. The university got worse.", "Simpson's paradox — aggregation reverses trends.", "intuition", ["simpsons-paradox", "base-rate-hospital", "p-hacking-lab"]),
    ("friendship-paradox-club", "Your friends have more friends than you.", "Friendship paradox — degree bias in sampling.", "networks", ["friendship-paradox", "majority-illusion", "wisdom-and-madness-of-crowds"]),
    ("standing-ovation", "When does one person stand?", "Threshold cascade in an auditorium.", "systems", ["threshold-models", "complex-contagion-protest", "pluralistic-ignorance-pool"]),
    ("weak-tie-bridge", "Your weak tie got you the job.", "Granovetter bridges — strength of weak ties.", "networks", ["wisdom-and-madness-of-crowds", "information-cascade-falls", "complex-contagion"]),
    ("cobra-farm", "Pay for dead cobras. Breed cobras.", "Perverse incentives — Goodhart in the wild.", "systems", ["goodharts-law", "goodhart-school", "metric-hydra"]),
    ("braess-roads", "We added a highway. Traffic got worse.", "Braess paradox — selfish routing.", "systems", ["braess-paradox", "percolation-city", "social-choice"]),
    ("information-cascade-falls", "Jump because others jumped.", "Information cascade on a cliff edge.", "networks", ["information-cascades", "wisdom-and-madness-of-crowds", "pluralistic-ignorance-pool"]),
    ("base-rate-hospital", "The test said positive. You're probably fine.", "Bayes with base rates — prevalence matters.", "intuition", ["prosecutors-dna", "monty-hall-carnival", "bayesian-therapy"]),
    ("p-hacking-lab", "Keep running tests until p < 0.05.", "Multiple comparisons without correction.", "intuition", ["goodharts-law", "simpsons-paradox-university", "metric-hydra"]),
    ("prosecutors-dna", "One in a million match. Guilty?", "Prosecutor's fallacy — conflating P(E|I) and P(I|E).", "intuition", ["base-rate-hospital", "monty-hall", "bayesian-therapy"]),
    ("fat-tail-farm", "Average yield looks fine. You went bankrupt.", "Fat tails — mean hides ruin.", "intuition", ["ergodicity-street", "st-petersburg-paradox", "ergodicity"]),
    ("galton-board", "Random paths, normal pile.", "Central limit theorem as peg board.", "intuition", ["birthday-paradox", "probability-statistics", "base-rate-hospital"]),
    ("parrondo-casino", "Two losing games. Win by alternating.", "Parrondo's paradox — negative + negative = positive.", "paradox", ["st-petersburg-paradox", "prisoners-dilemma", "evolution-of-trust"]),
    ("bayesian-therapy", "Update beliefs with evidence.", "Bayes as interactive belief revision.", "intuition", ["base-rate-hospital", "prosecutors-dna", "monty-hall-carnival"]),
    ("metric-hydra", "Cut one metric. Two grow back.", "Goodhart hydra — metric gaming spawns proxies.", "systems", ["goodhart-school", "cobra-farm", "goodharts-law"]),
    ("stochastic-resonance-democracy", "Noise helps weak signals get heard.", "Stochastic resonance in collective choice.", "systems", ["social-choice", "to-build-a-better-ballot", "information-cascades"]),
    ("polya-culture-wars", "Minority becomes majority by chance.", "Pólya urn — path-dependent culture.", "networks", ["complex-contagion", "wisdom-and-madness-of-crowds", "schelling-segregation"]),
    ("deffuant-polarization", "Opinions move; camps form.", "Bounded confidence model — echo chambers emerge.", "networks", ["wisdom-and-madness-of-crowds", "krebs-cycle-of-outrage", "we-become-what-we-behold"]),
]

PARADOXES = [
    ("monty-hall", "Monty Hall Problem", "Switch doors — counterintuitively, you should.", ["monty-hall-carnival", "predict-then-reveal", "base-rate-hospital"]),
    ("simpsons-paradox", "Simpson's Paradox", "Trends reverse when you stratify.", ["simpsons-paradox-university", "p-hacking-lab", "base-rate-hospital"]),
    ("st-petersburg-paradox", "St. Petersburg Paradox", "Infinite expected value, finite willingness to pay.", ["fat-tail-farm", "ergodicity", "ergodicity-street"]),
    ("two-envelope-paradox", "Two Envelope Paradox", "Should you switch? Both answers seem valid.", ["st-petersburg-paradox", "newcomb-paradox", "bayesian-therapy"]),
    ("sleeping-beauty", "Sleeping Beauty Problem", "How much do you update on waking?", ["newcomb-paradox", "bayesian-therapy", "predict-then-reveal"]),
    ("newcomb-paradox", "Newcomb's Paradox", "Free will vs prediction.", ["newcomb-predictor", "predict-then-reveal", "evolution-of-trust"]),
    ("prisoners-dilemma", "Prisoner's Dilemma", "Individual rationality, collective disaster.", ["evolution-of-trust", "iterated-prisoners-dilemma", "commons-garden"]),
    ("tragedy-of-the-commons", "Tragedy of the Commons", "Shared resource, private incentive to overuse.", ["commons-garden", "ostrom-commons-design", "2009-ostrom-commons"]),
    ("braess-paradox", "Braess Paradox", "More capacity, worse flow.", ["braess-roads", "percolation-city", "social-choice"]),
    ("friendship-paradox", "Friendship Paradox", "Most people have fewer friends than their friends do.", ["friendship-paradox-club", "majority-illusion", "wisdom-and-madness-of-crowds"]),
    ("birthday-paradox", "Birthday Paradox", "23 people — 50% chance of a shared birthday.", ["galton-board", "probability-statistics", "monty-hall"]),
    ("unexpected-hanging", "Unexpected Hanging", "Logic eats itself on surprise.", ["predict-then-reveal", "newcomb-paradox", "sleeping-beauty"]),
]

EXPERIMENTS = [
    ("milgram-obedience", "Milgram Obedience Experiments", "Authority overrides conscience — in a lab.", ["asch-conformity", "stanford-prison-experiment", "pluralistic-ignorance-pool"]),
    ("asch-conformity", "Asch Conformity Experiments", "Wrong answers become contagious.", ["milgram-obedience", "pluralistic-ignorance-pool", "standing-ovation"]),
    ("stanford-prison-experiment", "Stanford Prison Experiment", "Roles reshape behavior — controversial but iconic.", ["milgram-obedience", "role-as-system", "we-become-what-we-behold"]),
    ("wason-selection-task", "Wason Selection Task", "We confirm; we don't falsify.", ["invisible-gorilla", "cognitive-science", "base-rate-hospital"]),
    ("invisible-gorilla", "Invisible Gorilla", "Attention is narrow; you miss the obvious.", ["wason-selection-task", "cognitive-science", "we-become-what-we-behold"]),
    ("ultimatum-game", "Ultimatum Game", "Fairness beats pure payoff maximization.", ["evolution-of-trust", "prisoners-dilemma-tournament", "commons-garden"]),
    ("marshmallow-test", "Marshmallow Test", "Delay of gratification — and later nuance.", ["feedback-loops", "cognitive-science", "evolution-of-trust"]),
    ("stroop-experiment", "Stroop Experiment", "Automatic reading interferes with naming color.", ["cognitive-science", "invisible-gorilla", "wason-selection-task"]),
    ("centola-complex-contagion", "Centola Complex Contagion", "Online health behavior needs reinforced exposure.", ["complex-contagion", "2007-centola-complex-contagion", "complex-contagion-protest"]),
    ("prisoners-dilemma-tournament", "Prisoner's Dilemma Tournament", "Axelrod's iterated games — cooperation wins.", ["evolution-of-trust", "iterated-prisoners-dilemma", "prisoners-dilemma"]),
]

EVIDENCE = [
    ("2013-petrie-harassment-multiplier", "paper", "Petrie Harassment Multiplier (2013)", "Equal per-capita harassment rates still produce unequal harm across groups.", ["petrie-multiplier", "complex-systems", "social-science"]),
    ("1978-granovetter-threshold", "paper", "Granovetter Threshold (1978)", "Threshold models of collective behavior.", ["threshold-models", "standing-ovation", "complex-contagion-protest"]),
    ("2007-centola-complex-contagion", "paper", "Centola Complex Contagion (2007)", "Empirical evidence for complex contagion online.", ["complex-contagion", "centola-complex-contagion", "complex-contagion-protest"]),
    ("schelling-1971-dynamic-models", "paper", "Schelling Dynamic Models (1971)", "Micromotives and macro-segregation.", ["schelling-segregation", "parable-of-polygons", "micromotives-and-macrobehavior"]),
    ("2009-ostrom-commons", "paper", "Nobel: Ostrom Commons (2009)", "Governing the commons — design principles.", ["ostrom-commons-design", "commons-garden", "tragedy-of-the-commons"]),
    ("micromotives-and-macrobehavior", "book", "Micromotives and Macrobehavior", "Schelling's classic — segregation, sorting, tipping.", ["schelling-segregation", "schelling-1971-dynamic-models", "parable-of-polygons"]),
    ("explorable-explanations", "discipline", "Explorable Explanations", "The medium Bret Victor named — learn by manipulating.", ["nicky-case", "agent-placement", "predict-then-reveal"]),
    ("complex-systems", "discipline", "Complex Systems", "Emergence, networks, feedback — the systems wing.", ["emergence", "schelling-segregation", "feedback-loops"]),
    ("game-theory", "discipline", "Game Theory", "Strategic interaction — cooperation and defection.", ["evolution-of-trust", "prisoners-dilemma", "social-choice"]),
    ("probability-statistics", "discipline", "Probability & Statistics", "Uncertainty, base rates, paradoxes.", ["monty-hall", "base-rate-hospital", "birthday-paradox"]),
    ("cognitive-science", "discipline", "Cognitive Science", "How minds decide, attend, and err.", ["invisible-gorilla", "wason-selection-task", "adventures-with-anxiety"]),
    ("nicky-case", "designer", "Nicky Case", "Gallery of Masters anchor — nine canon explorables.", ["parable-of-polygons", "evolution-of-trust", "we-become-what-we-behold"]),
]


def write_thy():
    promote_schelling()
    for i, (slug, title, wing, hook, body_text, related) in enumerate(THY, 2):
        if slug == "schelling-segregation":
            continue
        fm = {
            "id": f"THY-{i:04d}",
            "type": "theory",
            "slug": slug,
            "title": title,
            "summary": hook,
            "status": "canonical",
            "wing": wing,
            "created": "2026-06-26",
            "updated": "2026-06-26",
            "related": {"theories": related[:3], "simulations": {"existing": ["parable-of-polygons"] if slug != "emergence" else []}},
            "explorable": {"verdict": "essential", "best_medium": "web-simulation", "best_medium_stars": 4},
        }
        body = f"""# {title}

> **Hook:** *{hook}*

## Why this belongs in the museum

{body_text}

## Play it

See related exhibits — especially [[{related[0]}]].

## Related exhibits

""" + " · ".join(f"[[{r}]]" for r in related) + """

## Discovery suggestions

- [ ] Link to evidence papers when built
- [ ] Add native sim embed when Tier S ships
"""
        write_page(slug, "theory", fm, body)


def write_design():
    for i, (slug, typ, title, hook, body_text, related) in enumerate(DESIGN, 1):
        prefix = {"interaction-pattern": "PAT", "visual-metaphor": "MET", "storytelling-structure": "STR"}[typ]
        fm = {
            "id": f"{prefix}-{i:04d}",
            "type": typ,
            "slug": slug,
            "title": title,
            "summary": hook,
            "status": "canonical",
            "wing": "design",
            "created": "2026-06-26",
            "updated": "2026-06-26",
            "related": {"design": {"patterns": related[:2]}},
            "explorable": {"verdict": "essential", "best_medium": "web-simulation", "best_medium_stars": 4},
        }
        body = f"""# {title}

> **Pattern:** *{hook}*

## Definition

{body_text}

## Where to steal it

""" + " · ".join(f"[[{r}]]" for r in related) + """

## Discovery suggestions

- [ ] Annotated GIF from canon exhibit
- [ ] Anti-pattern callouts
"""
        write_page(slug, typ, fm, body)


def write_tier_d():
    for i, (slug, title, tagline, wing, related) in enumerate(TIER_D, 19):
        fm = {
            "id": f"SIM-{i:04d}",
            "type": "simulation-concept",
            "slug": slug,
            "title": title,
            "summary": tagline,
            "status": "canonical",
            "wing": wing,
            "build_difficulty": "medium",
            "created": "2026-06-26",
            "updated": "2026-06-26",
            "explorable": {"verdict": "essential", "best_medium": "web-simulation", "best_medium_stars": 4},
            "related": {"theories": related[:2]},
        }
        body = f"""# {title}

> **Tagline:** *{tagline}*

## E.C.H.O.

| Element | Spec |
|---------|------|
| **Hook** | {title} |
| **Engine** | See research doc |
| **Control** | Predict-then-reveal primary |
| **Outcome gap** | User commits before reveal |

## Related exhibits

""" + " · ".join(f"[[{r}]]" for r in related) + """
"""
        write_page(slug, "simulation-concept", fm, body)


def write_paradoxes():
    for i, (slug, title, hook, related) in enumerate(PARADOXES, 1):
        fm = {
            "id": f"PAR-{i:04d}",
            "type": "paradox",
            "slug": slug,
            "title": title,
            "summary": hook,
            "status": "canonical",
            "wing": "paradox",
            "created": "2026-06-26",
            "updated": "2026-06-26",
            "related": {"paradoxes": related[:2], "simulations": {"concepts": [related[0] + "-carnival" if "monty" in related[0] else related[0]]}},
            "explorable": {"verdict": "essential", "best_medium": "web-simulation", "best_medium_stars": 5},
        }
        body = f"""# {title}

> **Paradox:** *{hook}*

## Why play it

Reading the solution isn't the same as feeling your intuition break. Commit with [[predict-then-reveal]] before the reveal.

## Related exhibits

""" + " · ".join(f"[[{r}]]" for r in related) + """
"""
        write_page(slug, "paradox", fm, body)


def write_experiments():
    for i, (slug, title, hook, related) in enumerate(EXPERIMENTS, 1):
        fm = {
            "id": f"EXP-{i:04d}",
            "type": "experiment",
            "slug": slug,
            "title": title,
            "summary": hook,
            "status": "canonical",
            "wing": "systems",
            "created": "2026-06-26",
            "updated": "2026-06-26",
            "related": {"experiments": related[:2]},
            "explorable": {"verdict": "essential", "best_medium": "web-simulation", "best_medium_stars": 4},
        }
        body = f"""# {title}

> **Finding:** *{hook}*

## Museum note

Classic psychology experiments — ethical context required in classroom use. Pair with [[role-as-system]] and [[pluralistic-ignorance-pool]].

## Related exhibits

""" + " · ".join(f"[[{r}]]" for r in related) + """
"""
        write_page(slug, "experiment", fm, body)


def write_evidence():
    for i, (slug, typ, title, summary, related) in enumerate(EVIDENCE, 1):
        prefix = {"paper": "PAP", "book": "BOK", "discipline": "DIS", "designer": "DSN"}[typ]
        fm = {
            "id": f"{prefix}-{i:04d}",
            "type": typ,
            "slug": slug,
            "title": title,
            "summary": summary,
            "status": "canonical",
            "wing": "evidence" if typ == "paper" else typ,
            "created": "2026-06-26",
            "updated": "2026-06-26",
            "related": {"theories": related[:2] if typ in ("paper", "book") else [], "disciplines": related[:2] if typ == "discipline" else []},
        }
        body = f"""# {title}

> **Anchor:** *{summary}*

## Links to play

""" + " · ".join(f"[[{r}]]" for r in related) + """
"""
        write_page(slug, typ, fm, body)


def type_label(typ: str) -> str:
    return {
        "existing-explorable": "EXE",
        "simulation-concept": "SIM",
        "theory": "THY",
        "interaction-pattern": "PAT",
        "visual-metaphor": "MET",
        "storytelling-structure": "STR",
        "paradox": "PAR",
        "experiment": "EXP",
        "paper": "PAP",
        "book": "BOK",
        "discipline": "DIS",
        "designer": "DSN",
    }.get(typ, typ.upper()[:3])


def build_export_entry(slug: str, title: str, summary: str, typ: str, wing: str, related: list[str], embed_url: str | None = None, play_url: str | None = None) -> dict:
    entry = {
        "slug": slug,
        "title": title,
        "summary": summary,
        "hook": summary,
        "type": type_label(typ),
        "wing": wing,
        "status": "canonical",
        "related": related,
    }
    if embed_url:
        entry["embedUrl"] = embed_url
    if play_url:
        entry["playUrl"] = play_url
    return entry
