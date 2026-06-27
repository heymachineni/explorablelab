"""Write expansion topic hubs and concept pages for ExplorableLab."""

from __future__ import annotations

from canonical_promote import CONTENT, fm_block, write_page

# (slug, title, summary, related_slugs)
HUBS: list[tuple[str, str, str, list[str]]] = [
    (
        "human-behaviour-psychology",
        "Human Behaviour and Psychology",
        "Why people act against their interests and repeat familiar patterns.",
        ["cognitive-dissonance", "defense-mechanisms", "psychological-projection", "asch-conformity"],
    ),
    (
        "cognitive-biases",
        "Cognitive Biases",
        "How mental shortcuts quietly shape beliefs, decisions, and debates.",
        ["confirmation-bias", "availability-heuristic", "hindsight-bias", "dunning-kruger-effect"],
    ),
    (
        "probability-and-risk",
        "Probability and Risk",
        "Why rare events often matter more than averages and predictions fail.",
        ["black-swan-events", "fat-tailed-distributions", "regression-to-the-mean", "st-petersburg-paradox"],
    ),
    (
        "technology-and-society",
        "Technology and Society",
        "How tools reshape behaviour, influence, and privacy.",
        ["surveillance-capitalism", "algorithmic-bias", "digital-panopticon", "we-become-what-we-behold"],
    ),
    (
        "behavioural-finance",
        "Behavioural Finance",
        "Why markets move on emotion, narratives, and fear more than logic.",
        ["loss-aversion", "herd-behaviour", "overconfidence-bias", "goodharts-law"],
    ),
    (
        "evolutionary-psychology",
        "Evolutionary Psychology",
        "How ancient instincts shape modern behaviour.",
        ["mate-selection-theory", "kin-selection", "status-signaling", "evolution-of-trust"],
    ),
    (
        "history-of-power",
        "History of Power",
        "How authority is earned, justified, challenged, and lost.",
        ["elite-circulation", "legitimacy-and-authority", "soft-power", "machiavellian-realism"],
    ),
    (
        "economics-incentives",
        "Economics: Incentives over Intentions",
        "Why people respond to rewards and penalties more than good intentions.",
        ["principal-agent-problem", "moral-hazard", "unintended-consequences", "cobra-farm"],
    ),
    (
        "statistics-interpretation",
        "Statistics: Interpretation",
        "How numbers persuade, mislead, and influence narratives.",
        ["correlation-vs-causation", "survivorship-bias", "base-rate-neglect", "simpsons-paradox"],
    ),
    (
        "sociology-of-status",
        "Sociology of Status",
        "Why prestige, class, and hierarchy shape social life.",
        ["cultural-capital", "status-anxiety", "social-stratification", "schelling-segregation"],
    ),
    (
        "decision-making-uncertainty",
        "Decision-Making Under Uncertainty",
        "Why confidence often outperforms accuracy in complex situations.",
        ["bounded-rationality", "heuristics-decision-making", "satisficing", "predict-then-reveal"],
    ),
    (
        "scientific-method-skepticism",
        "Scientific Method and Skepticism",
        "How knowledge is tested, questioned, and refined.",
        ["falsifiability", "replication-crisis", "peer-review-process", "p-hacking-lab"],
    ),
    (
        "negotiation-game-theory",
        "Negotiation and Game Theory",
        "How cooperation, conflict, and strategy interact.",
        ["prisoners-dilemma", "nash-equilibrium", "zero-sum-games", "iterated-prisoners-dilemma"],
    ),
    (
        "cultural-history",
        "Cultural History",
        "How societies remember, forget, and reinterpret the past.",
        ["collective-memory", "myth-creation", "historical-storytelling", "information-cascades"],
    ),
    (
        "language-and-framing",
        "Language and Framing",
        "Why how something is said often matters more than what is said.",
        ["linguistic-relativity", "euphemism-cycles", "emotionally-charged-language", "framing-effects-media"],
    ),
    (
        "moral-psychology",
        "Moral Psychology",
        "Why thoughtful people strongly disagree about values.",
        ["moral-foundations-theory", "in-group-bias", "value-diversity", "ultimatum-game"],
    ),
    (
        "philosophy-of-ethics",
        "Philosophy of Ethics",
        "How people reason about right, wrong, and moral gray areas.",
        ["utilitarianism", "deontology", "virtue-ethics", "moral-relativism"],
    ),
    (
        "geopolitics",
        "Geopolitics",
        "Why countries often behave like insecure actors on a world stage.",
        ["balance-of-power", "deterrence-theory", "multipolar-world-dynamics", "evolution-of-trust"],
    ),
    (
        "media-literacy",
        "Media Literacy",
        "How narratives are framed, amplified, and selectively highlighted.",
        ["agenda-setting", "framing-effects-media", "propaganda-model", "echo-chambers"],
    ),
    (
        "systems-thinking",
        "Systems Thinking",
        "Why solving one problem often creates another.",
        ["feedback-loops", "second-order-effects", "unintended-system-behavior", "emergence"],
    ),
    (
        "scaling-and-growth",
        "Scaling and Growth",
        "How organisms, cities, and organisations change as they get bigger.",
        ["square-cube-law", "metabolic-scaling", "scaling-growth-life-and-organizations", "domino-effect"],
    ),
]

