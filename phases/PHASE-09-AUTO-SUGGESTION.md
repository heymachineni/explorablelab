# Phase 9 — Auto-Suggestion Protocol ✅

**Status:** Complete  
**Agent guide:** [`AGENT_GUIDE.md`](../AGENT_GUIDE.md)  
**Template:** [`templates/discovery-report.md`](../templates/discovery-report.md)

## Trigger → mandatory outputs

| You add… | Must suggest |
|----------|--------------|
| **Paper** | SCI authors, THY introduced, EXP replications, SIM from key result |
| **Theory** | DIS, related PAR, PAT+MET, SIM if score≥8, EXE coverage check |
| **Scientist** | PAP list, THY developed, unexplored SIM opportunities |
| **Experiment** | PHN, interactive recreation spec, ethics note |
| **Existing EXE** | THY coverage %, PAT used, gaps, extension SIM |
| **Simulation SIM** | THY, PAT, MET, diff vs EXE |
| **Broken [[link]]** | `status: stub` page in same PR |

## Discovery Report (append to every page)

```markdown
## Discovery suggestions

### Missing pages to create
| Slug | Type | Priority | Reason |
|------|------|----------|--------|

### Potential simulations
| Title | Theory | Medium | Priority |
|-------|--------|--------|----------|

### Visual metaphors
| Metaphor | Mapping |

### Interaction patterns
| Pattern | Use |

### Cross-disciplinary links
| Target | Connection |

### Existing coverage
| EXE | Overlap | Gap | Action |
|-----|---------|-----|--------|
```

## Stub rule

```yaml
status: stub
summary: "One line."
related:
  theories: [parent-that-linked-here]
```

Full page within 180 days or delete.

## Continuous enrichment

When editing **any** page:

1. Re-run mental Discovery Report
2. Update backlinks on neighbors
3. Bump `updated:` date
4. Re-score if explorable landscape changed (new EXE)

## Validation

```bash
python3 scripts/validate-frontmatter.py
```

Flags: orphan stubs, missing explorable block, unregistered tags, broken related slugs.

---

**All 9 phases complete.** Start expanding corpus from [`indices/maps-of-content/master-graph.md`](../indices/maps-of-content/master-graph.md).
