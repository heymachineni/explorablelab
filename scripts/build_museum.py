#!/usr/bin/env python3
"""Build ExplorableLab museum floor: canonical pages, collections, paths, site data."""

from __future__ import annotations

import json
import re
from pathlib import Path

from canonical_promote import (
    THY,
    DESIGN,
    TIER_D,
    PARADOXES,
    EXPERIMENTS,
    EVIDENCE,
    build_export_entry,
    write_design,
    write_evidence,
    write_experiments,
    write_paradoxes,
    write_thy,
    write_tier_d,
)

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
SITE_DATA = ROOT / "site" / "src" / "data"

# --- EXE canon (from research autopsies) ---

EXE_PAGES = {
    "parable-of-polygons": {
        "id": "EXE-0001",
        "year": 2014,
        "url": "https://ncase.me/polygons/",
        "summary": "Drag unhappy shapes; watch benign bias produce segregation — then undo it with anti-bias.",
        "theories": ["schelling-segregation", "emergence", "threshold-models"],
        "patterns": ["agent-placement", "parameter-slider", "sandbox-mode", "innocence-horror-hope"],
        "body": """# Parable of the Polygons

> **Play:** [ncase.me/polygons](https://ncase.me/polygons/) · **With:** Vi Hart · **Year:** 2014

## Why this belongs in the museum

Reading "33% tolerance threshold" is abstract. Dragging one unhappy triangle and watching clusters crystallize makes segregation *felt*. You perform the reasonable action and cause the outcome yourself — complicity without accusation.

## Theory

Thomas Schelling's dynamic segregation model (1971), extended with **anti-bias** (demand for diversity) as a desegregation mechanism.

## Interaction spine

1. **Manual agent placement** — you move unhappy shapes
2. **Automated simulation** — watch the system run
3. **Parameter slider** — tolerance threshold
4. **Initial-condition flip** — world starts segregated
5. **Sandbox** — prove generality

## Why interaction beats reading

The aha requires **complicity**: one benign move cracks an integrated grid. Zero bias doesn't undo history; anti-bias can.

## Design principles demonstrated

- Agent-based micro-rules → macro emergence
- Innocence → horror → hope narrative arc
- [[agent-placement]] · [[neighborhood-grid]] · [[sandbox-mode]]

## Related exhibits

- [[schelling-segregation]] · [[evolution-of-trust]] · [[goodhart-school]]

## Discovery suggestions

- [ ] Real-world data layer (census tracts)
- [ ] Three+ group extension
- [ ] Annotated edge to [[schelling-segregation]] — 90% coverage
""",
    },
    "evolution-of-trust": {
        "id": "EXE-0002",
        "year": 2017,
        "url": "https://ncase.me/trust/",
        "summary": "Play iterated Prisoner's Dilemma; watch cooperation evolve — and break under noise.",
        "theories": ["iterated-prisoners-dilemma", "emergence"],
        "patterns": ["playable-game", "but-chain", "parameter-slider", "sandbox-mode"],
        "body": """# Evolution of Trust

> **Play:** [ncase.me/trust](https://ncase.me/trust/) · **Year:** 2017

## Why this belongs in the museum

Payoff matrices are dead on paper. Playing against Tit-for-Tat, Grudger, and Cheater makes strategy visceral. Betrayal hurts because you invested rounds.

## Theory

Iterated Prisoner's Dilemma; Axelrod's evolution of cooperation; noise, forgiveness (Win-Stay Lose-Shift), reputation, population dynamics.

## Interaction spine (BUT-chain)

Cooperation works **BUT** one-shot fails **BUT** repeated works **BUT** noise breaks it **BUT** forgiveness fixes it — plot twists as pedagogy.

## Why interaction beats reading

Each chapter destroys the previous solution. Historical hook: Christmas truce. Tournament reveal is a set-piece.

## Related exhibits

- [[iterated-prisoners-dilemma]] · [[commons-garden]] · [[we-become-what-we-behold]]

## Discovery suggestions

- [ ] Institution / enforcement chapter as sim extension
""",
    },
    "we-become-what-we-behold": {
        "id": "EXE-0003",
        "year": 2016,
        "url": "https://ncase.me/ballot/",
        "summary": "You are the camera. What you photograph causes the tragedy.",
        "theories": ["feedback-loops", "information-cascades"],
        "patterns": ["role-as-system", "innocence-horror-hope"],
        "body": """# We Become What We Behold

> **Play:** [ncase.me/social-media](https://ncase.me/social-media/) · **Year:** 2016

## Why this belongs in the museum

You *are* the camera. Choosing what to photograph *causes* the tragedy — procedural rhetoric (Ian Bogost). The mechanic *is* the thesis; no lecture needed.

## Theory

Media feedback loops; selective attention; othering; reinforcing cycles.

## Interaction spine

**Role-play as system** → single mechanic (photograph) → escalating feedback loop → closed parable (no sandbox).

## Why interaction beats reading

~5 minutes. Cute accelerates to horror. Ending reframes entire playthrough: *you caused this.*

## Related exhibits

- [[krebs-cycle-of-outrage]] · [[wisdom-and-madness-of-crowds]] · [[majority-illusion]]

## Discovery suggestions

- [ ] Pair with [[polya-culture-wars]] hybrid sim
""",
    },
    "to-build-a-better-ballot": {
        "id": "EXE-0004",
        "year": 2016,
        "url": "https://ncase.me/ballot/",
        "summary": "Same voters, six voting systems — six different winners.",
        "theories": ["social-choice"],
        "patterns": ["comparison-view", "ladder-of-abstraction", "sandbox-mode"],
        "body": """# To Build a Better Ballot

> **Play:** [ncase.me/ballot](https://ncase.me/ballot/) · **Year:** 2016

## Why this belongs in the museum

Same voter preferences, different systems → different winners. Must be *seen* simultaneously — Ka-Ping Yee-style comparison view.

## Theory

Social choice; FPTP, IRV, Borda, Approval, Score, Condorcet; spoiler effect; Arrow's theorem implications.

## Interaction spine

Single voter concrete → scale to election → **side-by-side system switcher** → spoiler scenario → shareable sandbox.

## Related exhibits

- [[social-choice]] · [[newcomb-predictor]] · [[stochastic-resonance-democracy]]

## Discovery suggestions

- [ ] Ranked-choice policy sandbox for user's locale
""",
    },
    "loopy": {
        "id": "EXE-0005",
        "year": 2017,
        "url": "https://ncase.me/loopy/",
        "summary": "Draw feedback loops; press play; watch circles close.",
        "theories": ["feedback-loops"],
        "patterns": ["sandbox-mode"],
        "body": """# Loopy

> **Play:** [ncase.me/loopy](https://ncase.me/loopy/) · **Year:** 2017

## Why this belongs in the museum

Static diagrams don't *run*. Drawing and simulating your own loops externalizes mental models — climate, addiction, poverty traps.

## Theory

Reinforcing vs balancing feedback loops; causal loop diagrams; systems thinking.

## Interaction spine

**Authoring tool** → live simulation → no prescribed narrative. You become author.

## Related exhibits

- [[feedback-loops]] · [[feedback-loop-circle]] · [[goodhart-school]]

## Discovery suggestions

- [ ] Embed Loopy diagrams in other exhibit pages
""",
    },
    "fireflies": {
        "id": "EXE-0006",
        "year": 2017,
        "url": "https://ncase.me/fireflies/",
        "summary": "Chaos synchronizes — no conductor required.",
        "theories": ["emergence"],
        "patterns": ["parameter-slider", "sandbox-mode"],
        "body": """# Fireflies

> **Play:** [ncase.me/fireflies](https://ncase.me/fireflies/) · **Year:** 2017

## Why this belongs in the museum

Phase alignment is dynamic; you must watch desync → sync. Beauty as pedagogical tool — collective pulse is emotionally satisfying.

## Theory

Coupled oscillators; Kuramoto-style self-synchronization; emergence without leader.

## Interaction spine

Parameter play (coupling, disorder) → sandbox.

## Related exhibits

- [[emergence]] · [[standing-ovation]] · [[sandpile-avalanche]]
""",
    },
    "wisdom-and-madness-of-crowds": {
        "id": "EXE-0007",
        "year": 2018,
        "url": "https://ncase.me/crowds/",
        "summary": "Same message, different network — opposite fate.",
        "theories": ["information-cascades", "complex-contagion"],
        "patterns": ["graph-rewiring", "comparison-view"],
        "body": """# Wisdom and/or Madness of Crowds

> **Play:** [ncase.me/crowds](https://ncase.me/crowds/) · **Year:** 2018

## Why this belongs in the museum

Network structure changes spread of the *same* message. Topology must be manipulable — rewire and compare.

## Theory

Social learning; information cascades; echo chambers vs bridge networks; complex contagion.

## Interaction spine

Place message → watch diffusion → **rewire network** → compare topologies.

## Related exhibits

- [[majority-illusion]] · [[information-cascade-falls]] · [[weak-tie-bridge]]

## Discovery suggestions

- [ ] Pair with [[complex-contagion-protest]] — threshold type vs topology
""",
    },
    "adventures-with-anxiety": {
        "id": "EXE-0008",
        "year": 2019,
        "url": "https://ncase.me/anxiety/",
        "summary": "Play as the anxiety voice — recognition, not instruction.",
        "theories": ["feedback-loops"],
        "patterns": ["role-as-system", "innocence-horror-hope"],
        "body": """# Adventures with Anxiety

> **Play:** [ncase.me/anxiety](https://ncase.me/anxiety/) · **Year:** 2019

## Why this belongs in the museum

You play *as* the anxiety voice — role reversal creates insight impossible from a pamphlet. Comedy lowers defenses; horror lands.

## Theory

Anxiety as protective feedback loop gone wrong; CBT-adjacent reframing.

## Interaction spine

Play the antagonist system → escalation → reframe.

## Related exhibits

- [[we-become-what-we-behold]] · [[feedback-loops]] · [[krebs-cycle-of-outrage]]
""",
    },
    "how-to-remember-anything-forever-ish": {
        "id": "EXE-0009",
        "year": 2018,
        "url": "https://ncase.me/remember/",
        "summary": "The explorable is the instrument — Orbit proves spacing while teaching it.",
        "theories": [],
        "patterns": ["predict-then-reveal", "sandbox-mode"],
        "body": """# How to Remember Anything Forever-ish

> **Play:** [ncase.me/remember](https://ncase.me/remember/) · **Year:** 2018

## Why this belongs in the museum

Self-referential design: Orbit-style flashcards *demonstrate* spaced repetition while teaching it. You forget during reading; the tool saves you.

## Theory

Spaced repetition; forgetting curve (Ebbinghaus); testing effect.

## Interaction spine

Explorable + embedded SR tool → self-referential proof.

## Related exhibits

- [[predict-then-reveal]] · [[echo-start-sandbox-end]]
""",
    },
}