# type, folder, slug, title, summary, wing, related, body sections as dict
CONCEPTS: list[dict] = [
    {
        "type": "theory",
        "folder": "physics",
        "slug": "square-cube-law",
        "title": "Square–Cube Law",
        "summary": "Volume grows faster than surface area as size increases — reshaping what is possible at each scale.",
        "wing": "systems",
        "related": ["metabolic-scaling", "scaling-growth-life-and-organizations", "emergence"],
        "essence": "When length doubles, area quadruples and volume octuples — so strength, heat loss, and transport constraints change with size.",
        "why": "Explains why ants carry many times their body weight but elephants cannot jump, why cities need different infrastructure than villages, and why the same design rules do not scale linearly from prototype to institution.",
        "core": "For similar shapes, surface area scales as *L*² while volume (and mass) scales as *L*³. Any process limited by surface area — cooling, respiration, structural load through cross-section — becomes **relatively weaker** as size increases. Processes tied to volume — weight, metabolic demand — grow **faster**.",
        "mechanism": "1. Hold shape constant and increase characteristic length *L*. 2. Area ∝ *L*²; volume ∝ *L*³. 3. Strength of limbs and bones scales roughly with cross-sectional area (*L*²). 4. Weight scales with volume (*L*³). 5. At sufficient size, weight outruns strength — Galileo noted this for bones; modern biomechanics confirms it across species.",
        "implications": "- Small organisms can be proportionally stronger and faster relative to body mass.\n- Large animals need disproportionately thick limbs and slower movement.\n- Engineering and organisations face analogous constraints when scaling processes designed for small teams.",
        "reading": "- Galilei, G. (1638). *Two New Sciences* — bones and scaling arguments.\n- Schmidt-Nielsen, K. (1984). *Scaling: Why is Animal Size So Important?* Cambridge University Press.",
    },
    {
        "type": "theory",
        "folder": "evolution",
        "slug": "metabolic-scaling",
        "title": "Metabolic Scaling",
        "summary": "Metabolic rate does not scale linearly with body mass — Kleiber's 3/4 power law links biology to networks.",
        "wing": "systems",
        "related": ["square-cube-law", "scaling-growth-life-and-organizations", "percolation"],
        "essence": "A mouse's metabolism per gram dwarfs an elephant's — metabolic rate scales sublinearly with mass across species.",
        "why": "Predicts lifespans, food needs, cancer rates, and city energy use. Connects geometry (square–cube) to network supply (circulatory, vascular, organisational communication).",
        "core": "Basal metabolic rate *B* often scales as *B* ∝ *M*^{3/4} across mammals (Kleiber, 1932), not *M*^{2/3} as simple surface-area arguments suggest. Network models (West, Brown, Enquist) argue fractal-like delivery networks optimise transport under constraint.",
        "mechanism": "1. Metabolic demand tied to cell mass (volume). 2. Supply through branching networks (blood, air, infrastructure). 3. Network optimisation yields quarter-power exponents in idealised models. 4. Empirical scatter exists — scaling exponents vary by taxa and measurement.",
        "implications": "- Larger animals live slower metabolic lives per cell; lifespans and heartbeats scale predictably.\n- Cities sometimes show superlinear/sublinear scaling in outputs vs population — analogies to biology are debated but productive.",
        "reading": "- Kleiber, M. (1932). Body size and metabolism. *Hilgardia*, 6(11), 315–353.\n- West, G. B., Brown, J. H., & Enquist, B. J. (1997). A general model for the origin of allometric scaling laws in biology. *Science*, 276(5309), 122–126.",
    },
    {
        "type": "theory",
        "folder": "complex-systems",
        "slug": "scaling-growth-life-and-organizations",
        "title": "Scaling Growth in Life and Organizations",
        "summary": "Organisms and institutions grow under different constraints — biology, networks, and coordination costs shape what scales.",
        "wing": "systems",
        "related": ["square-cube-law", "metabolic-scaling", "emergence", "goodharts-law"],
        "essence": "Growth is not uniform enlargement — new levels of structure appear when old rules hit geometric, metabolic, or social limits.",
        "why": "Startups, cities, bodies, and ecosystems all grow — but doubling size does not double every capability. Misunderstanding scaling drives failed expansion, bureaucratic bloat, and surprise collapse.",
        "core": "**Biological growth** follows developmental programs constrained by square–cube and metabolic scaling. **Organisational growth** adds layers — hierarchy, specialisation, process — when coordination via informal networks breaks down. Geoffrey West and colleagues compare cities to organisms; others emphasise that firms face selection and strategy, not only physics.",
        "mechanism": "1. Early growth often super-linear in outputs (learning, network effects). 2. Constraints emerge: communication overhead (~ Brooks's law), metabolic/network limits in biology. 3. New structures (organs, departments, platforms) absorb complexity. 4. Without adaptation, growth hits diminishing returns or fragility (see [[fat-tailed-distributions]]).",
        "implications": "- Copying a small-team culture at 10× headcount rarely works without new institutions.\n- Biological metaphors for companies are illuminating but incomplete — incentives and power matter.",
        "reading": "- West, G. (2017). *Scale*. Penguin.\n- Bettencourt, L. M. A. et al. (2007). Growth, innovation, scaling, and the pace of life in cities. *PNAS*, 104(17), 7301–7306.",
    },
    {
        "type": "mental-model",
        "folder": None,
        "slug": "domino-effect",
        "title": "Domino Effect",
        "summary": "A small trigger propagates through a prepared chain — order and spacing determine whether collapse is local or total.",
        "wing": "systems",
        "related": ["threshold-models", "percolation", "information-cascades", "feedback-loops"],
        "essence": "One event knocks the next in sequence — the system was already arranged for propagation.",
        "why": "Bank runs, supply-chain failures, social contagion, and geopolitical escalation often look like dominoes — understanding spacing, thresholds, and buffers prevents catastrophising and identifies real vulnerability.",
        "core": "The domino effect is a **chain reaction** metaphor: elements in series with failure thresholds. Real systems add branching, redundancy, and heterogeneity — pure domino models are limits, not literal descriptions.",
        "mechanism": "1. Elements coupled so state change in one affects neighbours. 2. Each element has activation threshold. 3. Trigger exceeds first threshold; energy/information propagates. 4. Without gaps or damping, cascade continues.",
        "implications": "- Removing one link or increasing spacing stops cascades — policy relevance for firewalls, circuit breakers, cooling-off periods.\n- Confusing correlation in time with mechanical domino causality leads to bad forecasts.",
        "reading": "- Perrow, C. (1984). *Normal Accidents*. Princeton — tightly coupled systems.\n- Link to [[threshold-models]] and [[percolation]] for formal models.",
    },
]

