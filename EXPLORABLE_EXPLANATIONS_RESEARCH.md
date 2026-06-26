# Explorable Explanations Research Lab
## Reverse-Engineering Nicky Case → Discovering Hidden Truths Through Interaction

*Research document · Interaction Design Lab · June 2026*

**References:** [Parable of the Polygons](https://ncase.me/polygons/) · [Nicky Case on GitHub](https://github.com/ncase) · [How I Make Explorable Explanations](https://blog.ncase.me/how-i-make-an-explorable-explanation/) · Bret Victor's [Explorable Explanations](https://worrydream.com/ExplorableExplanations/) · Austin Kleon's *Steal Like an Artist*

---

# Phase 1: Nicky Case — Project Autopsies & Extracted Principles

## 1. Parable of the Polygons (2014, with Vi Hart)

| Dimension | Analysis |
|-----------|----------|
| **Theory** | Thomas Schelling's dynamic segregation model (1971); extended with *anti-bias* (demand for diversity) as desegregation mechanism |
| **Why it matters** | Explains how structural segregation emerges without individual malice — housing, schools, social networks, hiring |
| **Why interaction > reading** | Reading "33% threshold" is abstract; dragging one unhappy triangle and watching clusters crystallize makes the mechanism *felt* |
| **Emotional engagement** | Cute anthropomorphized shapes with minimal faces; guilt-free framing ("slightly shapist"); moral arc from innocence → horror → hope |
| **Shareability** | Counter-intuitive punchline ("harmless bias → harmful world"); progressive reveals; quotable moral; diversity-box puzzle is memeable |
| **Interaction pattern** | **Manual agent placement** → **automated simulation** → **parameter slider** → **initial-condition flip** → **sandbox** |
| **Why it clicks** | User performs the "reasonable" action (move unhappy shapes to empty spots) and *causes* segregation themselves — the aha is self-incrimination without accusation |

**Extracted principles:** Agent-based micro-rules → macro emergence; start with user as benevolent actor; invert the fix (zero bias doesn't undo history); sandbox proves generality.

---

## 2. The Evolution of Trust (2017)

| Dimension | Analysis |
|-----------|----------|
| **Theory** | Iterated Prisoner's Dilemma; evolution of cooperation (Axelrod); noise, forgiveness (Win-Stay Lose-Shift), reputation, population dynamics |
| **Why it matters** | Trust, betrayal, institutions, WWI trench truces, online toxicity — cooperation is fragile and conditional |
| **Why interaction > reading** | Payoff matrices are dead on paper; *playing* against Tit-for-Tat, Grudger, Cheater makes strategy visceral |
| **Emotional engagement** | Historical hook (Christmas truce); characters as archetypes; betrayal *hurts* because you've invested rounds |
| **Shareability** | "One-shot vs repeated game" is endlessly applicable; tournament reveal is a set-piece; meme-friendly character names |
| **Interaction pattern** | **Playable mini-game** → **BUT-chain narrative** → **tournament simulation** → **noise slider** → **population evolution** → **sandbox** |
| **Why it clicks** | Each chapter destroys the previous solution: cooperation works BUT one-shot fails BUT repeated works BUT noise breaks it BUT forgiveness fixes it — plot twists as pedagogy |

**Extracted principles:** Chain counter-intuitive reveals with "BUT"; personify strategies; historical anchor; let user lose and feel why.

---

## 3. We Become What We Behold (2016)

| Dimension | Analysis |
|-----------|----------|
| **Theory** | Media feedback loops; selective attention; othering; vicious/reinforcing cycles (systems thinking) |
| **Why it matters** | News cycles, social media outrage, polarization, representation in media |
| **Why interaction > reading** | User *is* the camera; choosing what to photograph *causes* the tragedy — procedural rhetoric (Ian Bogost) |
| **Emotional engagement** | Short, cute, accelerates to horror in ~5 minutes; user complicity; inevitable ending creates dread |
| **Shareability** | Complete experience in one sitting; highly streamable; "you caused this" is a share trigger |
| **Interaction pattern** | **Role-play as system component** → **single mechanic (photograph)** → **escalating feedback loop** → **no sandbox (closed parable)** |
| **Why it clicks** | The mechanic *is* the thesis; no lecture needed; ending reframes entire playthrough |

**Extracted principles:** Player as part of the system; one input, many consequences; brevity; complicity over instruction.

---

## 4. Loopy (2017)

| Dimension | Analysis |
|-----------|----------|
| **Theory** | Systems thinking; reinforcing vs balancing feedback loops; causal loop diagrams |
| **Why it matters** | Climate, addiction, poverty traps, organizational dysfunction — most problems are loops, not lines |
| **Why interaction > reading** | Static diagrams don't *run*; drawing and simulating your own loops externalizes mental models |
| **Emotional engagement** | Creative tool ownership; "I built this model of my life/company" |
| **Shareability** | User-generated models are shareable artifacts; embeddable |
| **Interaction pattern** | **Authoring tool** → **live simulation** → **no prescribed narrative** |
| **Why it clicks** | Immediate run button on hand-drawn diagram; circles literally close before your eyes |

**Extracted principles:** Tool-as-explorable; loops must animate; minimal syntax, maximal expressivity; user becomes author.

---

## 5. To Build a Better Ballot (2016)

| Dimension | Analysis |
|-----------|----------|
| **Theory** | Social choice theory; voting systems (FPTP, IRV, Borda, Approval, Score, Condorcet); Arrow's theorem implications; spoiler effect |
| **Why it matters** | Democracy design; every election; ranked-choice debates |
| **Why interaction > reading** | Same voter preferences, different systems → different winners — must be *seen* simultaneously |
| **Emotional engagement** | Civic stakes; "your vote counts differently" personal relevance; sandbox debates |
| **Shareability** | Custom scenario sharing; politically timely; sandbox invites argument-with-evidence |
| **Interaction pattern** | **Single voter concrete** → **scale to election** → **side-by-side system switcher** → **spoiler scenario** → **shareable sandbox** |
| **Why it clicks** | Ka-Ping Yee-style visualization: one dataset, six outcomes — comparison is the insight |

**Extracted principles:** Ladder of abstraction (Bret Victor); same input, rule-variant output; shareable scenarios for discourse.

---

## 6. Fireflies (2017)

| Dimension | Analysis |
|-----------|----------|
| **Theory** | Coupled oscillators; self-synchronization (Kuramoto-style intuition); emergence without leader |
| **Why it matters** | Heart cells, neural sync, fireflies, grid stability — order from local rules |
| **Why interaction > reading** | Phase alignment is dynamic; must watch desync → sync transition |
| **Emotional engagement** | Beauty; meditative; collective pulse is emotionally satisfying |
| **Shareability** | Aesthetic GIFs; "no conductor" surprise |
| **Interaction pattern** | **Parameter play (coupling, disorder)** → **sandbox** |
| **Why it clicks** | Starts chaotic, ends unified — visual metaphor for invisible coordination |

**Extracted principles:** Beauty as pedagogical tool; continuous parameter; emergent rhythm.

---

## 7. The Wisdom and/or Madness of Crowds (2018)

| Dimension | Analysis |
|-----------|----------|
| **Theory** | Network topology + social learning; information cascades; echo chambers vs bridge networks; complex contagion |
| **Why it matters** | Misinformation, cult formation, innovation diffusion, weak ties |
| **Why interaction > reading** | Network structure changes *same* message spread — topology must be manipulable |
| **Emotional engagement** | "Madness" in title; watching your message die or go viral |
| **Shareability** | Network sandbox; surprising bridge-node result |
| **Interaction pattern** | **Place message** → **watch diffusion** → **rewire network** → **compare topologies** |
| **Why it clicks** | Same idea, different graph → opposite outcome; instant network literacy |

**Extracted principles:** Topology > content; interactive graph rewiring; compare side-by-side.

---

## 8. Coming Out Simulator (2014)

| Dimension | Analysis |
|-----------|----------|
| **Theory** | Lived experience of marginalization; branching narrative; emotional decision theory (not formal) |
| **Why it matters** | Empathy; LGBTQ+ visibility; how systems of people respond to disclosure |
| **Why interaction > reading** | Choices under social pressure can't be conveyed by essay; timing and tone matter |
| **Emotional engagement** | Autobiographical authenticity; humor → tension → heartbreak |
| **Shareability** | Personal story; identity; "play this to understand" |
| **Interaction pattern** | **Branching dialogue** → **phone/text UI verisimilitude** → **forced tradeoffs** |
| **Why it clicks** | You *are* the protagonist; failure states teach without lecturing |

**Extracted principles:** First-person embodiment; familiar UI; real stakes in choices; narrative as proof.

---

## 9. Adventures with Anxiety (2019)

| Dimension | Analysis |
|-----------|----------|
| **Theory** | Anxiety as protective feedback loop gone wrong; CBT-adjacent reframing; embodied cognition |
| **Why it matters** | Mental health literacy; destigmatization |
| **Why interaction > reading** | You play *as* the anxiety voice — role reversal creates insight impossible from pamphlet |
| **Emotional engagement** | Humor + horror; wolf character; self-recognition |
| **Shareability** | "Send this to someone who doesn't get anxiety" |
| **Interaction pattern** | **Play the antagonist system** → **escalation** → **reframe** |
| **Why it clicks** | Hearing your own anxious logic externalized is recognition, not instruction |

**Extracted principles:** Personify internal systems; comedy lowers defenses; player plays the "wrong" role first.

---

## 10. Neurotic Neurons (2015)

| Dimension | Analysis |
|-----------|----------|
| **Theory** | Hebbian learning ("fire together wire together"); neural habit formation; trigger-response loops |
| **Why it matters** | Addiction, PTSD triggers, habit change |
| **Why interaction > reading** | Synapses strengthening visually mirrors the mechanism |
| **Emotional engagement** | Cute neurons; watching pathways thicken is unsettling |
| **Shareability** | Short; visual metaphor is sticky |
| **Interaction pattern** | **Click to fire** → **pathway thickens** → **trigger becomes automatic** |
| **Why it clicks** | You literally wire the bad habit |

**Extracted principles:** Metaphor is mechanism; repeated action changes structure; show physical change in system.

---

## 11. How to Remember Anything Forever-ish (2018)

| Dimension | Analysis |
|-----------|----------|
| **Theory** | Spaced repetition; forgetting curve (Ebbinghaus); testing effect |
| **Why it matters** | Learning how to learn; fights cram culture |
| **Why interaction > reading** | Orbit-style embedded flashcards *demonstrate* spacing while teaching it |
| **Emotional engagement** | Meta: the medium proves the message |
| **Shareability** | Practical utility; Orbit integration |
| **Interaction pattern** | **Explorable + embedded SR tool** → **self-referential proof** |
| **Why it clicks** | You forget during reading, then the tool saves you — lived demonstration |

**Extracted principles:** Self-referential design; tool embedded in lesson; immediate personal benefit.

---

## 12. Emoji Simulator (2017)

| Dimension | Analysis |
|-----------|----------|
| **Theory** | Cellular automata; Conway's Game of Life; emergence from simple rules |
| **Why it matters** | Computation, artificial life, complex systems entry point |
| **Why interaction > reading** | Rules are trivial; *running* them reveals universality |
| **Emotional engagement** | Playful emoji; surprise gliders/guns |
| **Shareability** | User-built patterns; meme language |
| **Interaction pattern** | **Rule editor** → **playfield** → **sandbox creation** |
| **Why it clicks** | Two rules → infinite behavior |

**Extracted principles:** Absurd/friendly skin on deep math; user-authored rules; emergence playground.

---

## 13. Sight & Light (2014)

| Dimension | Analysis |
|-----------|----------|
| **Theory** | 2D raycasting; visibility polygons; computational geometry for game dev |
| **Why it matters** | Teaches *making* not just *knowing*; procedural literacy |
| **Why interaction > reading** | Drag light source, see shadows update — geometry becomes intuition |
| **Emotional engagement** | "I can build games" empowerment |
| **Shareability** | Dev audience; tutorial that respects intelligence |
| **Interaction pattern** | **Interactive diagram** → **incremental code reveal** → **live playground** |
| **Why it clicks** | See the algorithm, then see the code — dual ladder |

**Extracted principles:** Bret Victor "Inventing on Principle"; immediate visual feedback on code concepts; maker pathway.

---

## 14. Attractor Landscapes (2017)

| Dimension | Analysis |
|-----------|----------|
| **Theory** | Dynamical systems; attractors; bifurcations; ball-in-bowl metaphor |
| **Why it matters** | Depression/trauma wells, climate tipping points, market equilibria |
| **Why interaction > reading** | Potential energy surfaces need dragging the ball |
| **Emotional engagement** | Tipping over a ridge feels dramatic |
| **Shareability** | Visual metaphor transfers to many domains |
| **Interaction pattern** | **Drag ball on surface** → **parameter morphs landscape** → **bifurcation** |
| **Why it clicks** | Stable states become literal valleys |

**Extracted principles:** Physical metaphor for math; parameter-induced topology change.

---

## 15. Nutshell / Explorable Explanations Hub

| Dimension | Analysis |
|-----------|----------|
| **Theory** | Expandable explanations; platform for ecosystem |
| **Why it matters** | Infrastructure for genre; lowers barrier |
| **Interaction pattern** | **Tool + curation** |
| **Principles** | Meta-layer; empower others; public domain ethos |

---

## Consolidated Design DNA (Reusable Principles)

1. **Start with 🤔** — Pose a question via story, game, or paradox before any theory.
2. **Concrete before abstract** — Hand before equation (Ladder of Abstraction).
3. **BUT-chain pedagogy** — Each answer contains the seed of its own destruction.
4. **Simple rules → surprising emergence** — Agent models, loops, automata.
5. **Procedural rhetoric** — Mechanics embody thesis (WBWWB, Polygons drag).
6. **Complicity without blame** — User causes outcome with good intentions.
7. **Personification** — Strategies, neurons, shapes, anxiety-wolf as characters.
8. **Parameter revelation** — Sliders expose hidden levers (bias %, noise, coupling).
9. **Initial conditions matter** — History persists; equilibrium instability.
10. **Comparison view** — Same setup, different rule/system/topology.
11. **Predict-then-reveal** — Bet before simulation runs.
12. **Sandbox ending** — Graduate from author questions to user questions.
13. **Public domain generosity** — Remix-friendly, classroom-ready.
14. **Aesthetic warmth** — Cute, human, funny — never sterile textbook.
15. **One sitting or one month** — Match length to insight (WBWWB: 5 min; Trust: 30 min).
16. **Self-referential tools** — The explorable can be the instrument (Orbit, Loopy).
17. **End with 🤔** — More questions, not closure.

---

# Phase 2: The Explorable Explanation Framework

## The E.C.H.O. Model

Every strong Nicky Case–class experience can be decomposed into:

| Element | Definition | Design Question |
|---------|------------|-----------------|
| **E — Engine** | Hidden system of agents/rules/forces | What are the 1–3 local rules? |
| **C — Control** | What the user can touch | Does control feel like play, not homework? |
| **H — Hook** | Emotional/cognitive question | Would a curious 14-year-old care? |
| **O — Outcome gap** | Distance between intuition and result | Is the surprise *earned* by the user's actions? |

## The 9-Beat Structure (Optional Spine)

1. **Hook question** (no jargon)
2. **Play the naive version** (user succeeds with wrong mental model)
3. **First twist** (system produces unexpected result)
4. **Name the rule** (minimal vocabulary)
5. **Stress test** (change one parameter)
6. **Second twist** (fix fails or new problem)
7. **Real-world bridge** (one concrete implication)
8. **Sandbox** (open exploration)
9. **Return question** (deeper 🤔)

## Interaction Pattern Taxonomy

| Pattern | Example Projects | Best For |
|---------|------------------|----------|
| Agent placement | Polygons | Emergence, segregation |
| Repeated game | Trust | Game theory, evolution |
| Role-as-system-part | WBWWB, Anxiety | Feedback, complicity |
| Graph rewiring | Wisdom/Madness | Networks |
| Rule comparison | Ballot | Mechanism design |
| Oscillator/field | Fireflies, Attractors | Dynamics, sync |
| Authoring tool | Loopy, Emoji Sim | Systems, CA |
| Branching narrative | Coming Out | Empathy, decision |
| Self-referential tool | Remember Forever | Meta-learning |
| Live algorithm | Sight & Light | CS/math procedural |

## Quality Gate (Pre-Build)

An idea passes if it has:
- [ ] Emergent behavior not obvious from rules
- [ ] Visual representation that *is* the concept
- [ ] User action causing the surprise (not animation-only)
- [ ] Real-world stake beyond academia
- [ ] Sandbox or replay variant

---

# Phase 3: Cross-Disciplinary Theory Landscape

Scanned domains for *under-explored* interactive potential (not exhaustive — discovery space):

**Behavioral Econ:** Loss aversion, endowment effect, hyperbolic discounting, ergodicity economics (Ole Peters), mental accounting, default effects, Allais/Ellsberg paradoxes.

**Game Theory:** Stag hunt, signaling games, cheap talk, Schelling focal points, war of attrition, matching pennies, Bayesian games, mechanism design, Vickrey-Clarke-Groves.

**Psychology/Cognition:** Stroop, change blindness, McGurk, anchoring, availability, base rate neglect, Dunning-Kruger dynamics, Pygmalion effect, fundamental attribution error.

**Probability/Stats:** Monty Hall, Simpson's paradox, Berkson's paradox, regression to mean, prosecutor's fallacy, multiple comparisons, Anscombe's quartet, Galton board, birthday paradox, fat tails vs normal.

**Networks:** Percolation threshold, preferential attachment, friendship paradox, majority illusion, weak ties, structural holes, information cascades, complex contagion (≥2 exposures).

**Complex Systems:** Self-organized criticality, sandpile model, edge of chaos, Bak-Tang-Wiesenfeld, power laws, Lotka-Volterra, renormalization intuition.

**Evolution:** Red Queen, Fisher runaway, handicap principle, kin selection, Muller's ratchet, fitness landscapes, host-parasite coevolution.

**Physics:** Entropy/statistical mechanics, Maxwell's demon, diffusion, resonance, critical mass, double-well potential, stochastic resonance.

**Economics:** Tragedy of commons, Ostrom design principles, comparative advantage, Jevons paradox, Goodhart's law, Braess paradox, Hotelling's law, Gini dynamics.

**Logic/Paradox:** Newcomb's problem, sleeping beauty, Raven paradox, blue eyes/common knowledge, trolley variants, Simpson's paradox as logic.

**Cybernetics:** Ashby's requisite variety, homeostasis, PID intuition, W. Ross Ashby's law, goal-directed systems.

**Information Theory:** Channel capacity, compression vs meaning, mutual information, error correction intuition, Shannon's source coding.

**Urban/Spatial:** Schelling (done), Axelrod culture model, TOD vs sprawl, percolation of services, Jane Jacobs diversity conditions.

**Obscure Gems:** Petrie multiplier, Parrondo's paradox, Moravec's paradox, Lindy effect, Cobra effect, Campbell's law, Hanlon+Goodhart in metrics, Hegselmann-Krause bounded confidence, Deffuant opinion dynamics, Kruskal count, Polya urn, Yule-Simon, Kingman's formula (queues), Little's law, Kelly criterion, Mandelbrot's 1/f noise in risk.

---

# Phase 4: Scoring Methodology

Each candidate scored 1–10 on: Visual Potential (V), Interaction Potential (I), Surprise (S), Educational Value (E), Emotional Impact (Em), Virality (Vi), Replayability (R), Simplicity (Si), Beauty (B), Aha (A).

**Composite** = weighted: 0.15×A + 0.12×I + 0.12×S + 0.12×E + 0.10×V + 0.10×Em + 0.08×Vi + 0.08×R + 0.08×Si + 0.05×B

**Discard threshold:** Any dimension ≤3, or composite <6.0, or "already exists as major explorable."

*Existing major explorables to avoid duplicating:* Schelling segregation, Iterated PD/Trust, Voting systems (Ballot), Firefly sync, Media feedback (WBWWB), Network contagion (Wisdom/Madness), Spaced repetition (Remember Forever), Loopy-style CLD, Game of Life, 2D lighting tutorial, Monty Hall (many), Prisoner's Dilemma (many), Tragedy of Commons (many), Double slit (some).

---

# Phase 5: Candidate Concepts (120)

**Format:** Name · Theory · One-liner · Core interaction · Visual · Control · Changes · Emergence · Aha · Build · Time · Audience · Scores (V/I/S/E/Em/Vi/R/Si/B/A)

---

## Society & Institutions (1–15)

**1. The Standing Ovation** · Granovetter threshold model · One person clapping can start a standing ovation — or fail. · Click individuals to stand; watch cascade or fizzle · Auditorium of dots · Who stands first · Applause spreads or dies · Critical threshold · "I caused the ovation by moving one person" · Med · 3wk · Civics, sociology · 8/9/9/8/7/8/9/9/7/9

**2. The Veil Room** · Rawls' veil of ignorance · Design a society before you know your place in it. · Allocate resources blind; reveal your assigned role · Lottery masks · Slider allocations · Gini, mobility · Unfair rules feel fair until reveal · Self-designed inequality · Med · 4wk · Ethics, policy · 7/8/8/9/9/7/6/7/7/9

**3. The Petrie Multiplier** · Petrie (2013) · Harassment targets minorities disproportionately even with equal individual rates. · Set harassment probability equal; vary group size · Conference floor · Group ratio · Harassment counts · Quadratic asymmetry · "Equal meanness ≠ equal harm" · Low · 2wk · Tech, DEI · 8/8/9/9/9/8/7/9/6/10

**4. The Overton Window** · Overton window · Ideas move from unthinkable → policy by shifting acceptability. · Drag idea markers; watch coalition form/dissolve · Spectrum slider · Acceptability thresholds · Policy adoption · Gradual normalization · "Today's fringe is tomorrow's center" · Med · 3wk · Political science · 7/7/7/8/8/8/6/8/6/7

**5. The Commons Garden** · Ostrom + Hardin · Eight design principles save a commons; missing one collapses it. · Toggle governance rules; harvest yearly · Shared grid · Rule toggles · Fish population · Collapse or sustainability · "Commons can work — with institutions" · Med · 4wk · Environmental econ · 8/9/8/9/8/7/8/7/7/8

**6. The Cobra Farm** · Cobra effect · Rewarding snake tails increases snake breeding. · Set bounty; watch fake vs real behavior · Colonial map · Bounty slider · Snake count · Perverse incentive spike · "Metrics create the monster they measure" · Low · 2wk · Policy, mgmt · 8/8/9/8/7/9/8/9/6/9

**7. The Goodhart School** · Goodhart's law · When a measure becomes a target, it ceases to be a good measure. · Teachers optimize test scores; watch real learning diverge · School dashboard · Test weight · Scores vs literacy · Teaching to test · "Optimizing the metric broke the goal" · Med · 3wk · Education · 8/8/9/9/7/8/7/8/6/9

**8. The Campbell Scoreboard** · Campbell's law · Social pressure corrupts quantitative indicators. · Publish rankings; actors adapt strategically · Leaderboard · Ranking visibility · Metric inflation · Corruption emergence · "Transparency can weaponize gaming" · Med · 3wk · Governance · 7/8/8/8/7/7/7/7/6/8

**9. The Majority Illusion** · Majority illusion (Lerman et al.) · Your feed makes fringe views look universal. · Rewire social graph; same minority % · Social graph · Edge visibility · Perceived majority · Illusion of consensus · "My bubble lies about what's normal" · Med · 3wk · Media literacy · 9/9/9/8/7/9/8/8/7/9

**10. The Weak Tie Bridge** · Granovetter weak ties · Job offers come from acquaintances, not close friends. · Cut edges; watch opportunity flow stop · Network · Bridge deletion · Job reach · Cluster isolation · "Acquaintances hold the keys" · Med · 3wk · Career, networks · 8/8/7/8/6/7/9/8/6/8

**11. The Focal Point** · Schelling focal points · People coordinate without communication on salient features. · Place two players blind; reward matching · Grid with landmarks · Highlight features · Match rate · Salience wins · "We agreed without talking" · Low · 2wk · Game theory · 7/9/8/8/6/7/9/10/6/8

**12. The Pygmalion Class** · Pygmalion effect · Teacher expectations become student outcomes. · Set hidden expectations; watch performance drift · Classroom · Expectation slider · Student scores · Self-fulfilling prophecy · "Belief writes reality" · Med · 3wk · Education · 8/7/8/9/9/7/6/8/6/8

**13. The Matthew Effect** · Matthew effect · Small early advantage compounds into dominance. · Equal talent; unequal starting luck · Race track · Initial luck · Wealth gap · Runaway inequality · "The lucky get luckier" · Low · 2wk · Inequality · 8/8/8/9/8/8/9/9/7/9

**14. The Institutional Ratchet** · Path dependence · Temporary policies become permanent infrastructure. · Add/remove rules; measure removal cost · Bureaucracy tree · Policy toggles · Removal difficulty · Lock-in · "We can't undo what we built" · Med · 3wk · Public admin · 7/7/7/8/7/6/7/7/6/7

**15. The Pluralistic Ignorance Pool** · Pluralistic ignorance · Everyone privately rejects norm but publicly conforms. · Adjust private/public expression · Pool party metaphor · Conformity pressure · Apparent consensus · Hidden dissent · "Nobody wanted it but everyone did it" · Med · 3wk · Social psych · 8/8/9/9/8/8/7/8/7/9

---

## Mind & Cognition (16–30)

**16. The Stroop Storm** · Stroop effect · Color words hijack reading; conflict is measurable. · Name ink color while words lie · Word tiles · Speed clicks · RT spikes · Automatic reading · "Your brain can't not read" · Low · 1wk · Psych 101 · 9/10/7/8/5/6/8/10/7/7

**17. The Change Blindness Street** · Change blindness · Big scene changes go unseen without attention. · Spot difference during flicker · Street scene · Flicker timing · Missed changes · Attention gate · "You didn't see what changed" · Low · 2wk · Perception · 9/10/8/8/6/8/7/9/7/8

**18. The Anchoring Auction** · Anchoring · Random number skews estimates. · Spin wheel then bid · Auction · Anchor value · Bid distribution · Shifted estimates · "Random number owned your price" · Low · 1wk · Behavioral econ · 8/9/8/9/6/7/8/10/6/9

**19. The Availability Weather** · Availability heuristic · Recent vivid events distort risk perception. · Feed news; watch perceived vs actual risk · Weather map · News injection · Risk estimates · Distorted priorities · "Headlines rewrite your fears" · Med · 3wk · Media literacy · 8/8/8/9/7/8/7/8/6/8

**20. The Base Rate Hospital** · Base rate neglect · Test accuracy misleads without prevalence context. · Adjust disease rate; same test · Hospital bay · Prevalence slider · False positive rate · Counter-intuitive negatives · "A positive test can mean nothing" · Med · 2wk · Medicine, stats · 8/8/9/10/7/7/6/8/6/10

**21. The Dunning Valley** · Dunning-Kruger · Incompetence hides incompetence; experts doubt themselves. · Self-rate vs actual on tasks · Skill landscape · Task difficulty · Metacognition gap · Double peak error · "The worst think they're best" · Med · 3wk · Self-awareness · 8/7/8/8/8/8/7/7/6/8

**22. The Sunk Cost Tunnel** · Sunk cost fallacy · Past investment irrationally affects future choices. · Dig tunnel; costs escalate · Tunnel · Continue/quit · Depth vs value · Escalation · "Throwing good money after bad" · Low · 2wk · Decision making · 7/8/8/9/7/7/8/9/6/8

**23. The Endowment Mug** · Endowment effect · Owning instantly raises value. · Randomly give mug; trade · Mug market · Trade offers · WTA > WTP · Instant attachment · "It's yours so it's worth more" · Low · 1wk · Behavioral econ · 7/9/7/8/6/6/7/10/6/7

**24. The Hyperbolic Snack** · Hyperbolic discounting · Now beats later disproportionately. · Choose today vs future rewards · Timeline · Delay slider · Impatient choices · Time inconsistency · "Future you is a stranger" · Low · 2wk · Habits, finance · 8/8/8/9/7/7/8/9/6/8

**25. The McGurk Mouth** · McGurk effect · Vision overrides hearing in speech. · Mismatch audio/visual phonemes · Face video · A/V pairing · Heard syllable · Cross-modal override · "You heard what you saw" · Low · 1wk · Neuroscience · 9/10/9/8/6/8/5/8/7/9

**26. The Fundamental Attribution Stage** · Fundamental attribution error · Others' acts = character; ours = situation. · Same action, different labels · Stage · Perspective toggle · Blame assignment · Asymmetric attribution · "Their flaw, my circumstance" · Med · 2wk · Social psych · 7/8/7/9/8/7/6/8/6/8

**27. The Confirmation Lens** · Confirmation bias · Seeking evidence that confirms beliefs. · Search database with biased query · Document pile · Search terms · Retrieved set · Filter bubble · "You found what you looked for" · Med · 3wk · Critical thinking · 8/8/7/9/6/7/8/8/6/7

**28. The Hindsight Chronicle** · Hindsight bias · Past seems predictable after outcome known. · Predict then reveal outcome · Timeline · Outcome reveal · "I knew it" ratings · Predictability inflation · "It was obvious (it wasn't)" · Low · 2wk · History, law · 7/7/7/8/6/6/7/9/6/7

**29. The Memory Palace Builder** · Method of loci · Spatial memory amplifies recall. · Place items in room; test recall · Isometric room · Item placement · Recall score · Spatial boost · "Location is memory" · Med · 3wk · Learning · 9/8/6/8/6/7/9/7/8/7

**30. The Chunking Piano** · Chunking (Miller) · Grouping expands effective memory capacity. · Memorize notes with/without patterns · Piano roll · Grouping aid · Recall accuracy · Pattern advantage · "Structure frees capacity" · Low · 2wk · Learning · 8/8/6/8/5/5/8/9/7/7

---

## Probability & Statistics (31–45)

**31. The Monty Hall Carnival** · Monty Hall · Switching doors doubles win probability. · Play many trials; compare strategies · Game show · Switch/stay · Win rate · 2/3 vs 1/3 · "Staying feels right but loses" · Low · 1wk · Probability · 8/9/10/9/5/8/10/8/6/10 *(many exist — variant: 100-door)*

**32. The Simpson's Paradox University** · Simpson's paradox · Aggregated trend reverses when stratified. · Admit students by department · University · Dept weights · Overall vs dept · Reversal · "The average lied" · Med · 2wk · Stats · 8/8/10/10/6/7/7/7/6/10

**33. The Berkson's Ward** · Berkson's paradox · Hospital data shows spurious negative correlation. · Sample only admitted patients · Hospital · Admission criteria · Correlation sign · Artifact · "Selection created the pattern" · Med · 2wk · Epidemiology · 7/8/9/9/5/5/6/7/6/9

**34. The Galton Board** · Central limit theorem · Random bounces sum to normal distribution. · Drop balls; watch bell curve form · Peg board · Drop rate · Histogram · Normal emergence · "Chaos becomes normal" · Low · 2wk · Stats · 9/8/8/9/5/7/9/9/9/8

**35. The Regression Sports Line** · Regression to mean · Extreme performance likely followed by average. · Track rookie seasons · Sports chart · Season # · Next year drop · Mean reversion · "They weren't declining — regressing" · Med · 2wk · Sports analytics · 8/7/8/9/6/6/8/8/6/8

**36. The Prosecutor's DNA** · Prosecutor's fallacy · P(match|innocent) ≠ P(innocent|match) · Adjust population size · Courtroom · Population · Guilt probability · Base rate trap · "Match ≠ guilt" · Med · 2wk · Law · 7/8/9/10/7/6/5/8/6/10

**37. The Birthday Cluster** · Birthday paradox · 23 people → 50% shared birthday. · Add people; highlight collisions · Party room · Headcount · Match probability · Counter-intuitive jump · "So few, so likely" · Low · 1wk · Probability · 8/9/9/8/5/8/9/10/6/9

**38. The Fat Tail Farm** · Fat tails vs normal · Extreme events dominate under power laws. · Compare crop ruin under Gaussian vs fat tail · Farm · Distribution type · Ruin frequency · Tail risk · "Average year misleads" · Med · 3wk · Finance, climate · 8/8/9/10/7/7/8/7/6/9

**39. The P-Hacking Lab** · Multiple comparisons · Testing until significance finds false positives. · Run studies; watch false discovery · Lab bench · Variables tested · Significant p's · False positives · "Ask enough, answer appears" · Med · 3wk · Science literacy · 8/8/9/10/6/8/8/7/6/9

**40. The Anscombe Quartet** · Anscombe's quartet · Same stats, wildly different shapes. · Four plots, identical summary · Scatter · Dataset select · Visual shape · Stats lie · "Mean and r aren't enough" · Low · 1wk · Data literacy · 9/7/8/10/4/6/6/8/7/9

**41. The Lindy Library** · Lindy effect · Expected life grows with age for non-perishable ideas. · Books on shelf; survival curves · Library · Age · Expected remaining · Counter-intuitive longevity · "Old ideas may outlive new" · Med · 2wk · Culture · 7/6/7/7/6/7/8/8/7/7

**42. The Kelly Bet** · Kelly criterion · Optimal bet size maximizes long-run growth; overbet ruins. · Simulate bankroll · Casino · Bet fraction · Growth/ruin · Optimal peak · "Half-Kelly is wisdom" · Med · 3wk · Finance · 7/9/8/9/6/6/10/7/6/8

**43. The Ergodicity Street** · Ole Peters ergodicity · Ensemble average ≠ time average for individuals. · Parallel vs sequential coin flips · Wealth paths · Gamble choice · Ruin vs average gain · Individual vs group · "Average return hides ruin" · Med · 4wk · Economics · 8/9/10/10/8/8/9/6/6/10

**44. The Polya Urn** · Polya urn · Rich-get-richer from positive feedback · Draw balls; color reinforces · Urn · Draw · Dominant color · Path dependence · "Early luck locks in" · Low · 2wk · Complex systems · 8/8/8/8/5/6/9/10/7/8

**45. The Raven Paradox** · Hempel's raven paradox · Observing green apple confirms "all ravens black" · Toggle evidence items · Logic garden · Evidence type · Confirmation · Absurd confirmation · "Every non-black non-raven counts" · Med · 3wk · Philosophy · 6/7/8/8/4/5/6/6/5/8

---

## Networks & Information (46–60)

**46. The Percolation City** · Percolation theory · City services fail when connectivity crosses critical threshold. · Randomly close roads · City grid · Block probability · Giant component · Phase transition · "One more closure killed the city" · Med · 3wk · Urban, epidemiology · 9/9/10/9/7/8/8/8/7/10

**47. The Preferential Attachment Web** · Barabási-Albert · New nodes link to hubs; power law emerges. · Grow network · Web graph · Link rule · Hub dominance · Scale-free · "The rich get richer online" · Med · 3wk · Networks · 9/8/8/9/6/7/9/8/7/8

**48. The Six Degrees Letter** · Small world · Few long links collapse average distance. · Add random long edges · World map · Long link density · Path length · Small world · "One bridge shrinks the world" · Med · 3wk · Sociology · 8/8/8/8/5/7/9/8/6/8

**49. The Information Cascade Falls** · Bikhchandani cascade · People ignore private signal, follow predecessors. · Sequential choices · Waterfall · Signal strength · Herding · Wrong consensus · "They knew better but followed" · Med · 3wk · Finance, social · 8/8/9/9/7/7/7/8/6/9

**50. The Complex Contagion Protest** · Complex contagion · Some behaviors need multiple exposures to spread. · Simple vs complex spread rules · Protest square · Threshold · Spread speed · Critical mass difference · "One seeing isn't enough" · Med · 3wk · Social movements · 8/9/9/9/8/8/7/8/7/9

**51. The Echo Chamber Engine** · Echo chambers · Homophily + recommendation → polarization without malice. · Tune recommendation strength · Two-party graph · Algorithm weight · Polarization index · Sorting · "No bad actors needed" · Med · 4wk · Media · 9/8/8/9/8/8/7/7/6/8

**52. The PageRank Village** · PageRank intuition · Importance from important links. · Link pages; watch rank flow · Mini web · Link creation · Rank distribution · Recursive status · "Votes from voters matter" · Med · 3wk · CS, media · 8/8/7/8/5/6/8/7/6/7

**53. The Structural Hole Broker** · Burt structural holes · Spanning disconnected groups yields advantage. · Bridge positions · Corporate graph · Bridge placement · Information rent · Broker power · "Gap between clusters is gold" · Med · 3wk · Business · 8/7/7/8/6/6/8/7/6/7

**54. The Friendship Paradox Club** · Friendship paradox · Your friends have more friends than you. · Random node vs neighbor avg · Party graph · Pick person · Degree comparison · Statistical illusion · "I'm less popular than my friends" · Low · 2wk · Networks · 8/8/9/8/6/8/9/9/6/9

**55. The Compression Poetry** · Shannon source coding · More frequent symbols get shorter codes. · Build Huffman tree · Text stream · Symbol frequency · Code length · Optimal compression · "Common = short" · Med · 3wk · Information theory · 7/8/7/9/4/5/8/7/6/7

**56. The Error Correction Choir** · Error correcting codes · Redundancy detects/fixes noise. · Corrupt transmitted message · Choir singing · Noise level · Recovery · Robust transmission · "Redundancy saves truth" · Med · 4wk · CS, biology · 7/8/7/8/5/5/7/6/6/7

**57. The Mutual Information Mirror** · Mutual information · How much knowing X reduces uncertainty about Y. · Toggle variables · Venn animation · Dependency · Info gain · Shared information · "How much does A tell about B" · High · 4wk · ML, stats · 7/8/6/9/4/4/7/5/6/7

**58. The Naming Game Tower** · Naming game · Local agreement globalizes word meaning. · Pairwise interactions · Tower of Babel · Interaction rate · Lexicon convergence · Self-organization · "Language without designer" · Med · 3wk · Linguistics · 8/8/8/8/5/6/9/8/7/8

**59. The Deffuant Polarization** · Deffuant model · Bounded confidence: similar opinions converge, distant repel. · Opinion slider on line · Opinion line · Confidence ε · Clusters · Polarization · "Too far to talk" · Med · 3wk · Discourse · 8/9/8/9/7/7/8/8/6/8

**60. The Hegselmann-Krause Camps** · HK bounded confidence · Agents average only within confidence interval. · Move agents; watch camps · Opinion space · ε · Factions · Cluster count · "Tolerance radius sets politics" · Med · 3wk · Political modeling · 8/9/8/9/7/6/8/7/6/8

---

## Cooperation, Conflict & Game Theory (61–75)

**61. The Stag Hunt Woods** · Stag hunt · Risk-dominant vs payoff-dominant equilibrium. · Choose hunt stag or rabbit · Forest · Partner strategy · Equilibrium selection · Coordination failure · "Safe choice killed cooperation" · Low · 2wk · Game theory · 8/8/8/9/7/6/8/9/7/8

**62. The Signaling Peacock** · Spence signaling · Costly signals prove quality. · Peacock tail cost vs mate success · Jungle · Tail size · Population fitness · Honest signaling · "Wasteful can be rational" · Med · 3wk · Evolution, econ · 9/8/8/9/6/7/8/8/9/8

**63. The Cheap Talk Negotiation** · Cheap talk vs costly · Words without cost are ignored. · Send messages; verify · Negotiation table · Message cost · Trust rate · Credible vs cheap · "Talk is cheap unless it hurts" · Med · 3wk · Negotiation · 7/8/7/8/6/5/7/8/6/7

**64. The War of Attrition Clock** · War of attrition · Escalation until one quits; time cost · Bid war; clock ticks · Auction · Bid increment · Exit time · Overpayment · "Last one standing loses least" · Med · 3wk · Conflict · 7/8/8/8/7/6/7/7/6/8

**65. The Allais Gamble** · Allais paradox · Violations of expected utility axioms. · Choose between framed lotteries · Lottery wheel · Frame · Preference reversal · Axiom violation · "Your choices aren't consistent" · Med · 2wk · Decision theory · 6/9/8/9/5/5/7/7/5/8

**66. The Ellsberg Urn** · Ellsberg ambiguity aversion · People prefer known probabilities. · Choose known vs unknown urn · Two urns · Ambiguity · Choice pattern · Ambiguity premium · "Unknown feels worse" · Med · 2wk · Economics · 7/9/7/8/6/5/7/8/5/7

**67. The Newcomb Predictor** · Newcomb's problem · One-box vs two-box tests belief in prediction. · Play against predictor · Boxes · One/two box · Payout · Decision paradox · "Free will vs prediction" · Med · 3wk · Philosophy · 7/8/9/8/7/7/8/7/6/9

**68. The Common Knowledge Blue Eyes** · Common knowledge · Public announcement enables cascade · Island puzzle interactive · Island · Announcement · Leave times · Induction cascade · "Everyone knowing everyone knows…" · High · 4wk · Logic · 7/8/9/9/6/6/7/5/6/9

**69. The Braess Roads** · Braess paradox · Adding road increases travel time. · Add link to network · Traffic network · New road · Flow equilibrium · Counter-intuitive slowdown · "More capacity = worse" · Med · 3wk · Urban planning · 9/9/10/9/6/8/8/7/7/10

**70. The Vickrey Auction** · Second-price auction · Truthful bidding is dominant strategy. · Compare auction formats · Auction · Bid · Revenue, truthfulness · Strategy-proof · "Honesty is optimal (here)" · Med · 2wk · Mechanism design · 7/9/7/9/4/4/7/8/6/7

**71. The Hotelling Beach** · Hotelling's law · Competitors cluster at center. · Place two ice cream carts · Beach line · Location · Customer split · Median convergence · "Sameness is rational" · Low · 2wk · Economics · 8/8/7/8/5/6/8/9/6/7

**72. The Median Voter Park** · Median voter theorem · Candidates converge to median. · Move voter distribution · Political line · Distribution · Candidate positions · Convergence · "Politics races to middle" · Med · 2wk · Political econ · 7/8/6/8/5/5/7/8/6/6

**73. The Tragedy Lake** · Tragedy of commons · Individual incentive depletes shared resource · Fish/harvest *(many exist — twist: partial cooperation)* · Lake · Harvest rate · Stock · Collapse · "Rational = ruin" · Low · 2wk · Environment · 8/8/7/8/7/6/8/9/6/7

**74. The Parrondo Casino** · Parrondo's paradox · Two losing games combine to win. · Alternate game A/B · Casino · Switch pattern · Bankroll · Winning combo · "Two wrongs make a right" · Med · 3wk · Probability · 8/9/10/9/6/8/9/6/6/10

**75. The Hawk Dove Meadow** · Hawk-dove game · Aggression polymorphism equilibrium. · Population mix · Meadow · Hawk fraction · Stable mix · Evolutionary stable · "Society needs doves and hawks" · Med · 2wk · Evolution · 8/8/7/9/6/6/8/8/7/7

---

## Nature, Evolution & Physics (76–90)

**76. The Red Queen Treadmill** · Red Queen hypothesis · Running to stay in place in coevolution. · Host-parasite arms race · Treadmill · Mutation rate · Fitness · Zero-sum evolution · "Progress is mandatory" · Med · 3wk · Biology · 8/8/8/9/6/6/9/7/7/8

**77. The Handicap Peacock Run** · Zahavi handicap principle · Costly traits prove fitness. · Tail weight vs survival · Savanna · Tail cost · Predator catch · Honest signal · "Burden as proof" · Med · 3wk · Evolution · 9/8/7/9/5/6/7/8/8/7

**78. The Lotka-Volterra Loop** · Predator-prey cycles · Foxes and rabbits oscillate. · Parameters · Phase plane · Growth rates · Cycles · Limit cycles · "Predator creates prey creates predator" · Med · 2wk · Ecology · 9/8/8/9/6/6/9/8/8/8

**79. The Trophic Cascade Kelp** · Trophic cascades · Removing apex predator reshapes ecosystem. · Remove otters · Kelp forest · Species toggles · Kelp collapse · Top-down control · "Wolves shape rivers" · Med · 3wk · Ecology · 9/8/9/9/8/7/7/8/9/9

**80. The Sandpile Avalanche** · Self-organized criticality · Systems naturally reach critical state. · Drop grains · Sandpile · Drop rate · Power-law avalanches · Criticality · "One grain, big slide" · Med · 3wk · Complex systems · 9/8/9/9/6/7/9/8/8/9

**81. The Maxwell's Demon Box** · Maxwell's demon · Sorting appears to violate entropy. · Demon gates molecules · Two chambers · Sorting · Entropy accounting · Resolution via info · "Information has thermodynamic cost" · High · 4wk · Thermodynamics · 8/8/9/10/6/7/7/6/7/9

**82. The Double Well Tunnel** · Bistability · Small push crosses barrier between equilibria. · Ball in double well · Potential curve · Push strength · State flip · Tipping · "Stable until it isn't" · Med · 2wk · Climate, psych · 9/8/8/9/7/6/8/8/8/8

**83. The Stochastic Resonance Whisper** · Stochastic resonance · Noise helps detect weak signals. · Add noise to threshold · Signal wave · Noise level · Detection · Noise helps · "More noise = clearer signal" · Med · 3wk · Neuroscience · 8/8/10/9/5/6/7/6/6/10

**84. The Fermi Silence** · Fermi paradox · Great filters in Drake equation. · Toggle filter probabilities · Galaxy · Filter sliders · Expected civilizations · Great silence · "Where is everybody?" · Med · 3wk · Astronomy · 9/7/8/8/8/8/8/7/9/8

**85. The Critical Mass Reactor** · Nuclear criticality · Chain reaction threshold. · Control rod depth · Reactor · Enrichment · Reaction rate · Exponential · "Subcritical → supercritical" · Med · 3wk · Physics · 9/8/9/9/7/7/8/7/7/9

**86. The Resonance Bridge** · Mechanical resonance · Matching frequency amplifies vibration. · Drive bridge at frequency · Bridge · Frequency · Amplitude · Tacoma intuition · "Right rhythm destroys" · Med · 2wk · Physics · 9/8/8/8/7/7/7/8/8/8

**87. The Diffusion Ink** · Diffusion · Random walk spreads concentration. · Drop ink · Water · Temperature · Spread · Normal emergence · "Random motion, predictable spread" · Low · 2wk · Physics, chem · 9/8/6/8/4/5/8/9/9/6

**88. The Muller's Ratchet** · Muller's ratchet · Asexual populations accumulate deletions. · Toggle recombination · Genome · Mutation · Fitness · Irreversible decline · "Sex shuffles out bad luck" · Med · 3wk · Evolution · 7/7/8/9/5/5/7/7/5/8

**89. The Fisher Runaway Ribbon** · Fisherian runaway · Preference and trait co-evolve to extremes. · Peahen preference · Birds · Preference strength · Tail length · Runaway · "Beauty spirals absurd" · Med · 3wk · Evolution · 9/8/8/9/5/7/8/7/8/8

**90. The Island Biogeography** · MacArthur-Wilson · Species richness vs island size/distance. · Create islands · Archipelago · Size, distance · Species count · Equilibrium · "Isolation shapes diversity" · Med · 3wk · Ecology · 9/8/7/9/6/6/8/8/8/7

---

## Time, Money & Cities (91–105)

**91. The Compound Cliff** · Exponential growth · Linear intuition fails on compound growth. · Compare linear vs exponential savings · Graph · Time · Wealth gap · Exponential divergence · "Later is too late" · Low · 2wk · Finance literacy · 8/8/8/9/7/8/8/9/6/8

**92. The Jevons Fireplace** · Jevons paradox · Efficiency increases consumption. · Improve bulb efficiency · Home · Efficiency · Energy use · Rebound · "Efficient = more use" · Med · 2wk · Climate · 8/8/8/9/7/7/7/8/6/8

**93. The Hysteresis Thermostat** · Hysteresis · Path-dependent switching thresholds. · Heat/cool room · Thermostat · On/off offsets · State history · Memory in systems · "Where you were matters" · Med · 2wk · Systems · 8/8/7/8/5/5/8/8/6/7

**94. The QWERTY Lock** · Path dependence / lock-in · Inferior standard persists. · Network adoption curve · Keyboard · Early adopters · Standard lock · Lock-in · "Better lost to early" · Med · 2wk · Technology · 7/7/7/8/6/6/7/8/5/7

**95. The Comparative Advantage Port** · Ricardo · Trade benefits even when one side is better at everything. · Two countries, two goods · Port · Productivity · Trade gains · Mutual benefit · "Worse at everything still wins trade" · Med · 3wk · Economics · 8/7/7/9/5/5/7/7/6/8

**96. The Gini City** · Wealth inequality dynamics · Small transaction biases amplify Gini. · Random trading with bias · City · Bias ε · Gini coefficient · Inequality · "Neutral rules, unequal outcomes" · Med · 3wk · Inequality · 9/8/8/9/8/7/9/8/6/8

**97. The Little's Law Queue** · Little's law · L = λW in steady state. · Adjust arrival/service · Queue · Rates · Length, wait · Invariant · "Three variables, one equation" · Med · 2wk · Operations · 7/8/7/8/4/4/8/8/5/7

**98. The Kingman Queue** · Kingman's formula · Waiting time explodes near utilization=1. · Utilization slider · Service desk · Utilization · Wait time · Queue blowup · "Almost full = chaos" · Med · 2wk · Healthcare, ops · 8/9/8/9/6/6/8/7/5/9

**99. The Jane Jacobs Corner** · Jacobs four generators · Diversity needs mixed use, short blocks, old+new buildings, density. · Build city blocks · Neighborhood · Block parameters · Vitality · Emergent street life · "Four rules for life" · High · 5wk · Urbanism · 10/8/7/9/8/7/7/6/9/8

**100. The Braess Commute** · *(see 69 — variant: bike lanes)* · Urban mobility · Med · — · —

**101. The Rent Control Building** · Price controls · Short-term help, long-term shortage. · Cap rent · Apartment · Cap level · Supply, quality · Unintended shortage · "Help that hurts" · Med · 3wk · Housing policy · 8/7/7/8/7/6/7/7/6/7

**102. The Broken Window Shop** · Broken window fallacy · Destruction doesn't create wealth. · Break windows; track wealth · Street · Break rate · GDP vs wealth · Fallacy visible · "Repair isn't growth" · Low · 2wk · Economics · 7/8/7/8/6/6/7/9/6/7

**103. The Moravec Mountain** · Moravec's paradox · Easy for humans is hard for AI and vice versa. · Compare task difficulty human vs machine · Mountain · Task type · Difficulty gap · Inverse difficulty · "Walking is harder than chess" · Med · 3wk · AI literacy · 8/7/8/9/7/8/7/8/6/8

**104. The Alignment Paperclip** · Instrumental convergence · Misaligned goals consume resources. · Give AI goal; watch · Factory · Goal spec · Paperclips · Resource drain · "Perfect obedience, disaster" · Med · 4wk · AI safety · 8/8/8/9/8/8/6/7/6/8

**105. The Overfit Mirror** · Bias-variance · Model memorizes noise. · Train on points · Curve · Polynomial degree · Fit quality · Overfit · "Perfect on data, fails on world" · Med · 3wk · ML literacy · 8/9/8/9/5/6/8/7/6/8

---

## Perception, Logic & Misc (106–120)

**106. The Gestalt Spin** · Gestalt principles · Whole perception ≠ parts sum. · Toggle grouping cues · Shapes · Cue type · Perceived objects · Emergent forms · "Context creates object" · Low · 2wk · Design · 9/9/6/7/4/6/7/9/8/6

**107. The Color Opponent Wheel** · Opponent process · Red-green, blue-yellow channels. · Afterimage · Color wheel · Stare/adapt · Afterimage · Neural opponency · "No such thing as reddish-green" · Low · 1wk · Vision · 9/10/7/7/5/6/6/9/8/7

**108. The Blind Spot Face** · Blind spot · Brain fills missing retina data. · Vanishing dot trick · Face · Fixation · Fill-in · Completion · "You don't see the hole" · Low · 1wk · Neuroscience · 9/10/8/7/5/7/5/10/6/7

**109. The Zipf Word Mountain** · Zipf's law · Word frequency follows power law. · Build corpus · Word hill · Word rank · Frequency · Power law · "Few words dominate" · Low · 2wk · Linguistics · 8/7/7/8/4/5/8/9/7/6

**110. The Sapir-Whorf Lens** · Linguistic relativity (weak) · Language nudges categorization. · Color naming splits perception · Color grid · Language · Boundary · Category shift · "Words carve perception" · Med · 3wk · Linguistics · 8/8/6/7/6/5/6/7/7/6

**111. The Zeno Arrow** · Zeno paradox · Motion as infinite steps — resolved by calculus intuition. · Halve distances · Arrow · Steps · Limit · Convergence · "Infinite steps, finite time" · Med · 3wk · Math · 7/8/7/8/4/4/7/6/6/7

**112. The Sleeping Beauty Coins** · Sleeping beauty problem · Probability and self-locating belief. · Wake/amnesia rounds · Bedroom · Coin · Beauty's credence · Thirding vs halving · "Beauty disagrees with you" · High · 4wk · Philosophy · 6/8/9/8/5/6/6/5/5/8

**113. The Trolley Yarn** · Trolley problem variants · Fat man, loop, footbridge — intuitions conflict. · Branching scenarios · Tracks · Lever · Death count · Moral inconsistency · "Your ethics contradict" · Med · 2wk · Ethics · 7/8/7/8/9/7/5/8/5/7

**114. The Hanabi Signal** · Common knowledge in cooperation · Partial info requires signaling conventions. · Cooperative card game sim · Table · Clues · Success rate · Convention emergence · "We know they know" · High · 5wk · Game theory · 8/9/8/8/7/6/9/6/7/8

**115. The CAP Triangle** · CAP theorem · Pick 2 of consistency, availability, partition tolerance. · Simulate partition · Distributed nodes · Failure mode · Behavior · Tradeoff · "Can't have all three" · Med · 3wk · Distributed systems · 7/8/7/9/4/5/7/7/5/7

**116. The Byzantine Generals Camp** · Byzantine fault tolerance · Agreement with traitors. · Toggle traitors · Camp · Traitor count · Consensus · Threshold · "Trust requires numbers" · High · 4wk · CS · 7/8/7/9/5/5/6/6/5/7

**117. The Ashby Variety Dial** · Law of requisite variety · Controller must match system complexity. · Thermostat vs complex house · Control panel · Variety · Stability · Control failure · "Simple control, complex chaos" · Med · 3wk · Cybernetics · 7/8/7/9/5/5/7/7/6/8

**118. The Wason Card Pub** · Wason selection task · Most fail logic unless social context. · Choose cards to flip · Pub · Context frame · Success rate · Facilitation · "Logic is social" · Low · 2wk · Logic · 7/9/8/8/5/6/7/8/5/8

**119. The Streetlight Search** · Streetlight effect · Search where light is, not where keys are. · Place light and keys · Parking lot · Light position · Search time · Bias · "Easy to measure ≠ important" · Low · 2wk · Research methods · 8/8/7/8/6/7/7/9/6/7

**120. The Kruskal Card Trick** · Kruskal count · Mathematical force in card ordering. · Follow deal procedure · Cards · Deal · Predicted stop · Magic from math · "You had no choice" · Low · 2wk · Recreational math · 8/8/9/7/6/8/9/8/6/8

---

# Phase 6: Concept Clusters

| Category | Concepts (IDs) |
|----------|----------------|
| **Society** | 1, 3, 4, 7, 8, 11, 13, 14, 15, 49, 50 |
| **Mind** | 16–30 |
| **Probability** | 31–45, 74 |
| **Networks** | 46–60, 10, 51 |
| **Cooperation & Conflict** | 61–75, 2 |
| **Nature & Evolution** | 76–80, 88–90 |
| **Physics & Energy** | 81–87, 85–86 |
| **Time & Path Dependence** | 91–94, 14 |
| **Money & Economics** | 91–96, 101–102, 42–43 |
| **Cities & Infrastructure** | 69, 99, 97–98, 46 |
| **Information & Communication** | 55–58, 59–60 |
| **AI & Computation** | 103–105, 115–116 |
| **Perception & Beauty** | 106–108, 25 |
| **Logic & Paradox** | 45, 67–68, 111–113, 118 |
| **Space & Cosmos** | 84 |
| **Ethics & Institutions** | 2, 5, 113 |
| **Education & Metrics** | 7, 8, 12 |
| **Health & Medicine** | 20, 36, 98 |

---

# Phase 7: Top 20 — Full One-Page Concepts

---

## 1. THE PETRI MULTIPLIER
**Tagline:** *Equal meanness. Unequal harm.*

**Theory:** The Petrie multiplier (2013) — in mixed groups, harassment experienced by minorities scales with group size asymmetry even when per-capita rates are identical.

**Audience:** Tech workers, conference organizers, DEI skeptics who think "we treat everyone the same."

**Learning objective:** Understand why neutral-seeming environments produce asymmetric harm without assuming different intent.

**Interaction model:** Isometric conference floor. Adjust gender/race ratio (default 80/20). Set harassment probability *equal* for all agents. Run simulation. Watch counter tick: minority members receive disproportionate total harassment. Toggle "reporting threshold" to show visibility bias.

**Animation:** Speech-bubble micro-aggressions as tiny sparks; heat map of accumulated harm; multiplier graph as ratio changes.

**Progressive reveal:** (1) Equal rates — seems fair. (2) Run — minority counter races ahead. (3) Reveal formula: majority→minority interactions dominate. (4) Add Petrie multiplier math minimally. (5) Sandbox: your workplace ratio.

**Surprise moments:** Setting harassment to *zero* for majority still leaves minority experiencing cross-group dynamics; "fixing individuals" slider does nothing without structural ratio change.

**Sound:** Subtle crowd murmur; sharp ping on each incident; cumulative drum beat accelerating.

**Art direction:** Clean flat vectors like Polygons; dots with minimal identity markers; no villain faces — system blame.

**References:** Petrie 2013; Polygons for tone; *The Memo* pipeline discussions.

**Differentiation:** Not "bias training" — pure combinatorics of interaction pairs.

**Extensions:** Add power asymmetry (manager/report); intersectionality (two minority axes); conference scheduling optimization game.

---

## 2. ERGODICITY STREET
**Tagline:** *The average person doesn't exist.*

**Theory:** Ole Peters' ergodicity economics — ensemble averages mislead when processes are non-ergodic; time-average ≠ ensemble-average for individuals.

**Audience:** Anyone offered "expected return" investments, crypto leverage, gambling ads.

**Learning objective:** Feel why 100 people doing a bet ≠ 1 person doing it 100 times.

**Interaction model:** Split screen: LEFT = 100 parallel players one coin flip each. RIGHT = you, sequential flips, wealth compounds. Same +50%/-40% " favorable" bet. Left shows average wealth up; right shows you going bust.

**Animation:** Wealth paths as glowing trails; ensemble average line vs your single path.

**Progressive reveal:** (1) Bet looks good (positive expected value). (2) Ensemble wins. (3) Your path hits zero. (4) Define ergodicity in one sentence. (5) Kelly fraction slider saves you.

**Surprise:** Positive EV bet *guarantees* your ruin over time.

**Sound:** Coin clinks; bankruptcy thud; crowd cheer on left only.

**Art direction:** Bauhaus finance — stark split, red ruin path, blue ensemble cloud.

**References:** Peters *Ergodicity Economics*; Nassim Taleb tail risk; Kelly criterion explainer.

**Differentiation:** Most finance explainers show averages; this shows *you* specifically.

**Extensions:** Real historical asset returns; pension fund governance; insurance.

---

## 3. THE PERCOLATION CITY
**Tagline:** *One more closed road killed the hospital.*

**Theory:** Percolation threshold — random node removal; giant connected component collapses at critical probability p_c.

**Audience:** Urban planners, pandemic policy, infrastructure nerds.

**Learning objective:** Intuit phase transitions in connectivity; critical thresholds aren't gradual.

**Interaction model:** Grid city: homes, hospital, fire station. Randomly close roads (or block buildings). Live stats: reachable hospital %, fire coverage. At p_c, services suddenly fail for most.

**Animation:** Water-flow metaphor for connectivity; hospital pulse dims; avalanche when threshold crossed.

**Progressive reveal:** (1) Remove 10% — fine. (2) 30% — still OK. (3) 38% — collapse. (4) Show percolation math briefly. (5) Targeted vs random removal comparison.

**Surprise:** Removing *random* roads is worse than removing *least-used* — Braess/percolation combo beat.

**Sound:** Traffic hum → silence; heartbeat flatline at collapse.

**Art direction:** Mini SimCity; warm daytime; cold grey when disconnected.

**References:** Schelling (adjacent); Braess paradox (#69); COVID hospital capacity maps.

**Differentiation:** Percolation rarely gets cute UI; connects abstract math to 911 response time.

**Extensions:** Vaccination as bond percolation; power grid; misinformation percolation in networks.

---

## 4. THE MAJORITY ILLUSION
**Tagline:** *Everyone you see agrees. That's the bug.*

**Theory:** Majority illusion — in heterogeneous networks, local neighborhoods oversample high-degree nodes, distorting perceived popularity.

**Audience:** Social media users, parents, policymakers on "everyone believes X."

**Learning objective:** See how graph structure creates false consensus without censorship.

**Interaction model:** Build social graph (clusters + bridges). Color nodes by opinion (40% red, 60% blue). Show each node's *perceived* neighborhood majority vs global reality. Rewire edges — same global %, different local illusions.

**Animation:** Each avatar looks around; thought bubble shows "80% agree with me!"; global counter shows 40%.

**Progressive reveal:** (1) Global truth. (2) Each person's view. (3) Add influencer hubs — illusion intensifies. (4) Remove bridges — illusions diverge further.

**Surprise:** Lower global minority can appear locally dominant.

**Sound:** Echo chamber reverb; whispers sync.

**Art direction:** WBWWB-adjacent camera metaphor but graph-native; pastel nodes.

**References:** Lerman et al. 2016; Wisdom/Madness of Crowds (adjacent — don't duplicate).

**Differentiation:** Focuses on *perception* illusion, not diffusion speed.

**Extensions:** Algorithmic feed that optimizes engagement; intervention: follow one random low-degree node.

---

## 5. THE GOODHART SCHOOL
**Tagline:** *When the test became the target, learning died.*

**Theory:** Goodhart's law / Campbell's law — metric optimization decouples from goal.

**Audience:** Teachers, managers, anyone with KPIs.

**Learning objective:** Understand why metrics rot when incentivized; distinguish proxy from goal.

**Interaction model:** School sim: real literacy (hidden) vs test score (visible). Teacher AI allocates time: teach vs drill. Principal sets bonus tied to scores. Watch literacy vs scores diverge.

**Animation:** Two diverging lines; classroom scenes cross-fade drill vs exploration.

**Progressive reveal:** (1) No incentive — aligned. (2) Tie pay to scores — divergence. (3) Publish rankings — corruption. (4) Campbell quote. (5) Sandbox: design your metric.

**Surprise:** Scores *rise* while literacy *falls*.

**Sound:** Pencil scratch vs robotic chant; alarm when gap exceeds threshold.

**Art direction:** Paper schoolhouse; satirical but warm; Polygons innocence→horror arc.

**References:** Goodhart 1975; Campbell 1979; Soviet nail factory joke.

**Differentiation:** Cobra effect (#6) is one-shot; this shows gradual rot.

**Extensions:** Healthcare metrics; police stats; academic citations.

---

## 6. THE SIMPSON'S PARADOX UNIVERSITY
**Tagline:** *Every department improved. The university got worse.*

**Theory:** Simpson's paradox — trend reversal in aggregated vs stratified data.

**Audience:** Data journalists, medical readers, anyone who trusts "overall stats."

**Learning objective:** Always ask "compared within what group?"

**Interaction model:** Admissions sim: two departments, two genders. Adjust acceptance rates per dept (both improve for both groups). Aggregate bar chart reverses — overall rate drops for a group.

**Animation:** Bars animate; stratification toggle flips narrative.

**Progressive reveal:** (1) Overall chart — discrimination? (2) Split by dept — opposite. (3) User adjusts weights. (4) Berkeley 1973 story.

**Surprise:** You *caused* the paradox with your slider.

**Sound:** Gavel; record scratch on reveal.

**Art direction:** Clean infographic; Distill.pub clarity.

**References:** Bickel et al. 1975; Pearl causal diagrams (extension).

**Differentiation:** Interactive weight manipulation vs static textbook bars.

**Extensions:** COVID mortality by age; batting averages.

---

## 7. THE COMPLEX CONTAGION PROTEST
**Tagline:** *One person kneeling isn't a movement. Ten might be.*

**Theory:** Complex contagion — behavior requires multiple exposures (threshold ≥2 in social contact model).

**Audience:** Activists, marketers, public health.

**Learning objective:** Why some ideas need repeated social proof; difference from viral disease spread.

**Interaction model:** Grid agents. Simple contagion (1 exposure) vs complex (2+ exposures). Start with one activist. Compare spread curves. Add counter-protest with different threshold.

**Animation:** Ripple vs fire — simple spreads fast; complex needs clusters.

**Progressive reveal:** (1) Simple — instant wave. (2) Complex — stalls then explodes. (3) Centola experiments. (4) Design optimal seeding.

**Surprise:** More connected network *slows* complex contagion initially.

**Sound:** Single voice → chorus.

**Art direction:** Silhouette protest; warm gold when threshold met.

**References:** Centola & Macy 2007; simple vs complex contagion literature.

**Differentiation:** Wisdom/Madness covers topology; this covers threshold type.

**Extensions:** Vaccine hesitancy; fashion trends.

---

## 8. THE BASE RATE HOSPITAL
**Tagline:** *The test said positive. You're probably fine.*

**Theory:** Base rate neglect / Bayes — P(disease|+) depends on prevalence.

**Audience:** Patients, journalists covering screening, COVID era survivors of panic.

**Learning objective:** Intuitive Bayes without formula first; formula after felt experience.

**Interaction model:** Adjust disease prevalence (1% vs 50%). Fixed test sensitivity/specificity. Run 1000 patients — tree diagram fills. Highlight false positives swamp true positives at low prevalence.

**Animation:** Patient icons flow through test; green/red; Bayes tree grows live.

**Progressive reveal:** (1) 99% accurate test! (2) 1% prevalence — mostly false positives. (3) Show Bayes. (4) Mammography / COVID rapid test real params.

**Surprise:** "Accurate" test is wrong most of the time when positive at low base rate.

**Sound:** Heartbeat; ding for true pos; wrong buzzer for false (more frequent).

**Art direction:** Clean medical; empathetic not clinical cold.

**References:** Gigerenzer natural frequencies; *Factfulness* health chapter.

**Differentiation:** Many static Bayes — this makes prevalence the hero slider.

**Extensions:** Prosecutor's fallacy (#36) as sequel chapter.

---

## 9. THE BRAESS ROADS
**Tagline:** *We added a highway. Traffic got worse.*

**Theory:** Braess paradox — new capacity increases travel time at Nash equilibrium.

**Audience:** Drivers, urbanists, network engineers.

**Learning objective:** Equilibrium ≠ optimum; selfish routing creates paradox.

**Interaction model:** Wardrop equilibrium sim. 4 nodes classic network. Add Braess link — watch travel time increase. Toggle "central planner optimum" vs "selfish drivers."

**Animation:** Cars as particles; road thickens; speed drops counter-intuitively.

**Progressive reveal:** (1) Slow network. (2) Add shortcut — worse! (3) Remove it — better. (4) Price of anarchy.

**Surprise:** Individually rational choices harm everyone.

**Sound:** Honking increases with new road.

**Art direction:** Mini highway diagram; SimCity aesthetic.

**References:** Braess 1968; Roughgarden price of anarchy.

**Differentiation:** Interactive add/remove link vs static diagram.

**Extensions:** Ride-share surge; server load balancing.

---

## 10. THE PARRONDO CASINO
**Tagline:** *Two losing games. One winning strategy.*

**Theory:** Parrondo's paradox — alternating losing games can produce winning expected value.

**Audience:** Probability lovers, anti-gambling education, complexity fans.

**Learning objective:** Non-linear combination breaks intuition; hope for combining weak interventions.

**Interaction model:** Game A and B both lose alone. Toggle alternating pattern AABBAB… Bankroll over time. Heatmap of win probability by pattern.

**Animation:** Slot-machine emoji; bankroll cliff vs climb.

**Progressive reveal:** (1) A loses. (2) B loses. (3) Alternate — wins. (4) Biology: molecular motors use this.

**Surprise:** Losing + losing = winning.

**Sound:** Casino; sad trombone solo; jazz combo win.

**Art direction:** Neon casino; playful distrust of casino itself.

**References:** Parrondo & Dinis; Abbott & Frey.

**Differentiation:** Almost no mainstream interactives exist.

**Extensions:** Policy: two harmful policies alternating; ecology.

---

## 11. THE STANDING OVATION
**Tagline:** *Would you stand? Depends who stood first.*

**Theory:** Granovetter threshold model — heterogeneous thresholds produce cascades.

**Audience:** Social influence, marketing, revolution mechanics.

**Learning objective:** Critical mass; sensitivity to early movers and threshold distribution.

**Interaction model:** Auditorium. Each seat has hidden threshold (% others standing needed). Click individuals to stand early. Replay with different threshold distributions.

**Animation:** Domino wave; failed cascade fizzles.

**Progressive reveal:** (1) You stand alone — embarrassment. (2) Seed three — cascade. (3) Threshold histogram matters.

**Surprise:** Same average threshold, different variance → opposite outcomes.

**Sound:** Sparse clap → roar; awkward silence.

**Art direction:** Bird's-eye theater; Polygons-like dots.

**References:** Granovetter 1978; Watts threshold models.

**Differentiation:** Simpler than full agent model; pure cascade intuition.

**Extensions:** Misinformation cascades; bank runs.

---

## 12. THE PLURALISTIC IGNORANCE POOL
**Tagline:** *Nobody wanted to. Everyone did.*

**Theory:** Pluralistic ignorance — private rejection, public conformity.

**Audience:** Teens, workplace culture, hazing prevention.

**Learning objective:** How public signals hide private preferences; breaking requires coordination.

**Interaction model:** Pool party: everyone privately prefers not to jump. Public expression slider. Show gap between private average and public behavior. "First honest person" button can shift equilibrium.

**Animation:** Thought bubbles vs body actions diverge.

**Progressive reveal:** (1) Everyone jumps — looks unanimous. (2) Reveal private prefs. (3) One honest voice. (4) New equilibrium.

**Surprise:** 90% privately opposed, 90% publicly conform.

**Sound:** Splash; internal monologue whispers.

**Art direction:** Summer pool; expressive faces.

**References:** Prentice & Miller; no-alcohol college party studies.

**Differentiation:** Emotional social sim vs abstract threshold.

**Extensions:** Workplace overtime culture.

---

## 13. THE SANDPILE AVALANCHE
**Tagline:** *One grain. Sometimes one mountain falls.*

**Theory:** Self-organized criticality (Bak-Tang-Wiesenfeld).

**Audience:** Complexity, finance (fat tails), earthquake intuition.

**Learning objective:** Systems self-tune to criticality; event sizes follow power law.

**Interaction model:** Drop grains on grid. Avalanche sizes logged. Histogram emerges power law. Toggle slow drive vs fast — critical state maintains.

**Animation:** Beautiful pixel sand; avalanche shimmer.

**Progressive reveal:** (1) Drop — small slides. (2) Rare huge. (3) Histogram. (4) Connect to earthquakes/markets.

**Surprise:** No tuning parameter — system finds critical alone.

**Sound:** Grain tick; rumble scale with size.

**Art direction:** Zen garden meets cellular automata.

**References:** Bak et al. 1987; Mandelbrot.

**Differentiation:** Visual beauty + deep theory; rare combo.

**Extensions:** Forest fire model link; financial crash sizes.

---

## 14. THE COMMONS GARDEN (OSTROM)
**Tagline:** *Eight rules. Or the lake dies.*

**Theory:** Elinor Ostrom's design principles for successful commons governance.

**Audience:** Environmental policy, community organizers, Hardin skeptics.

**Learning objective:** Commons *can* work; specific institutional features matter.

**Interaction model:** Fishing lake. Toggle Ostrom principles (boundary, rules, monitoring, sanctions, conflict resolution, recognition, nested enterprise). Hardin baseline collapses; full Ostrom sustains.

**Animation:** Lake color; fish count; community trust meter.

**Progressive reveal:** (1) Tragedy default. (2) Add one principle — still fails. (3) Stack principles — recovery. (4) Real communities (Nepal, Spain).

**Surprise:** Partial governance worse than none (confusion).

**Sound:** Water lap; community bell.

**Art direction:** Folk art landscape; hopeful unlike pure tragedy demos.

**References:** Ostrom 1990; Nobel lecture.

**Differentiation:** Positive actionable design vs despair-only commons sims.

**Extensions:** Climate treaty design; open source maintenance.

---

## 15. THE COBRA FARM
**Tagline:** *The bounty worked. That's the problem.*

**Theory:** Perverse incentives / Cobra effect.

**Audience:** Policy makers, metric designers.

**Learning objective:** Incentives reshape behavior in unanticipated ways.

**Interaction model:** Colonial India cobra metaphor. Set bounty per tail. Farmers breed cobras. Government ends bounty — cobras released. Snake population explodes.

**Animation:** Cartoon cobras multiply; bounty counter.

**Progressive reveal:** (1) Problem. (2) Bounty. (3) Gaming. (4) Worse than start.

**Surprise:** Good-faith solution maximizes problem.

**Sound:** Hiss; cash register.

**Art direction:** Satirical colonial poster aesthetic; sharp not preachy.

**References:** Historical anecdote (possibly apocryphal — note that); Goodhart link.

**Differentiation:** Faster emotional hit than Goodhart School; pairs as diptych.

**Extensions:** Wells Fargo accounts scandal sim.

---

## 16. THE REGRESSION SPORTS ROOKIE
**Tagline:** *They were a flash in the pan. They were just lucky.*

**Theory:** Regression to the mean.

**Audience:** Sports fans, investors chasing last year's winners, managers.

**Learning objective:** Extreme performance partially luck; expect partial revert without "decline."

**Interaction model:** Rookie season performance = skill + luck slider. Next year predict. Show league-wide scatter: extreme rookies mostly regress.

**Animation:** Scatter plot live; rookie dot falls toward mean.

**Progressive reveal:** (1) Hero rookie. (2) Predict sophomore slump. (3) Skill unchanged — still "slump." (4) Sports / fund manager examples.

**Surprise:** Best rookies almost always "disappoint" — math not morality.

**Sound:** Crowd roar → confused murmur.

**Art direction:** Sports newspaper infographic.

**References:** Kahneman on sports; Tversky "hot hand" adjacent.

**Differentiation:** User generates luck; not passive chart.

**Extensions:** CEO of the year curse; mutual fund mean reversion.

---

## 17. THE MAXWELL'S DEMON BOX
**Tagline:** *He sorted hot from cold. Entropy didn't like that.*

**Theory:** Maxwell's demon resolved by information thermodynamics (Landauer).

**Audience:** Physics-curious; entropy intuition for information age.

**Learning objective:** Information erasure has energy cost; entropy and knowledge linked.

**Interaction model:** Two-chamber gas. Demon opens door for fast molecules only. Temperature difference grows — apparent violation. Add "memory erasure cost" — total entropy conserved.

**Animation:** Molecules as dots; demon as cute sprite; battery drains on erase.

**Progressive reveal:** (1) Demon wins. (2) Thermodynamics "broken"? (3) Landauer cost. (4) Resolved.

**Surprise:** Thinking has thermodynamic price.

**Sound:** Molecular hiss; erase static.

**Art direction:** Victorian steampunk + particle sim.

**References:** Landauer 1961; Bennett 1982.

**Differentiation:** Demon as playable character; rare interactivity.

**Extensions:** Quantum Maxwell's demon; computation energy limits.

---

## 18. THE DEFFUANT POLARIZATION LINE
**Tagline:** *Talk to people slightly unlike you. Ignore the rest.*

**Theory:** Deffuant bounded confidence model — agents converge if opinions within ε, repel otherwise.

**Audience:** Political discourse, filter bubble fighters.

**Learning objective:** Tolerance radius determines cluster count; small ε → polarization without bad faith.

**Interaction model:** Opinion line 0–1. Agents random pairs. Adjust ε. Watch 1 cluster → 2 → many. Seed extremists.

**Animation:** Color gradient merging/splitting.

**Progressive reveal:** (1) High ε — consensus. (2) Lower — camps. (3) Extremists pull edges. (4) Compare to US Congress ε estimate sandbox.

**Surprise:** Good-faith conversation with bounded trust still polarizes.

**Sound:** Merge tone vs split dissonance.

**Art direction:** Minimal gradient line; elegant math aesthetic.

**References:** Deffuant et al. 2000; Hegselmann-Krause compare mode.

**Differentiation:** Continuous opinion vs binary network models.

**Extensions:** Algorithmic feed that shrinks ε artificially.

---

## 19. THE JANE JACOBS CORNER
**Tagline:** *Four rules for a neighborhood that breathes.*

**Theory:** Jane Jacobs' four conditions for urban vitality (mixed primary uses, short blocks, old buildings, density).

**Audience:** Urbanists, NIMBY/YIMBY discourse participants.

**Learning objective:** Why some blocks feel alive; systemic urban design.

**Interaction model:** Top-down block builder. Toggle each Jacobs condition. Pedestrian agents; street life meter; economic diversity index.

**Animation:** Day-night cycle; shop lights; foot traffic heat.

**Progressive reveal:** (1) Suburb — dead. (2) Add density alone — insufficient. (3) Stack conditions — emergence. (4) Compare Le Corbusier tower option.

**Surprise:** Old buildings slider unlocks cheap experimentation for small business.

**Sound:** Street jazz; cricket chirp in dead mode.

**Art direction:** Isometric pixel city; loving detail.

**References:** *Death and Life of Great American Cities*; Alexander *Pattern Language*.

**Differentiation:** Positive urbanism playable; most city games are traffic-only.

**Extensions:** Import real OSM neighborhood; score it.

---

## 20. THE NEWCOMB PREDICTOR
**Tagline:** *The box was predicted. Was your choice?*

**Theory:** Newcomb's problem — decision theory vs prediction paradox.

**Audience:** Philosophy curious; AI prediction ethics.

**Learning objective:** Feel tension between EDT vs CDT; understand why smart people disagree.

**Interaction model:** Play against predictor with stated accuracy. One-box vs two-box. Reveal predictor's method (simulation of your brain). Run tournament of strategies.

**Animation:** Mysterious box glow; predictor as oracle.

**Progressive reveal:** (1) Obvious two-box? (2) Predictor always right. (3) One-box wins historically. (4) CDT defense. (5) No resolution — sit with paradox.

**Surprise:** Causal reasoning and winning strategy diverge.

**Sound:** Mystical hum; cash reveal.

**Art direction:** Minimal mysticism; respectful not hokey.

**References:** Nozick; Aaronson on Newcomb and free will.

**Differentiation:** Genuine unresolved paradox as feature.

**Extensions:** AI that models you to sell; FDT primer.

---

# Phase 8: Novel Hybrid Concepts (Not Known to Exist)

These combine multiple theories into interactives with no major existing counterpart:

### H1. **Bayesian Therapy** (Bayes × Base Rate Neglect × Availability)
Update beliefs with evidence sliders; availability feed injects vivid but irrelevant data; watch posterior ignore base rate until forced natural-frequency mode. *Aha:* Same evidence, different framing → opposite medical decision.

### H2. **Memory Channel** (Information Theory × Forgetting Curve)
Send message through noisy channel with limited bandwidth; player must compress; spaced repetition gate controls error correction over days (accelerated). *Aha:* Memory is compression under constraint — forgetting is optimal not failure.

### H3. **Evolutionary Trust Ecology** (Evolution × Game Theory × Networks)
Spatial PD on graph; strategies evolve; adding mobility destroys cooperation; adding local reputation restores it. *Aha:* Trust isn't one game — it's game + topology + memory.

### H4. **Urban Percolation Equity** (Percolation × Schelling × Jane Jacobs)
Services only reach percolated cluster; segregation reduces percolation even with equal infrastructure spend. *Aha:* Integration is infrastructure — segregated cities literally disconnect from hospitals.

### H5. **The Metric Hydra** (Goodhart × Campbell × Cobra × Petrie)
Four-headed sim: fix one metric, another head bites. Player must manage system with only indirect levers. *Aha:* Metric governance is whack-a-mole unless you measure what you want, not proxy.

### H6. **Ergodic Inequality** (Ergodicity × Matthew Effect × Kelly)
Population of agents with multiplicative wealth; ensemble average rises while median path hits zero; taxation as ergodicity restorer. *Aha:* "The economy grew" can mean "most paths died."

### H7. **Contagion of Courage** (Complex Contagion × Pluralistic Ignorance × Standing Ovation)
Jumping requires seeing 2 others jump AND believing they want to — dual threshold. First honest actor needs ally. *Aha:* Bravery spreads differently than ideas.

### H8. **The Forecasting Market of Crowds** (Prediction markets × Dunning-Kruger × Information Cascades)
Traders with hidden skill; cascades override skilled minority; confidence-weighted aggregation beats both. *Aha:* Smart crowds need independence, not just headcount.

### H9. **Thermodynamic Attention** (Entropy × Maxwell's Demon × Social Media)
Demon curates feed to maximize engagement; entropy of beliefs decreases locally, heat waste globally (polarization). *Aha:* Attention economy is thermodynamics — sorting is never free.

### H10. **The Ostrom Network** (Ostrom × Network Science × Tragedy of Commons)
Commons on graph; monitoring only works with sufficient local clustering; global monitoring too expensive. *Aha:* Community size and network structure are governance tech.

### H11. **Paradox Traffic of Ideas** (Braess × Wisdom/Madness × Echo Chamber)
Add "shortcut" information link (aggregators); travel time to truth increases; remove shortcut — improves. *Aha:* More information highways can slow collective truth.

### H12. **Sleeping Beauty's Portfolio** (Sleeping Beauty × Ergodicity × Kelly)
Beauty wakes with amnesia; bet on coin; thirding vs halving strategies over repeated wakes; bankroll paths. *Aha:* Self-locating belief meets real money — philosophy becomes portfolio ruin.

### H13. **Stochastic Resonance Democracy** (Stochastic Resonance × Deffuant × Noise)
Tiny random noise helps agents find compromise basin; too much noise destroys; too little stuck polarized. *Aha:* Democracies may need *some* randomness (lottery committees, sortition).

### H14. **The Krebs Cycle of Outrage** (WBWWB feedback × Neurotic Neurons × Availability)
Photograph outrage → pathway thickens → faster trigger next time. Neurological layer on media loop. *Aha:* Outrage is learned physiology, not just culture war.

### H15. **Polya Culture Wars** (Polya Urn × Axelrod Culture × Deffuant)
Memetic colors reinforce on contact; polarization without enemies. *Aha:* Culture war from neutral reinforcement alone.

---

# Phase 9: Master Ranking (Top 30 by Rubric)

**Rubric dimensions (1–10):** Novelty (N), Depth (D), Timelessness (T), Educational value (Ev), Interaction quality (Iq), Beauty (B), Shareability (Sh), Memorability (M), Signature potential (Sg)

| Rank | Concept | N | D | T | Ev | Iq | B | Sh | M | Sg | **Total** |
|------|---------|---|---|---|----|----|---|----|----|----|-----------|
| 1 | Ergodicity Street | 9 | 10 | 10 | 10 | 9 | 7 | 9 | 10 | 10 | **94** |
| 2 | Petrie Multiplier | 9 | 9 | 9 | 10 | 8 | 7 | 10 | 9 | 9 | **90** |
| 3 | Percolation City | 8 | 9 | 10 | 9 | 10 | 9 | 8 | 9 | 9 | **89** |
| 4 | Majority Illusion | 8 | 8 | 9 | 9 | 9 | 8 | 10 | 9 | 9 | **87** |
| 5 | Parrondo Casino | 10 | 8 | 9 | 9 | 9 | 7 | 9 | 9 | 8 | **86** |
| 6 | Base Rate Hospital | 6 | 9 | 10 | 10 | 9 | 7 | 8 | 9 | 8 | **84** |
| 7 | Braess Roads | 7 | 9 | 10 | 9 | 9 | 7 | 8 | 8 | 8 | **83** |
| 8 | Goodhart School | 7 | 9 | 10 | 10 | 8 | 7 | 8 | 9 | 8 | **83** |
| 9 | Simpson's University | 6 | 9 | 10 | 10 | 8 | 7 | 7 | 8 | 7 | **80** |
| 10 | Sandpile Avalanche | 7 | 10 | 10 | 8 | 9 | 10 | 7 | 9 | 8 | **86** |
| 11 | Commons Garden (Ostrom) | 8 | 9 | 10 | 10 | 8 | 8 | 7 | 9 | 8 | **85** |
| 12 | Complex Contagion Protest | 7 | 8 | 9 | 9 | 9 | 8 | 8 | 8 | 8 | **82** |
| 13 | Pluralistic Ignorance Pool | 8 | 8 | 9 | 9 | 8 | 8 | 9 | 9 | 8 | **84** |
| 14 | Maxwell's Demon Box | 8 | 10 | 10 | 9 | 8 | 9 | 6 | 9 | 8 | **85** |
| 15 | Jane Jacobs Corner | 9 | 8 | 10 | 9 | 8 | 10 | 7 | 8 | 8 | **85** |
| 16 | Standing Ovation | 6 | 8 | 9 | 8 | 9 | 7 | 8 | 8 | 7 | **78** |
| 17 | Cobra Farm | 7 | 7 | 9 | 8 | 8 | 8 | 9 | 8 | 7 | **79** |
| 18 | Deffuant Polarization | 7 | 8 | 9 | 9 | 9 | 8 | 7 | 8 | 7 | **80** |
| 19 | Newcomb Predictor | 9 | 9 | 10 | 8 | 7 | 7 | 7 | 9 | 8 | **82** |
| 20 | Regression Sports | 5 | 8 | 10 | 9 | 8 | 6 | 7 | 8 | 6 | **75** |
| 21 | H4 Urban Percolation Equity | 10 | 9 | 10 | 10 | 8 | 8 | 9 | 9 | 9 | **90** |
| 22 | H6 Ergodic Inequality | 10 | 10 | 10 | 10 | 8 | 7 | 8 | 10 | 9 | **90** |
| 23 | H1 Bayesian Therapy | 8 | 9 | 10 | 10 | 9 | 7 | 8 | 9 | 8 | **86** |
| 24 | H7 Contagion of Courage | 10 | 8 | 9 | 9 | 9 | 8 | 9 | 9 | 9 | **88** |
| 25 | H14 Krebs Cycle of Outrage | 9 | 8 | 8 | 9 | 9 | 8 | 10 | 9 | 9 | **87** |
| 26 | Information Cascade Falls | 6 | 8 | 9 | 9 | 8 | 7 | 7 | 8 | 7 | **77** |
| 27 | Friendship Paradox Club | 7 | 7 | 8 | 8 | 8 | 6 | 9 | 8 | 7 | **76** |
| 28 | Fat Tail Farm | 7 | 9 | 10 | 10 | 7 | 6 | 7 | 9 | 8 | **81** |
| 29 | Trophic Cascade Kelp | 6 | 8 | 10 | 9 | 8 | 9 | 7 | 8 | 7 | **80** |
| 30 | Stochastic Resonance Whisper | 8 | 9 | 9 | 8 | 8 | 7 | 6 | 8 | 7 | **78** |

## Signature Tier — Build These First

If the goal is "I finally understand this" + internet longevity:

1. **Ergodicity Street** — fixes a civilization-scale math error in personal finance
2. **Petrie Multiplier** — combinatorics of harm; shareable in every industry fight
3. **Percolation City** — phase transitions are universally misunderstood
4. **H4 Urban Percolation Equity** — novel synthesis; policy relevant
5. **Majority Illusion** — one screenshot explains social media
6. **Parrondo Casino** — pure viral paradox joy
7. **H7 Contagion of Courage** — emotional + structural; activism tool

---

# Appendix: Design Checklist (From Nicky Case DNA)

Before building any concept, verify:

- [ ] Can the user *cause* the surprising outcome in first 60 seconds?
- [ ] Is there a BUT-chain of at least 3 counter-intuitive beats?
- [ ] Does the visual metaphor map 1:1 to mechanism (not decoration)?
- [ ] Is jargon withheld until after first surprise?
- [ ] Is there a sandbox with shareable state?
- [ ] Would Vi Hart nod at the math? Would Bret Victor nod at the interaction?
- [ ] Would a teacher assign it without embarrassment?
- [ ] Would someone share it to win an argument?

---

*Document complete. 120 candidates · 20 full concepts · 15 novel hybrids · Master ranking.*
*Steal the philosophy, not the polygons.*
