---
id: "PAT-0005"
type: "interaction-pattern"
slug: "predict-then-reveal"
title: "Predict-Then-Reveal"
summary: "Commit before the simulation runs."
status: "canonical"
wing: "design"
created: "2026-06-26"
updated: "2026-06-26"
related:
  design: {'patterns': ['monty-hall-carnival', 'petrie-multiplier']}
explorable:
  verdict: "essential"
  best_medium: "web-simulation"
  best_medium_stars: 4
---

# Predict-Then-Reveal

> **One-line essence:** Commit before the simulation runs — prediction creates stakes; reveal creates memory.

## What it is

Predict-then-reveal forces the learner to register a forecast — a button choice, a numeric guess, a probability allocation — **before** seeing the simulation outcome or formal answer. The interface locks the commitment, runs the model, then compares prediction to result.

The pattern exploits a cognitive gap: reading the correct answer produces recognition; being wrong produces **durable recalibration**. Misforecasting hurts just enough to stick.

## When to use it

Use predict-then-reveal whenever intuition reliably **conflicts with correct reasoning** — probability paradoxes, base-rate neglect, emergent thresholds, network effects that look linear.

Essential for:

- Monty Hall–class conditional probability
- "Common sense" quantitative wrongness (birthday paradox, friendship paradox)
- Simulations where the output direction is debatable before the run
- Classroom settings where you want accountable engagement

Less useful when the learning goal is open exploration ([[sandbox-mode]]) or when there is no single forecastable outcome.

## How it works in an explorable

1. **Pose a concrete question** — "If you switch doors, what are your odds of winning?"
2. **Collect commitment** — buttons, slider, or typed number; no peeking
3. **Seal the prediction** — visual lock, optional "you chose B"
4. **Run simulation or show derivation** — animation, enumeration, or live draw
5. **Reveal and contrast** — highlight gap between prediction and outcome
6. **Explain the wedge** — why intuition misfired; optional second prediction to test transfer

The reveal should feel **fair** — not mockery. The user was supposed to get it wrong the first time.

## Design notes

- **Binary choices lower friction.** "Switch or stay?" beats "enter exact probability" for first contact.
- **Show your work on reveal.** Count doors, run 10,000 trials, display the sample path — skepticism dissolves with transparency.
- **Allow one retry** — second prediction tests whether the explanation landed; unlimited retries gamify guessing.
- **Log surprise optionally** — "67% of visitors predicted X" social proof normalizes error.
- **Pair with paradox pages** — our corpus links paradox entries to this pattern explicitly.
- **Separate prediction UI from result UI** — prevents accidental spoiler layout.

## Anti-patterns

- **Reveal before ask** — diagram showing the answer, then "what do you think?" performs engagement theater
- **No commitment mechanism** — rhetorical "take a guess" without recording choice
- **Punitive tone on wrong answers** — shame shuts down the second prediction
- **Ambiguous question** — if experts disagree on wording, users feel tricked not taught
- **Prediction without explanation** — surprise without repair is a party trick, not an explorable

## Examples in our corpus

- [[monty-hall-carnival]] — switch vs stay commitment before doors open
- [[monty-hall]] — paradox page prescribing predict-then-reveal before reading the solution
- [[petrie-multiplier]] — guess prevalence of harassment before seeing cascade math
- [[newcomb-predictor]] — predict box choice before the predictor's accuracy is shown
- [[base-rate-hospital]] — diagnose probability before Bayesian update animation
- [[birthday-paradox]] — guess collision probability before simulating a room of people

## Related

- [[playable-game]] — games embed predictions in every move; this pattern isolates one beat
- [[but-chain]] — multi-step belief revision; predict-then-reveal is single-step
- [[comparison-view]] — sometimes reveal is side-by-side outcomes rather than one answer
- [[echo-start-sandbox-end]] — opening prediction can echo in closing sandbox reflection
- [[probability-statistics]] — discipline hub linking paradox exhibits to this pattern

## Discovery suggestions

- [ ] Annotated GIF: prediction lock → simulation run → contrast overlay
- [ ] Transfer test: second prediction on structurally similar problem
- [ ] Aggregate chart of visitor predictions vs outcomes (anonymized)
- [ ] Anti-pattern gallery: "click to see answer" buttons without prior commitment
