"""Schelling-quality body content for expansion MORE_CONCEPTS pages."""

from __future__ import annotations

from pathlib import Path

from canonical_promote import CONTENT


def schelling_body(
    title: str,
    essence: str,
    why: str,
    core: str,
    mechanism: str,
    implications: str,
    related: list[str],
    reading: str,
    misconceptions: list[tuple[str, str]] | None = None,
) -> str:
    rel = " · ".join(f"[[{r}]]" for r in related[:6])
    impl = implications.strip()
    if not impl.startswith("-"):
        impl = "\n".join(f"- {line.lstrip('- ')}" for line in impl.split("\n") if line.strip())

    parts = [
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
        "## Mechanism",
        "",
        mechanism,
        "",
        "## Implications",
        "",
        impl,
    ]
    if misconceptions:
        parts.extend(
            [
                "",
                "## Common misconceptions",
                "",
                "| Wrong | Right |",
                "|-------|-------|",
            ]
        )
        for wrong, right in misconceptions:
            parts.append(f"| {wrong} | {right} |")

    parts.extend(
        [
            "",
            "## Related",
            "",
            rel,
            "",
            "## Further reading",
            "",
            reading,
            "",
            "## Discovery suggestions",
            "",
            "- [ ] Interactive scenario illustrating the mechanism",
            "- [ ] Cross-link to experiment or simulation where applicable",
        ]
    )
    return "\n".join(parts) + "\n"