# Additional concepts keyed by slug — compact batch for remaining topics
MORE_CONCEPTS: list[tuple[str, str, str, str, str, list[str]]] = [
    # slug, title, summary, wing, folder/type prefix, related
    ("cognitive-dissonance", "Cognitive Dissonance", "Mental discomfort when beliefs and actions conflict — often resolved by changing beliefs.", "systems", "cognitive-science", ["human-behaviour-psychology", "confirmation-bias", "asch-conformity"]),
    ("defense-mechanisms", "Defense Mechanisms", "Unconscious strategies that reduce anxiety by distorting perception of threat.", "systems", "cognitive-science", ["psychological-projection", "cognitive-dissonance", "human-behaviour-psychology"]),
    ("psychological-projection", "Psychological Projection", "Attributing one's own unacceptable feelings or motives to others.", "systems", "cognitive-science", ["defense-mechanisms", "in-group-bias", "human-behaviour-psychology"]),
    ("confirmation-bias", "Confirmation Bias", "Seeking and remembering evidence that supports what we already believe.", "intuition", "cognitive-science", ["cognitive-biases", "availability-heuristic", "predict-then-reveal"]),
    ("availability-heuristic", "Availability Heuristic", "Judging frequency by how easily examples come to mind.", "intuition", "cognitive-science", ["confirmation-bias", "hindsight-bias", "cognitive-biases"]),
    ("hindsight-bias", "Hindsight Bias", "After an outcome, believing it was predictable all along.", "intuition", "cognitive-science", ["availability-heuristic", "overconfidence-bias", "cognitive-biases"]),
    ("dunning-kruger-effect", "Dunning–Kruger Effect", "Low competence can impair recognition of one's own incompetence.", "intuition", "cognitive-science", ["overconfidence-bias", "cognitive-biases", "scientific-method-skepticism"]),
    ("black-swan-events", "Black Swan Events", "Rare, high-impact outcomes that look predictable only in retrospect.", "intuition", "probability", ["fat-tailed-distributions", "probability-and-risk", "st-petersburg-paradox"]),
    ("fat-tailed-distributions", "Fat-Tailed Distributions", "Extreme outcomes occur far more often than normal curves suggest.", "intuition", "probability", ["black-swan-events", "ergodicity", "fat-tail-farm"]),
    ("regression-to-the-mean", "Regression to the Mean", "Extreme measurements tend to be followed by less extreme ones.", "intuition", "probability", ["statistics-interpretation", "simpsons-paradox", "base-rate-neglect"]),
    ("surveillance-capitalism", "Surveillance Capitalism", "Business models that extract and predict behaviour from digital traces.", "networks", "social-science", ["digital-panopticon", "algorithmic-bias", "technology-and-society"]),
    ("algorithmic-bias", "Algorithmic Bias", "Systematic errors in automated decisions that disadvantage groups.", "networks", "social-science", ["surveillance-capitalism", "goodharts-law", "technology-and-society"]),
    ("digital-panopticon", "Digital Panopticon", "Visibility and perceived observation reshape behaviour at scale.", "networks", "social-science", ["surveillance-capitalism", "we-become-what-we-behold", "technology-and-society"]),
    ("loss-aversion", "Loss Aversion", "Losses loom larger than equivalent gains — roughly twice as salient in many studies.", "intuition", "economics", ["behavioural-finance", "herd-behaviour", "overconfidence-bias"]),
    ("herd-behaviour", "Herd Behaviour", "Following others' actions when private information is weak or costly.", "networks", "social-science", ["information-cascades", "loss-aversion", "behavioural-finance"]),
    ("overconfidence-bias", "Overconfidence Bias", "Systematic overestimation of one's accuracy, knowledge, or control.", "intuition", "cognitive-science", ["dunning-kruger-effect", "behavioural-finance", "predict-then-reveal"]),
    ("mate-selection-theory", "Mate Selection Theory", "Evolutionary frameworks for partner choice, competition, and signalling.", "systems", "evolution", ["status-signaling", "kin-selection", "evolutionary-psychology"]),
    ("kin-selection", "Kin Selection", "Evolution favours helping relatives when benefit weighted by relatedness exceeds cost.", "systems", "evolution", ["mate-selection-theory", "evolution-of-trust", "evolutionary-psychology"]),
    ("status-signaling", "Status Signaling", "Costly displays that communicate rank, fitness, or group membership.", "networks", "social-science", ["sociology-of-status", "cultural-capital", "evolutionary-psychology"]),
    ("elite-circulation", "Elite Circulation", "How ruling groups turn over — recruitment, co-optation, or replacement.", "systems", "social-science", ["legitimacy-and-authority", "history-of-power", "machiavellian-realism"]),
    ("legitimacy-and-authority", "Legitimacy and Authority", "Power persists when subjects believe rulers have right to rule.", "systems", "social-science", ["soft-power", "history-of-power", "ostrom-commons-design"]),
    ("soft-power", "Soft Power", "Influence through attraction and norms rather than coercion.", "networks", "social-science", ["legitimacy-and-authority", "geopolitics", "history-of-power"]),
    ("machiavellian-realism", "Machiavellian Realism", "Political analysis stressing power, fear, and fortune over ideals.", "systems", "social-science", ["history-of-power", "prisoners-dilemma", "geopolitics"]),
    ("principal-agent-problem", "Principal–Agent Problem", "Misaligned incentives when one party acts on another's behalf.", "systems", "economics", ["moral-hazard", "economics-incentives", "cobra-farm"]),
    ("moral-hazard", "Moral Hazard", "Hidden actions after a contract — agents take risks others bear.", "systems", "economics", ["principal-agent-problem", "economics-incentives", "goodharts-law"]),
    ("unintended-consequences", "Unintended Consequences", "Interventions produce effects nobody planned — often via incentives.", "systems", "economics", ["cobra-farm", "goodharts-law", "second-order-effects"]),
    ("correlation-vs-causation", "Correlation vs Causation", "Association does not prove one variable produced another.", "intuition", "probability", ["statistics-interpretation", "simpsons-paradox", "base-rate-neglect"]),
    ("survivorship-bias", "Survivorship Bias", "Drawing lessons from winners while ignoring silent failures.", "intuition", "probability", ["statistics-interpretation", "goodharts-law", "p-hacking-lab"]),
    ("base-rate-neglect", "Base Rate Neglect", "Ignoring how common an outcome is when interpreting evidence.", "intuition", "probability", ["base-rate-hospital", "statistics-interpretation", "bayesian-therapy"]),
    ("cultural-capital", "Cultural Capital", "Knowledge, taste, and credentials that confer social advantage.", "networks", "social-science", ["social-stratification", "sociology-of-status", "status-anxiety"]),
    ("status-anxiety", "Status Anxiety", "Distress from perceived rank relative to peers or ideals.", "networks", "social-science", ["sociology-of-status", "social-stratification", "loss-aversion"]),
    ("social-stratification", "Social Stratification", "Durable hierarchies of class, caste, or prestige.", "networks", "social-science", ["cultural-capital", "schelling-segregation", "sociology-of-status"]),
    ("bounded-rationality", "Bounded Rationality", "Deciders use limited information and simplified rules — not full optimisation.", "intuition", "cognitive-science", ["heuristics-decision-making", "satisficing", "decision-making-uncertainty"]),
    ("heuristics-decision-making", "Heuristics in Decision-Making", "Fast rules that work well in some environments and fail in others.", "intuition", "cognitive-science", ["bounded-rationality", "availability-heuristic", "decision-making-uncertainty"]),
    ("satisficing", "Satisficing", "Choosing the first acceptable option rather than the global optimum.", "intuition", "cognitive-science", ["bounded-rationality", "decision-making-uncertainty", "predict-then-reveal"]),
    ("falsifiability", "Falsifiability", "A claim is scientific if it could in principle be proven wrong.", "evidence", "social-science", ["scientific-method-skepticism", "replication-crisis", "peer-review-process"]),
    ("replication-crisis", "Replication Crisis", "Many published findings fail to reproduce — methods and incentives under scrutiny.", "evidence", "social-science", ["p-hacking-lab", "peer-review-process", "scientific-method-skepticism"]),
    ("peer-review-process", "Peer Review", "Expert evaluation before publication — gatekeeper with known biases.", "evidence", "social-science", ["scientific-method-skepticism", "replication-crisis", "falsifiability"]),
    ("nash-equilibrium", "Nash Equilibrium", "No player gains by unilaterally changing strategy given others' choices.", "systems", "game-theory", ["prisoners-dilemma", "negotiation-game-theory", "iterated-prisoners-dilemma"]),
    ("zero-sum-games", "Zero-Sum vs Non-Zero-Sum Games", "Whether one side's gain equals another's loss — framing cooperation.", "systems", "game-theory", ["prisoners-dilemma", "negotiation-game-theory", "commons-garden"]),
    ("collective-memory", "Collective Memory", "Groups share reconstructed pasts — monuments, rituals, media.", "networks", "social-science", ["myth-creation", "cultural-history", "information-cascades"]),
    ("myth-creation", "Myth Creation", "Stories that simplify history to bind identity or justify power.", "networks", "social-science", ["collective-memory", "historical-storytelling", "cultural-history"]),
    ("historical-storytelling", "Historical Storytelling", "Narrative choices — heroes, villains, turning points — shape memory.", "networks", "social-science", ["collective-memory", "myth-creation", "language-and-framing"]),
    ("linguistic-relativity", "Linguistic Relativity", "Language structure may influence habitual thought — Sapir–Whorf debate.", "intuition", "cognitive-science", ["language-and-framing", "emotionally-charged-language", "framing-effects-media"]),
    ("euphemism-cycles", "Euphemism Cycles", "Polite terms for harsh realities eventually absorb the stigma they replace.", "networks", "social-science", ["language-and-framing", "emotionally-charged-language", "goodharts-law"]),
    ("emotionally-charged-language", "Emotionally Charged Language", "Word choice triggers affect before argument — framing by connotation.", "networks", "social-science", ["language-and-framing", "framing-effects-media", "propaganda-model"]),
    ("moral-foundations-theory", "Moral Foundations Theory", "Multiple moral intuitions — care, fairness, loyalty, authority, sanctity — combine differently across cultures.", "systems", "social-science", ["moral-psychology", "value-diversity", "in-group-bias"]),
    ("in-group-bias", "In-Group Bias", "Favouring members of one's own group — cooperation and conflict.", "networks", "social-science", ["moral-psychology", "schelling-segregation", "asch-conformity"]),
    ("value-diversity", "Value Diversity", "Plausible moral outlooks disagree — pluralism vs relativism.", "systems", "social-science", ["moral-psychology", "moral-relativism", "philosophy-of-ethics"]),
    ("utilitarianism", "Utilitarianism", "Right action maximises overall welfare — greatest good for greatest number.", "systems", "social-science", ["philosophy-of-ethics", "deontology", "moral-relativism"]),
    ("deontology", "Deontology", "Some duties are binding regardless of outcomes — rules and rights.", "systems", "social-science", ["utilitarianism", "virtue-ethics", "philosophy-of-ethics"]),
    ("virtue-ethics", "Virtue Ethics", "Character and flourishing matter more than isolated acts or rules.", "systems", "social-science", ["philosophy-of-ethics", "deontology", "utilitarianism"]),
    ("moral-relativism", "Moral Relativism", "Moral truth varies by culture or individual — descriptive vs normative claims.", "systems", "social-science", ["philosophy-of-ethics", "value-diversity", "moral-psychology"]),
    ("balance-of-power", "Balance of Power", "States align to prevent any single actor from dominating.", "networks", "social-science", ["geopolitics", "deterrence-theory", "multipolar-world-dynamics"]),
    ("deterrence-theory", "Deterrence Theory", "Threat of retaliation prevents attack — credibility and misperception matter.", "networks", "social-science", ["geopolitics", "balance-of-power", "prisoners-dilemma"]),
    ("multipolar-world-dynamics", "Multipolar World Dynamics", "Three or more great powers — shifting alliances and complexity.", "networks", "social-science", ["geopolitics", "balance-of-power", "evolution-of-trust"]),
    ("agenda-setting", "Agenda Setting", "Media influence what people think **about** — not always what to think.", "networks", "social-science", ["media-literacy", "framing-effects-media", "propaganda-model"]),
    ("framing-effects-media", "Framing Effects", "Presenting the same facts in different frames changes preference and blame.", "networks", "social-science", ["media-literacy", "agenda-setting", "language-and-framing"]),
    ("propaganda-model", "Propaganda Model", "Structural filters — ownership, advertising, sourcing — shape news content.", "networks", "social-science", ["media-literacy", "agenda-setting", "surveillance-capitalism"]),
    ("echo-chambers", "Echo Chambers", "Homogeneous information environments that amplify beliefs and reduce correction.", "networks", "social-science", ["media-literacy", "confirmation-bias", "information-cascades"]),
    ("second-order-effects", "Second-Order Effects", "Consequences of consequences — interventions ripple beyond first intent.", "systems", "complex-systems", ["systems-thinking", "unintended-system-behavior", "feedback-loops"]),
    ("unintended-system-behavior", "Unintended System Behavior", "System output nobody designed — emergence plus perverse incentives.", "systems", "complex-systems", ["systems-thinking", "emergence", "cobra-farm"]),
]

