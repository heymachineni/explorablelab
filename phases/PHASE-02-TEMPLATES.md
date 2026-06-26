# Phase 2 — Markdown Templates ✅

**Status:** Complete  
**Location:** [`templates/`](../templates/)

## Content types (19 templates)

| Template | ID | Destination |
|----------|-----|-------------|
| theory.md | THY | content/theories/{discipline}/ |
| paradox.md | PAR | content/paradoxes/ |
| phenomenon.md | PHN | content/phenomena/ |
| mental-model.md | MOD | content/mental-models/ |
| paper.md | PAP | content/publications/papers/ |
| book.md | BOK | content/publications/books/ |
| nobel.md | NOB | content/publications/nobel/ |
| scientist.md | SCI | content/people/scientists/ |
| designer.md | DSN | content/people/designers/ |
| experiment.md | EXP | content/experiments/ |
| simulation-concept.md | SIM | content/simulations/concepts/ |
| prototype-idea.md | PRO | content/simulations/prototypes/ |
| existing-explorable.md | EXE | content/simulations/existing/ |
| interaction-pattern.md | PAT | content/design/interaction-patterns/ |
| visual-metaphor.md | MET | content/design/visual-metaphors/ |
| storytelling-structure.md | STR | content/design/storytelling-structures/ |
| medium.md | MED | content/design/mediums/ |
| discipline.md | DIS | content/disciplines/ |
| historical-event.md | EVT | content/events/ |

## Universal frontmatter (every type)

```yaml
id: TYPE-0000          # immutable
type: theory            # node type
slug: kebab-case        # globally unique
title: "Human Title"
summary: "One sentence."
status: stub|draft|mature|canonical
created: YYYY-MM-DD
updated: YYYY-MM-DD
confidence: low|medium|high
related: { ... }       # typed graph edges
```

## Theory-specific required blocks

Every **THY**, **PAR**, **PHN** must include:

### `explorable` frontmatter

```yaml
explorable:
  verdict: essential|strong|moderate|weak|none
  why_interaction: "..."
  can_become:
    simulation: true|false
    interactive_game: true|false
    physical_toy: true|false
    classroom_activity: true|false
    visualization: true|false
    social_experiment: true|false
    mobile_app: true|false
    webgl_demo: true|false
    card_game: true|false
    board_game: true|false
    data_visualization: true|false
  best_medium: web-simulation
  best_medium_stars: 1-5
  best_medium_reason: "..."
  anti_patterns: []
```

### Body sections

1. Why this matters  
2. Core idea  
3. Why interaction beats reading  
4. Can become (table)  
5. Best medium ★ rating  
6. Related graph  
7. **Discovery suggestions** (Phase 9)

## Scores block (THY, PAR, PHN, SIM)

All 15 dimensions — see [Phase 5](PHASE-05-SCORING.md).

## Copy workflow

```bash
cp templates/theory.md content/theories/complex-systems/my-theory.md
# Edit frontmatter; assign ID from meta/id-registry.md
```

→ [Phase 3 — Relationships](PHASE-03-RELATIONSHIPS.md)