# Fix WBWWB URL in content - I used wrong url for we-become-what-we-behold
EXE_PAGES["we-become-what-we-behold"]["url"] = "https://ncase.me/social-media/"

TIER_S = {
    "petrie-multiplier": ("Equal meanness. Unequal harm.", "Petrie multiplier (2013) — harassment scales with group asymmetry even at equal per-capita rates.", "systems", 9.2),
    "ergodicity-street": ("The average person doesn't exist.", "Ensemble averages mislead when processes are non-ergodic.", "intuition", 9.0),
    "percolation-city": ("One more closed road killed the hospital.", "Connectivity collapses at critical probability p_c.", "systems", 8.8),
    "majority-illusion": ("Everyone you see agrees. That's the bug.", "Local neighborhoods distort global opinion.", "networks", 8.7),
    "goodhart-school": ("When the test became the target, learning died.", "Metric optimization decouples from goal.", "systems", 8.9),
    "simpsons-paradox-university": ("Every department improved. The university got worse.", "Aggregate trends reverse when stratified.", "intuition", 8.8),
    "complex-contagion-protest": ("One person kneeling isn't a movement. Ten might be.", "Behavior needs multiple exposures.", "networks", 8.6),
    "base-rate-hospital": ("The test said positive. You're probably fine.", "P(disease|+) depends on prevalence.", "intuition", 8.7),
    "braess-roads": ("We added a highway. Traffic got worse.", "Selfish routing can increase travel time.", "systems", 8.8),
    "pluralistic-ignorance-pool": ("Nobody wanted to. Everyone did.", "Private rejection, public conformity.", "systems", 8.5),
    "sandpile-avalanche": ("Mountains of sand. Power-law avalanches.", "Self-organized criticality.", "systems", 8.4),
    "commons-garden": ("Share the garden — or watch it die.", "Ostrom principles vs tragedy of commons.", "systems", 8.7),
    "maxwells-demon-box": ("Sort hot from cold — pay in entropy.", "Information has thermodynamic cost.", "systems", 8.3),
    "jane-jacobs-corner": ("Four conditions for street life.", "Urban vitality from stacked factors.", "systems", 8.4),
    "urban-percolation-equity": ("Segregation disconnects services.", "Percolation × Schelling hybrid.", "systems", 8.6),
    "contagion-of-courage": ("Bravery spreads differently than ideas.", "Dual threshold hybrid.", "networks", 8.5),
    "ergodic-inequality": ("Average wealth up. You went bust.", "Ergodicity × inequality hybrid.", "intuition", 8.5),
    "krebs-cycle-of-outrage": ("Outrage loops thicken pathways.", "WBWWB × Hebbian hybrid.", "canon", 8.6),
}

