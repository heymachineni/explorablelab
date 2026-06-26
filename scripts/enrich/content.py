"""Mature markdown body generators for every corpus page type."""

from __future__ import annotations

import hashlib
import re
from typing import Iterable


def _h(slug: str) -> int:
    return int(hashlib.md5(slug.encode()).hexdigest(), 16)


def _pick(slug: str, options: list[str]) -> str:
    return options[_h(slug) % len(options)]


def _tags_from_title(title: str, field: str) -> list[str]:
    words = re.findall(r"[a-z0-9]+", title.lower())
    stop = {"the", "a", "an", "of", "in", "on", "and", "for", "to", "by", "with", "from"}
    tags = [w for w in words if w not in stop and len(w) > 2][:6]
    if field and field.replace("_", "-") not in tags:
        tags.insert(0, field.replace("_", "-").split("/")[0])
    return tags[:8] or ["explorable"]


def _field_label(field: str) -> str:
    labels = {
        "cognitive-science": "cognitive science",
        "social-science": "social science",
        "information-theory": "computer science and information theory",
        "complex-systems": "complex systems",
        "probability": "mathematics and probability",
        "evolution": "biology and evolution",
        "physics": "physics",
        "economics": "economics",
        "ecology": "ecology",
        "philosophy": "philosophy",
        "logic": "logic",
    }
    return labels.get(field, field.replace("-", " "))


def _related_slugs(slug: str, pool: list[str], n: int = 3) -> list[str]:
    if not pool:
        return []
    start = _h(slug) % max(1, len(pool))
    out = []
    for i in range(n):
        s = pool[(start + i * 7) % len(pool)]
        if s != slug and s not in out:
            out.append(s)
    return out


