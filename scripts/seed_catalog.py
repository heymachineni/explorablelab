#!/usr/bin/env python3
"""Curated + combinatorial seeds for corpus scale generation."""

# fmt: off

PSYCH_EFFECTS = """
stroop effect change blindness inattentional blindness anchoring effect availability heuristic
confirmation bias hindsight bias dunning kruger effect fundamental attribution error
cognitive dissonance halo effect priming mere exposure effect spacing effect
testing effect serial position effect von restorff effect misinformation effect
backfire effect continued influence effect illusory truth effect fluency heuristic
representativeness heuristic base rate neglect conjunction fallacy framing effect
loss aversion endowment effect sunk cost fallacy status quo bias default effect
nudge effect decoy effect compromise effect choice overload paradox of choice
spotlight effect illusion of transparency curse of knowledge empathy gap
hot cold empathy gap planning fallacy optimism bias pessimism bias
self serving bias blind spot bias in group bias out group homogeneity
false consensus effect pluralistic ignorance social proof bandwagon effect
bystander effect diffusion of responsibility social loafing free rider problem
deindividuation group polarization risky shift cautious shift groupthink
foot in door door in face low ball technique reciprocity norm
commitment consistency authority bias scarcity effect familiarity principle
peak end rule duration neglect affect heuristic somatic marker hypothesis
dual process theory system one system two prospect theory cumulative prospect theory
regret theory ambiguity aversion illusion of control gambler fallacy hot hand fallacy
clustering illusion apophenia pareidolia confirmation bias belief bias
motivated reasoning identity protective cognition cultural cognition
naive realism naive cynicism theory theory of mind mirror neuron hypothesis
embodied cognition extended mind hypothesis predictive processing
free energy principle active inference bayesian brain hypothesis
""".split()

PHYSICS_CONCEPTS = """
newtonian mechanics lagrangian mechanics hamiltonian mechanics least action principle
conservation of energy conservation of momentum conservation of angular momentum
thermodynamics zeroth law first law second law third law entropy production
statistical mechanics boltzmann distribution maxwell boltzmann statistics
quantum mechanics superposition uncertainty principle wave particle duality
quantum entanglement bell inequality quantum decoherence many worlds interpretation
copenhagen interpretation pilot wave theory quantum field theory standard model
general relativity special relativity equivalence principle spacetime curvature
black hole thermodynamics hawking radiation cosmic inflation dark matter dark energy
electromagnetism maxwell equations lorentz force faraday law lenz law
optics geometric optics wave optics diffraction interference polarization
fluid dynamics navier stokes euler equations bernoulli principle reynolds number
turbulence chaos theory butterfly effect strange attractors bifurcation theory
percolation theory phase transitions critical phenomena renormalization group
self organized criticality scale invariance power laws fractal geometry
nuclear physics fission fusion chain reaction critical mass radioactivity
particle physics quark model higgs mechanism neutrino oscillation cp violation
solid state physics band theory semiconductor physics superconductivity bcs theory
""".split()

ECON_CONCEPTS = """
supply and demand marginal utility comparative advantage gains from trade
comparative statics general equilibrium partial equilibrium pareto efficiency
externality public goods tragedy of commons free rider problem coase theorem
pigouvian tax cap and trade mechanism design auction theory vickrey auction
game theory nash equilibrium subgame perfection bayesian nash equilibrium
correlated equilibrium evolutionary stable strategy folk theorem repeated games
signaling screening adverse selection moral hazard principal agent problem
information asymmetry market for lemons reputation mechanism implicit contracts
behavioral economics prospect theory mental accounting hyperbolic discounting
nudge libertarian paternalism choice architecture default effects
macroeconomics is lm model phillips curve quantity theory of money
keynesian economics monetarism rational expectations real business cycles
efficient market hypothesis capital asset pricing model arbitrage pricing theory
modern portfolio theory black scholes option pricing risk neutral valuation
ergodicity economics kelly criterion fat tails black swan antifragility
goodharts law campbells law cobra effect ratchet effect regulatory capture
rent seeking public choice theory median voter theorem voting paradoxes
arrow impossibility theorem gibbard satterthwaite theorem condorcet paradox
ostrom commons polycentric governance institutional economics transaction costs
property rights theory hold up problem incomplete contracts theory of firm
""".split()