HUB_RELATED = {
    "human-behaviour-psychology": ["cognitive-biases", "moral-psychology"],
    "cognitive-biases": ["statistics-interpretation", "decision-making-uncertainty"],
    "probability-and-risk": ["statistics-interpretation", "ergodicity"],
    "technology-and-society": ["media-literacy", "surveillance-capitalism"],
    "behavioural-finance": ["economics-incentives", "loss-aversion"],
    "evolutionary-psychology": ["sociology-of-status", "mate-selection-theory"],
    "history-of-power": ["geopolitics", "legitimacy-and-authority"],
    "economics-incentives": ["goodharts-law", "principal-agent-problem"],
    "statistics-interpretation": ["base-rate-neglect", "probability-and-risk"],
    "sociology-of-status": ["cultural-capital", "schelling-segregation"],
    "decision-making-uncertainty": ["bounded-rationality", "predict-then-reveal"],
    "scientific-method-skepticism": ["replication-crisis", "p-hacking-lab"],
    "negotiation-game-theory": ["game-theory", "prisoners-dilemma"],
    "cultural-history": ["collective-memory", "myth-creation"],
    "language-and-framing": ["framing-effects-media", "media-literacy"],
    "moral-psychology": ["philosophy-of-ethics", "ultimatum-game"],
    "philosophy-of-ethics": ["moral-foundations-theory", "utilitarianism"],
    "geopolitics": ["balance-of-power", "deterrence-theory"],
    "media-literacy": ["agenda-setting", "information-cascades"],
    "systems-thinking": ["feedback-loops", "emergence"],
    "scaling-and-growth": ["square-cube-law", "metabolic-scaling"],
}


