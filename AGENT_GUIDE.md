# Agent Guide

Instructions for AI agents expanding this knowledge base collaboratively with humans.

## Mission

Store **ideas that become dramatically easier to understand through interaction** — not facts alone.

## Before creating any page

1. Read [`ARCHITECTURE.md`](ARCHITECTURE.md)
2. Copy correct template from [`templates/`](templates/)
3. Check slug doesn't exist: search `content/` for `slug:`
4. Assign next ID from [`meta/id-registry.md`](meta/id-registry.md)
5. Register new tags in [`meta/taxonomy/tag-registry.md`](meta/taxonomy/tag-registry.md)

## Auto-suggestion protocol (REQUIRED)

When you add or edit **any** page, output and file a **Discovery Report**:

### Template: Discovery Report

```markdown
## Discovery Report — {slug} — {date}

### Related pages updated
- [[slug]] — added backlink

### Missing pages to create (stubs)
| Slug | Type | Priority | Reason |
|------|------|----------|--------|
| | THY | high | |

### Potential simulations (SIM)
| Title | Theory | Medium | Priority | Novelty |
|-------|--------|--------|----------|---------|
| | | web-simulation | 8.5 | |

### Visual metaphors (MET)
| Metaphor | Maps |
|----------|------|

### Interaction patterns (PAT)
| Pattern | Use for this concept |

### Cross-disciplinary links
| From | To | Connection |

### Existing coverage check
| EXE | Overlap | Gap | Recommendation |
|-----|---------|-----|----------------|
| | 70% | sandbox | extend don't duplicate |

### Scores to set
| Dimension | Score | Justification |
```

Append Discovery Report to page's `## Discovery suggestions` section.

## Trigger matrix

| Trigger | Mandatory actions |
|---------|-------------------|
| New **PAP** | Create/update SCI stubs; THY for each model introduced; check SIM/EXE |
| New **THY** | Link DIS; score all dimensions; propose ≥1 SIM if verdict ≥ strong; list PAT/MET |
| New **SCI** | List papers; flag unexplored theories for SIM |
| New **EXE** | List THY + PAT; set existing_coverage on related THY high |
| New **SIM** | Link THY, PAT, MET; diff against EXE |
| New **PAR** | Link paradox_of THY; propose choice-based interaction |
| New **EXP** | Link PHN; propose interactive recreation |
| Broken `[[link]]` | Create `status: stub` page same PR |

## Scoring automation

For THY/PAR/PHN/SIM, always set:

```yaml
scores:
  visual_potential: N
  # ... all 15 dimensions
explorable:
  verdict: essential|strong|moderate|weak|none
  can_become: { ... all mediums ... }
  best_medium: ...
  best_medium_stars: 1-5
  best_medium_reason: "..."
```

Compute `composite` per [`meta/scoring/rubric.md`](meta/scoring/rubric.md).

**Reject page** if:
- `interaction_potential` ≤ 3 AND `visual_potential` ≤ 3
- `explorable.verdict: none`

## Graph enrichment

Minimum edges for `status: mature`:

| Type | Min edges |
|------|-----------|
| THY | 3 related theories OR 1 theory + 2 papers + 1 PAT |
| PAP | 1 SCI + 1 THY |
| SIM | 1 THY + 1 PAT + 1 MET |
| EXE | 1 THY + 2 PAT |
| SCI | 2 PAP or THY |

## Stub creation format

```yaml
---
id: THY-0999
type: theory
slug: pending-concept
title: "Pending Concept"
summary: "One line."
status: stub
created: YYYY-MM-DD
related:
  theories: [parent-concept]
---
# Pending Concept

*Stub — requested by [[source-slug]].*

## Discovery suggestions
- [ ] Full page needed because…
```

## Batch expansion strategy

1. **Seed discipline hub** (DIS)
2. **Add 5 canonical THY** with scores
3. **Add key PAP + SCI**
4. **Add PAT/MET vocabulary**
5. **Add SIM concepts** for top-scored THY
6. **Add EXE** for existing explorables (canon)
7. **Update indices**

## Do not

- Copy Wikipedia prose
- Create pages without explorable thesis
- Duplicate EXE as SIM without gap analysis
- Invent unregistered tags
- Leave orphan pages

## Priority queue

Build SIM stubs first for THY where:
- `scores.composite` ≥ 8.0
- `existing_coverage` ≤ 4
- `explorable.verdict` = essential

See [`ROADMAP.md`](ROADMAP.md) and [`indices/by-score/tier-s.md`](indices/by-score/tier-s.md).