BIO_CONCEPTS = """
natural selection sexual selection kin selection inclusive fitness gene selection
group selection multilevel selection evolutionary developmental biology evo devo
modern synthesis neutral theory punctuated equilibrium adaptive radiation
coevolution red queen hypothesis arms race mimicry camouflage aposematism
handicap principle fisherian runaway good genes hypothesis
hardy weinberg equilibrium genetic drift gene flow founder effect bottleneck effect
molecular clock horizontal gene transfer endosymbiosis rna world hypothesis
central dogma transcription translation gene regulation epigenetics
crispr cas9 genome editing pcr dna sequencing synthetic biology
cell theory membrane transport osmosis diffusion active transport
photosynthesis cellular respiration krebs cycle electron transport chain
immune system clonal selection antibody diversity mhc presentation
neuroscience action potential synaptic plasticity long term potentiation
ecology lotka volterra predator prey carrying capacity logistic growth
trophic cascade keystone species competitive exclusion principle niche partitioning
island biogeography metapopulation theory r k selection life history theory
epidemiology sir model r0 herd immunity superspreader basic reproduction number
developmental biology morphogenesis hox genes induction organizer
microbiome holobiont one health concept
""".split()

MATH_CONCEPTS = """
calculus limits derivatives integrals fundamental theorem of calculus
linear algebra vector spaces eigenvalues eigenvectors singular value decomposition
probability theory random variables expectation variance law of large numbers
central limit theorem markov chains martingales stochastic processes brownian motion
statistics hypothesis testing confidence intervals bayesian inference maximum likelihood
regression analysis causal inference potential outcomes model do calculus
graph theory network flows matching theory coloring problems planarity
topology homotopy homology manifolds differential geometry riemannian geometry
number theory prime distribution modular forms elliptic curves fermat last theorem
group theory ring theory field theory galois theory representation theory
category theory functors natural transformations adjunctions topos theory
logic propositional logic predicate logic godel incompleteness completeness
set theory zfc axioms continuum hypothesis axiom of choice
combinatorics generating functions ramsey theory extremal combinatorics
optimization linear programming convex optimization duality lagrange multipliers
dynamical systems fixed points stability lyapunov exponents ergodic theory
information theory shannon entropy channel capacity kolmogorov complexity
game theory combinatorial game theory fair division social choice theory
""".split()

CS_CONCEPTS = """
algorithm analysis big o notation np completeness p versus np
computability turing machines halting problem church turing thesis
data structures trees graphs hash tables priority queues
sorting algorithms graph algorithms dynamic programming greedy algorithms
machine learning supervised learning unsupervised learning reinforcement learning
deep learning backpropagation convolutional networks transformers attention mechanism
bias variance tradeoff overfitting regularization cross validation
explainable ai fairness in ml adversarial examples robustness
cryptography public key encryption zero knowledge proofs hash functions
distributed systems cap theorem flp impossibility byzantine generals consensus
raft paxos blockchain proof of work proof of stake smart contracts
programming languages type systems lambda calculus functional programming
operating systems scheduling memory management virtual memory paging
computer networks tcp ip routing protocols congestion control
human computer interaction fitts law hicks law gulf of execution
affordances cognitive load theory mental models in hci
""".split()

SOC_CONCEPTS = """
symbolic interactionism structural functionalism conflict theory social constructivism
labeling theory strain theory differential association social learning theory
rational choice theory habitus field theory cultural capital social reproduction
network society digital divide social capital bonding bridging weak ties
homophily triadic closure structural holes small world networks scale free networks
collective action problem free rider olson logic mobilization resource mobilization
political opportunity framing social movements contentious politics
demographic transition second demographic transition fertility decline
urbanization suburbanization gentrification spatial mismatch hypothesis
world systems theory dependency theory modernization theory
institutional theory organizational ecology population ecology of organizations
""".split()

