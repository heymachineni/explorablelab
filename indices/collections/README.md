# Collections — Museum Exhibitions

**Purpose:** Curated galleries for ExplorableLab visitors.  
**Not:** Alphabetical dumps (`indices/awesome/*` are workshop indexes).

Each collection is a **permanent or rotating exhibition** with narrative, time estimate, and emotional arc.

---

## Launch collections (v1 — create these first)

| File | Title | Stops | Minutes |
|------|-------|-------|---------|
| `start-here-first-visit.md` | Start Here: First Visit | 5 | 15 |
| `paradoxes-everyone-should-play.md` | Paradoxes Everyone Should Play Once | 8 | 25 |
| `innocence-horror-hope.md` | Innocence → Horror → Hope | 5 | 20 |
| `why-groups-act-weird.md` | Why Groups Act Weird | 6 | 20 |
| `math-that-lies-to-you.md` | Math That Lies to You | 7 | 30 |
| `systems-that-shape-society.md` | Systems That Shape Society | 8 | 35 |
| `steal-from-nicky-case.md` | Steal From Nicky Case | 7 | 40 |
| `trust-betrayal-forgiveness.md` | Trust, Betrayal, and Forgiveness | 5 | 20 |
| `networks-youre-inside-of.md` | Networks You're Inside Of | 6 | 25 |
| `ideas-every-designer-should-understand.md` | Ideas Every Designer Should Understand | 10 | 45 |
| `under-five-minutes.md` | Under 5 Minutes | 6 | 5 each |
| `build-these-next-tier-s.md` | Build These Next (Tier S) | 18 | reference |

---

## Template

```yaml
---
id: COL-0001
type: collection
slug: start-here-first-visit
title: "Start Here: First Visit"
summary: "Five exhibits. One sitting. See the world differently."
status: canonical
wing: null
audience: [everyone, first-visit]
time_minutes: 15
emotional_arc: "curiosity → surprise → complicity → hope"
stops:
  - slug: parable-of-polygons
    type: existing-explorable
    hook: "Move one triangle. Watch society crack."
  - slug: monty-hall
    type: paradox
    hook: "Your intuition is wrong. Bet on it."
  - slug: petrie-multiplier
    type: simulation-concept
    hook: "Equal rules. Unequal harm."
  - slug: schelling-segregation
    type: theory
    hook: "No villains required."
  - slug: evolution-of-trust
    type: existing-explorable
    hook: "Cooperation works—until it doesn't."
related_collections: [paradoxes-everyone-should-play, steal-from-nicky-case]
created: 2026-06-26
updated: 2026-06-26
---

# Start Here: First Visit

> **For:** Anyone landing on ExplorableLab for the first time.  
> **Time:** ~15 minutes.  
> **Feeling when done:** "I want one more."

## Why this path

Each stop is playable or will be soon. Together they show what ExplorableLab *is* — not reading about ideas, but **causing** them.

## Stops

### 1. [[parable-of-polygons]]
…

## You may also like

- [[innocence-horror-hope]]
- [[steal-from-nicky-case]]
```

---

## Full collection backlog (55 target)

See [`PRODUCT-SPEC.md`](../PRODUCT-SPEC.md) §6 for the complete list of 55 planned exhibitions.

---

## Rules

1. **5–15 stops** per collection (except reference collections like Tier S build queue)
2. Every stop must be in [`meta/CANONICAL-REGISTRY.md`](../meta/CANONICAL-REGISTRY.md) or marked `coming-soon: true`
3. Each stop needs a **one-line hook**, not just a wikilink
4. Name the **emotional arc** in frontmatter
5. Collections are editorial — never auto-generated from folder listings
