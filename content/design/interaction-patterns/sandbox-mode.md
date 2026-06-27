---
id: "PAT-0003"
type: "interaction-pattern"
slug: "sandbox-mode"
title: "Sandbox Mode"
summary: "Prove generality after the lesson."
status: "canonical"
wing: "design"
created: "2026-06-26"
updated: "2026-06-26"
related:
  design: {'patterns': ['evolution-of-trust', 'to-build-a-better-ballot']}
explorable:
  verdict: "essential"
  best_medium: "web-simulation"
  best_medium_stars: 4
---

# Sandbox Mode

> **One-line essence:** Prove generality after the lesson — hand the learner the full toy and step back.

## What it is

Sandbox mode is the phase of an explorable where guided narration ends and the learner receives unrestricted access to controls, initial conditions, and parameters. No script. No next button. The user tests whether the rule they just learned holds beyond the author's curated examples.

Sandboxes answer the silent question every thoughtful reader asks: **"Was that a trick of your scenario?"** Free play converts a single anecdote into a demonstrated law.

## When to use it

Use sandbox mode after a **completed guided path** — never as the opening move for counterintuitive models.

Sandboxes earn their place when:

- The lesson risked feeling rigged (carefully chosen initial conditions, cherry-picked payoffs)
- Generalization is part of the claim ("this happens for many thresholds, not just 33%")
- Replayability extends classroom or self-study value
- The model is genuinely fun to poke — discovery becomes motivation

Skip sandbox when the concept is a single historical fact, a one-shot paradox with one correct answer, or when unrestricted play produces mostly noise without insight.

## How it works in an explorable

1. **Guided chapters finish** — learner has seen manual, automated, and parameterized versions
2. **Transition signal** — "Your turn" or "Free play" — explicit handoff from author to user
3. **Full control surface** — sliders, reset, speed, initial conditions, optional agent placement
4. **No scoring** — curiosity, not gamification; failure states are informative
5. **Optional share/permalink** — let users save interesting configurations ([[permalink]] pattern)

The sandbox is not a separate app. It is the same simulation with guardrails removed.

## Design notes

- **Earn the sandbox.** Releasing controls too early produces fiddling without comprehension.
- **Keep defaults sane.** Blank canvas should still produce interesting behavior within seconds.
- **Preserve the guided path.** Users who want the story should not be forced into sandbox; offer both routes.
- **Surface constraints quietly.** If certain combinations crash or stall, degrade gracefully with a one-line explanation.
- **Seed interesting presets.** A "try this" button lowers the activation energy for less exploratory users.
- **Pair with [[echo-start-sandbox-end]]** narrative structure when the opening and closing beats should mirror each other.

## Anti-patterns

- **Sandbox first** — no framing means users never learn what to look for
- **Fake sandbox** — only three preset buttons disguised as freedom
- **Empty sandbox** — full controls but no default state that produces motion or structure
- **Scored sandbox** — leaderboards turn exploration into optimization of the wrong objective
- **Abandoning the sandbox** — building it but hiding it behind an unlabeled icon

## Examples in our corpus

- [[evolution-of-trust]] — tournament sandbox after the narrative arc; run any strategy mix
- [[parable-of-polygons]] — free placement and threshold tuning after the four guided chapters
- [[to-build-a-better-ballot]] — compare voting systems with user-defined electorates
- [[loopy]] — draw arbitrary feedback loops without tutorial scaffolding
- [[commons-garden]] — harvest rates and regeneration parameters under learner control

## Related

- [[ladder-of-abstraction]] — sandbox sits at the top rung
- [[parameter-slider]] — primary sandbox control for continuous models
- [[agent-placement]] — spatial sandbox for grid-based models
- [[playable-game]] — games can embed sandbox as post-credits free play
- [[echo-start-sandbox-end]] — storytelling structure pairing guided open and close

## Discovery suggestions

- [ ] Annotated GIF: guided path ending → sandbox handoff → user discovers edge case
- [ ] "Break the model" challenge card for classrooms
- [ ] Preset gallery of community-discovered configurations
- [ ] Anti-pattern callout: exhibits that end on a rhetorical question instead of free play