def _concept_body(title: str, essence: str, summary: str, related: list[str], extra_core: str = "") -> str:
    core = extra_core or summary
    rel = " · ".join(f"[[{r}]]" for r in related[:6])
    return f"""# {title}

> **One-line essence:** {essence}

## Why this matters

{summary} Understanding this idea helps explain patterns in behaviour, institutions, and public debate that otherwise look like isolated mistakes or malice.

## Core idea

{core}

## Mechanism

1. **Trigger or input** — situation presents evidence, incentive, or threat.\n2. **Process** — minds, markets, or institutions apply rules, heuristics, or structures.\n3. **Output** — beliefs, prices, policies, or norms shift — sometimes stabilising, sometimes amplifying error.\n4. **Feedback** — outcomes reshape the next round (see [[feedback-loops]]).

## Implications

- Appearances of rational disagreement often mix evidence with structural bias — map which mechanism is active.\n- Interventions that ignore second-order effects ([[second-order-effects]]) frequently fail or backfire.\n- Pair this concept with related ideas in the same hub for fuller pictures.

## Related

{rel}

## Further reading

- Consult standard references in the field; link formal models where they exist in ExplorableLab ([[schelling-segregation]] as quality bar).\n- Cross-check claims against [[scientific-method-skepticism]] — especially for contested social science.

## Discovery suggestions

- [ ] Add interactive scenario for this concept\n- [ ] Link to experiment or paradox pages where applicable
"""


