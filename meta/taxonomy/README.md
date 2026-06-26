# Taxonomy

Controlled vocabularies for frontmatter. **Do not invent tags without registering here.**

| File | Purpose |
|------|---------|
| [fields.yaml](fields.yaml) | Top-level disciplines |
| [applications.yaml](applications.yaml) | Real-world application domains |
| [simulation-types.yaml](simulation-types.yaml) | Simulation mechanics |
| [tag-registry.md](tag-registry.md) | Free tags + deprecated aliases |

Fields and subfields use YAML IDs in frontmatter:

```yaml
fields: [complex-systems, social-science]
subfields: [agent-based-modeling]
tags: [emergence, threshold]  # must be in tag-registry
```