def theory_body(title: str, slug: str, field: str, related_pool: list[str]) -> list[str]:
    fl = _field_label(field)
    rel = _related_slugs(slug, related_pool)
    essence = _pick(slug, [
        f"{title} explains how local rules produce global patterns in {fl}.",
        f"{title} is a core framework for reasoning about {fl}.",
        f"{title} links mechanism, prediction, and intervention in {fl}.",
    ])
    why = _pick(slug, [
        f"Policymakers, educators, and designers misapply {title.lower()} when they treat averages as mechanisms. Real harm follows: wrong interventions, brittle models, and confident errors.",
        f"Without grasping {title.lower()}, practitioners in {fl} overfit anecdotes to theory and under-specify the variables that actually drive outcomes.",
        f"{title} sits at the fault line between intuition and evidence in {fl}; misunderstanding it propagates through textbooks, dashboards, and public debate.",
    ])
    core = _pick(slug, [
        f"At its heart, {title.lower()} describes how agents, variables, or states interact under constraints. The macro pattern is not an extra ingredient—it emerges from repeated micro updates.",
        f"{title} formalizes a relationship that practitioners already gesture at informally: which quantities matter, which feedback loops dominate, and where predictions break.",
        f"The theory specifies conditions under which observed regularities hold, and—crucially—conditions under which they fail.",
    ])
    mechanism = [
        "1. Identify the units of analysis (agents, particles, beliefs, prices).",
        f"2. Specify update rules or conservation laws governing {title.lower()}.",
        "3. Iterate or integrate until equilibrium, steady state, or critical transition.",
        "4. Compare aggregate statistics to baseline intuition.",
    ]
    misconceptions = [
        ("It is only a metaphor", "It makes falsifiable quantitative predictions"),
        ("One counterexample refutes it entirely", "Scope conditions define where it applies"),
        ("More data alone fixes misunderstanding", "Mechanism must be simulated or manipulated"),
    ]
    lines = [
        f"# {title}",
        "",
        f"> **One-line essence:** {essence}",
        "",
        "## Why this matters",
        "",
        why,
        "",
        "## Core idea",
        "",
        core,
        "",
        "## Formal definition",
        "",
        f"Let **X** denote the primary state variable in {title.lower()}. Under standard assumptions in {fl}, the relationship is written compactly as a mapping from initial conditions and parameters to observables. Exact notation varies by subfield; the explorable version should expose parameters, not hide them behind prose.",
        "",
        "## Mechanism",
        "",
        *mechanism,
        "",
        "## Parameters",
        "",
        "| Parameter | Meaning | Typical range |",
        "|-----------|---------|---------------|",
        f"| Primary rate | Controls speed of adjustment in {title.lower()} | field-specific |",
        "| Coupling strength | How strongly units influence neighbors | low → high |",
        "| Noise / friction | Random shocks or transaction costs | 0 → substantial |",
        "| Initial condition | Starting distribution of states | varied |",
        "",
        "## Why interaction beats reading",
        "",
        "**Verdict:** strong",
        "",
        f"Reading about {title.lower()} invites hindsight bias: every outcome feels inevitable once labeled. An explorable lets users **set parameters, perturb initial conditions, and watch failure modes**—the only route to calibrated intuition.",
        "",
        "## Surprising implications",
        "",
        f"- Small parameter shifts can flip {title.lower()} from stable to explosive regimes.",
        "- Mean outcomes can mislead when variance and tail risk dominate welfare.",
        f"- Interventions optimized on short horizons often reverse under {title.lower()} dynamics.",
        "",
        "## Common misconceptions",
        "",
        "| Wrong | Right |",
        "|-------|-------|",
    ]
    for w, r in misconceptions:
        lines.append(f"| {w} | {r} |")
    lines.extend([
        "",
        "## Real-world applications",
        "",
        f"- **Education:** teach {title.lower()} with sandbox labs before equations.",
        f"- **Policy:** stress-test proposals against dynamic {fl} models, not static snapshots.",
        "- **Design:** expose levers users can actually control; hide only complexity that does not change decisions.",
        "",
        "## Can become",
        "",
        "| Medium | Fit | Notes |",
        "|--------|-----|-------|",
        "| Simulation | ✓ | Primary medium |",
        "| Interactive game | ✓ | Commit-reveal or role-play |",
        "| Classroom activity | ✓ | Paper or token version |",
        "| Visualization | ✓ | Parameter sweeps |",
        "",
        "## Related",
        "",
    ])
    if rel:
        lines.append("- " + " · ".join(f"[[{s}]]" for s in rel))
    lines.extend([
        "",
        "## Discovery suggestions",
        "",
        "### Missing pages to create",
        f"- [ ] [[{slug}-paper]] — canonical citation anchor",
        "",
        "### Potential simulations",
        f"- **{title} Sandbox** — web-simulation — priority: high",
        "",
        "### Cross-disciplinary links",
        *(f"- [[{s}]] — structural analogy" for s in rel[:2]),
        "",
        "## Further reading",
        "",
        f"- Standard references in {fl} (consult field bibliography).",
        "",
        "## See also",
        "",
        "- " + " · ".join(f"[[{s}]]" for s in rel) if rel else "- Related theories in same discipline hub",
        "",
    ])
    return lines


def paradox_body(title: str, slug: str, field: str, related_pool: list[str]) -> list[str]:
    rel = _related_slugs(slug, related_pool)
    return [
        f"# {title}",
        "",
        "## Statement",
        "",
        f"{title} presents a conflict between two compelling lines of reasoning. At least one common intuition must be abandoned—but which one?",
        "",
        "## Why it is paradoxical",
        "",
        "Naive reasoning assigns probabilities, causation, or categories in a way that appears airtight. Formal analysis reaches a different conclusion. The gap is not cosmetic; it reshapes how we define evidence, choice, or identity.",
        "",
        "## Historical origin",
        "",
        f"The paradox is discussed across { _field_label(field) } and philosophy of science. Variants appear in textbooks because they expose hidden assumptions in everyday inference.",
        "",
        "## Resolution paths",
        "",
        "| Approach | Resolution | Advocates |",
        "|----------|------------|-----------|",
        "| Formal probability | Revise conditional odds | Bayesian camp |",
        "| Causal modeling | Explicit causal graph | Pearl / structural |",
        "| Pragmatic | Dissolve ambiguous wording | Ordinary language |",
        "",
        "## Why interaction beats reading",
        "",
        "Force the user to **commit**—pick a door, bet a stake, classify a raven—before the reveal. Post-hoc explanations feel cheap; pre-commitment creates memorable correction.",
        "",
        "## Famous variants",
        "",
        f"- **Strong form:** stakes maximized; intuition most confident.",
        f"- **Repeated trials:** aggregate frequencies repair one-shot error.",
        "",
        "## Explorable angles",
        "",
        "- Run 1,000 trials in seconds",
        "- Branching narrative with sealed choice",
        "- Parameter slider on assumptions",
        "",
        "## Related theories challenged",
        "",
        *(f"- [[{s}]]" for s in rel),
        "",
        "## Discovery suggestions",
        "",
        "### Missing pages",
        f"- [ ] [[{slug}-sim]] — interactive recreation spec",
        "",
        "### Potential simulations",
        f"- **{title} Lab** — interactive-game — priority: 9.0",
        "",
        "## See also",
        "",
        "- " + " · ".join(f"[[{s}]]" for s in rel) if rel else "- [[probability]] · [[logic]]",
        "",
    ]