NATIVE_SIMS = {
    "petrie-multiplier": "/sims/petrie-multiplier/",
    "ergodicity-street": "/sims/ergodicity-street/",
}

COLLECTIONS = [
    ("start-here-first-visit", "Start Here: First Visit", 15, "curiosity → surprise → complicity → hope",
     ["parable-of-polygons", "monty-hall-carnival", "petrie-multiplier", "schelling-segregation", "evolution-of-trust"]),
    ("paradoxes-everyone-should-play", "Paradoxes Everyone Should Play Once", 25, "bet → wrong → learn",
     ["monty-hall-carnival", "simpsons-paradox-university", "newcomb-predictor", "braess-roads", "friendship-paradox-club", "st-petersburg-paradox", "two-envelope-paradox", "birthday-paradox"]),
    ("innocence-horror-hope", "Innocence → Horror → Hope", 20, "warm → dread → agency",
     ["parable-of-polygons", "we-become-what-we-behold", "goodhart-school", "commons-garden", "evolution-of-trust"]),
    ("why-groups-act-weird", "Why Groups Act Weird", 20, "alone → together → strange",
     ["pluralistic-ignorance-pool", "asch-conformity", "standing-ovation", "milgram-obedience", "complex-contagion-protest", "information-cascade-falls"]),
    ("math-that-lies-to-you", "Math That Lies to You", 30, "confidence → doubt → precision",
     ["simpsons-paradox-university", "base-rate-hospital", "ergodicity-street", "friendship-paradox-club", "monty-hall-carnival", "p-hacking-lab", "prosecutors-dna"]),
    ("systems-that-shape-society", "Systems That Shape Society", 35, "individual → structure → intervention",
     ["schelling-segregation", "goodharts-law", "ostrom-commons-design", "braess-roads", "commons-garden", "cobra-farm", "jane-jacobs-corner", "metric-hydra"]),
    ("steal-from-nicky-case", "Steal From Nicky Case", 40, "watch → extract → apply",
     ["parable-of-polygons", "evolution-of-trust", "we-become-what-we-behold", "to-build-a-better-ballot", "loopy", "agent-placement", "but-chain"]),
    ("trust-betrayal-forgiveness", "Trust, Betrayal, and Forgiveness", 20, "cooperate → defect → repair",
     ["evolution-of-trust", "iterated-prisoners-dilemma", "commons-garden", "ultimatum-game", "prisoners-dilemma-tournament"]),
    ("networks-youre-inside-of", "Networks You're Inside Of", 25, "node → graph → illusion",
     ["wisdom-and-madness-of-crowds", "majority-illusion", "weak-tie-bridge", "complex-contagion-protest", "information-cascade-falls", "friendship-paradox-club"]),
    ("ideas-every-designer-should-understand", "Ideas Every Designer Should Understand", 45, "pattern → principle → exhibit",
     ["agent-placement", "but-chain", "predict-then-reveal", "comparison-view", "sandbox-mode", "role-as-system", "emergence", "goodharts-law", "feedback-loops", "threshold-models"]),
    ("under-five-minutes", "Under 5 Minutes", 5, "quick hits",
     ["we-become-what-we-behold", "fireflies", "cobra-farm", "friendship-paradox-club", "how-to-remember-anything-forever-ish", "adventures-with-anxiety"]),
    ("build-these-next-tier-s", "Build These Next (Tier S)", 0, "spec → build → ship",
     list(TIER_S.keys())),
]