def _full_concept_body(c: dict) -> str:
    rel = " · ".join(f"[[{r}]]" for r in c["related"])
    impl = c.get("implications", "").strip()
    impl_block = "\n".join(f"- {line.lstrip('- ')}" for line in impl.split("\n") if line.strip()) if impl else "- See related hub and cross-links above."
    return f"""# {c['title']}

> **One-line essence:** {c['essence']}

## Why this matters

{c['why']}

## Core idea

{c['core']}

## Mechanism

{c['mechanism']}

## Implications

{impl_block}

## Related

{rel}

## Further reading

{c['reading']}

## Discovery suggestions

- [ ] Native simulation or classroom activity\n- [ ] Cross-link from hub collection
"""


def write_hub(slug: str, title: str, summary: str, concepts: list[str], idx: int) -> None:
    related_hubs = HUB_RELATED.get(slug, ["systems-thinking", "cognitive-biases"])[:3]
    concept_lines = "\n".join(f"- [[{c}]]" for c in concepts)
    hub_links = " · ".join(f"[[{h}]]" for h in related_hubs)
    body = f"""# {title}

> **One-line essence:** {summary}

## Overview

This hub collects read-only explanations for core ideas in **{title.lower()}**. Each linked page follows the museum quality bar: mechanism, implications, misconceptions where relevant, and citations — not bullet lists alone.

## Key ideas in this area

{concept_lines}

## How to read this hub

Start with any concept that matches your question. Follow `[[wikilinks]]` sideways across hubs — for example, [[confirmation-bias]] connects to [[statistics-interpretation]] and [[media-literacy]].

## Related hubs

{hub_links}

## Discovery suggestions

- [ ] Add path collection linking this hub\n- [ ] Promote sub-concepts as they reach Schelling quality bar
"""
    fm = {
        "id": f"DIS-{20 + idx:04d}",
        "type": "discipline",
        "slug": slug,
        "title": title,
        "summary": summary,
        "status": "canonical",
        "wing": "discipline",
        "created": "2026-06-26",
        "updated": "2026-06-26",
        "related": {"disciplines": concepts[:4], "theories": related_hubs},
    }
    write_page(slug, "discipline", fm, body, CONTENT / "disciplines" / f"{slug}.md")