PARADOX_LIST = """
liar paradox berry paradox russell paradox cantor paradox burali forti paradox
curry paradox yablo paradox surprise examination unexpected hanging
lottery paradox preface paradox ravens paradox grue paradox goodman paradox
simpson paradox spurious correlation regression paradoxes ecological fallacy
friendship paradox inspection paradox waiting time paradox
birthday paradox monty hall two envelope sleeping beauty thomson lamp
zeno paradox achilles tortoise dichotomy arrow paradox
olbers paradox fermi paradox dark night sky
maxwell demon loschmidt paradox gibbs paradox
epr paradox bell theorem nonlocality
twin paradox barn pole paradox ladder paradox
grandfather paradox bootstrap paradox predestination paradox
ship of theseus sorites paradox heap paradox
prisoners dilemma tragedy of commons stag hunt coordination failure
allais paradox ellsberg paradox st petersburg paradox
newcomb paradox smoking lesion evidential decision theory
braess paradox downfall paradox productivity paradox
jevons paradox rebound effect energy efficiency
moravec paradox polanyi paradox
petrie multiplier paradox majority illusion paradox
simpson paradox reversal berkson paradox will rogers phenomenon
downfall paradox productivity paradox abilene paradox hedgehog dilemma
""" + " ".join(f"logical paradox {i}" for i in range(1, 400))

MENTAL_MODELS = """
first principles thinking second order effects inversion map territory circle competence
margin of safety probabilistic thinking bayesian updating expected value
opportunity cost trade offs comparative advantage specialization
supply demand elasticity price signals market clearing
feedback loops stocks flows systems thinking leverage points
critical mass tipping points phase transitions network effects
switching costs lock in path dependence increasing returns
principal agent information asymmetry signaling screening
creative destruction disruptive innovation s curve diffusion of innovations
pareto principle power law long tail winner take all
barbell strategy via negativa antifragility skin in the game
red team blue team premortem postmortem after action review
occams razor hanlons razor chestertons fence lindys law
steel man straw man weak man strongest counterargument
OODA loop decision matrix weighted scoring multi criteria analysis
Eisenhower matrix pareto frontier satisficing bounded rationality
""".split() + PSYCH_EFFECTS[:80]

EXPERIMENT_NAMES = (
    """
asch conformity milgram obedience stanford prison robbers cave
marshmallow test wisconsin card sort stroop test visual cliff
bobo doll little albert harlow monkeys bystander effect
cognitive dissonance festinger lost in mall false memory
invisible gorilla change blindness choice blindness
ultimatum game dictator game trust game public goods game
prisoners dilemma tournament tit for tat evolution of cooperation
wason selection task framing effect asian disease problem
prospect theory experiments anchoring experiment
libet readiness potential split brain sperry
dual process bat ball problem cognitive reflection test
implicit association test stereotype threat stereotype lift
minimal group paradigm minimal group tajfel
stanford marshmallow replication power pose study
growth mindset duckworth grit study
broken windows field experiment hawthorne effect
randomized controlled trial rct gold standard
ablation study factorial design latin square design
"""
    + " ".join(f"replication study {i}" for i in range(1, 400))
)

BOOK_TITLES = (
    """
on the origin of species selfish gene extended phenotype blind watchmaker
godel escher bach structure scientific revolutions
thinking fast and slow noise predictably irrational nudge
black swan antifragile fooled by randomness bed of procrustes
sapiens homo deus 21 lessons guns germs steel collapse
why nations fail narrow corridor capital in twenty first century
prisoners dilemma evolution of cooperation micromotives macrobehavior
death and life great american cities image of city
governing commons politics without romance seeing like a state
wealth of nations theory moral sentiments general theory employment
keynes general theory hayek road serfdom friedman capitalism freedom
da capo series fermats last theorem joy of x infinite powers
surely youre joking feynman pleasure finding things out
brief history of time universe in nutshell grand design
cosmos pale blue dot demon haunted world contact
silent spring limits to growth small is beautiful
permaculture designers manual one straw revolution
man search for meaning paradoxical intention logotherapy
flow psychology optimal experience creativity
mindstorms children computers powerful ideas
mind in society pedagogy of oppressed
"""
    + " ".join(f"explorable reader volume {i}" for i in range(1, 200))
)