PATHS = [
    ("graph-in-one-hour", "The Graph in One Hour", 60, ["schelling-segregation", "emergence", "agent-placement", "parable-of-polygons", "petrie-multiplier", "ergodicity-street", "evolution-of-trust"]),
    ("design-your-first-explorable", "Design Your First Explorable", 45, ["steal-from-nicky-case", "agent-placement", "but-chain", "predict-then-reveal", "sandbox-mode", "petrie-multiplier"]),
    ("classroom-monday", "Classroom Ready: Monday Morning", 30, ["asch-conformity", "milgram-obedience", "pluralistic-ignorance-pool", "base-rate-hospital", "standing-ovation"]),
    ("from-paradox-to-proof", "From Paradox to Proof", 40, ["monty-hall-carnival", "base-rate-hospital", "simpsons-paradox-university", "2013-petrie-harassment-multiplier"]),
    ("systems-weekend", "Systems Thinking Weekend", 90, ["feedback-loops", "loopy", "commons-garden", "goodhart-school", "braess-roads", "sandpile-avalanche"]),
]

WINGS = [
    ("wing-paradox", "Hall of Paradoxes", "Commit before the reveal.", ["monty-hall-carnival", "newcomb-predictor", "simpsons-paradox-university", "parrondo-casino"]),
    ("wing-systems", "Systems Garden", "Local rules, global patterns.", ["schelling-segregation", "emergence", "commons-garden", "sandpile-avalanche", "feedback-loops"]),
    ("wing-intuition", "Street of Misconceptions", "Your gut is wrong. Good.", ["ergodicity-street", "base-rate-hospital", "simpsons-paradox-university", "fat-tail-farm"]),
    ("wing-networks", "City of Networks", "Topology beats content.", ["wisdom-and-madness-of-crowds", "majority-illusion", "weak-tie-bridge", "complex-contagion-protest"]),
    ("wing-design", "Studio of Explorable Design", "Steal like an artist.", ["agent-placement", "but-chain", "predict-then-reveal", "innocence-horror-hope"]),
    ("wing-canon", "Gallery of Masters", "Nicky Case and friends.", list(EXE_PAGES.keys())),
    ("wing-evidence", "Evidence Library", "Papers behind the play.", ["2013-petrie-harassment-multiplier", "1978-granovetter-threshold", "schelling-1971-dynamic-models"]),
]


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


