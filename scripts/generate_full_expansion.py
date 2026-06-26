#!/usr/bin/env python3
"""
Generate full corpus expansion:
- 120 simulation concepts (from EXPLORABLE_EXPLANATIONS_RESEARCH.md)
- 15 hybrid simulation concepts
- 45 paradoxes
- 30 experiments
- 35 papers
- 25 Nobel discoveries
- 40 mental models
- 35 phenomena
- Supporting scientists
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RESEARCH = ROOT / "EXPLORABLE_EXPLANATIONS_RESEARCH.md"
CONTENT = ROOT / "content"


def slugify(title):
    t = re.sub(r"^The\s+", "", title, flags=re.I)
    t = re.sub(r"[^a-zA-Z0-9\s-]", "", t)
    return t.lower().strip().replace(" ", "-").replace("--", "-")


def yaml_block(d, indent=0):
    lines = []
    sp = "  " * indent
    for k, v in d.items():
        if isinstance(v, dict):
            lines.append(f"{sp}{k}:")
            lines.extend(yaml_block(v, indent + 1))
        elif isinstance(v, list):
            if not v:
                lines.append(f"{sp}{k}: []")
            elif all(isinstance(i, str) for i in v):
                lines.append(f"{sp}{k}: [{', '.join(v)}]")
            else:
                lines.append(f"{sp}{k}:")
                for i in v:
                    lines.append(f"{sp}  - {i}")
        elif isinstance(v, bool):
            lines.append(f"{sp}{k}: {'true' if v else 'false'}")
        elif isinstance(v, (int, float)):
            lines.append(f"{sp}{k}: {v}")
        else:
            s = str(v).replace('"', '\\"')
            lines.append(f'{sp}{k}: "{s}"')
    return lines


def write(path, fm, body_lines):
    p = CONTENT / path if not str(path).startswith("indices") else ROOT / path
    if p.exists():
        return False
    p.parent.mkdir(parents=True, exist_ok=True)
    text = "---\n" + "\n".join(yaml_block(fm)) + "\n---\n\n" + "\n".join(body_lines) + "\n"
    p.write_text(text, encoding="utf-8")
    return True


def parse_research_sims():
    if not RESEARCH.exists():
        return []
    text = RESEARCH.read_text(encoding="utf-8")
    entries = []
    for m in re.finditer(
        r"\*\*(\d+)\.\s+The\s+([^*]+)\*\*\s*·\s*([^·]+)·\s*([^·]+)·",
        text,
    ):
        num, title, theory, one_liner = m.group(1), m.group(2).strip(), m.group(3).strip(), m.group(4).strip()
        if "see 69" in title.lower():
            continue
        slug = slugify(title)
        entries.append({
            "num": int(num),
            "title": f"The {title}",
            "slug": slug,
            "theory_name": theory,
            "summary": one_liner.strip(),
        })
    return entries


# --- PARADOXES ---
PARADOXES = [
    ("monty-hall-problem", "Monty Hall Problem", "Switching doors wins 2/3 of the time.", "probability", ["bayes-theorem"]),
    ("simpsons-paradox", "Simpson's Paradox", "Aggregated trends reverse when stratified.", "probability", ["regression-to-mean"]),
    ("newcomb-problem", "Newcomb's Problem", "One-box vs two-box challenges causal decision theory.", "philosophy", ["bayes-theorem"]),
    ("st-petersburg-paradox", "St. Petersburg Paradox", "Infinite expected value; finite willingness to pay.", "probability", []),
    ("raven-paradox", "Raven Paradox", "Green apples confirm all ravens are black.", "philosophy", []),
    ("birthday-paradox", "Birthday Paradox", "23 people give 50% collision probability.", "probability", []),
    ("allais-paradox", "Allais Paradox", "Choices violate expected utility axioms.", "economics", ["loss-aversion"]),
    ("ellsberg-paradox", "Ellsberg Paradox", "Ambiguity aversion vs known probabilities.", "economics", []),
    ("braess-paradox", "Braess Paradox", "Adding capacity increases travel time.", "engineering", ["percolation"]),
    ("parrondos-paradox", "Parrondo's Paradox", "Two losing games combine to win.", "probability", []),
    ("fermi-paradox", "Fermi Paradox", "Great silence despite vast universe.", "physics", []),
    ("berksons-paradox", "Berkson's Paradox", "Spurious correlation from selection bias.", "probability", []),
    ("survivorship-bias-paradox", "Survivorship Bias", "We only see survivors; failures invisible.", "probability", ["cognitive-biases-overview"]),
    ("sleeping-beauty-problem", "Sleeping Beauty Problem", "Self-locating belief upon waking.", "philosophy", ["bayes-theorem"]),
    ("two-envelope-paradox", "Two Envelope Paradox", "Switching envelopes seems always better.", "probability", []),
    ("unexpected-hanging-paradox", "Unexpected Hanging Paradox", "Self-referential prediction.", "logic", []),
    ("liar-paradox", "Liar Paradox", "This statement is false.", "logic", []),
    ("ship-of-theseus", "Ship of Theseus", "Identity through gradual replacement.", "philosophy", []),
    ("zenos-paradox", "Zeno's Paradox", "Motion requires infinite steps.", "mathematics", []),
    ("olbers-paradox", "Olbers' Paradox", "Why is the night sky dark?", "physics", []),
    ("gibbs-paradox", "Gibbs Paradox", "Entropy and indistinguishable particles.", "physics", ["entropy"]),
    ("maxwells-demon-paradox", "Maxwell's Demon", "Demon sorts molecules; violates entropy?", "physics", ["entropy"]),
    ("moravecs-paradox", "Moravec's Paradox", "Easy/hard tasks invert for humans vs AI.", "cognitive-science", []),
    ("jevons-paradox", "Jevons Paradox", "Efficiency increases consumption.", "economics", []),
    ("friendship-paradox", "Friendship Paradox", "Your friends have more friends than you.", "network-science", ["preferential-attachment"]),
    ("petrie-multiplier-paradox", "Petrie Multiplier", "Equal harassment rates; unequal harm.", "social-science", []),
    ("inspection-paradox", "Inspection Paradox", "Observed waiting times exceed average.", "probability", ["queueing-theory"]),
    ("prosecutors-fallacy", "Prosecutor's Fallacy", "P(match|innocent) confused with P(innocent|match).", "probability", ["bayes-theorem"]),
    ("base-rate-fallacy", "Base Rate Fallacy", "Ignoring prevalence in diagnosis.", "probability", ["bayes-theorem"]),
    ("conjunction-fallacy", "Conjunction Fallacy", "Linda problem; vivid beats probable.", "cognitive-science", ["cognitive-biases-overview"]),
    ("sorites-paradox", "Sorites Paradox", "Heap paradox; vague predicates.", "philosophy", []),
    ("preface-paradox", "Preface Paradox", "Believing each claim yet doubting the book.", "philosophy", []),
    ("lottery-paradox", "Lottery Paradox", "Each ticket won't win; one will.", "probability", []),
    ("preface-paradox-kyburg", "Kyburg Lottery", "Rational acceptance of inconsistent beliefs.", "philosophy", []),
    ("doomsday-argument", "Doomsday Argument", "Anthropic reasoning on human extinction.", "philosophy", []),
    ("simulation-argument", "Simulation Argument", "We may live in a simulation.", "philosophy", []),
    ("banach-tarski-paradox", "Banach-Tarski Paradox", "Sphere decomposed and reassembled into two.", "mathematics", []),
    ("gabriels-horn", "Gabriel's Horn", "Infinite surface, finite volume.", "mathematics", []),
    ("potato-paradox", "Potato Paradox", "99% water potato dries to 98% — still 50% water?", "probability", []),
    ("will-rogers-phenomenon", "Will Rogers Phenomenon", "Moving patients between groups improves both survival rates.", "medicine", ["simpsons-paradox"]),
    ("anthropic-principle-paradox", "Anthropic Principle", "Observing universe constrains its properties.", "physics", []),
    ("black-hole-information-paradox", "Black Hole Information Paradox", "Information lost in black holes?", "physics", []),
    ("grandfather-paradox", "Grandfather Paradox", "Time travel prevents own existence.", "physics", []),
    ("bootstrap-paradox", "Bootstrap Paradox", "Information without origin in time loop.", "physics", []),
    ("unexpected-examination", "Unexpected Exam Paradox", "Teacher announces surprise exam.", "logic", []),
]

# --- EXPERIMENTS ---
EXPERIMENTS = [
    ("asch-conformity", "Asch Conformity Experiments", 1951, "Group pressure distorts line judgment.", ["pluralistic-ignorance"], ["social-science"]),
    ("milgram-obedience", "Milgram Obedience Experiments", 1963, "Authority drives harmful obedience.", [], ["social-science"]),
    ("stanford-prison-experiment", "Stanford Prison Experiment", 1971, "Roles shape cruelty in simulated prison.", [], ["social-science"]),
    ("marshmallow-test", "Stanford Marshmallow Experiment", 1972, "Delayed gratification predicts outcomes.", ["hyperbolic-discounting"], ["cognitive-science"]),
    ("wisconsin-card-sort", "Wisconsin Card Sort Test", 1948, "Cognitive flexibility and set shifting.", [], ["cognitive-science"]),
    ("stroop-experiment", "Stroop Experiment", 1935, "Automatic reading interferes with color naming.", [], ["cognitive-science"]),
    ("robbers-cave", "Robbers Cave Experiment", 1954, "Intergroup conflict and superordinate goals.", [], ["social-science"]),
    ("bystander-effect-experiment", "Darley & Latane Bystander Experiments", 1968, "Diffusion of responsibility reduces helping.", [], ["social-science"]),
    ("cognitive-dissonance-festinger", "Festinger Cognitive Dissonance Study", 1959, "Beliefs shift to reduce dissonance.", [], ["cognitive-science"]),
    ("invisible-gorilla", "Invisible Gorilla Experiment", 1999, "Inattentional blindness during focused task.", [], ["cognitive-science"]),
    ("lost-in-mall", "Lost in the Mall False Memory", 1995, "False memories implanted via narrative.", [], ["cognitive-science"]),
    ("little-albert", "Little Albert Experiment", 1920, "Fear conditioning in infant.", [], ["cognitive-science"]),
    ("harlow-monkeys", "Harlow Monkey Experiments", 1958, "Attachment over food in primates.", [], ["psychology"]),
    ("blue-eyes-brown-eyes", "Jane Elliott Blue Eyes/Brown Eyes", 1968, "Arbitrary group discrimination in classroom.", ["schelling-segregation"], ["social-science"]),
    ("ultimatum-game-experiment", "Ultimatum Game Experiments", 1982, "Fairness rejects unfair splits.", ["loss-aversion"], ["economics"]),
    ("public-goods-game", "Public Goods Game Experiments", 1990, "Free riding in group contributions.", ["tragedy-of-commons"], ["economics"]),
    ("trust-game-experiment", "Trust Game (Berg et al.)", 1995, "Trust and reciprocity in economic exchange.", ["iterated-prisoners-dilemma"], ["economics"]),
    ("wason-selection-task", "Wason Selection Task", 1966, "Logic failure except in social contexts.", [], ["cognitive-science"]),
    ("tversky-kahneman-framing", "Asian Disease Framing Experiment", 1981, "Framing changes risky choice.", ["loss-aversion"], ["economics"]),
    ("libet-experiments", "Libet Free Will Experiments", 1983, "Readiness potential precedes conscious intent.", [], ["neuroscience-discipline"]),
    ("split-brain-experiments", "Sperry Split-Brain Experiments", 1960, "Hemisphere specialization.", [], ["neuroscience-discipline"]),
    ("visual-cliff", "Visual Cliff Experiment", 1960, "Depth perception in infants.", [], ["cognitive-science"]),
    ("bobo-doll-experiment", "Bandura Bobo Doll Experiment", 1961, "Observational learning of aggression.", ["hebbian-learning"], ["social-science"]),
    ("minnesota-twin-study", "Minnesota Twin Study", 1979, "Heritability of traits.", ["natural-selection"], ["biology"]),
    ("prisoners-dilemma-tournament", "Axelrod PD Tournament", 1980, "Tit-for-tat wins iterated PD.", ["evolution-of-cooperation"], ["game-theory"]),
    ("milgram-variant-teacher", "Milgram Teacher Learner Variant", 1963, "Proximity reduces obedience.", [], ["social-science"]),
    ("granovetter-strength-weak-ties", "Granovetter Weak Ties Survey", 1973, "Weak ties yield job information.", ["information-cascades"], ["network-science"]),
    ("centola-complex-contagion", "Centola Complex Contagion Experiments", 2010, "Health behaviors need multiple exposures.", ["complex-contagion"], ["network-science"]),
    ("henrich-ultra-social", "Henrich Cross-Cultural Ultimatum", 2001, "Fairness varies by culture.", [], ["anthropology-discipline"]),
    ("latané-social-impact", "Latane Social Impact Theory Tests", 1981, "Impact scales with source strength and number.", [], ["social-science"]),
]

# --- PAPERS ---
PAPERS = [
    ("1980-axelrod-evolution-of-cooperation", "axelrod-1980-evolution-of-cooperation", "The Evolution of Cooperation", 1980, ["robert-axelrod"], ["evolution-of-cooperation"], "Science"),
    ("1990-ostrom-governing-commons", "ostrom-1990-governing-commons", "Governing the Commons", 1990, ["elinor-ostrom"], ["ostrom-commons-design"], "Cambridge"),
    ("1979-kahneman-prospect-theory", "kahneman-tversky-1979-prospect-theory", "Prospect Theory: An Analysis of Decision under Risk", 1979, [], ["loss-aversion"], "Econometrica"),
    ("1973-granovetter-weak-ties", "granovetter-1973-strength-of-weak-ties", "The Strength of Weak Ties", 1973, [], ["information-cascades"], "AJS"),
    ("1992-bikhchandani-information-cascades", "bikhchandani-1992-informational-cascades", "A Theory of Fads, Fashion, Custom", 1992, [], ["information-cascades"], "Journal of Political Economy"),
    ("1968-hardin-tragedy-commons", "hardin-1968-tragedy-commons", "The Tragedy of the Commons", 1968, [], ["tragedy-of-commons"], "Science"),
    ("2013-petrie-harassment-multiplier", "petrie-2013-harassment-multiplier", "Petrie Multiplier: harassment asymmetry", 2013, [], [], "blog/model"),
    ("2019-peters-ergodicity", "peters-2019-ergodicity-economics", "Ergodicity Economics", 2019, [], ["ergodicity"], "Nature Physics"),
    ("2000-deffuant-bounded-confidence", "deffuant-2000-bounded-confidence", "Mixing Beliefs Among Interacting Agents", 2000, [], [], "Advances in Complex Systems"),
    ("1999-barabasi-emergence-scaling", "barabasi-1999-emergence-scaling", "Emergence of Scaling in Random Networks", 1999, [], ["preferential-attachment"], "Science"),
    ("1953-shannon-information", "shannon-1948-information-theory", "A Mathematical Theory of Communication", 1948, [], ["shannon-entropy"], "Bell System Technical Journal"),
    ("1978-granovetter-threshold", "granovetter-1978-threshold-models", "Threshold Models of Collective Behavior", 1978, [], ["threshold-models"], "J Math Sociology"),
    ("1984-axelrod-book-tournament", "axelrod-1984-book-cooperation", "The Evolution of Cooperation (book)", 1984, ["robert-axelrod"], ["evolution-of-cooperation"], "Basic Books"),
    ("2007-centola-complex-contagion", "centola-2007-complex-contagions", "Complex Contagions and the Weakness of Long Ties", 2007, [], ["complex-contagion"], "AJS"),
    ("2016-lerman-majority-illusion", "lerman-2016-majority-illusion", "Majority Illusion in Social Networks", 2016, [], [], "PLoS ONE"),
    ("1971-vickrey-auctions", "vickrey-1961-counterspeculation", "Counterspeculation, Auctions, and Competitive Sealed Tenders", 1961, [], ["mechanism-design"], "Journal of Finance"),
    ("1951-arrow-impossibility", "arrow-1951-social-choice", "Social Choice and Individual Values", 1951, [], ["social-choice"], "Yale"),
    ("1968-braess-paradox", "braess-1968-paradox", "Uber ein Paradoxon aus der Verkehrsplanung", 1968, [], ["percolation"], "Unternehmensforschung"),
    ("1961-landauer-eraser", "landauer-1961-irreversibility", "Irreversibility and Heat Generation", 1961, [], ["entropy"], "IBM Journal"),
    ("1972-kahneman-anchoring", "tversky-kahneman-1974-heuristics", "Judgment under Uncertainty: Heuristics and Biases", 1974, [], ["cognitive-biases-overview"], "Science"),
    ("1990-ostrom-design-principles", "ostrom-1990-design-principles", "Design Principles for Robust CPR Institutions", 1990, ["elinor-ostrom"], ["ostrom-commons-design"], "DAE"),
    ("2005-schelling-nobel-lecture", "schelling-2005-nobel-lecture", "Schelling Nobel Lecture on game theory", 2005, ["thomas-schelling"], ["schelling-segregation"], "Nobel"),
    ("1988-axelrod-evolutionary-approaches", "axelrod-1988-evolutionary-approaches", "The Evolution of Cooperation (follow-up)", 1988, ["robert-axelrod"], [], "Science"),
    ("1963-milgram-behavioral-study", "milgram-1963-behavioral-study", "Behavioral Study of Obedience", 1963, [], [], "J Abnormal Psychology"),
    ("1956-miller-magic-number", "miller-1956-magic-number", "The Magical Number Seven", 1956, [], ["cognitive-biases-overview"], "Psychological Review"),
    ("1974-ostrom-framework", "ostrom-2009-polycentric", "Beyond Markets and States: Polycentric Governance", 2010, ["elinor-ostrom"], ["ostrom-commons-design"], "Nobel Prize lecture"),
    ("2014-peters-optimal-betting", "peters-2014-optimal-betting", "Optimal Betting under Parameter Uncertainty", 2014, [], ["ergodicity"], "PRL"),
    ("1992-bak-sandpile", "bak-1987-self-organized-criticality", "Self-Organized Criticality", 1987, [], ["self-organized-criticality"], "PRL"),
    ("1967-thompson-paradox", "thompson-1952-paradox", "On the Likelihood that One Unknown Probability Exceeds Another", 1933, [], ["bayes-theorem"], "Biometrika"),
    ("2000-watts-small-world", "watts-1998-small-world", "Collective Dynamics of Small-World Networks", 1998, [], ["preferential-attachment"], "Nature"),
    ("2011-ebersole-replication", "open-science-collaboration-2015", "Estimating the Reproducibility of Psychological Science", 2015, [], [], "Science"),
    ("1975-bickel-simpsons-paradox", "bickel-1975-sex-bias-berkeley", "Sex Bias in Graduate Admissions: Data from Berkeley", 1975, [], ["regression-to-mean"], "Science"),
    ("1999-blackmore-meme-machine", "dawkins-1976-selfish-gene", "The Selfish Gene (memes chapter)", 1976, [], ["natural-selection"], "Oxford"),
    ("2004-pentland-honest-signals", "pentland-2008-honest-signals", "Honest Signals (social physics)", 2008, [], ["signaling-games"], "MIT Press"),
    ("2017-henrich-weird", "henrich-2010-weird", "The Weirdest People in the World?", 2010, [], [], "BBS"),
]

# --- NOBEL ---
NOBELS = [
    ("2005-schelling-game-theory", 2005, "economics", "Game-theory analysis of conflict and cooperation", ["thomas-schelling"], ["schelling-segregation"]),
    ("2009-ostrom-commons", 2009, "economics", "Economic governance of the commons", ["elinor-ostrom"], ["ostrom-commons-design"]),
    ("2002-kahneman-behavioral-economics", 2002, "economics", "Prospect theory and behavioral economics", [], ["loss-aversion", "cognitive-biases-overview"]),
    ("1994-nash-game-theory", 1994, "economics", "Non-cooperative game theory", [], ["iterated-prisoners-dilemma"]),
    ("2020-wilson-evolutionary-economics", 2020, "economics", "Improve auctions and marketplace design", [], ["mechanism-design"]),
    ("1973-lorenz-chaos", 1973, "physics", "Nonperiodic deterministic flow (chaos)", [], ["emergence"]),
    ("2021-manabe-climate", 2021, "physics", "Physical modeling of Earth's climate", [], []),
    ("1962-watson-crick-dna", 1962, "medicine", "Structure of DNA", [], ["natural-selection"]),
    ("2020-doudna-crispr", 2020, "chemistry", "CRISPR-Cas9 genome editing", [], []),
    ("1970-samuelson-economics", 1970, "economics", "Scientific work in economic sciences", [], ["comparative-advantage"]),
    ("1998-amartya-sen-capabilities", 1998, "economics", "Welfare economics and social choice", [], ["social-choice"]),
    ("2017-thaler-nudge", 2017, "economics", "Behavioral economics and nudge", [], ["loss-aversion"]),
    ("1906-pavlov-reflexes", 1904, "medicine", "Physiology of digestion / conditioning", [], ["hebbian-learning"]),
    ("1986-rubbia-particles", 1984, "physics", "W and Z boson discovery", [], []),
    ("1965-feynman-qed", 1965, "physics", "Quantum electrodynamics", [], []),
    ("2019-esther-duflo-development", 2019, "economics", "Experimental approach to alleviating poverty", [], []),
    ("2007-mirror-neurons-discovery", 2007, "none", "Mirror neuron system characterization", [], ["hebbian-learning"]),
    ("1952-hodgkin-neuron", 1952, "medicine", "Ionic mechanisms nerve excitation", [], []),
    ("1990-merton-capital-asset", 1990, "economics", "Financial economics theory", [], ["ergodicity"]),
    ("2016-hart-contract-theory", 2016, "economics", "Contract theory", [], ["mechanism-design"]),
    ("2001-akerlof-markets", 2001, "economics", "Markets with asymmetric information", [], ["signaling-games"]),
    ("1982-kreps-reputation", 1982, "economics", "Reputation in repeated games", [], ["iterated-prisoners-dilemma"]),
    ("2014-tirole-industrial", 2014, "economics", "Market power and regulation", [], []),
    ("1936-keynes-general-theory", 1936, "economics", "General Theory (macro foundation)", [], []),
    ("2023-quantum-dots", 2023, "chemistry", "Quantum dots discovery", [], []),
]

# --- MENTAL MODELS ---
MENTAL_MODELS = [
    ("map-is-not-territory", "The Map Is Not the Territory", "Models differ from reality; don't confuse them.", ["cognitive-biases-overview"]),
    ("circle-of-competence", "Circle of Competence", "Know what you know and don't know.", []),
    ("inversion", "Inversion", "Solve backward; avoid failure modes.", []),
    ("second-order-thinking", "Second-Order Thinking", "Ask 'and then what?'", []),
    ("occams-razor", "Occam's Razor", "Prefer simpler explanations.", []),
    ("hanlons-razor", "Hanlon's Razor", "Don't attribute to malice what stupidity explains.", []),
    ("chestertons-fence", "Chesterton's Fence", "Understand before removing institutions.", ["ostrom-commons-design"]),
    ("lindy-effect", "Lindy Effect", "Non-perishable things live longer if old.", []),
    ("probabilistic-thinking", "Probabilistic Thinking", "Reason in probabilities not certainties.", ["bayes-theorem"]),
    ("opportunity-cost", "Opportunity Cost", "Every choice forecloses alternatives.", ["comparative-advantage"]),
    ("margin-of-safety", "Margin of Safety", "Buffer against error and uncertainty.", []),
    ("feedback-loops-model", "Feedback Loops (mental model)", "Outputs circle back as inputs.", ["feedback-loops"]),
    ("critical-mass", "Critical Mass", "Threshold after which growth accelerates.", ["threshold-models"]),
    ("tipping-point-model", "Tipping Point", "Small change triggers large shift.", ["threshold-models"]),
    ("network-effects-model", "Network Effects", "Value grows with users.", ["preferential-attachment"]),
    ("switching-costs", "Switching Costs", "Lock-in from changing systems.", ["path-dependence"]),
    ("tragedy-of-commons-model", "Tragedy of the Commons (mental model)", "Individual incentive vs collective good.", ["tragedy-of-commons"]),
    ("principal-agent", "Principal-Agent Problem", "Misaligned incentives between delegate and delegator.", ["mechanism-design"]),
    ("information-asymmetry", "Information Asymmetry", "One party knows more than another.", ["signaling-games"]),
    ("survivorship-bias-model", "Survivorship Bias", "Dead don't report.", ["regression-to-mean"]),
    ("availability-heuristic-model", "Availability Heuristic", "Recent/vivid = frequent.", ["cognitive-biases-overview"]),
    ("confirmation-bias-model", "Confirmation Bias", "Seek confirming evidence.", ["cognitive-biases-overview"]),
    ("sunk-cost-model", "Sunk Cost", "Past costs shouldn't drive future choices.", []),
    ("hyperbolic-discounting-model", "Hyperbolic Discounting", "Now beats later too strongly.", ["loss-aversion"]),
    ("social-proof", "Social Proof", "Follow others under uncertainty.", ["information-cascades"]),
    ("reciprocity-norm", "Reciprocity", "Repay in kind.", ["iterated-prisoners-dilemma"]),
    ("commitment-consistency", "Commitment and Consistency", "Align with prior public choices.", []),
    ("authority-bias", "Authority Bias", "Defer to perceived experts.", []),
    ("scarcity-urgency", "Scarcity", "Limited availability increases desire.", []),
    ("loss-aversion-model", "Loss Aversion (mental model)", "Losses hurt more than gains please.", ["loss-aversion"]),
    ("expected-value", "Expected Value", "Probability-weighted outcomes.", ["bayes-theorem"]),
    ("reversion-to-mean-model", "Reversion to the Mean", "Extremes tend toward average.", ["regression-to-mean"]),
    ("power-law-thinking", "Power Law Thinking", "Few dominate distributions.", ["preferential-attachment"]),
    ("emergence-model", "Emergence (mental model)", "Whole ≠ sum of parts.", ["emergence"]),
    ("antifragility", "Antifragility", "Gain from disorder (popularization).", []),
    ("via-negativa", "Via Negativa", "Improve by removal not addition.", []),
    ("red-team-thinking", "Red Team Thinking", "Adversarial challenge to plans.", []),
    ("premortem", "Premortem", "Imagine failure before starting.", []),
    ("steel-manning", "Steel Manning", "Strongest version of opponent's argument.", []),
    ("systems-thinking-model", "Systems Thinking", "See interconnections and loops.", ["feedback-loops"]),
    ("goodharts-law-model", "Goodhart's Law (mental model)", "Metrics corrupt when targeted.", ["goodharts-law"]),
]

# --- PHENOMENA ---
PHENOMENA = [
    ("residential-segregation", "Residential Segregation", "Spatial separation of demographic groups.", ["schelling-segregation"], "social-science"),
    ("bystander-effect", "Bystander Effect", "Help decreases with more observers.", [], "social-science"),
    ("groupthink", "Groupthink", "Consensus pressure suppresses dissent.", ["pluralistic-ignorance"], "social-science"),
    ("filter-bubble", "Filter Bubble", "Algorithmic narrowing of information.", [], "social-science"),
    ("echo-chamber-phenomenon", "Echo Chamber", "Homogeneous views amplify.", ["information-cascades"], "social-science"),
    ("viral-misinformation", "Viral Misinformation", "Falsehood spreads faster than truth.", ["complex-contagion"], "social-science"),
    ("wealth-inequality", "Wealth Inequality", "Unequal asset distribution.", ["comparative-advantage"], "economics"),
    ("climate-tipping-points", "Climate Tipping Points", "Nonlinear Earth system shifts.", ["self-organized-criticality"], "environmental-science"),
    ("market-bubbles", "Market Bubbles", "Asset prices detach from fundamentals.", ["information-cascades"], "economics"),
    ("bank-runs", "Bank Runs", "Self-fulfilling liquidity crises.", ["information-cascades"], "economics"),
    ("traffic-jams", "Traffic Jams", "Phantom jams from density.", ["percolation"], "engineering"),
    ("predator-prey-cycles", "Predator-Prey Cycles", "Population oscillations.", ["natural-selection"], "ecology"),
    ("keystone-species-effects", "Keystone Species Effects", "Disproportionate ecosystem impact.", [], "ecology"),
    ("inattentional-blindness", "Inattentional Blindness", "Miss obvious when attention elsewhere.", [], "cognitive-science"),
    ("change-blindness-phenomenon", "Change Blindness", "Fail to detect large scene changes.", [], "cognitive-science"),
    ("placebo-effect", "Placebo Effect", "Belief produces physiological change.", [], "medicine"),
    ("nocebo-effect", "Nocebo Effect", "Harm from negative expectation.", [], "medicine"),
    ("stereotype-threat", "Stereotype Threat", "Performance drops when stereotype salient.", [], "social-science"),
    ("fundamental-attribution", "Fundamental Attribution Error (phenomenon)", "Overattribute others' acts to character.", [], "social-science"),
    ("hot-hand-fallacy", "Hot Hand Fallacy", "Perceive streaks in random sequences.", ["regression-to-mean"], "probability"),
    ("anchoring-phenomenon", "Anchoring (phenomenon)", "First number biases estimates.", [], "cognitive-science"),
    ("conformity-norm", "Social Conformity", "Align behavior with group.", ["pluralistic-ignorance"], "social-science"),
    ("cultural-evolution", "Cultural Evolution", "Ideas replicate and mutate.", ["natural-selection"], "anthropology-discipline"),
    ("language-change", "Language Change", "Meaning drifts over generations.", [], "linguistics-discipline"),
    ("urban-decay", "Urban Decay", "Neighborhood decline spiral.", ["jacobs-four-generators"], "urbanism"),
    ("gentrification", "Gentrification", "Displacement from rising rents.", [], "urbanism"),
    ("scientific-revolutions", "Scientific Revolutions", "Paradigm shifts in science.", [], "history-of-science-discipline"),
    ("replication-crisis", "Replication Crisis", "Many studies fail to replicate.", [], "history-of-science-discipline"),
    ("ai-hallucination", "AI Hallucination", "Confident false model outputs.", [], "computer-science"),
    ("filter-feed-algorithm", "Algorithmic Feed Curation", "Engagement optimization shapes belief.", [], "social-science"),
    ("polarization", "Political Polarization", "Opinion clusters diverge.", [], "political-science"),
    ("social-media- outrage-cycles", "Outrage Cycles", "Anger amplifies in feedback loops.", ["feedback-loops"], "social-science"),
    ("pandemic-exponential-growth", "Exponential Epidemic Growth", "Early epidemic doubling.", ["percolation"], "medicine"),
    ("herd-immunity-threshold", "Herd Immunity Threshold", "Vaccination fraction stops spread.", ["percolation"], "medicine"),
    ("network-outage-cascades", "Network Outage Cascades", "Infrastructure failure chains.", ["percolation"], "engineering"),
]

# Fix typo in phenomena slug
PHENOMENA = [(s.replace("social-media- outrage", "social-media-outrage"), *rest) for s, *rest in PHENOMENA]

# --- HYBRID SIMS ---
HYBRIDS = [
    ("bayesian-therapy", "Bayesian Therapy", "Bayes × base rate × availability heuristic.", ["bayes-theorem", "cognitive-biases-overview"]),
    ("memory-channel", "Memory Channel", "Information theory × forgetting curve.", ["shannon-entropy", "spaced-repetition"]),
    ("evolutionary-trust-ecology", "Evolutionary Trust Ecology", "Evolution × game theory × networks.", ["evolution-of-cooperation", "iterated-prisoners-dilemma"]),
    ("urban-percolation-equity", "Urban Percolation Equity", "Percolation × Schelling × Jacobs.", ["percolation", "schelling-segregation", "jacobs-four-generators"]),
    ("metric-hydra", "The Metric Hydra", "Goodhart × Campbell × Cobra × Petrie.", ["goodharts-law", "petrie-multiplier-paradox"]),
    ("ergodic-inequality", "Ergodic Inequality", "Ergodicity × Matthew effect × Kelly.", ["ergodicity", "regression-to-mean"]),
    ("contagion-of-courage", "Contagion of Courage", "Complex contagion × pluralistic ignorance × threshold.", ["complex-contagion", "pluralistic-ignorance"]),
    ("forecasting-market-crowds", "Forecasting Market of Crowds", "Prediction markets × Dunning-Kruger × cascades.", ["information-cascades", "cognitive-biases-overview"]),
    ("thermodynamic-attention", "Thermodynamic Attention", "Entropy × Maxwell demon × social feeds.", ["entropy", "feedback-loops"]),
    ("ostrom-network", "The Ostrom Network", "Ostrom × network science × commons.", ["ostrom-commons-design", "percolation"]),
    ("paradox-traffic-of-ideas", "Paradox Traffic of Ideas", "Braess × echo chambers.", ["information-cascades", "percolation"]),
    ("sleeping-beauty-portfolio", "Sleeping Beauty's Portfolio", "Sleeping beauty × ergodicity × Kelly.", ["ergodicity", "sleeping-beauty-problem"]),
    ("stochastic-resonance-democracy", "Stochastic Resonance Democracy", "Stochastic resonance × opinion dynamics.", ["coupled-oscillators", "pluralistic-ignorance"]),
    ("krebs-cycle-of-outrage", "Krebs Cycle of Outrage", "Media feedback × Hebbian learning.", ["feedback-loops", "hebbian-learning"]),
    ("polya-culture-wars", "Polya Culture Wars", "Polya urn × cultural polarization.", ["preferential-attachment", "pluralistic-ignorance"]),
]

# Theory slug map from research theory names (approximate)
THEORY_MAP = {
    "Petrie (2013)": "petrie-multiplier-paradox",
    "Granovetter threshold model": "threshold-models",
    "Rawls' veil of ignorance": "social-choice",
    "Ostrom + Hardin": "ostrom-commons-design",
    "Cobra effect": "goodharts-law",
    "Goodhart's law": "goodharts-law",
    "Campbell's law": "goodharts-law",
    "Majority illusion (Lerman et al.)": "information-cascades",
    "Granovetter weak ties": "information-cascades",
    "Schelling focal points": "mechanism-design",
    "Monty Hall": "bayes-theorem",
    "Simpson's paradox": "regression-to-mean",
    "Ole Peters ergodicity": "ergodicity",
    "Percolation theory": "percolation",
    "Complex contagion": "complex-contagion",
    "Iterated Prisoner's Dilemma": "iterated-prisoners-dilemma",
    "Newcomb's problem": "newcomb-problem",
    "Braess paradox": "percolation",
    "Parrondo's paradox": "parrondos-paradox",
}


def theory_slug(name):
    name = name.strip()
    if name in THEORY_MAP:
        return THEORY_MAP[name]
    s = slugify(name.split("(")[0])
    return s if s else "emergence"


def main():
    counts = {"sim": 0, "par": 0, "exp": 0, "pap": 0, "nob": 0, "mod": 0, "phn": 0, "hyb": 0, "sci": 0}

    # SIM from research
    sims = parse_research_sims()
    for i, s in enumerate(sims, 1):
        sid = f"SIM-{i:04d}"
        thy = theory_slug(s["theory_name"])
        fm = {
            "id": sid,
            "type": "simulation-concept",
            "slug": s["slug"],
            "title": s["title"],
            "summary": s["summary"],
            "status": "mature",
            "created": "2026-06-26",
            "updated": "2026-06-26",
            "build_difficulty": "medium",
            "build_estimate_weeks": 3,
            "related": {"theories": [thy], "design": {"patterns": ["parameter-slider", "sandbox-mode"]}},
            "explorable": {
                "verdict": "essential",
                "best_medium": "web-simulation",
                "best_medium_stars": 5,
                "best_medium_reason": "Behavior only becomes intuitive when users manipulate parameters.",
            },
        }
        body = [
            f"# {s['title']}",
            "",
            f"**Tagline:** {s['summary']}",
            "",
            f"## Theory\n\n- [[{thy}]]",
            "",
            "## Core interaction",
            "",
            s["summary"],
            "",
            "## Discovery suggestions",
            "",
            f"- Based on research concept #{s['num']}",
        ]
        if write(f"simulations/concepts/{s['slug']}.md", fm, body):
            counts["sim"] += 1

    # Hybrid SIMs
    for i, (slug, title, summary, theories) in enumerate(HYBRIDS, 1):
        sid = f"SIM-{1000 + i:04d}"
        fm = {
            "id": sid,
            "type": "simulation-concept",
            "slug": slug,
            "title": title,
            "summary": summary,
            "status": "mature",
            "created": "2026-06-26",
            "updated": "2026-06-26",
            "hybrid": True,
            "related": {"theories": theories},
            "explorable": {"verdict": "essential", "best_medium": "web-simulation", "best_medium_stars": 5},
        }
        body = [f"# {title}", "", summary, "", "## Combined theories", ", ".join(f"[[{t}]]" for t in theories)]
        if write(f"simulations/concepts/{slug}.md", fm, body):
            counts["hyb"] += 1

    # Paradoxes
    for i, (slug, title, summary, field, theories) in enumerate(PARADOXES, 1):
        fm = {
            "id": f"PAR-{i:04d}",
            "type": "paradox",
            "slug": slug,
            "title": title,
            "summary": summary,
            "status": "mature",
            "created": "2026-06-26",
            "updated": "2026-06-26",
            "fields": [field] if field else ["philosophy"],
            "related": {"theories": theories},
            "explorable": {
                "verdict": "strong",
                "why_interaction": "Paradox resolves only after user commits to a choice or runs simulation.",
                "best_medium": "interactive-game",
                "best_medium_stars": 4,
            },
        }
        body = [f"# {title}", "", "## Statement", summary, "", "## Why interaction beats reading", "Force prediction before reveal."]
        if write(f"paradoxes/{field}/{slug}.md" if field else f"paradoxes/{slug}.md", fm, body):
            counts["par"] += 1

    # Experiments
    for i, (slug, title, year, summary, theories, fields) in enumerate(EXPERIMENTS, 1):
        fm = {
            "id": f"EXP-{i:04d}",
            "type": "experiment",
            "slug": slug,
            "title": title,
            "summary": summary,
            "status": "mature",
            "year": year,
            "created": "2026-06-26",
            "updated": "2026-06-26",
            "fields": fields or ["social-science"],
            "related": {"theories": theories},
            "explorable": {
                "verdict": "strong",
                "why_interaction": "Recreate as subject or experimenter.",
                "best_medium": "interactive-game",
                "best_medium_stars": 4,
            },
        }
        body = [f"# {title}", "", f"**Year:** {year}", "", summary]
        if write(f"experiments/{slug}.md", fm, body):
            counts["exp"] += 1

    # Papers
    for i, (fname, slug, title, year, authors, theories, venue) in enumerate(PAPERS, 1):
        fm = {
            "id": f"PAP-{i + 1:04d}",
            "type": "paper",
            "slug": slug,
            "title": title,
            "summary": f"Published {year}. {venue}.",
            "status": "mature",
            "year": year,
            "venue": venue,
            "created": "2026-06-26",
            "updated": "2026-06-26",
            "authors": authors,
            "related": {"theories": theories},
            "explorable": {"verdict": "moderate", "why_interaction": "Key results deserve simulation."},
        }
        body = [f"# {title}", "", f"**Year:** {year} · **Venue:** {venue}"]
        if write(f"publications/papers/{fname}.md", fm, body):
            counts["pap"] += 1

    # Nobel
    for i, (slug, year, cat, summary, laureates, theories) in enumerate(NOBELS, 1):
        fm = {
            "id": f"NOB-{i:04d}",
            "type": "nobel",
            "slug": slug,
            "title": summary,
            "summary": summary,
            "status": "mature",
            "year": year,
            "category": cat,
            "created": "2026-06-26",
            "updated": "2026-06-26",
            "laureates": laureates,
            "related": {"theories": theories},
            "explorable": {"verdict": "moderate", "best_medium": "visualization", "best_medium_stars": 3},
        }
        body = [f"# {summary}", "", f"**Year:** {year} · **Category:** {cat}"]
        if write(f"publications/nobel/{slug}.md", fm, body):
            counts["nob"] += 1

    # Mental models
    for i, (slug, title, summary, theories) in enumerate(MENTAL_MODELS, 1):
        fm = {
            "id": f"MOD-{i:04d}",
            "type": "mental-model",
            "slug": slug,
            "title": title,
            "summary": summary,
            "status": "mature",
            "created": "2026-06-26",
            "updated": "2026-06-26",
            "related": {"theories": theories},
            "explorable": {"verdict": "moderate", "best_medium": "visualization", "best_medium_stars": 3},
        }
        body = [f"# {title}", "", summary]
        if write(f"mental-models/{slug}.md", fm, body):
            counts["mod"] += 1

    # Phenomena
    for i, (slug, title, summary, theories, field) in enumerate(PHENOMENA, 1):
        fm = {
            "id": f"PHN-{i:04d}",
            "type": "phenomenon",
            "slug": slug,
            "title": title,
            "summary": summary,
            "status": "mature",
            "created": "2026-06-26",
            "updated": "2026-06-26",
            "fields": [field],
            "related": {"theories": theories},
            "explorable": {"verdict": "strong", "why_interaction": "Phenomenon visible only when system runs."},
        }
        body = [f"# {title}", "", summary]
        if write(f"phenomena/{field}/{slug}.md", fm, body):
            counts["phn"] += 1

    # Scientists
    scientists = [
        ("daniel-kahneman", "Daniel Kahneman", "Prospect theory; behavioral economics Nobel 2002."),
        ("amos-tversky", "Amos Tversky", "Heuristics and biases with Kahneman."),
        ("mark-granovetter", "Mark Granovetter", "Weak ties; threshold models."),
        ("daniel-kahneman", "Daniel Kahneman", "duplicate skip"),
    ]
    seen = set()
    sci_i = 4
    for slug, title, summary in [
        ("daniel-kahneman", "Daniel Kahneman", "Prospect theory; Nobel 2002."),
        ("amos-tversky", "Amos Tversky", "Heuristics and biases."),
        ("mark-granovetter", "Mark Granovetter", "Weak ties; threshold models."),
        ("ole-peters", "Ole Peters", "Ergodicity economics."),
        ("daniel-c-dennett", "Daniel Dennett", "Consciousness; evolution of memes."),
        ("thomas-b-schelling", "Thomas C. Schelling", "See thomas-schelling."),
        ("duncan-j-watts", "Duncan J. Watts", "Small-world networks."),
        ("albert-laszlo-barabasi", "Albert-László Barabási", "Scale-free networks."),
        ("daniel-kahneman", "skip", "skip"),
    ]:
        if slug in seen or slug == "skip":
            continue
        seen.add(slug)
        sci_i += 1
        fm = {
            "id": f"SCI-{sci_i:04d}",
            "type": "scientist",
            "slug": slug,
            "title": title,
            "summary": summary,
            "status": "mature",
            "created": "2026-06-26",
            "updated": "2026-06-26",
        }
        if write(f"people/scientists/{slug}.md", fm, [f"# {title}", "", summary]):
            counts["sci"] += 1

    print("Generated:", counts)
    total = sum(counts.values())
    print(f"Total new files: {total}")


if __name__ == "__main__":
    main()