INTERACTION_PATTERNS = (
    """
agent placement parameter slider sandbox mode but chain predict then reveal
comparison view role as system graph rewiring ladder of abstraction
playable game drag and drop direct manipulation scrubbable timeline
linked brushing small multiples coordinated views crossfilter
tangle reactive documents explorable explanation
branching narrative choose your own adventure dialogue tree
progressive disclosure accordion wizard stepped tutorial
spatial zoom pan filter sort search faceted navigation
undo redo reset randomize seed share permalink
multiplayer synchronous collaborative editing voting together
tournament mode leaderboard replay ghost replay
before after slider side by side diff split view
commit and reveal sealed bid hidden information reveal
build your own author your own user generated rules
physical manipulation tangible interface gesture based
voice interaction speech recognition conversational ui
real data live data streaming data historical playback
"""
    + " ".join(f"pattern variant {i}" for i in range(1, 150))
)

VISUAL_METAPHORS = (
    """
neighborhood grid feedback loop circle double well potential network graph
phase space sandpile avalanche galton board treemap sankey flow
decision tree force directed graph chord diagram voronoi tessellation
heat map contour plot vector field stream plot quiver plot
pendulum wave interference ripple tank particle system flocking boids
pipeline waterfall conveyor belt assembly line factory floor
balance scale seesaw lever pulley gear clockwork domino chain
iceberg tip hidden mass onion layers russian doll matryoshka
maze labyrinth bridge island archipelago watershed river delta
garden ecosystem aquarium terrarium ant colony beehive
"""
    + " ".join(f"metaphor motif {i}" for i in range(1, 120))
)

STORY_STRUCTURES = (
    """
heros journey monomyth three act structure five act structure
kishotenketsu four act structure freytag pyramid
in media res cold open frame story story within story
echo start sandbox end innocence horror hope but chain narrative
problem solution benefit before after bridge
inverted pyramid journalism explainer pyramid
challenge conflict change resolution coda
setup confrontation resolution epilogue
"""
    + " ".join(f"narrative beat template {i}" for i in range(1, 130))
)

SCIENTIST_NAMES = (
    """
isaac newton albert einstein niels bohr werner heisenberg erwin schrodinger
paul dirac richard feynman murray gell mann sheldon glashow steven weinberg
marie curie rosalind franklin linus pauling dmitri mendeleev
charles darwin gregor mendel james watson francis crick
rachel carson jane goodall dian fossey edward wilson
john maynard keynes friedrich hayek milton friedman paul samuelson
kenneth arrow john nash reinhard selten thomas schelling
daniel kahneman amos tversky richard thaler robert shiller eugene fama
elinor ostrom paul krugman joseph stiglitz amartya sen abhijit banerjee
claude shannon alan turing john von neumann grace hopper ada lovelace
tim berners lee vinton cerf bob kahn donald knuth edsger dijkstra
geoffrey hinton yann lecun yoshua bengio
sigmund freud carl jung jean piaget lev vygotsky b f skinner
william james wilhelm wundt ivan pavlov john watson
noam chomsky steven pinker george lakoff mark johnson
max weber emile durkheim karl marx auguste comte
bell hooks angela davis
"""
    + " ".join(f"researcher {i}" for i in range(1, 250))
)

NOBEL_CATEGORIES = ["physics", "chemistry", "medicine", "literature", "peace", "economics"]

FIELD_FOLDERS = {
    "psychology": "cognitive-science",
    "physics": "physics",
    "economics": "economics",
    "biology": "evolution",
    "mathematics": "probability",
    "computer-science": "information-theory",
    "sociology": "social-science",
    "default": "complex-systems",
}

def unique_slug(base, existing):
    base = base.replace("_", "-").replace(" ", "-")
    base = "".join(c for c in base.lower() if c.isalnum() or c == "-")
    while "--" in base:
        base = base.replace("--", "-")
    slug = base.strip("-") or "concept"
    if slug not in existing:
        return slug
    n = 2
    while f"{slug}-{n}" in existing:
        n += 1
    return f"{slug}-{n}"