def find_path(slug: str, typ: str) -> Path | None:
    for p in CONTENT.rglob("*.md"):
        if p.name == "README.md":
            continue
        t = p.read_text(encoding="utf-8", errors="replace")
        if re.search(rf'^slug:\s*"?{re.escape(slug)}"?', t, re.M) and re.search(rf'^type:\s*"?{typ}"?', t, re.M):
            return p
    return None


def default_path(slug: str, typ: str) -> Path:
    mapping = {
        ("existing-explorable",): CONTENT / "simulations/existing" / f"{slug}.md",
        ("simulation-concept",): CONTENT / "simulations/concepts" / f"{slug}.md",
        ("theory",): CONTENT / "theories/complex-systems" / f"{slug}.md",
        ("interaction-pattern",): CONTENT / "design/interaction-patterns" / f"{slug}.md",
        ("visual-metaphor",): CONTENT / "design/visual-metaphors" / f"{slug}.md",
        ("storytelling-structure",): CONTENT / "design/storytelling-structures" / f"{slug}.md",
        ("paradox",): CONTENT / "paradoxes/probability" / f"{slug}.md",
        ("experiment",): CONTENT / "experiments" / f"{slug}.md",
    }
    for keys, path in mapping.items():
        if typ in keys:
            return path
    return CONTENT / "disciplines" / f"{slug}.md"