def write_concept_full(c: dict, idx: int) -> None:
    typ = c["type"]
    slug = c["slug"]
    if typ == "mental-model":
        path = CONTENT / "mental-models" / f"{slug}.md"
        id_prefix = "MOD"
        folder_key = "mental_models"
    else:
        folder = c.get("folder", "complex-systems")
        path = CONTENT / "theories" / folder / f"{slug}.md"
        id_prefix = "THY"
        folder_key = "theories"
    fm = {
        "id": f"{id_prefix}-{100 + idx:04d}",
        "type": typ.replace("-", "_") if typ == "mental-model" else "theory",
        "slug": slug,
        "title": c["title"],
        "summary": c["summary"],
        "status": "canonical",
        "wing": c["wing"],
        "created": "2026-06-26",
        "updated": "2026-06-26",
        "confidence": "high",
        "fields": [c.get("folder") or "general"],
        "difficulty": "introductory",
        "related": {folder_key: c["related"][:4]},
        "explorable": {
            "verdict": "essential",
            "best_medium": "visualization",
            "best_medium_stars": 4,
        },
    }
    write_page(slug, "theory" if typ != "mental-model" else "mental-model", fm, _full_concept_body(c), path)


def write_concept_compact(
    slug: str,
    title: str,
    summary: str,
    wing: str,
    folder: str,
    related: list[str],
    idx: int,
) -> None:
    essence = summary.rstrip(".")
    path = CONTENT / "theories" / folder / f"{slug}.md"
    fm = {
        "id": f"THY-{200 + idx:04d}",
        "type": "theory",
        "slug": slug,
        "title": title,
        "summary": summary,
        "status": "canonical",
        "wing": wing,
        "created": "2026-06-26",
        "updated": "2026-06-26",
        "confidence": "medium",
        "fields": [folder.replace("-", "_")],
        "difficulty": "introductory",
        "related": {"theories": related[:4]},
        "explorable": {"verdict": "essential", "best_medium": "visualization", "best_medium_stars": 3},
    }
    write_page(slug, "theory", fm, _concept_body(title, essence, summary, related), path)


def write_expansion_topics() -> tuple[list[tuple], list[tuple], list[tuple]]:
    """Write all markdown files. Returns export tuples for build_museum."""
    hub_exports: list[tuple] = []
    thy_exports: list[tuple] = []
    mod_exports: list[tuple] = []

    for i, (slug, title, summary, concepts) in enumerate(HUBS):
        write_hub(slug, title, summary, concepts, i)
        hub_exports.append((slug, title, summary, concepts[:4]))

    for i, c in enumerate(CONCEPTS):
        write_concept_full(c, i)
        if c["type"] == "mental-model":
            mod_exports.append((c["slug"], c["title"], c["summary"], c["wing"], c["related"][:4]))
        else:
            thy_exports.append((c["slug"], c["title"], c["summary"], c["wing"], c["related"][:4]))

    for i, row in enumerate(MORE_CONCEPTS):
        slug, title, summary, wing, folder, related = row
        write_concept_compact(slug, title, summary, wing, folder, related, i)
        thy_exports.append((slug, title, summary, wing, related[:4]))

    return hub_exports, thy_exports, mod_exports


if __name__ == "__main__":
    h, t, m = write_expansion_topics()
    print(f"Wrote {len(h)} hubs, {len(t)} theories, {len(m)} mental models")