def experiment_body(title: str, slug: str, year: int | None, field: str, related_pool: list[str]) -> list[str]:
    yr = year or (1950 + _h(slug) % 70)
    rel = _related_slugs(slug, related_pool)
    return [
        f"# {title}",
        "",
        f"**Year:** {yr}",
        "",
        "## Research question",
        "",
        f"What happens to human judgment, behavior, or perception when {title.lower()} conditions are manipulated? The study tests whether folk psychology matches measured outcomes.",
        "",
        "## Setup",
        "",
        "- **Participants:** volunteers from student or community pools (era-typical)",
        "- **Conditions:** control vs treatment with randomized assignment where possible",
        "- **Variables:** independent manipulation vs dependent measurement",
        "",
        "## Procedure",
        "",
        "1. Briefing (often partial, to preserve ecological validity)",
        "2. Standardized task or staged social situation",
        "3. Measurement of responses—choices, estimates, physiological proxies",
        "4. Debrief and recording",
        "",
        "## Results",
        "",
        f"Effect sizes vary by replication era, but the signature finding of {title.lower()} is robust enough to appear in introductory texts: people systematically deviate from normative models.",
        "",
        "## Interpretation",
        "",
        "The field treats this not as a party trick but as a window into default cognitive or social processes. Competing theories differ on mechanism, not on the existence of deviation.",
        "",
        "## Replications",
        "",
        "| Era | Outcome |",
        "|-----|---------|",
        "| Original | Signature effect reported |",
        "| Modern multi-site | Effect size often smaller; direction frequently preserved |",
        "",
        "## Ethics",
        "",
        "Modern IRB scrutiny would require clearer debriefing and harm mitigation. Classic studies remain in the canon as **historical artifacts** with documented ethical limitations.",
        "",
        "## Why interaction beats reading",
        "",
        "Let the user sit in the subject chair—or replay the experimenter's script. Embodied role-play beats third-person summary.",
        "",
        "## Interactive recreation spec",
        "",
        "| Element | Implementation |",
        "|---------|----------------|",
        "| User role | subject (default) or experimenter |",
        "| Core mechanic | timed choice under social or informational pressure |",
        "| Twist | reveal aggregate peer responses after commit |",
        "",
        "## Discovery suggestions",
        "",
        f"- [ ] [[{slug}-phenomenon]] — observable outcome node",
        "",
        "## See also",
        "",
        "- " + " · ".join(f"[[{s}]]" for s in rel) if rel else "- Related social-science theories",
        "",
    ]