def write_exe():
    for slug, data in EXE_PAGES.items():
        path = CONTENT / "simulations/existing" / f"{slug}.md"
        fm = {
            "id": data["id"],
            "type": "existing-explorable",
            "slug": slug,
            "title": slug.replace("-", " ").title().replace(" Of ", " of ").replace(" To ", " to "),
            "summary": data["summary"],
            "status": "canonical",
            "year": data["year"],
            "url": data["url"],
            "created": "2026-06-26",
            "updated": "2026-06-26",
            "wing": "canon",
            "related": {"theories": data.get("theories", []), "design": {"patterns": data.get("patterns", [])}},
            "explorable": {
                "verdict": "essential",
                "why_interaction": data["summary"],
                "best_medium": "web-simulation",
                "best_medium_stars": 5,
            },
        }
        titles = {
            "parable-of-polygons": "Parable of the Polygons",
            "evolution-of-trust": "Evolution of Trust",
            "we-become-what-we-behold": "We Become What We Behold",
            "to-build-a-better-ballot": "To Build a Better Ballot",
            "wisdom-and-madness-of-crowds": "Wisdom and/or Madness of Crowds",
            "how-to-remember-anything-forever-ish": "How to Remember Anything Forever-ish",
            "adventures-with-anxiety": "Adventures with Anxiety",
        }
        fm["title"] = titles.get(slug, fm["title"])
        path.write_text(fm_block(fm) + "\n\n" + data["body"] + "\n", encoding="utf-8")


def write_tier_s():
    for i, (slug, (tagline, theory, wing, composite)) in enumerate(TIER_S.items(), 1):
        path = find_path(slug, "simulation-concept") or default_path(slug, "simulation-concept")
        title = tagline.split(".")[0] if "." in tagline else slug.replace("-", " ").title()
        fm = {
            "id": f"SIM-{i:04d}",
            "type": "simulation-concept",
            "slug": slug,
            "title": title,
            "summary": tagline,
            "status": "canonical",
            "wing": wing,
            "build_difficulty": "medium",
            "build_estimate_weeks": 3,
            "created": "2026-06-26",
            "updated": "2026-06-26",
            "scores": {"composite": composite},
            "explorable": {"verdict": "essential", "best_medium": "web-simulation", "best_medium_stars": 5},
            "related": {"theories": ["emergence", "schelling-segregation"][:1]},
        }
        body = f"""# {title}

> **Tagline:** *{tagline}*

## Theory

{theory}

Full build spec: [`EXPLORABLE_EXPLANATIONS_RESEARCH.md`](../../EXPLORABLE_EXPLANATIONS_RESEARCH.md) Phase 7.

## E.C.H.O.

| Element | Spec |
|---------|------|
| **Hook** | {tagline} |
| **Engine** | See research one-pager |
| **Control** | Primary slider(s) named in spec |
| **Outcome gap** | User commits before reveal |

## Build status

| Status | Notes |
|--------|-------|
| Spec | ✅ Canonical |
| Prototype | {'✅ `' + NATIVE_SIMS[slug] + '`' if slug in NATIVE_SIMS else '⬜ Queue'} |
| Ship | Tier S priority |

## Related exhibits

- [[schelling-segregation]] · [[parable-of-polygons]] · [[agent-placement]]

## Discovery suggestions

- [ ] Link to evidence papers when canonical
"""
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(fm_block(fm) + "\n\n" + body + "\n", encoding="utf-8")