UPGRADES: dict[str, dict] = {
    "cognitive-dissonance": {
        "essence": "Mental discomfort when beliefs and actions conflict — often resolved by changing beliefs, not behaviour.",
        "why": "Explains post-purchase rationalisation, smoking-while-knowing-the-risks, and why facts rarely change minds once someone has acted. Without dissonance theory, persuasion campaigns misdiagnose resistance as ignorance.",
        "core": "Leon Festinger's**cognitive dissonance**is the aversive tension from holding inconsistent cognitions — especially when behaviour contradicts self-image. People reduce it by changing beliefs, adding justifications, or avoiding disconfirming information rather than reversing costly actions.",
        "mechanism": "1. Person holds belief *B* (e.g. \"I am rational\") and performs action *A* inconsistent with *B*.\n2. Dissonance produces psychological discomfort.\n3. Mind seeks least-cost resolution: often cheaper to revise *B* (\"the product is fine\") than undo *A*.\n4. Justifications accumulate; subsequent information is filtered to preserve the new consistency.",
        "implications": "- Small commitments escalate — foot-in-the-door exploits dissonance after initial compliance.\n- Harsh initiation rituals increase group loyalty by making exit psychologically costly.\n- Debates after someone has publicly committed rarely succeed by adding facts alone.",
        "reading": "- Festinger, L. (1957). *A Theory of Cognitive Dissonance*. Stanford University Press.\n- Festinger & Carlsmith (1959). Cognitive consequences of forced compliance. *Journal of Abnormal and Social Psychology*.\n- Link to [[asch-conformity]] for social pressure variants.",
        "misconceptions": [
            ("Dissonance means lying consciously", "Much resolution is automatic and feels sincere"),
            ("More evidence always fixes inconsistency", "Action-first paths often change beliefs instead"),
        ],
    },
    "defense-mechanisms": {
        "essence": "Unconscious strategies that reduce anxiety by distorting how threat is perceived.",
        "why": "Maps how people deny, project, or rationalise without deliberate deception — relevant in conflict, therapy, and organisational blame cycles.",
        "core": "Freudian and neo-Freudian**defense mechanisms** (denial, projection, rationalisation, displacement) shield the ego from intolerable affect. They are not moral failures but automatic regulators — useful in acute stress, costly when they become habitual.",
        "mechanism": "1. Ego registers impulse, memory, or fact that threatens self-esteem or safety.\n2. Anxiety signal exceeds tolerable threshold.\n3. Unconscious process reframes, blocks, or redirects the threat (e.g. anger at boss → snapped at partner).\n4. Relief reinforces the pattern; insight may require external mirror or crisis.",
        "implications": "- Feedback that ignores underlying threat triggers stronger defenses, not learning.\n- Organisational scapegoating often displaces anxiety from systemic failure onto individuals.\n- Therapeutic and mediation settings work partly by lowering threat enough to reduce defensive distortion.",
        "reading": "- Freud, A. (1936). *The Ego and the Mechanisms of Defence*. Hogarth Press.\n- Cramer, P. (2006). *Protecting the Self: Defense Mechanisms in Action*. Guilford.\n- See [[psychological-projection]] for one high-salience mechanism.",
        "misconceptions": [
            ("Defense mechanisms are excuses for bad behaviour", "They describe unconscious regulation, not moral permission"),
            ("Healthy people don't use them", "Everyone uses them; question is flexibility vs rigidity"),
        ],
    },
    "psychological-projection": {
        "essence": "Attributing one's own unacceptable feelings or motives to others.",
        "why": "Clarifies accusations that reveal more about the accuser than the accused — common in polarised politics, jealousy, and workplace conflict.",
        "core": "**Projection**externalises disowned inner states: if I cannot admit envy, I \"see\" others as envious of me. It preserves self-image while exporting discomfort — often sincerely felt, not calculated.",
        "mechanism": "1. Person experiences impulse or trait incompatible with ideal self (hostility, desire, incompetence).\n2. Ego rejects ownership — anxiety spikes.\n3. Same content is perceived in others' behaviour with high confidence.\n4. External conflict validates the projection; loop tightens until insight or relationship rupture.",
        "implications": "- \"What bothers you about them may live in you\" is mechanistic, not mystical.\n- Projection fuels moral panics when groups disown collective impulses.\n- De-escalation often requires separating observed behaviour from attributed motive.",
        "reading": "- Freud, S. (1915). *Instincts and Their Vicissitudes* — projection as defense.\n- Newman, D. S., Duff, K. J., & Baumeister, R. F. (1997). A new look at defensive projection. *Journal of Personality and Social Psychology*.\n- [[defense-mechanisms]] · [[in-group-bias]]",
    },
    "confirmation-bias": {
        "essence": "Seeking, interpreting, and remembering evidence that supports what we already believe.",
        "why": "Undermines naive empiricism: even careful people cherry-pick without noticing. Explains filter bubbles, bad hiring, and why smart teams double down on failed strategies.",
        "core": "**Confirmation bias**operates at three stages: search (ask questions that can confirm), interpretation (ambiguous data read as supportive), and memory (recall hits, forget misses). It is not stupidity — it is efficient belief maintenance with systematic error.",
        "mechanism": "1. Prior hypothesis or identity-linked belief activates.\n2. Information search skews toward confirming sources and tests.\n3. Ambiguous evidence weighted toward prior; disconfirming evidence held to higher standard.\n4. Selective recall strengthens narrative; belief feels evidence-based.",
        "implications": "- Pre-registration and blind analysis in science directly counter confirmation at design stage.\n- Devil's advocate roles fail if they are performative — need genuine incentive to find disconfirmation.\n- Pair with [[predict-then-reveal]] in explorable design to surface bias before outcomes.",
        "reading": "- Nickerson, R. S. (1998). Confirmation bias: A ubiquitous phenomenon in many guises. *Review of General Psychology*.\n- Wason, P. C. (1960). On the failure to eliminate hypotheses. *Quarterly Journal of Experimental Psychology* — link [[wason-selection-task]].\n- Kahneman, D. (2011). *Thinking, Fast and Slow*. Farrar, Straus and Giroux.",
        "misconceptions": [
            ("Only partisan hacks confirm", "Experts confirm within their paradigms too"),
            ("Showing counter-evidence instantly updates belief", "Identity-linked beliefs resist; dissonance routes around facts"),
        ],
    },
    "availability-heuristic": {
        "essence": "Judging frequency or probability by how easily examples come to mind.",
        "why": "Media coverage, vivid anecdotes, and personal trauma distort risk perception — plane crashes feel commoner than bathtub falls; shark attacks loom larger than heart disease in beach towns.",
        "core": "Tversky and Kahneman's**availability heuristic**substitutes recall fluency for statistical frequency. Recent, emotional, or well-publicised events dominate judgment even when base rates say otherwise.",
        "mechanism": "1. Question requires frequency or risk estimate.\n2. Mind retrieves exemplars — not a random sample from population.\n3. Ease of retrieval treated as proxy for prevalence.\n4. Decisions (insurance, policy, parenting) follow biased mental sample.",
        "implications": "- News cycles systematically skew public priorities toward spectacular rare events.\n- After disasters, overreaction and expensive precaution often follow availability spikes.\n- Corrective: explicit base rates ([[base-rate-neglect]]) and reference class forecasting.",
        "reading": "- Tversky, A., & Kahneman, D. (1973). Availability: A heuristic for judging frequency and probability. *Cognitive Psychology*.\n- Slovic, P. (1987). Perception of risk. *Science*.\n- [[cognitive-biases]] hub.",
    },
    "hindsight-bias": {
        "essence": "After an outcome, believing it was predictable all along — \"I knew it all along.\"",
        "why": "Corrupts accountability: leaders judged harshly for surprises that were genuinely uncertain; historians rewrite inevitability into complex paths.",
        "core": "**Hindsight bias**rewrites memory and probability judgments after the fact. Outcomes that were 40% likely feel obvious at 90% — distorting learning from failure and legal standards of foresight.",
        "mechanism": "1. Outcome becomes known.\n2. Memory reconstructs pre-outcome beliefs as closer to actual result.\n3. Narrative coherence demands inevitability — randomness edited out.\n4. Observers blame actors for not \"seeing the obvious.\"",
        "implications": "- Post-mortems must capture *contemporaneous* forecasts, not retrofitted stories.\n- Medical and legal malpractice standards struggle with hindsight-inflated expectations.\n- Explorable design: record predictions before reveal ([[predict-then-reveal]]).",
        "reading": "- Fischhoff, B. (1975). Hindsight ≠ foresight: The effect of outcome knowledge on judgment under uncertainty. *Journal of Experimental Psychology*.\n- Roese, N. J., & Vohs, K. D. (2012). Hindsight bias. *Perspectives on Psychological Science*.\n- [[overconfidence-bias]] often compounds hindsight.",
    },
    "dunning-kruger-effect": {
        "essence": "Low competence can impair recognition of one's own incompetence — confidence and skill decouple at the bottom.",
        "why": "Explains confident wrongness in novices, bad tutorials, and why expertise requires meta-skill to evaluate quality. Cautionary for crowdsourced \"expertise.\"",
        "core": "The**Dunning–Kruger effect** (Kruger & Dunning, 1999) describes a statistical pattern: the least skilled in a domain often overestimate themselves most, because the same deficits that hurt performance hurt self-assessment. Experts may slightly underestimate relative to peers.",
        "mechanism": "1. Novice lacks knowledge to recognise good vs bad performance.\n2. Self-assessment uses same flawed toolkit as task performance.\n3. Overconfidence peaks at low absolute skill in many domains.\n4. Training both improves skill and calibration — meta-cognitive loop closes.",
        "implications": "- Feedback from unskilled peers can reinforce error — need external benchmarks.\n- Humility training alone fails without actual competence building.\n- Internet debates often pair peak overconfidence with minimal domain knowledge.",
        "reading": "- Kruger, J., & Dunning, D. (1999). Unskilled and unaware of it. *Journal of Personality and Social Psychology*.\n- Dunning, D. (2011). The Dunning–Kruger effect: On being ignorant of one's own ignorance. *Advances in Experimental Social Psychology*.\n- Note: meme versions exaggerate; effect is contested at margins but calibration literature is robust.",
        "misconceptions": [
            ("Smart people never overestimate", "Expertise miscalibration takes different forms — not always novice overconfidence"),
            ("DK proves idiots can't learn", "Training improves both skill and self-assessment"),
        ],
    },
    "black-swan-events": {
        "essence": "Rare, high-impact outcomes that look predictable only in retrospect.",
        "why": "Financial crises, pandemics, and technological shocks break models tuned on \"normal\" history. Risk management that ignores tail events is fragile by design.",
        "core": "Nassim Taleb's**black swan**metaphor: outliers outside prior experience that reshape systems. They are not merely unlikely — they rewrite the reference class and expose silent assumptions in models and institutions.",
        "mechanism": "1. Models and institutions fit past regularities (thin-tail assumptions).\n2. Hidden exposure accumulates (leverage, monoculture, just-in-time supply).\n3. Tail event occurs — impact disproportional to ex ante probability.\n4. Retrospective narratives declare it \"obvious\"; few penalties for prior blindness.",
        "implications": "- Stress-test for survival, not average performance — [[fat-tailed-distributions]] matter.\n- Redundancy and optionality beat optimised efficiency under tail risk.\n- Post-hoc regulation often fights the last black swan, not the next.",
        "reading": "- Taleb, N. N. (2007). *The Black Swan*. Random House.\n- Taleb, N. N. (2012). *Antifragile*. Random House.\n- Mandelbrot, B. (1963). The variation of certain speculative prices. *Journal of Business* — fat tails in finance.",
    },
    "fat-tailed-distributions": {
        "essence": "Extreme outcomes occur far more often than Gaussian curves predict.",
        "why": "Mean-variance finance, Gaussian safety margins, and \"six sigma\" thinking fail when variance is infinite or dominated by rare giants — wealth, casualties, viral spread.",
        "core": "**Fat tails**mean probability mass in extremes decays slowly (power laws vs exponential). Sample averages and maxima from small samples wildly underestimate true tail risk — the worst event seen is not the worst possible.",
        "mechanism": "1. Process generates outcomes with heavy-tailed law (returns, city sizes, epidemic superspreaders).\n2. Observers fit thin-tail models from limited data.\n3. Routine period confirms \"normality\"; rare draw moves system more than entire prior history.\n4. Models recalibrated after crisis — until next tail.",
        "implications": "- Portfolio and infrastructure design: cap downside, not optimise mean.\n- \"Never happened before\" ≠ safe when tails are fat.\n- Simulations: [[fat-tail-farm]] · [[sandpile-avalanche]] for intuition.",
        "reading": "- Newman, M. E. J. (2005). Power laws, Pareto distributions and Zipf's law. *Contemporary Physics*.\n- Taleb, N. N. (2020). *Statistical Consequences of Fat Tails*. STEM Academic Press.\n- Clauset, A., Shalizi, C. R., & Newman, M. E. J. (2009). Power-law distributions in empirical data. *SIAM Review*.",
    },
    "regression-to-the-mean": {
        "essence": "Extreme measurements tend to be followed by less extreme ones — partly statistics, partly real dynamics.",
        "why": "Misattributes improvement to interventions (coaching, medicine, punishment) when extremes were partly luck. Also explains sports \" sophomore slumps\" and CEO hero narratives.",
        "core": "**Regression to the mean**occurs when variables correlate imperfectly over time: an unusually high score likely combined skill with positive noise; next draw likely less noise → lower score even if skill unchanged.",
        "mechanism": "1. Select cases by extreme performance (best schools, sickest patients, worst quarters).\n2. Component of extreme was transient (measurement error, luck, mood).\n3. Next measurement closer to long-run average.\n4. Observers credit intervention or punishment for \"natural\" rebound.",
        "implications": "- Control groups essential — without them, regression masquerades as treatment effect.\n- Performance pay on short windows rewards luck then punishes reversion.\n- Pair with [[simpsons-paradox]] when aggregating trends.",
        "reading": "- Galton, F. (1886). Regression towards mediocrity in hereditary stature. *Journal of the Anthropological Institute*.\n- Kahneman, D. (2011). *Thinking, Fast and Slow* — chapter on regression.\n- Barnett, A. G., van der Pols, J. C., & Dobson, A. J. (2005). Regression to the mean. *International Journal of Epidemiology*.",
        "misconceptions": [
            ("Regression means everyone becomes average", "It is about relative movement toward one's own mean, not global homogenisation"),
            ("Only a statistical artefact", "Real dynamic processes also mean-revert (thermostats, fatigue)"),
        ],
    },
    "surveillance-capitalism": {
        "essence": "Business models that extract behavioural data and predict — then shape — human action for profit.",
        "why": "Explains why \"free\" platforms feel manipulative, how prediction markets in attention reshape democracy, and why privacy is a collective not individual problem.",
        "core": "Shoshana Zuboff's**surveillance capitalism**describes firms converting experience into behavioural data, using machine intelligence to predict behaviour, and selling**behavioural futures** — with tuning via nudges, A/B tests, and dark patterns.",
        "mechanism": "1. Users generate digital exhaust (clicks, location, social graph).\n2. Platforms infer traits and predict next actions with increasing accuracy.\n3. Predictions sold to advertisers, insurers, political campaigns.\n4. Feedback loop: products redesigned to maximise data yield and prediction edge — not necessarily user welfare.",
        "implications": "- Consent frameworks lag — harms are cumulative and collective ([[digital-panopticon]]).\n- Regulatory focus on data ownership may miss prediction-and-modification core.\n- Alternatives require different incentive architectures, not privacy toggles alone.",
        "reading": "- Zuboff, S. (2019). *The Age of Surveillance Capitalism*. PublicAffairs.\n- Zuboff, S. (2015). Big other: Surveillance capitalism and the prospects of an information civilization. *Journal of Information Technology*.\n- [[technology-and-society]] hub.",
    },
    "algorithmic-bias": {
        "essence": "Systematic errors in automated decisions that disadvantage groups — often encoded in data and objectives.",
        "why": "Hiring filters, credit scores, policing tools, and medical triage increasingly gate life chances. \"Objective algorithm\" branding hides historical inequity and proxy discrimination.",
        "core": "**Algorithmic bias**arises from skewed training data, biased labels, wrong optimization targets, and feedback loops (predict policing → more arrests in same neighbourhoods). Fairness requires explicit values — no neutral default.",
        "mechanism": "1. Historical decisions recorded as training labels (who was hired, arrested, lent to).\n2. Model learns patterns including proxies for protected attributes (zip code, grammar).\n3. Deployment at scale amplifies disparities faster than human inconsistency.\n4. Monitoring on aggregate accuracy misses harms concentrated on minorities.",
        "implications": "- Fairness metrics conflict (equal accuracy vs equal false-positive rate) — politics embedded in math.\n- Audits need affected-community participation, not vendor self-certification.\n- Link [[goodharts-law]] when optimising single KPI.",
        "reading": "- O'Neil, C. (2016). *Weapons of Math Destruction*. Crown.\n- Barocas, S., Hardt, M., & Narayanan, A. (2023). *Fairness and Machine Learning*. fairmlbook.org.\n- Buolamwini, J., & Gebru, T. (2018). Gender shades. *Proceedings of Machine Learning Research*.",
        "misconceptions": [
            ("Remove race column = fair", "Proxies reintroduce protected information"),
            ("Bias is a bug to patch once", "Production systems need ongoing monitoring and contested objectives"),
        ],
    },
    "digital-panopticon": {
        "essence": "Visibility and perceived observation reshape behaviour at scale — even when nobody is watching.",
        "why": "Workplace monitoring, social media performance, and state surveillance change what people say, organise, and invent — chilling effects precede actual punishment.",
        "core": "Bentham's**panopticon**updated: digital infrastructure makes observation cheap, persistent, and asymmetric. People internalise watchers — self-censor, conform, optimise metrics — whether or not anyone reads the logs.",
        "mechanism": "1. Institution or platform makes surveillance plausible (cameras, logs, social feeds).\n2. Subjects uncertain when observation is active — perpetual maybe-watched state.\n3. Behaviour shifts toward legibility and risk avoidance (safe opinions, metric gaming).\n4. Power asymmetry: watchers aggregate; watched fragmented.",
        "implications": "- Democratic dissent and experimentation require zones of practical privacy.\n- Metric transparency without power sharing becomes discipline, not accountability.\n- [[we-become-what-we-behold]] — media mirrors amplify performative behaviour.",
        "reading": "- Foucault, M. (1975). *Discipline and Punish* — panopticism chapter.\n- Braman, S. (2006). The annualized costs of surveillance. *Information, Communication & Society*.\n- Zuboff, S. (2019). *The Age of Surveillance Capitalism* — [[surveillance-capitalism]].",
    },
    "loss-aversion": {
        "essence": "Losses loom larger than equivalent gains — often roughly twice as psychologically salient.",
        "why": "Explains status quo bias, endowment effect, risk-seeking in losses, and why reformers underestimate opposition to small perceived losses.",
        "core": "Kahneman and Tversky's**prospect theory**embeds**loss aversion**: the pain of losing $100 exceeds pleasure of gaining $100. Reference points — not absolute wealth — drive choice.",
        "mechanism": "1. Decision framed relative to reference point (current salary, portfolio peak, pre-policy status quo).\n2. Outcomes evaluated as gains or losses, not final states.\n3. Loss branch steeper than gain branch — reject fair gambles, fight to avoid cuts.\n4. Framing manipulates reference point (\"save $200\" vs \"lose $200\").",
        "implications": "- Policy: compensate visible losers or package as gain — naked loss triggers asymmetric fight.\n- Investors hold losers too long, sell winners too early (disposition effect).\n- [[behavioural-finance]] and negotiation design must map reference points explicitly.",
        "reading": "- Kahneman, D., & Tversky, A. (1979). Prospect theory: An analysis of decision under risk. *Econometrica*.\n- Thaler, R. H. (1980). Toward a positive theory of consumer choice. *Journal of Economic Behavior & Organization*.\n- [[loss-aversion]] simulation links in [[behavioural-finance]].",
    },
    "herd-behaviour": {
        "essence": "Following others' actions when private information is weak, costly, or ambiguous.",
        "why": "Bank runs, meme stocks, fashion cycles, and protest waves often look irrational but are locally sensible — ignoring others' information is costly.",
        "core": "**Herd behaviour**aggregates private signals through observable actions. Rational agents may rationally ignore their own evidence and follow the crowd — especially when early movers are informed.",
        "mechanism": "1. Individuals hold noisy private signals about state of world.\n2. Others' actions partially reveal their signals (buying, protesting, vaccinating).\n3. Weight on social observation rises when private info weak or reputational risk of dissent high.\n4. Cascade: everyone follows first movers; mass behaviour decouples from fundamentals.",
        "implications": "- Transparency of *reasons* matters — opaque crowds trigger panic.\n- Minor shocks can flip equilibria when thresholds cluster ([[information-cascades]]).\n- Leaders and influencers are structural — not cosmetic — in cascade-prone domains.",
        "reading": "- Banerjee, A. V. (1992). A simple model of herd behavior. *Quarterly Journal of Economics*.\n- Bikhchandani, S., Hirshleifer, D., & Welch, I. (1992). A theory of fads, fashion, custom, and cultural change as informational cascades. *Journal of Political Economy*.\n- [[wisdom-and-madness-of-crowds]] explorable.",
    },
    "overconfidence-bias": {
        "essence": "Systematic overestimation of one's accuracy, knowledge, or control — calibration fails upward.",
        "why": "Drives excessive trading, war initiation, project overruns, and expert punditry. Markets and democracies price overconfidence if they forget it exists.",
        "core": "**Overconfidence**spans overprecision (narrow confidence intervals), overestimation (skill above average), and overplacement (better than peers). Experts are not immune — domain knowledge can increase narrative confidence.",
        "mechanism": "1. Question demands probability or skill judgment.\n2. Self-generated answer feels coherent — coherence mistaken for accuracy.\n3. Confidence intervals too narrow; plans omit unknown unknowns.\n4. Feedback delayed or ambiguous — little calibration improvement.",
        "implications": "- Premortems and red teams institutionalise disconfirmation.\n- Prediction markets and track records beat seniority for forecast quality.\n- Combine with [[dunning-kruger-effect]] at low skill, [[hindsight-bias]] after outcomes.",
        "reading": "- Moore, D. A., & Healy, P. J. (2008). The trouble with overconfidence. *Psychological Review*.\n- Russo, J. E., & Schoemaker, P. J. H. (1992). *Decision Traps*. Doubleday.\n- Tetlock, P. E. (2005). *Expert Political Judgment*. Princeton University Press.",
    },
    "mate-selection-theory": {
        "essence": "Evolutionary and economic frameworks for partner choice, competition, and honest (or deceptive) signalling.",
        "why": "Dating markets, status display, and gender-role debates involve trade-offs — parental investment, fertility cues, resource provision — not pure romance or pure oppression narratives alone.",
        "core": "**Mate selection theory**integrates sexual selection (preferences, competition), life-history trade-offs, and strategic interaction. Traits evolve as signals when cost makes faking hard — or as arms races when deception pays.",
        "mechanism": "1. Sexes face asymmetric costs (gestation, risk, parental care) → different optimal strategies.\n2. Preferences filter traits correlated with fitness or resources (health, status, cooperation).\n3. Signalling arms race: honest costly signals vs mimics.\n4. Cultural norms and technology reshape but do not erase underlying incentives.",
        "implications": "- Market design (apps, assortative matching) changes inequality and sorting — not neutral pipes.\n- Cross-cultural variation in preferences does not falsify selection pressure — local equilibria differ.\n- Avoid just-so stories: hypotheses must be falsifiable with comparative data.",
        "reading": "- Buss, D. M. (2019). *Evolutionary Psychology* (6th ed.). Routledge — mate selection chapters.\n- Trivers, R. L. (1972). Parental investment and sexual selection. In *Sexual Selection and the Descent of Man*.\n- Zahavi, A. (1975). Mate selection — a selection for a handicap. *Journal of Theoretical Biology*.",
    },
    "kin-selection": {
        "essence": "Evolution favours helping relatives when benefit weighted by relatedness exceeds cost.",
        "why": "Explains nepotism, inheritance, organ donation patterns, and why cooperation scales differently in families vs strangers — Hamilton's rule unifies altruism puzzles.",
        "core": "**Kin selection** (Hamilton, 1964): genes promoting help to kin spread if *rB > C* (relatedness × benefit > cost). Apparent self-sacrifice can increase inclusive fitness.",
        "mechanism": "1. Actor shares fraction *r* genes with recipient (siblings ~0.5, cousins ~0.125).\n2. Helping raises recipient fitness by *B* at cost *C* to actor.\n3. Alleles for helping spread when *rB > C*.\n4. Humans extend kin categories via culture (fictive kin, clan) — blurring boundaries.",
        "implications": "- Institutions trying to override nepotism need aligned incentives, not sermons alone.\n- Explains partial cooperation in wartime units and family firms' strengths and failures.\n- Link [[evolution-of-trust]] for non-kin repeated games.",
        "reading": "- Hamilton, W. D. (1964). The genetical evolution of social behaviour I & II. *Journal of Theoretical Biology*.\n- Dawkins, R. (1976). *The Selfish Gene*. Oxford University Press — kin selection chapter.\n- West, S. A., Griffin, A. S., & Gardner, A. (2007). Social semantics. *Journal of Evolutionary Biology*.",
    },
    "status-signaling": {
        "essence": "Costly displays that communicate rank, fitness, or group membership — often wasteful by design.",
        "why": "Luxury goods, credentials, Twitter performance, and ritual sacrifice make sense as signals — understanding waste-as-function clarifies consumption and politics.",
        "core": "**Signalling theory** (Spence, Zahavi): when quality is hidden, agents send costly signals observers trust because faking is too expensive. Status is partly**legible investment**in reputation.",
        "mechanism": "1. Hidden trait (competence, loyalty, wealth) sought by observers (employers, mates, allies).\n2. Signal must be costlier for low-quality senders — handicap or investment.\n3. Observers reward signal with access, trust, or mates.\n4. Arms race escalates signal cost (bigger tail, pricier degree, louder virtue).",
        "implications": "- Banning visible signals often shifts channel, not motive ([[euphemism-cycles]]).\n- Progressive taxation on consumption may miss signalling motives driving waste.\n- [[cultural-capital]] and [[sociology-of-status]] for sociological layer.",
        "reading": "- Spence, M. (1973). Job market signaling. *Quarterly Journal of Economics*.\n- Zahavi, A. (1975). Mate selection — a selection for a handicap. *Journal of Theoretical Biology*.\n- Veblen, T. (1899). *The Theory of the Leisure Class*. Macmillan — conspicuous consumption.",
    },
    "elite-circulation": {
        "essence": "How ruling groups turn over — recruitment, co-optation, revolution, or decay.",
        "why": "Stagnant elites breed corruption and revolt; hyper-rotation destroys institutional memory. Reformers need models of who exits, who enters, and through what gates.",
        "core": "**Elite circulation** (Pareto, Mosca, elite theory tradition) tracks replacement of governing minorities. Open meritocracy, co-optation of challengers, and violent turnover are alternative modes with different stability profiles.",
        "mechanism": "1. Elite controls scarce resources: office, law, capital, violence.\n2. Challengers emerge from marginal elites or mass mobilisation.\n3. Regime responds: co-opt (absorb leaders), repress, or concede institutions.\n4. Circulation rate affects legitimacy — too little → sclerosis; too chaotic → failed state.",
        "implications": "- Token diversity without power redistribution is co-optation, not circulation.\n- Exams and credentials can democratise entry while reproducing new elite culture.\n- [[machiavellian-realism]] stresses fear and fortune in turnover dynamics.",
        "reading": "- Pareto, V. (1916). *Trattato di sociologia generale* — circulation of elites.\n- Mosca, G. (1896). *The Ruling Class*. McGraw-Hill.\n- Putnam, R. D. (1976). *The Comparative Study of Political Elites*. Prentice-Hall.",
    },
    "legitimacy-and-authority": {
        "essence": "Power persists when subjects believe rulers have the right to rule — not merely capacity to coerce.",
        "why": "Explains why weak armies sometimes win, why tax compliance varies, and why legitimacy crises flip regimes without proportional force.",
        "core": "Weber's**legitimate authority**types (traditional, charismatic, legal-rational) describe belief systems stabilising domination. Coercion alone is expensive; **voluntary compliance**scales.",
        "mechanism": "1. Ruler claims right via tradition, election, divine mandate, or performance.\n2. Subjects evaluate claim against experience and alternatives.\n3. High legitimacy → cooperation, information sharing, low enforcement cost.\n4. Legitimacy shock (scandal, defeat, famine) → compliance collapses faster than force.",
        "implications": "- Winning battles but losing legitimacy loses wars ([[history-of-power]]).\n- Transitions need narrative bridges — new rulers inherit or rewrite legitimacy scripts.\n- [[soft-power]] complements but does not replace perceived right to rule at home.",
        "reading": "- Weber, M. (1922). *Economy and Society* — domination and legitimacy.\n- Tyler, T. R. (2006). *Why People Obey the Law*. Princeton University Press.\n- Beetham, D. (1991). *The Legitimation of Power*. Macmillan.",
    },
    "soft-power": {
        "essence": "Influence through attraction, culture, and norms — not tanks or tariffs alone.",
        "why": "Explains US cultural reach, vaccine diplomacy, university prestige, and why coercive superpowers still invest in Hollywood and aid narratives.",
        "core": "Joseph Nye's**soft power**: others want what you want because your culture, policies, and values look legitimate or appealing. It shapes preferences before explicit bargaining.",
        "mechanism": "1. Actor projects culture, values, and success models globally (media, education, diaspora).\n2. Foreign publics and elites internalise preferences aligned with actor.\n3. Alignment reduces need for carrots and sticks in diplomacy and markets.\n4. Soft power erodes when hypocrisy gap widens (preach democracy, practice otherwise).",
        "implications": "- Sanctions and bombs can destroy soft power faster than hard assets.\n- Universities, open science, and immigration policy are geopolitical instruments.\n- [[legitimacy-and-authority]] at domestic level mirrors international attraction.",
        "reading": "- Nye, J. S. (2004). *Soft Power: The Means to Success in World Politics*. PublicAffairs.\n- Nye, J. S. (2011). *The Future of Power*. PublicAffairs.\n- [[geopolitics]] hub.",
    },
    "machiavellian-realism": {
        "essence": "Political analysis stressing power, fear, fortune, and self-interest over ideals.",
        "why": "Counters naive moralism in foreign policy and boardrooms — not to endorse cruelty but to map how actors behave when stakes are existential.",
        "core": "**Machiavellian realism** (Machiavelli, later Morgenthau) treats politics as conflict over scarce power where moral language often serves strategy. **Virtù** (skill, boldness) and**fortuna** (chance) shape outcomes alongside ethics.",
        "mechanism": "1. Leaders face rivals with incompatible interests and incomplete trust.\n2. Public virtue may conflict with state survival — incentives to dissemble.\n3. Force and fear secure compliance when love is insufficient — but excess breeds hatred.\n4. Institutions and balance-of-power constrain pure will — realism is not omnipotence.",
        "implications": "- Idealistic policies fail when they ignore opponent payoffs ([[prisoners-dilemma]]).\n- Transparency norms in domestic politics may be weaponised internationally.\n- Ethical realists still ask *which* powers ought to exist — description ≠ prescription.",
        "reading": "- Machiavelli, N. (1532). *The Prince*. Various translations.\n- Morgenthau, H. J. (1948). *Politics Among Nations*. Knopf.\n- Waltz, K. N. (1979). *Theory of International Politics*. Addison-Wesley — structural realism.",
        "misconceptions": [
            ("Realism means evil is smart", "It maps incentives; moral critique remains possible"),
            ("Realists ignore ideas", "Legitimacy and norms are power resources too"),
        ],
    },
    "principal-agent-problem": {
        "essence": "Misaligned incentives when one party (agent) acts on another's (principal's) behalf with hidden action or information.",
        "why": "CEOs and shareholders, doctors and insurers, politicians and voters — delegation is everywhere; naive trust leaks value.",
        "core": "The**principal–agent problem**arises from**information asymmetry**and**divergent incentives**. Principals want outcomes; agents optimise what is measured, paid, or career-safe.",
        "mechanism": "1. Principal delegates task requiring agent effort or expertise principal lacks.\n2. Agent's actions partly unobservable (moral hazard) or agent knows more (adverse selection).\n3. Agent maximises own utility — shirking, risk-shifting, empire-building.\n4. Principal designs contracts, monitoring, or reputation — each costly and gameable ([[goodharts-law]]).",
        "implications": "- Stock options align on paper but encourage short-term risk and accounting games.\n- Oversight bureaucracy grows until its own agency problems dominate.\n- [[cobra-farm]] is canonical unintended response to agent incentives.",
        "reading": "- Jensen, M. C., & Meckling, W. H. (1976). Theory of the firm. *Journal of Financial Economics*.\n- Holmström, B. (1979). Moral hazard and observability. *Bell Journal of Economics*.\n- [[economics-incentives]] hub.",
    },
    "moral-hazard": {
        "essence": "Hidden actions after a contract — one party takes risks because another bears the cost.",
        "why": "Insurance, bailouts, and guaranteed sales breed carelessness; financial crises repeat when downside is socialised.",
        "core": "**Moral hazard** (insurance literature): once protected against loss, behaviour changes toward risk — not always consciously. Post-contract information asymmetry on *effort* is the core.",
        "mechanism": "1. Principal offers coverage or guarantee (insurance, too-big-to-fail, health plan).\n2. Agent's marginal cost of risk falls — precautions less valuable privately.\n3. Risk-taking or shirking rises; principal cannot observe daily choices.\n4. Losses materialise; principal raises premiums or exits — or bailouts repeat cycle.",
        "implications": "- Deductibles and co-pays are not meanness — they re-align marginal incentives.\n- Bailouts need credible future penalty or risk migration continues.\n- Pair [[principal-agent-problem]] with [[unintended-consequences]] in policy design.",
        "reading": "- Arrow, K. J. (1963). Uncertainty and the welfare economics of medical care. *American Economic Review*.\n- Stiglitz, J. E. (2010). *Freefall*. Norton — moral hazard in finance.\n- Holmström, B. (1979). Moral hazard and observability. *Bell Journal of Economics*.",
    },
    "unintended-consequences": {
        "essence": "Interventions produce effects nobody planned — often through incentives and feedback.",
        "why": "Cobra bounties, prohibition, grade inflation, and algorithmic filters teach humility: systems route around rules.",
        "core": "Merton's**unintended consequences**arise from ignorance, error, imperious immediacy (focus on one goal), and**basic values** (pursuing good ends via means that trigger backlash). Not all are negative — but surprise is the signal.",
        "mechanism": "1. Policy targets visible metric or behaviour (kill cobras, reduce crime, raise test scores).\n2. Agents reoptimise — breed cobras, displace crime, teach to test.\n3. Second-order effects ripple ([[second-order-effects]]).\n4. Original problem worsens or mutates; blame assigned to bad faith not bad design.",
        "implications": "- Pilot with measurement of proxy gaming before scale.\n- Combine command with incentive alignment — not either/or.\n- [[cobra-farm]] · [[goodharts-law]] are museum-grade examples.",
        "reading": "- Merton, R. K. (1936). The unanticipated consequences of purposive social action. *American Sociological Review*.\n- Siegel, L. B. (2020). *The Cobra Effect*. Simon & Schuster.\n- [[unintended-system-behavior]] for emergent system layer.",
    },
    "correlation-vs-causation": {
        "essence": "Association does not prove one variable produced another — confounds and reverse causality abound.",
        "why": "Ice cream and drowning correlate; banning dessert won't fix pools. Bad causal claims drive medicine, education policy, and tech attribution.",
        "core": "**Correlation**measures statistical association; **causation**requires mechanism, intervention, or design that rules alternatives. *C* does not imply *A* caused *B* without addressing confounders *Z* and direction.",
        "mechanism": "1. Observe *X* and *Y* move together in data.\n2. Plausible story links *X* → *Y* (narrative causation).\n3. Hidden *Z* causes both, or *Y* → *X*, or coincidence in small sample.\n4. Policy targets *X*; *Y* unchanged — surprise unless RCT, diff-in-diff, or instrument.",
        "implications": "- Randomised trials gold standard where ethical; observational needs explicit causal diagrams.\n- \"Data-driven\" products often optimise correlations that break on deployment.\n- [[simpsons-paradox]] shows aggregation can invert apparent direction.",
        "reading": "- Pearl, J. (2009). *Causality* (2nd ed.). Cambridge University Press.\n- Cunningham, S. (2021). *Causal Inference: The Mixtape*. Yale University Press.\n- Bradford Hill (1965). Environment and disease — guidelines, not proof.",
        "misconceptions": [
            ("Large correlation = strong causation", "Confounded relationships can be tight and wrong"),
            ("No RCT means no knowledge", "Natural experiments and designs can identify causation"),
        ],
    },
    "survivorship-bias": {
        "essence": "Drawing lessons from winners while ignoring silent failures that never appear in the dataset.",
        "why": "WWII plane armour, startup advice from unicorns, and \"what successful people do\" omit the graveyard of identical strategies that failed.",
        "core": "**Survivorship bias**selects on the dependent variable: only entities that passed a filter (profit, fame, return) remain visible. Failed copies of the same strategy vanish from samples.",
        "mechanism": "1. Population attempts strategy *S*; most fail, few survive.\n2. Analysts study survivors' traits — courage, grit, morning routines.\n3. Failures shared traits but lacked luck or hidden factor *H*.\n4. Conclusion \"*S* causes success\" — biased sample.",
        "implications": "- Backtest financial strategies on delisted stocks, not current index.\n- Mentor myths ignore selection into visibility.\n- [[goodharts-law]] when optimising traits of survivors only.",
        "reading": "- Abraham Wald (1943). Memo on survivorship bias in WWII aircraft — reproduced in many stats texts.\n- Taleb, N. N. (2001). *Fooled by Randomness*. Random House.\n- Brown, S. J., Goetzmann, W. N., Ibbotson, R. G., & Ross, S. A. (1992). Survivorship bias in performance studies. *Review of Financial Studies*.",
    },
    "base-rate-neglect": {
        "essence": "Ignoring how common an outcome is when interpreting new evidence — vivid detail swamps priors.",
        "why": "Medical tests, terrorism risk, and hiring from impressive interviews all fail when base rates forgotten — Bayes' theorem is the fix, not intuition.",
        "core": "**Base rate neglect** (Kahneman & Tversky): people overweight case-specific evidence and underweight population frequency. A positive rare-disease test still often means no disease if base rate is tiny.",
        "mechanism": "1. Prior base rate *P(H)* known but psychologically dull.\n2. New evidence *E* (symptom, resume sparkle) salient.\n3. Judgment tracks *P(E|H)* intuition, not *P(H|E)* via Bayes.\n4. False positives dominate when *H* is rare.",
        "implications": "- Screening programs need communicated base rates — not just test accuracy.\n- Interviewers overweight candidate stories vs role base rate of success.\n- Simulations: [[base-rate-hospital]] · [[prosecutors-dna]].",
        "reading": "- Kahneman, D., & Tversky, A. (1973). On the psychology of prediction. *Psychological Review*.\n- Casscells, W., Schoenberger, A., & Graboys, T. (1978). Interpretation by physicians of clinical laboratory results. *New England Journal of Medicine*.\n- Gigerenzer, G. (2002). *Reckoning with Risk*. Penguin — natural frequencies.",
    },
    "cultural-capital": {
        "essence": "Knowledge, taste, credentials, and manner that confer advantage in social markets.",
        "why": "Explains why \"merit\" debates mix skills with coded class signals — who feels at home in museums, interviews, and elite schools.",
        "core": "Pierre Bourdieu's**cultural capital** — embodied (accent, posture), objectified (books, art), institutionalised (degrees) — converts to economic and social capital through**fields**with tacit rules.",
        "mechanism": "1. Families and institutions transmit cultural codes early (language register, hobbies).\n2. Gatekeepers (employers, admissions) reward familiarity with dominant codes.\n3. Misrecognition: advantage appears as natural talent or merit.\n4. Reproduction: elites invest in capital types fields reward.",
        "implications": "- Diversity hires fail if only credentials diversify, not embodied codes.\n- Universal basic income debates miss capital conversion frictions.\n- [[social-stratification]] · [[status-anxiety]] for emotional layer.",
        "reading": "- Bourdieu, P. (1986). The forms of capital. In *Handbook of Theory and Research for the Sociology of Education*.\n- Bourdieu, P., & Passeron, J.-C. (1970). *Reproduction in Education, Society and Culture*. Sage.\n- Lareau, A. (2003). *Unequal Childhoods*. University of California Press.",
    },
    "status-anxiety": {
        "essence": "Distress from perceived rank relative to peers or ideals — consumption and politics follow.",
        "why": "Relative deprivation drives debt, envy, reactionary politics, and burnout in \"successful\" careers — absolute wealth insufficient explanation.",
        "core": "De Botton and sociological status literature: **status anxiety**rises when comparisons upward are salient and mobility feels blocked. Self-worth couples to positional goods (school district, title, followers).",
        "mechanism": "1. Media and peers supply comparison targets above one's tier.\n2. Gap threatens identity and belonging needs.\n3. Compensatory behaviour: conspicuous spend, credential chasing, scapegoating lower tiers.\n4. Temporary relief; treadmill resets with new comparisons.",
        "implications": "- Growth without perceived fairness increases status conflict ([[loss-aversion]] on rank).\n- Social media amplifies upward comparison frequency.\n- Policies addressing only material poverty miss positional harms.",
        "reading": "- de Botton, A. (2004). *Status Anxiety*. Pantheon.\n- Frank, R. H. (1985). Choosing the right pond. *Human Nature*.\n- Marmot, M. (2004). *The Status Syndrome*. Bloomsbury.",
    },
    "social-stratification": {
        "essence": "Durable hierarchies of class, caste, prestige, and access — reproduced across generations.",
        "why": "Democracy and markets coexist with steep stratification; ignoring structure misreads poverty, health gaps, and political coalitions.",
        "core": "**Social stratification**ranks groups by access to resources, power, and honour. Mechanisms include property, credentials, race, gender, and network closure — often interacting ([[schelling-segregation]] spatial layer).",
        "mechanism": "1. Institutions allocate unequal life chances (school funding, inheritance law).\n2. Groups develop identity and norms matching tier.\n3. Intergenerational transmission — wealth, trauma, capital types.\n4. Legitimating ideologies mask contingency as desert or nature.",
        "implications": "- Mobility statistics must distinguish absolute vs relative movement.\n- Integration policies failing to address stratification reproduce tiers in new forms.\n- [[cultural-capital]] · [[elite-circulation]] specify elite dynamics.",
        "reading": "- Weber, M. (1922). *Economy and Society* — class, status, party.\n- Piketty, T. (2014). *Capital in the Twenty-First Century*. Harvard University Press.\n- Chetty, R., et al. (2014). Where is the land of opportunity? *Science*.",
    },
    "bounded-rationality": {
        "essence": "Deciders use limited information and simplified rules — not full optimisation.",
        "why": "Real organisations, voters, and consumers \" satisfice\"; models assuming infinite calculus mispredict behaviour and institutional design needs.",
        "core": "Simon’s**bounded rationality**: cognitive limits, uncertain environments, and time pressure force**heuristics**and**satisficing**instead of global optimisation. Rationality is procedural and contextual.",
        "mechanism": "1. Decision problem exceeds computational or informational capacity.\n2. Agent searches partially, uses rules of thumb.\n3. Chooses**good enough**option meeting aspiration level.\n4. Environment structure determines when heuristics succeed or fail ([[heuristics-decision-making]]).",
        "implications": "- Nudge design must respect actual search paths, not ideal calculators.\n- AI assistants can expand bounds — also new failure modes (over-trust).\n- [[decision-making-uncertainty]] hub connects probability layer.",
        "reading": "- Simon, H. A. (1957). *Models of Man*. Wiley.\n- Simon, H. A. (1990). Invariants of human behavior. *Annual Review of Psychology*.\n- Kahneman, D. (2003). Maps of bounded rationality. *American Economic Review*.",
    },
    "heuristics-decision-making": {
        "essence": "Fast rules that work well in some environments and fail badly in others.",
        "why": "Gigerenzer's \"less is more\" and Kahneman's biases share structure — ecology of rules matters more than bias labels alone.",
        "core": "**Heuristics** (take-the-best, recognition, 1/N) ignore information by design — lowering variance in stable environments, exploding error when cues mislead. Performance is**ecologically rational**.",
        "mechanism": "1. Cue environment offers valid or invalid shortcuts.\n2. Heuristic selects few cues, ignores rest.\n3. Low effort, fast decision — high accuracy if ecology matches.\n4. Ecology shift (new market, novel disease) → systematic bias until learning.",
        "implications": "- Training should teach *when* rules apply, not only list biases.\n- Complex models can overfit where simple heuristics win ([[predict-then-reveal]] tests).\n- [[availability-heuristic]] is one cue-based rule among many.",
        "reading": "- Gigerenzer, G., Todd, P. M., & ABC Research Group (1999). *Simple Heuristics That Make Us Smart*. Oxford University Press.\n- Kahneman, D., & Klein, G. (2009). Conditions for intuitive expertise. *American Psychologist*.\n- Tversky, A., & Kahneman, D. (1974). Judgment under uncertainty: Heuristics and biases. *Science*.",
    },
    "satisficing": {
        "essence": "Choosing the first acceptable option rather than searching for the global optimum.",
        "why": "Explains why consumers pick familiar brands, why deadlines produce \"good enough\" code, and why maximising metrics is not how humans actually decide.",
        "core": "Simon's**satisficing**: set**aspiration level**, search until alternative meets it, stop. Optimisation assumes known option set and unlimited search — rarely true.",
        "mechanism": "1. Agent sets threshold *A* (price, quality, ethics minimum).\n2. Sequential or partial search of alternatives.\n3. First option ≥ *A* chosen; search stops.\n4. Aspiration adapts with experience — rises after success, falls under pressure.",
        "implications": "- More choices can paralyse optimisers but help satisficers if any option clears bar.\n- Organisational slack allows higher aspirations; crisis lowers bars.\n- Design defaults that clear common aspiration levels ([[bounded-rationality]]).",
        "reading": "- Simon, H. A. (1956). Rational choice and the structure of the environment. *Psychological Review*.\n- Schwartz, B. (2004). *The Paradox of Choice*. Ecco — when maximising hurts.\n- [[decision-making-uncertainty]] hub.",
    },
    "falsifiability": {
        "essence": "A claim is scientific if it could in principle be proven wrong by observation.",
        "why": "Separates testable theories from unfalsifiable ideology — Popper's criterion underpins modern science and healthy skepticism.",
        "core": "Popper's**falsifiability**: theories earn scientific status by risking refutation. Confirming instances don't prove universal claims; one counterexample can break (if claim is sharp enough).",
        "mechanism": "1. Theory *T* implies observable prediction *P*.\n2. Design test where *P* could fail if *T* false.\n3. Outcome consistent → *T* corroborated, not verified forever.\n4. Outcome inconsistent → *T* revised or abandoned (ideally).",
        "implications": "- Vague prophecies and post-hoc fits evade falsification — pseudoscience signal.\n- Protecting core belief with auxiliary hypotheses can delay but shouldn't block tests forever.\n- [[replication-crisis]] tests whether fields actually risk refutation.",
        "reading": "- Popper, K. R. (1959). *The Logic of Scientific Discovery*. Hutchinson.\n- Popper, K. R. (1963). Conjectures and Refutations. Routledge.\n- Lakatos, I. (1970). Falsification and the methodology of scientific research programmes. *Criticism and the Growth of Knowledge*.",
    },
    "replication-crisis": {
        "essence": "Many published findings fail to reproduce — methods and incentives under scrutiny.",
        "why": "Psychology, medicine, and economics built policies on fragile results. Open science reforms follow from discovered emptiness in the file drawer.",
        "core": "The**replication crisis**: large-scale replications find smaller or null effects vs originals. Drivers include *p*-hacking, HARKing, publication bias, underpowered studies, and weak theorisation ([[p-hacking-lab]]).",
        "mechanism": "1. Incentives reward novel significant results, not null replications.\n2. Researchers flexibly analyse until *p* < .05.\n3. Journals publish positives; failures hidden.\n4. Meta-analyses and replication projects reveal inflated evidence.",
        "implications": "- Pre-registration, open data, and registered reports change incentive geometry.\n- \"One study\" policy is reckless — demand replication and effect sizes.\n- [[peer-review-process]] alone insufficient without structural reform.",
        "reading": "- Open Science Collaboration (2015). Estimating the reproducibility of psychological science. *Science*.\n- Ioannidis, J. P. A. (2005). Why most published research findings are false. *PLoS Medicine*.\n- Nosek, B. A., et al. (2015). Promoting an open research culture. *Science*.",
    },
    "peer-review-process": {
        "essence": "Expert evaluation before publication — gatekeeper with known biases and limits.",
        "why": "Science trusts peer review as quality seal, but delays, conservatism, and inability to detect fraud mean it is necessary not sufficient.",
        "core": "**Peer review**filters submissions for rigour, novelty, and fit. Anonymous reviewers advise editors; authors revise. Functions as**reputation laundering**and error catch — imperfectly.",
        "mechanism": "1. Author submits manuscript.\n2. Editor recruits reviewers with domain expertise (often unpaid).\n3. Reviewers critique methods, claims, ethics; recommend accept/revise/reject.\n4. Revised paper published — perceived as vetted though many errors survive.",
        "implications": "- Revolutionary work often struggles against reviewer conservatism.\n- Open peer review and post-publication review complement pre-publication gate.\n- [[falsifiability]] and [[replication-crisis]] expose gap between review and truth.",
        "reading": "- Smith, R. (2006). Peer review: a flawed process at the heart of science. *Journal of the Royal Society of Medicine*.\n- Tennant, J. P., & Ross-Hellauer, T. (2020). The limitations to our understanding of peer review. *MetaArXiv* preprint.\n- [[scientific-method-skepticism]] hub.",
    },
    "nash-equilibrium": {
        "essence": "No player gains by unilaterally changing strategy given others' choices.",
        "why": "Predicts stable outcomes in oligopoly, traffic routing, arms races, and penalty kicks — not always welfare-maximising.",
        "core": "A**Nash equilibrium**is a strategy profile where each player's choice is a best response to others'. Mutual defection in one-shot Prisoner's Dilemma is Nash; cooperation may require repetition or institutions.",
        "mechanism": "1. Each player chooses strategy maximising payoff given beliefs about others.\n2. Profile *s* is Nash if no player can improve by deviating alone.\n3. Multiple equilibria possible — coordination problem which one realises.\n4. Focal points, norms, or policy select among equilibria.",
        "implications": "- Bad equilibria stable without coordination ([[prisoners-dilemma]]).\n- Mechanism design shifts payoffs to make good equilibria Nash.\n- [[negotiation-game-theory]] applies to bargaining subsets.",
        "reading": "- Nash, J. F. (1950). Equilibrium points in n-person games. *Proceedings of the National Academy of Sciences*.\n- Nash, J. F. (1951). Non-cooperative games. *Annals of Mathematics*.\n- Dixit, A., Skeath, S., & Reiley, D. (2015). *Games of Strategy* (4th ed.). Norton.",
    },
    "zero-sum-games": {
        "essence": "Whether one side's gain equals another's loss — framing cooperation and conflict.",
        "why": "Trade, climate, and culture wars get misframed as zero-sum when gains from exchange exist — rhetoric shapes which equilibria feel natural.",
        "core": "**Zero-sum**payoffs: total benefit constant — your win is my loss. **Non-zero-sum**: mutual gain or loss possible ([[commons-garden]], [[evolution-of-trust]]). Framing alters perceived Nash set.",
        "mechanism": "1. Actors model interaction as zero or non-zero-sum.\n2. Zero-sum frame → competitive strategies, hide information.\n3. Non-zero-sum frame → trade, treaties, reputation investment.\n4. Misclassified games produce self-fulfilling conflict.",
        "implications": "- Populist rhetoric zero-sums immigration and trade — empirics often mixed gains/losses.\n- Classroom games teach difference: [[prisoners-dilemma]] vs dividing fixed pie.\n- [[negotiation-game-theory]] integrative vs distributive bargaining.",
        "reading": "- von Neumann, J., & Morgenstern, O. (1944). *Theory of Games and Economic Behavior*. Princeton University Press.\n- Axelrod, R. (1984). *The Evolution of Cooperation*. Basic Books.\n- Pinker, S. (2011). *The Better Angels of Our Nature* — zero-sum history critique.",
    },
    "collective-memory": {
        "essence": "Groups share reconstructed pasts — monuments, rituals, media — not identical individual recall.",
        "why": "Nations fight over textbooks and statues because shared past anchors identity and legitimacy — memory is political infrastructure.",
        "core": "Halbwachs' **collective memory**lives in institutions and rituals, not just brains. Commemoration selects events, heroes, and silences — updating as present needs shift.",
        "mechanism": "1. Group faces identity or legitimacy task (war, independence, trauma).\n2. Elites curate narratives via education, media, memorials.\n3. Members internalise selective past; deviants marginalised.\n4. Generational turnover rewrites emphasis — not necessarily falsification, but reconstruction.",
        "implications": "- Truth commissions compete with myth for narrative space ([[myth-creation]]).\n- Digital archives change but do not eliminate selective curation.\n- [[information-cascades]] in historical belief among publics.",
        "reading": "- Halbwachs, M. (1925). *Les cadres sociaux de la mémoire*. Presses Universitaires de France.\n- Nora, P. (1989). Between memory and history. *Representations*.\n- Assmann, J. (1995). *Collective Memory and Cultural Identity*. New German Critique.",
    },
    "myth-creation": {
        "essence": "Stories that simplify history to bind identity or justify power — fact and symbol merge.",
        "why": "Founding myths (revolutions, \"ancient\" traditions invented yesterday) mobilise sacrifice and obedience — analysts need symbol literacy.",
        "core": "**Myth creation**compresses messy history into moral archetypes: pure origins, betrayals, chosen victims. Hobsbawm's**invented traditions**show deliberate myth craft, not only folk drift.",
        "mechanism": "1. Political need for unity or regime legitimacy.\n2. Narrators select episodes, elide contradictions, cast roles (hero/villain).\n3. Ritual repetition (holidays, slogans) embeds myth as common sense.\n4. Counter-evidence labelled treason or irrelevance.",
        "implications": "- Debunking alone rarely dissolves identity-linked myths — need alternative stories.\n- Media literacy includes detecting myth functions, not just fake facts.\n- [[historical-storytelling]] · [[collective-memory]] interlock.",
        "reading": "- Hobsbawm, E., & Ranger, T. (1983). *The Invention of Tradition*. Cambridge University Press.\n- Barthes, R. (1957). *Mythologies*. Seuil.\n- Schudson, M. (1992). *Watergate in American Memory*. Basic Books.",
    },
    "historical-storytelling": {
        "essence": "Narrative choices — heroes, villains, turning points — shape what groups remember and demand.",
        "why": "Same events become tragedy or triumph by framing — historians and filmmakers are power brokers, not neutral clerks.",
        "core": "**Historical storytelling**selects agents, causality, and moral. White's**metahistory**argues narrative form (romance, tragedy) prefigures explanation — data never speak alone.",
        "mechanism": "1. Raw events and archives incompletely ordered.\n2. Storyteller imposes plot: beginning, crisis, resolution.\n3. Audience emotions and identity hook to characters.\n4. Memory institutions crystallise one plot as \"what happened.\"",
        "implications": "- Curriculum battles are plot wars, not only fact wars.\n- Interactive museum design can let users compare competing plots ([[ladder-of-abstraction]]).\n- [[language-and-framing]] tools apply to temporal narrative.",
        "reading": "- White, H. (1973). *Metahistory*. Johns Hopkins University Press.\n- Rosenstone, R. A. (1995). *Visions of the Past*. Harvard University Press.\n- Tversky, B., & Marsh, E. J. (2000). Biased retelling of events yield biased memories. *Cognitive Psychology*.",
    },
    "linguistic-relativity": {
        "essence": "Language structure may influence habitual thought — Sapir–Whorf debate, strong vs weak forms.",
        "why": "Colour words, gendered grammar, and spatial metaphors correlate with cognition in experiments — policy on bilingualism and AI language inherits the debate.",
        "core": "**Linguistic relativity** (Sapir–Whorf hypothesis): language categories habituate attention and memory. Strong form (language determines thought) largely rejected; **weak**form (language influences habit) supported in domains like colour, time, number.",
        "mechanism": "1. Language encodes some distinctions mandatory (evidentiality, kin terms).\n2. Speakers practise those distinctions in speech — reinforcing perceptual habits.\n3. Difficult concepts in L1 harder in L2 without equivalent — partial friction.\n4. Bilinguals shift cognitive style with language context in some tasks.",
        "implications": "- Translation is not neutral — carries worldview residue.\n- NLP models embed dominant language categories into \"default\" reasoning.\n- [[emotionally-charged-language]] adds affect layer to framing.",
        "reading": "- Whorf, B. L. (1956). *Language, Thought, and Reality*. MIT Press.\n- Boroditsky, L. (2011). How language shapes thought. *Scientific American*.\n- Levinson, S. C. (2003). *Space in Language and Cognition*. Cambridge University Press.",
        "misconceptions": [
            ("No word for X means can't think X", "Weak relativity is influence, not prison"),
            ("All Whorf is discredited", "Modern experiments revive moderated relativity"),
        ],
    },
    "euphemism-cycles": {
        "essence": "Polite terms for harsh realities eventually absorb the stigma they replace — treadmill of renaming.",
        "why": "HR language, disability terms, and military jargon rotate as new words inherit old contempt — understanding cycle prevents naive \"rebrand fixes bias.\"",
        "core": "**Euphemism cycles**: dysphemism → euphemism → pejoration → new euphemism. Attitudes travel with referent, not only label ([[language-and-framing]]).",
        "mechanism": "1. Direct term stigmatised (death, disability, layoffs).\n2. Softer substitute adopted for politeness or policy.\n3. Listeners infer same referent; negative associations transfer.\n4. New term taboo; cycle repeats (toilet → bathroom → restroom).",
        "implications": "- Inclusion training focusing only on vocabulary without status change fails.\n- Political euphemism (\"enhanced interrogation\") obscures accountability.\n- [[goodharts-law]] when metric is polite language use.",
        "reading": "- Pinker, S. (1994). *The Language Instinct* — euphemism treadmill chapter.\n- Allan, K., & Burridge, K. (2006). *Forbidden Words*. Cambridge University Press.\n- Lutz, W. D. (1989). *Doublespeak*. HarperCollins.",
    },
    "emotionally-charged-language": {
        "essence": "Word choice triggers affect before argument — framing by connotation, not propositional content alone.",
        "why": "Same policy as \"death tax\" vs \"estate tax\" splits polls; outrage economics runs on diction.",
        "core": "**Emotionally charged language**activates appraisal systems parallel to deliberation. Metaphor (war on drugs), moralised nouns (illegals), and vivid verbs shift attitude independent of facts.",
        "mechanism": "1. Message embeds high-arousal terms linked to threat or sacred values.\n2. Fast affective response colours subsequent reasoning.\n3. Counter-arguments processed as attacks on identity.\n4. Polarisation deepens; policy details barely heard.",
        "implications": "- Debate norms naming loaded terms can slow affect hijack.\n- Media incentives favour charge over nuance ([[propaganda-model]]).\n- [[framing-effects-media]] for equivalent facts, different words.",
        "reading": "- Lakoff, G. (2004). *Don't Think of an Elephant!*. Chelsea Green.\n- Reddy, W. M. (2001). *The Navigation of Feeling*. Cambridge University Press.\n- Slovic, P., et al. (2007). The affect heuristic. *European Journal of Operational Research*.",
    },
    "moral-foundations-theory": {
        "essence": "Multiple moral intuitions — care, fairness, loyalty, authority, sanctity — combine differently across cultures.",
        "why": "Culture war maps poorly onto single axis liberal/conservative — Haidt's foundations explain why some harms feel visceral to one group and invisible to another.",
        "core": "Haidt & Joseph's**Moral Foundations Theory** (MFT): modular moral intuitions evolved for cooperation problems. Liberals weight Care/Fairness; conservatives often balance Loyalty, Authority, Sanctity too — not mere ignorance.",
        "mechanism": "1. Social challenge activates foundation (cheating, betrayal, impurity).\n2. Intuition fires fast — reason constructs post-hoc justification.\n3. Cross-group dialogue talks past when different foundations salient.\n4. Appeals matching opponent foundations more persuasive than raw facts.",
        "implications": "- Persuasion across divide requires speaking multiple moral languages.\n- MFT descriptive not prescriptive — no foundation automatically right.\n- [[in-group-bias]] · [[value-diversity]] connect to pluralism.",
        "reading": "- Haidt, J. (2012). *The Righteous Mind*. Pantheon.\n- Graham, J., et al. (2013). Moral foundations theory: The pragmatic validity of moral pluralism. *Advances in Experimental Social Psychology*.\n- [[moral-psychology]] hub.",
    },
    "in-group-bias": {
        "essence": "Favouring members of one's own group — cooperation inside, suspicion or hostility outside.",
        "why": "Explains nepotism, nationalism, sports riots, and asymmetric empathy in disasters — minimal group experiments show bias from arbitrary labels.",
        "core": "**In-group bias** (Tajfel minimal groups): even random categories trigger preferential allocation and stereotyping. Reinforced by competition, threat, and sacred identity.",
        "mechanism": "1. Social categorisation labels self and others (team, nation, party).\n2. Motivation for positive distinctiveness favours in-group.\n3. Information processed with in-group benefit of doubt.\n4. Out-group homogeneity — \"they're all alike\" — sharpens contrast.",
        "implications": "- Institutions mixing groups under shared superordinate goals reduce bias ([[asch-conformity]] context).\n- Diversity without contact can increase perceived threat.\n- [[schelling-segregation]] spatial expression of group preference.",
        "reading": "- Tajfel, H., Billig, M. G., Bundy, R. P., & Flament, C. (1971). Social categorization and intergroup behaviour. *European Journal of Social Psychology*.\n- Brewer, M. B. (1999). The psychology of prejudice: Ingroup love and outgroup hate? *Journal of Social Issues*.\n- [[moral-psychology]] · [[psychological-projection]].",
    },
    "value-diversity": {
        "essence": "Plausible moral outlooks disagree — pluralism of ends, not only factual dispute.",
        "why": "Democratic conflict often irreconcilable values, not fixable ignorance — institutions must manage disagreement without expecting convergence.",
        "core": "**Value diversity** (Berlin's pluralism): multiple incompatible yet reasonable ways of life. Unlike relativism-as-anything-goes, acknowledges tragic choices when values collide.",
        "mechanism": "1. Citizens hold ranked values from different traditions (liberty, equality, sanctity).\n2. Policy forces trade-offs — no pareto improvement.\n3. Deliberation clarifies conflict but may not eliminate it.\n4. Procedures (vote, rights, courts) settle without moral unanimity.",
        "implications": "- Expecting \"right answer\" politics breeds authoritarian frustration.\n- Federalism and subsidiarity localise value conflict.\n- [[moral-relativism]] distinct — diversity ≠ all views equally valid.",
        "reading": "- Berlin, I. (1969). *Four Essays on Liberty* — value pluralism.\n- Galston, W. A. (2002). *Liberal Pluralism*. Cambridge University Press.\n- [[philosophy-of-ethics]] hub.",
    },
    "utilitarianism": {
        "essence": "Right action maximises overall welfare — greatest good for greatest number.",
        "why": "Public health, cost-benefit analysis, and effective altruism inherit utilitarian logic — also its paradoxes (trolley, organ lottery).",
        "core": "**Utilitarianism** (Bentham, Mill): judge acts and rules by consequences for total (or average) well-being. Impartial — \"each to count for one.\"",
        "mechanism": "1. Identify affected parties and outcome states.\n2. Estimate utility (happiness, preference satisfaction, QALYs).\n3. Sum or aggregate — allow trade-offs across persons.\n4. Choose action maximising total — rights as rules if they maximise long-run.",
        "implications": "- Forces explicit trade-offs — uncomfortable but transparent.\n- Aggregation can justify harming minority if gain large enough — critic target.\n- [[deontology]] · [[virtue-ethics]] offer rival frameworks.",
        "reading": "- Mill, J. S. (1863). *Utilitarianism*. Parker, Son, and Bourn.\n- Bentham, J. (1789). *An Introduction to the Principles of Morals and Legislation*.\n- Singer, P. (1979). *Practical Ethics*. Cambridge University Press.",
    },
    "deontology": {
        "essence": "Some duties are binding regardless of outcomes — rules, rights, and respect for persons.",
        "why": "Explains why lying to save lives still feels wrong to many; human rights discourse is largely deontological.",
        "core": "**Deontology** (Kant): morality of**maxims**and**duties** — treat humanity as end, not merely means. Certain acts wrong even if consequences good.",
        "mechanism": "1. Agent considers proposed action under universalisable rule.\n2. If rule treats persons as mere tools → forbidden.\n3. Rights and promises create side constraints on utility.\n4. Conflicts between duties resolved by hierarchy or casuistry — not cost-benefit alone.",
        "implications": "- Legal systems encode deontic prohibitions (torture bans) despite edge cases.\n- AI ethics debates pair utilitarian optimisation with rights constraints.\n- [[utilitarianism]] trolley problems expose fracture lines.",
        "reading": "- Kant, I. (1785). *Groundwork of the Metaphysics of Morals*. Various translations.\n- Ross, W. D. (1930). *The Right and the Good*. Clarendon Press — prima facie duties.\n- [[philosophy-of-ethics]] hub.",
    },
    "virtue-ethics": {
        "essence": "Character and flourishing matter more than isolated acts or rule-following alone.",
        "why": "Professional ethics, parenting, and leadership ask \"what kind of person should I be?\" — not only \"what rule applies?\"",
        "core": "**Virtue ethics** (Aristotle): cultivate**virtues** (courage, honesty, practical wisdom) for**eudaimonia** (flourishing). Moral learning is habit and exemplar, not algorithm.",
        "mechanism": "1. Community identifies virtues relevant to good life.\n2. Practice and imitation build stable character traits.\n3. **Phronesis** (practical wisdom) balances virtues in context.\n4. Acts express character — single deeds judged in life narrative.",
        "implications": "- Compliance training fails without role models and practice environments.\n- Modern revivals (MacIntyre) critique rule-and-calculus ethics alone.\n- Complements [[deontology]] rules and [[utilitarianism]] outcomes.",
        "reading": "- Aristotle. *Nicomachean Ethics*. Various translations — especially Book II & VI.\n- MacIntyre, A. (1981). *After Virtue*. University of Notre Dame Press.\n- Annas, J. (2011). *Intelligent Virtue*. Oxford University Press.",
    },
    "moral-relativism": {
        "essence": "Moral truth varies by culture or individual — distinguish descriptive vs normative claims.",
        "why": "Travel, anthropology, and multiculturalism trigger relativism debates — confusion between tolerance and \"anything goes\" enables bad faith.",
        "core": "**Descriptive moral relativism**: cultures disagree on morality. **Normative relativism**: therefore no universal ought — contested. **Metaethical relativism**: truth relative to framework. Each claim separable.",
        "mechanism": "1. Observer notes divergent moral codes across societies.\n2. Inference: either hidden universal + local error, or plural valid codes, or power-laundered custom.\n3. Tolerance policies may draw on descriptive fact without endorsing normative relativism.\n4. Human rights movements assert cross-cultural norms — anti-relativist practice.",
        "implications": "- Relativism-as-excuse collapses when criticising outsiders — performative inconsistency.\n- [[value-diversity]] allows disagreement without denying all judgment.\n- [[moral-foundations-theory]] describes, not legitimises, differences.",
        "reading": "- Wong, D. B. (2006). *Natural Moralities*. Oxford University Press.\n- Harman, G., & Thomson, J. J. (1996). *Moral Relativism and Moral Objectivity*. Blackwell.\n- [[philosophy-of-ethics]] hub.",
        "misconceptions": [
            ("All anthropologists are normative relativists", "Descriptive diversity ≠ approval"),
            ("Objectivism means one culture is always right", "Universal claims can still be argued critically"),
        ],
    },
    "balance-of-power": {
        "essence": "States align to prevent any single actor from dominating the system.",
        "why": "Explains shifting alliances in Europe, Middle East balancing, and concern over unipolar moments — structure independent of ideology.",
        "core": "**Balance of power**: states form coalitions against would-be hegemons. Automatic (multiple poles) or manual (alliances). Failure yields hegemony or systemic war.",
        "mechanism": "1. Rising power threatens others' survival or autonomy.\n2. Threatened states balance (arm, ally) or bandwagon (submit).\n3. Counter-coalition raises cost of dominance.\n4. Equilibrium shifts with technology, economy, leadership — never static.",
        "implications": "- Small states gain leverage as swing balancers.\n- Nuclear weapons alter balancing calculus ([[deterrence-theory]]).\n- [[multipolar-world-dynamics]] when poles multiply.",
        "reading": "- Waltz, K. N. (1979). *Theory of International Politics*. Addison-Wesley.\n- Morgenthau, H. J. (1948). *Politics Among Nations* — balance chapters.\n- Mearsheimer, J. J. (2001). *The Tragedy of Great Power Politics*. Norton.",
    },
    "deterrence-theory": {
        "essence": "Threat of retaliation prevents attack — credibility and misperception matter as much as arsenals.",
        "why": "Nuclear strategy, cyber red lines, and corporate litigation rely on credible punishment — incredible threats invite probes.",
        "core": "**Deterrence**: impose costs exceeding adversary gains from aggression. Requires**capability**, **communication**, and**credibility** (including reputation for resolve).",
        "mechanism": "1. Defender announces response to attack (sanctions, strike).\n2. Attacker weighs expected cost vs benefit.\n3. If cost > benefit and believed, attack deterred.\n4. Misperception, commitment problems, or domestic politics break deterrence.",
        "implications": "- Escalation ladders must be understandable — ambiguity can cause war.\n- Mini-strokes test deterrence — death by a thousand cuts.\n- [[prisoners-dilemma]] and [[balance-of-power]] structural cousins.",
        "reading": "- Schelling, T. C. (1966). *Arms and Influence*. Yale University Press.\n- Kahn, H., & Wiener, A. J. (1962). *On Thermonuclear War*. Princeton University Press.\n- Payne, K. B. (2016). *The Great American Gamble*. National Institute Press.",
    },
    "multipolar-world-dynamics": {
        "essence": "Three or more great powers — shifting alliances, complexity, and opaque conflict chains.",
        "why": "Cold War bipolar clarity gone; US–China–EU–India–Russia interactions need multipolar models — not automatic stability.",
        "core": "**Multipolarity**: no single dyad defines system. More possible coalitions, **buck-passing**, and**chain-ganging** — WWI classic case.",
        "mechanism": "1. Multiple poles with overlapping interests.\n2. Local crises entangle distant allies via alliance commitments.\n3. States free-ride or pass buck hoping others balance.\n4. Miscalculation probability rises with actor count and opaque intentions.",
        "implications": "- Institutions for communication (hotlines) more vital than bipolar era.\n- Middle powers pivotal — not merely pawns.\n- [[evolution-of-trust]] repeated games differ with many players.",
        "reading": "- Christensen, T. J., & Snyder, J. (1990). Chain gangs and passed bucks. *World Politics*.\n- Mearsheimer, J. J. (2001). *The Tragedy of Great Power Politics* — multipolar chapters.\n- [[geopolitics]] hub.",
    },
    "agenda-setting": {
        "essence": "Media influence what people think**about** — not always what to think.",
        "why": "If it bleeds it leads — public priorities track coverage more than objective risk lists. Policy windows open on salient issues only.",
        "core": "McCombs & Shaw's**agenda-setting**: media**gatekeep**and**rank**issues; audience**learns importance**from prominence. Second-level agenda-setting adds attribute framing.",
        "mechanism": "1. Media allocate attention (front page, trending).\n2. Audience infers issue importance from frequency and placement.\n3. Politicians respond to perceived public agenda — feedback loop.\n4. Neglected problems lack constituency despite objective severity.",
        "implications": "- Advocacy competes for attention, not only argument quality.\n- Algorithmic feeds are agenda-setters ([[surveillance-capitalism]]).\n- [[framing-effects-media]] adds how issues defined once salient.",
        "reading": "- McCombs, M., & Shaw, D. L. (1972). The agenda-setting function of mass media. *Public Opinion Quarterly*.\n- McCombs, M. (2014). *Setting the Agenda* (2nd ed.). Polity.\n- [[media-literacy]] hub.",
    },
    "framing-effects-media": {
        "essence": "Presenting the same facts in different frames changes preference, blame, and memory.",
        "why": "Gain vs loss frame shifts vaccination uptake; \"immigrants as workers vs burden\" splits coalitions — equivalent facts, divergent politics.",
        "core": "**Framing effects** (Tversky & Kahneman): description alters choice without changing stakes. Media frames package events (conflict, human interest, economic consequence).",
        "mechanism": "1. Event occurs with multi-dimensional aspects.\n2. Communicator emphasises subset (casualties vs budget vs hero).\n3. Audience evaluates via accessible dimension — **what you see is all there is**.\n4. Preferences and attributions shift; participants unaware of frame.",
        "implications": "- Fact-checking same numbers insufficient if frame untouched.\n- Multiple frames in one explorable reduce capture ([[comparison-view]]).\n- [[emotionally-charged-language]] amplifies frame stickiness.",
        "reading": "- Tversky, A., & Kahneman, D. (1981). The framing of decisions and the psychology of choice. *Science*.\n- Entman, R. M. (1993). Framing: Toward clarification of a fractured paradigm. *Journal of Communication*.\n- [[language-and-framing]] hub.",
    },
    "propaganda-model": {
        "essence": "Structural filters — ownership, advertising, sourcing, flak — shape news content before censorship.",
        "why": "Explains consistent biases in \"mainstream\" outlets without conspiracy — incentives and access journalism.",
        "core": "Herman & Chomsky's**propaganda model**: five filters (ownership, advertising, sourcing, flak, anti-communism ideology) skew coverage toward elite interests within democratic façade.",
        "mechanism": "1. Media firms need profit; advertisers sensitive to content.\n2. Beat reporters depend on official sources — reciprocity bias.\n3. Think tanks and flak punish deviance.\n4. Stories harming powerful interests face higher bar; patriotic frames default.",
        "implications": "- Diversity of outlets needed plus structural analysis, not only individual bias training.\n- State and corporate propaganda use same attention economics ([[agenda-setting]]).\n- Independent funding models alter filter strength.",
        "reading": "- Herman, E. S., & Chomsky, N. (1988). *Manufacturing Consent*. Pantheon.\n- Herman, E. S. (1999). The propaganda model revisited. *Monthly Review*.\n- [[media-literacy]] · [[surveillance-capitalism]].",
    },
    "echo-chambers": {
        "essence": "Homogeneous information environments amplify beliefs and reduce corrective exposure.",
        "why": "Polarisation, vaccine communities, and financial bubbles share topology — not only individual bias but network structure.",
        "core": "**Echo chambers** (Sunstein, network science): selective exposure + reinforcement + distrust of outsiders → beliefs intensify and diverge across groups. Distinct from epistemic bubbles (lack of info) vs full chambers (discredit outsiders).",
        "mechanism": "1. Algorithm or social choice homogenises feed.\n2. Confirming messages repeated; dissent rare or mocked.\n3. Group identity fuses with beliefs — exit costly.\n4. Cross-group distrust labels counter-evidence as enemy propaganda.",
        "implications": "- Breaking chambers needs trusted in-group dissidents, not only facts from outside.\n- Platform design (cross-cutting exposure) affects democracy scale.\n- [[confirmation-bias]] individual layer; [[information-cascades]] social layer.",
        "reading": "- Sunstein, C. R. (2017). *#Republic*. Princeton University Press.\n- Nguyen, C. T. (2020). Echo chambers and epistemic bubbles. *Episteme*.\n- Pariser, E. (2011). *The Filter Bubble*. Penguin.",
    },
    "second-order-effects": {
        "essence": "Consequences of consequences — interventions ripple beyond first intent.",
        "why": "Antibiotics create resistance; highway relief creates induced demand; welfare cliffs trap workers — first-order success hides second-order harm.",
        "core": "**Second-order effects**follow initial policy or innovation shock. Systems with delays and adaptation produce**feedback**often opposite to first-order goal ([[feedback-loops]]).",
        "mechanism": "1. Intervention changes incentive or environment (antibiotics, new road, metric bonus).\n2. Agents adapt behaviour to new equilibrium.\n3. Adaptation alters original problem or creates new externalities.\n4. Policymakers celebrate first-order metric while second-order accumulates.",
        "implications": "- Monitor downstream indicators, not only target KPI.\n- Simulation and sandbox before rollout ([[sandbox-mode]]).\n- [[unintended-consequences]] · [[unintended-system-behavior]] sibling concepts.",
        "reading": "- Merton, R. K. (1936). Unanticipated consequences — foundational.\n- Sterman, J. D. (2000). *Business Dynamics*. McGraw-Hill — system dynamics.\n- [[systems-thinking]] hub.",
    },
    "unintended-system-behavior": {
        "essence": "System output nobody designed — emergence plus perverse incentives.",
        "why": "Markets crash, traffic jams, and bureaucracies ossify without villain — structure produces behaviour.",
        "core": "**Unintended system behavior**combines**emergence** (local rules → global pattern) with**misaligned incentives** ([[cobra-farm]]). No central planner needed for pathology.",
        "mechanism": "1. Components follow local rules optimising local objective.\n2. Interactions produce global pattern (congestion, inequality, boom-bust).\n3. Observers attribute intent where none exists.\n4. Fixes targeting symptoms without structure often worsen ([[second-order-effects]]).",
        "implications": "- Leverage points often counterintuitive — intervene on feedback delays or goals ([[systems-thinking]]).\n- Explorable simulations make emergence visceral ([[emergence]] · [[feedback-loops]]).\n- Humility: \" who wanted this?\" wrong question; \" what structure yields this?\" right.",
        "reading": "- Meadows, D. H. (2008). *Thinking in Systems*. Chelsea Green.\n- Perrow, C. (1984). *Normal Accidents*. Princeton University Press.\n- Schelling, T. C. (1978). *Micromotives and Macrobehavior*. Norton — [[micromotives-and-macrobehavior]].",
        "misconceptions": [
            ("Unintended means no one responsible", "Designers still accountable for foreseeable incentives"),
            ("More control always fixes", "Over-control can amplify oscillation and gaming"),
        ],
    },
}


def upgrade_body(slug: str, title: str, summary: str, related: list[str]) -> str | None:
    entry = UPGRADES.get(slug)
    if entry is None:
        return None
    return schelling_body(
        title=title,
        essence=entry["essence"],
        why=entry["why"],
        core=entry["core"],
        mechanism=entry["mechanism"],
        implications=entry["implications"],
        related=related,
        reading=entry["reading"],
        misconceptions=entry.get("misconceptions"),
    )


def apply_upgrades() -> int:
    from expansion_topics import MORE_CONCEPTS

    count = 0
    for slug, title, summary, _wing, folder, related in MORE_CONCEPTS:
        body = upgrade_body(slug, title, summary, related)
        if body is None:
            continue
        path = CONTENT / "theories" / folder / f"{slug}.md"
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---"):
            continue
        parts = text.split("---", 2)
        if len(parts) < 3:
            continue
        frontmatter = parts[1]
        path.write_text(f"---{frontmatter}---\n\n{body}", encoding="utf-8")
        count += 1
    return count


if __name__ == "__main__":
    print(apply_upgrades())