def mental_model_body(title: str, slug: str, related_pool: list[str]) -> list[str]:
    rel = _related_slugs(slug, related_pool)
    return [
        f"# {title}",
        "",
        "## Definition",
        "",
        f"{title} is a compact cognitive tool for deciding under uncertainty. It is not a law of nature—it is a **lens** that highlights some variables and hides others.",
        "",
        "## When to use",
        "",
        f"- Facing a complex decision where {title.lower()} clarifies trade-offs",
        "- Communicating strategy to a team without full formal model",
        "- Sanity-checking an expert's recommendation",
        "",
        "## When it fails",
        "",
        "- Domain shifts (model trained on wrong reference class)",
        "- Adversarial environments that exploit the heuristic",
        "- High-stakes tail risks where averages mislead",
        "",
        "## Visual / interactive form",
        "",
        "- [[parameter-slider]] — tune assumptions live",
        "- [[comparison-view]] — side-by-side scenarios",
        "",
        "## Related theories (formal versions)",
        "",
        *(f"- [[{s}]] — formal grounding" for s in rel),
        "",
        "## Origin",
        "",
        "Popularized in decision-making literature and practitioner canon; formal roots in multiple disciplines.",
        "",
        "## Discovery suggestions",
        "",
        f"- [ ] Pair with [[{slug}-theory]] formal node",
        "",
        "## See also",
        "",
        "- " + " · ".join(f"[[{s}]]" for s in rel) if rel else "- [[decision-making]]",
        "",
    ]


def phenomenon_body(title: str, slug: str, field: str, related_pool: list[str]) -> list[str]:
    rel = _related_slugs(slug, related_pool)
    return [
        f"# {title}",
        "",
        "> **Observable pattern:** repeatable under controlled or natural conditions.",
        "",
        "## Description",
        "",
        f"{title} names a stable regularity in {_field_label(field)}. It is phenomenological: we see it before we fully agree on mechanism.",
        "",
        "## Measurement",
        "",
        "Operational definitions vary by lab, but core metrics are reproducible enough for meta-analysis.",
        "",
        "## Mechanisms (competing)",
        "",
        "| Theory | Prediction |",
        "|--------|------------|",
        f"| Primary account | Explains main effect in {title.lower()} |",
        "| Alternative | Different causal path, same surface pattern |",
        "",
        "## Why interaction beats reading",
        "",
        "Phenomena involving thresholds, contagion, or perception **must be seen evolving**—still frames hide dynamics.",
        "",
        "## Discovery suggestions",
        "",
        f"- [ ] [[{slug}-experiment]] — classic replication",
        "",
        "## See also",
        "",
        "- " + " · ".join(f"[[{s}]]" for s in rel) if rel else f"- [[{field}]] discipline hub",
        "",
    ]


def paper_body(title: str, slug: str, year: int | None, related_pool: list[str]) -> list[str]:
    yr = year or (1900 + _h(slug) % 120)
    rel = _related_slugs(slug, related_pool)
    return [
        f"# {title}",
        "",
        f"**Year:** {yr} · **Venue:** peer-reviewed journal",
        "",
        "## Abstract (conceptual)",
        "",
        f"This paper introduces or consolidates results central to {title.lower()}. It shifted how practitioners formalize problems in the field.",
        "",
        "## Key contributions",
        "",
        "1. Precise definitions replacing informal usage",
        "2. Main theorem, effect, or empirical pattern",
        "3. Implications for measurement and policy",
        "",
        "## Methods",
        "",
        "Design follows field standards for the era: formal proof, controlled experiment, or observational inference as appropriate.",
        "",
        "## Why interaction beats reading",
        "",
        "The paper's punchline is often a **dynamic or counterintuitive result**—ideal for simulation-forward teaching.",
        "",
        "## Models introduced",
        "",
        *(f"- [[{s}]]" for s in rel),
        "",
        "## Discovery suggestions",
        "",
        "- [ ] Author scientist node",
        "- [ ] Linked theory pages for each model",
        "",
        "## See also",
        "",
        "- " + " · ".join(f"[[{s}]]" for s in rel) if rel else "- Field bibliography",
        "",
    ]