def write_collections():
    d = COLLECTIONS
    out_dir = ROOT / "indices/collections"
    out_dir.mkdir(parents=True, exist_ok=True)
    site_cols = []
    for i, (slug, title, mins, arc, stops) in enumerate(d, 1):
        fm = {
            "id": f"COL-{i:04d}",
            "type": "collection",
            "slug": slug,
            "title": title,
            "summary": f"{len(stops)} exhibits · ~{mins} min" if mins else "Build queue reference",
            "status": "canonical",
            "time_minutes": mins,
            "emotional_arc": arc,
            "stops": stops,
            "created": "2026-06-26",
            "updated": "2026-06-26",
        }
        body = [f"# {title}", "", f"**Time:** ~{mins} minutes · **Arc:** {arc}", "", "## Stops", ""]
        for j, s in enumerate(stops, 1):
            body.append(f"{j}. [[{s}]]")
        body.append("")
        (out_dir / f"{slug}.md").write_text(fm_block(fm) + "\n\n" + "\n".join(body) + "\n", encoding="utf-8")
        site_cols.append({
            "slug": slug, "title": title, "summary": fm["summary"],
            "time_minutes": mins, "emotional_arc": arc, "stops": stops,
        })
    SITE_DATA.mkdir(parents=True, exist_ok=True)
    (SITE_DATA / "collections.json").write_text(json.dumps({"collections": site_cols}, indent=2), encoding="utf-8")


def write_paths():
    out = ROOT / "indices/paths"
    out.mkdir(parents=True, exist_ok=True)
    for slug, title, mins, stops in PATHS:
        fm = {"slug": slug, "title": title, "time_minutes": mins, "stops": stops, "status": "canonical"}
        body = f"# {title}\n\n**Time:** {mins} min\n\n" + "\n".join(f"- [[{s}]]" for s in stops) + "\n"
        (out / f"{slug}.md").write_text(fm_block(fm) + "\n\n" + body, encoding="utf-8")


def write_wings():
    out = ROOT / "indices/wings"
    out.mkdir(parents=True, exist_ok=True)
    for slug, title, tagline, stops in WINGS:
        fm = {"slug": slug, "title": title, "tagline": tagline, "stops": stops, "status": "canonical"}
        body = f"# {title}\n\n*{tagline}*\n\n" + "\n".join(f"- [[{s}]]" for s in stops) + "\n"
        (out / f"{slug}.md").write_text(fm_block(fm) + "\n\n" + body, encoding="utf-8")


EXE_TITLES = {
    "parable-of-polygons": "Parable of the Polygons",
    "evolution-of-trust": "Evolution of Trust",
    "we-become-what-we-behold": "We Become What We Behold",
    "to-build-a-better-ballot": "To Build a Better Ballot",
    "wisdom-and-madness-of-crowds": "Wisdom and/or Madness of Crowds",
    "how-to-remember-anything-forever-ish": "How to Remember Anything Forever-ish",
    "adventures-with-anxiety": "Adventures with Anxiety",
    "loopy": "Loopy",
    "fireflies": "Fireflies",
}


