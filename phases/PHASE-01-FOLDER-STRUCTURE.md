# Phase 1 — Folder Structure ✅

**Status:** Complete  
**Scale target:** 20,000+ markdown files · 20-year horizon

## Design decisions

| Decision | Rationale |
|----------|-----------|
| `content/` as single corpus root | One place to grep, clone, mirror |
| Discipline sharding at L2 | `theories/complex-systems/` not flat 1200 files |
| Letter-split at 400+ files | `complex-systems/a-f/` when shard fills |
| Global unique `slug` | Wikilinks work across types |
| Immutable `id` in frontmatter | Paths can move; IDs never change |
| `indices/` separate from `content/` | Navigation without polluting corpus |
| `graph/edges/` optional | Heavy edges don't bloat every page |
| `phases/` docs | Track completion of 9-phase build |

## Complete tree

```
/
├── README.md
├── ARCHITECTURE.md
├── CONTRIBUTING.md
├── AGENT_GUIDE.md
├── ROADMAP.md
├── LICENSE
├── EXPLORABLE_EXPLANATIONS_RESEARCH.md
│
├── phases/                          ← Phase completion docs
│   ├── PHASE-01-FOLDER-STRUCTURE.md
│   ├── PHASE-02-TEMPLATES.md
│   ├── … through PHASE-09
│
├── content/
│   ├── README.md
│   ├── theories/                    → THY · target 1,200+
│   │   ├── README.md
│   │   ├── complex-systems/
│   │   ├── game-theory/
│   │   ├── network-science/
│   │   ├── probability/
│   │   ├── economics/
│   │   ├── cognitive-science/
│   │   ├── physics/
│   │   ├── evolution/
│   │   ├── engineering/
│   │   ├── information-theory/
│   │   ├── social-science/
│   │   ├── urbanism/
│   │   └── political-science/
│   ├── paradoxes/                   → PAR · target 800+
│   │   └── README.md
│   ├── mental-models/               → MOD · target 600+
│   │   └── README.md
│   ├── phenomena/                   → PHN · target 500+
│   │   └── README.md
│   ├── people/
│   │   ├── README.md
│   │   ├── scientists/              → SCI · target 300+
│   │   └── designers/               → DSN
│   ├── publications/
│   │   ├── README.md
│   │   ├── papers/                  → PAP · target 300+
│   │   ├── books/                   → BOK · target 250+
│   │   └── nobel/                   → NOB · target 400+
│   ├── experiments/                 → EXP · target 500+
│   │   └── README.md
│   ├── simulations/
│   │   ├── README.md
│   │   ├── concepts/                → SIM · target 100+
│   │   ├── prototypes/              → PRO
│   │   └── existing/                → EXE
│   ├── design/
│   │   ├── README.md
│   │   ├── interaction-patterns/    → PAT · target 200+
│   │   ├── visual-metaphors/        → MET · target 150+
│   │   ├── storytelling-structures/ → STR · target 150+
│   │   └── mediums/                 → MED
│   ├── disciplines/                 → DIS · hub pages
│   ├── events/                      → EVT
│   └── organizations/               → ORG
│
├── templates/                       → 19 type templates
├── meta/
│   ├── id-registry.md
│   ├── taxonomy/
│   ├── scoring/
│   └── graph/
├── indices/
│   ├── README.md
│   ├── by-discipline/
│   ├── by-score/
│   ├── by-medium/
│   ├── maps-of-content/
│   └── awesome/
├── graph/
│   ├── README.md
│   └── edges/
└── scripts/
    ├── README.md
    └── validate-frontmatter.py
```

## Sharding playbook

When `content/theories/complex-systems/` hits **400 files**:

```
complex-systems/
├── README.md          ← index of sub-shards
├── core/              ← subtopic shard
├── a-f/
├── g-m/
└── n-z/
```

When a **discipline** exceeds **15 subtopics**, add `content/disciplines/{discipline}/` as MOC only — not duplicate theory files.

## File naming

- `{slug}.md` — kebab-case, no dates
- Papers: `{year}-{slug}.md` optional for sort
- Events: `{year}-{slug}.md`
- Nobel: `{year}-{slug}.md`

## Next

→ [Phase 2 — Templates](PHASE-02-TEMPLATES.md)