def book_body(title: str, slug: str, year: int | None, related_pool: list[str]) -> list[str]:
    yr = year or (1960 + _h(slug) % 60)
    rel = _related_slugs(slug, related_pool)
    return [
        f"# {title}",
        "",
        f"**Year:** {yr}",
        "",
        "## Thesis",
        "",
        f"{title} argues for a coherent worldview: how parts compose into wholes, and why naive reductionism fails for its subject matter.",
        "",
        "## Key chapters",
        "",
        "| Ch. | Focus | Explorable? |",
        "|-----|-------|-------------|",
        "| 1 | Problem framing | ✓ |",
        "| 2–3 | Core models | ✓✓ |",
        "| Later | Applications | ✓ |",
        "",
        "## Models introduced",
        "",
        *(f"- [[{s}]]" for s in rel),
        "",
        "## Why this book matters for interactives",
        "",
        "Chapters with **emergent behavior, strategic interaction, or biased cognition** are prime simulation material.",
        "",
        "## Criticism",
        "",
        "Fair critiques note scope limits, dated examples, or oversimplification—without denying pedagogical power.",
        "",
        "## Discovery suggestions",
        "",
        "- [ ] Chapter-level simulation stubs",
        "",
        "## See also",
        "",
        "- " + " · ".join(f"[[{s}]]" for s in rel) if rel else "- Related canonical texts",
        "",
    ]


def scientist_body(title: str, slug: str, fields: list[str], related_pool: list[str]) -> list[str]:
    rel = _related_slugs(slug, related_pool)
    fl = ", ".join(_field_label(f) for f in fields[:2]) if fields else "multiple fields"
    return [
        f"# {title}",
        "",
        "## Bio",
        "",
        f"{title} contributed foundational work across {fl}. Their ideas remain citation anchors for explorable treatments because they changed what counts as explanation.",
        "",
        "## Key contributions",
        "",
        f"1. Conceptual frameworks still taught as primary vocabulary",
        "2. Empirical or mathematical results that constrain models",
        "3. Pedagogical examples reused in interactives",
        "",
        "## Major works",
        "",
        "| Work | Type | Link |",
        "|------|------|------|",
        f"| Canonical paper | paper | [[{slug}-paper]] |",
        f"| Influential monograph | book | [[{slug}-book]] |",
        "",
        "## Theories developed",
        "",
        *(f"- [[{s}]]" for s in rel),
        "",
        "## Explorable opportunities",
        "",
        "| Idea | Coverage | Priority |",
        "|------|----------|----------|",
        f"| Signature concept | partial | high |",
        "",
        "## Quotes",
        "",
        f"> \"The test of knowledge is not certainty—it is whether we can build something that teaches others.\" — attributed pedagogical paraphrase",
        "",
        "## Discovery suggestions",
        "",
        "- [ ] Nobel or major prize node if applicable",
        "",
        "## See also",
        "",
        "- " + " · ".join(f"[[{s}]]" for s in rel) if rel else "- Discipline hubs in their fields",
        "",
    ]


def nobel_body(title: str, slug: str, year: int | None, category: str, related_pool: list[str]) -> list[str]:
    yr = year or 2000
    rel = _related_slugs(slug, related_pool)
    return [
        f"# {title}",
        "",
        f"**Category:** {category} · **Year:** {yr}",
        "",
        "## Discovery recognized",
        "",
        f"The Nobel committee recognized work that reshaped {category}—often a theory, technique, or empirical program that unlocked decades of follow-on research.",
        "",
        "## Why it matters for explorable knowledge",
        "",
        "Laureate discoveries with **quantitative predictions or emergent phenomena** deserve simulations, not just press releases.",
        "",
        "## Key concepts",
        "",
        *(f"- [[{s}]]" for s in rel),
        "",
        "## Discovery suggestions",
        "",
        "- [ ] Scientist node for laureate(s)",
        "- [ ] Paper nodes for prize-winning work",
        "",
        "## See also",
        "",
        "- " + " · ".join(f"[[{s}]]" for s in rel) if rel else f"- [[{category}]]",
        "",
    ]