def find_content_path(slug: str) -> str | None:
    for p in CONTENT.rglob("*.md"):
        if p.name == "README.md":
            continue
        t = p.read_text(encoding="utf-8", errors="replace")
        if re.search(rf'^slug:\s*"?{re.escape(slug)}"?\s*$', t, re.M):
            return str(p.relative_to(ROOT))
    return None


def attach_content_path(entry: dict) -> dict:
    path = find_content_path(entry["slug"])
    if path:
        entry["contentPath"] = path
    return entry


def export_site_data():
    exhibits = []
    for slug, data in EXE_PAGES.items():
        title = EXE_TITLES.get(slug, slug.replace("-", " ").title())
        exhibits.append(attach_content_path(build_export_entry(
            slug, title, data["summary"], "existing-explorable", "canon",
            data.get("theories", []) + data.get("patterns", []),
        )))
    for slug, (tagline, _, wing, _comp) in TIER_S.items():
        title = tagline.split(".")[0] if "." in tagline else slug.replace("-", " ").title()
        exhibits.append(attach_content_path(build_export_entry(
            slug, title, tagline, "simulation-concept", wing,
            ["schelling-segregation", "agent-placement", "parameter-slider"],
        )))
    exhibits.append(attach_content_path(build_export_entry(
        "schelling-segregation", "Schelling Segregation Model",
        "Mild individual preference for similar neighbors produces dramatic macro-segregation.",
        "theory", "systems",
        ["emergence", "threshold-models", "agent-placement"],
    )))
    for slug, title, wing, hook, _body, related in THY:
        if slug == "schelling-segregation":
            continue
        exhibits.append(attach_content_path(build_export_entry(slug, title, hook, "theory", wing, related)))
    for slug, typ, title, hook, _body, related in DESIGN:
        exhibits.append(attach_content_path(build_export_entry(slug, title, hook, typ, "design", related)))
    for slug, title, tagline, wing, related in TIER_D:
        exhibits.append(attach_content_path(build_export_entry(slug, title, tagline, "simulation-concept", wing, related)))
    for slug, title, hook, related in PARADOXES:
        exhibits.append(attach_content_path(build_export_entry(slug, title, hook, "paradox", "paradox", related)))
    for slug, title, hook, related in EXPERIMENTS:
        exhibits.append(attach_content_path(build_export_entry(slug, title, hook, "experiment", "systems", related)))
    for slug, typ, title, summary, related in EVIDENCE:
        wing = "evidence" if typ == "paper" else typ
        exhibits.append(attach_content_path(build_export_entry(slug, title, summary, typ, wing, related)))
    SITE_DATA.mkdir(parents=True, exist_ok=True)
    (SITE_DATA / "canonical.json").write_text(json.dumps({"exhibits": exhibits}, indent=2), encoding="utf-8")


def write_canonical_index():
    slugs = (
        list(EXE_PAGES.keys()) + list(TIER_S.keys()) + ["schelling-segregation"]
        + [t[0] for t in THY if t[0] != "schelling-segregation"]
        + [d[0] for d in DESIGN] + [t[0] for t in TIER_D]
        + [p[0] for p in PARADOXES] + [e[0] for e in EXPERIMENTS] + [ev[0] for ev in EVIDENCE]
    )
    lines = ["# Canonical Exhibits — Museum Floor", "", f"**{len(slugs)} promoted exhibits**", ""]
    for s in slugs:
        lines.append(f"- [[{s}]]")
    out = ROOT / "indices/awesome"
    out.mkdir(parents=True, exist_ok=True)
    (out / "canonical-exhibits.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    write_exe()
    write_tier_s()
    write_thy()
    write_design()
    write_tier_d()
    write_paradoxes()
    write_experiments()
    write_evidence()
    write_collections()
    write_paths()
    write_wings()
    export_site_data()
    write_canonical_index()
    print("Museum build complete: 105 canonical slugs, collections, paths, wings, site data")


if __name__ == "__main__":
    main()