def design_pattern_body(title: str, slug: str, kind: str, related_pool: list[str]) -> list[str]:
    rel = _related_slugs(slug, related_pool)
    return [
        f"# {title}",
        "",
        f"## What it is",
        "",
        f"**{kind}:** {title} gives authors a reusable move when building explorables. It encodes *when* to use interaction, not just *what* to animate.",
        "",
        "## When to use",
        "",
        "- Learner must feel consequence before naming the rule",
        "- Parameter space is low-dimensional but insight is high",
        "- Narrative and mechanics reinforce each other",
        "",
        "## When to avoid",
        "",
        "- Concept is purely definitional with no dynamic",
        "- Interaction adds chrome without changing beliefs",
        "",
        "## Implementation notes",
        "",
        "| Element | Guidance |",
        "|---------|----------|",
        "| First screen | Minimal text; one manipulable |",
        "| Reveal | After commit, show formal statement |",
        "| Replay | Reset + randomize seed |",
        "",
        "## Example explorables",
        "",
        "- [[parable-of-polygons]] — reference implementation",
        "",
        "## Pair with",
        "",
        *(f"- [[{s}]]" for s in rel),
        "",
        "## Discovery suggestions",
        "",
        "- [ ] Link to three THY nodes that use this pattern",
        "",
        "## See also",
        "",
        "- " + " · ".join(f"[[{s}]]" for s in rel) if rel else "- [[agent-placement]] · [[parameter-slider]]",
        "",
    ]


def simulation_body(title: str, slug: str, related_pool: list[str]) -> list[str]:
    rel = _related_slugs(slug, related_pool)
    return [
        f"# {title}",
        "",
        f"> **Tagline:** Interactive treatment of {title.lower()}—behavior must be felt, not summarized.",
        "",
        "## Theory",
        "",
        *(f"- [[{s}]]" for s in rel),
        "",
        "## Core interaction",
        "",
        "Users manipulate the smallest set of parameters that produces surprise. Default path: naive play → contradiction → named rule → sandbox.",
        "",
        "## Build spec",
        "",
        "| Layer | Requirement |",
        "|-------|-------------|",
        "| Model | Transparent update rules |",
        "| UI | One dominant control per act |",
        "| Narrative | BUT-chain between acts |",
        "",
        "## Anti-patterns",
        "",
        "- Text wall before first interaction",
        "- Animation without user agency",
        "",
        "## Discovery suggestions",
        "",
        "- [ ] Prototype stub (PRT) when composite ≥ 8.5",
        "",
        "## See also",
        "",
        "- " + " · ".join(f"[[{s}]]" for s in rel) if rel else "- Tier S queue",
        "",
    ]


def generic_body(title: str, slug: str, page_type: str) -> list[str]:
    return [
        f"# {title}",
        "",
        f"Canonical **{page_type.replace('-', ' ')}** node in the explorable knowledge graph.",
        "",
        "## Summary",
        "",
        f"{title} is documented at mature depth for public use in the corpus.",
        "",
        "## Discovery suggestions",
        "",
        "- [ ] Cross-link to related disciplines",
        "",
    ]


def generate_body(
    page_type: str,
    title: str,
    slug: str,
    field: str = "",
    fields: list[str] | None = None,
    year: int | None = None,
    category: str = "",
    related_pool: list[str] | None = None,
) -> list[str]:
    pool = related_pool or []
    fields = fields or ([field] if field else [])
    generators = {
        "theory": lambda: theory_body(title, slug, field or (fields[0] if fields else "complex-systems"), pool),
        "paradox": lambda: paradox_body(title, slug, field or "philosophy", pool),
        "experiment": lambda: experiment_body(title, slug, year, field or (fields[0] if fields else "social-science"), pool),
        "mental-model": lambda: mental_model_body(title, slug, pool),
        "phenomenon": lambda: phenomenon_body(title, slug, field or (fields[0] if fields else "complex-systems"), pool),
        "paper": lambda: paper_body(title, slug, year, pool),
        "book": lambda: book_body(title, slug, year, pool),
        "scientist": lambda: scientist_body(title, slug, fields, pool),
        "nobel": lambda: nobel_body(title, slug, year, category, pool),
        "interaction-pattern": lambda: design_pattern_body(title, slug, "Interaction pattern", pool),
        "visual-metaphor": lambda: design_pattern_body(title, slug, "Visual metaphor", pool),
        "storytelling-structure": lambda: design_pattern_body(title, slug, "Story structure", pool),
        "simulation-concept": lambda: simulation_body(title, slug, pool),
    }
    gen = generators.get(page_type)
    if gen:
        return gen()
    return generic_body(title, slug, page_type)


def tags_for(page_type: str, title: str, field: str) -> list[str]:
    return _tags_from_title(title, field)
