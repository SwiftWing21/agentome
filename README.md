# Agentome

**Genome-based context compression for AI agents.**

Agentome is a framework for treating AI agent context like a biological genome — compressing, storing, and selectively expressing knowledge instead of stuffing raw text into context windows.

This package is a thin wrapper around [Helix Context](https://github.com/SwiftWing21/helix-context), the reference implementation.

## Install

```bash
pip install agentome
```

This installs `helix-context` as a dependency and re-exports its entire public API.

## Quick Start

```python
from agentome import AgentomeManager, load_config

config = load_config()
manager = AgentomeManager(config)

# Ingest content into the genome
manager.ingest("Your codebase documentation here")

# Query compressed context (7x smaller than raw files)
window = manager.build_context("How does auth work?")
print(window.expressed_context)
print(window.context_health.status)  # aligned | sparse | denatured

# Learn from exchanges (automatic replication)
manager.learn("How does auth work?", "JWT middleware validates tokens...")
```

## What is an Agentome?

An **Agentome** is the complete set of compressed, structured knowledge that an AI agent carries as persistent memory. Like a biological genome:

- **Genes** store compressed knowledge units (code, docs, conversations)
- **Promoter tags** enable fast retrieval by topic
- **Chromatin state** controls accessibility (fresh vs stale)
- **Co-activation** builds associative memory over time
- **Replication** grows the genome from every conversation

The concept is described in the research paper: [The Agentome](https://mbachaud.substack.com/p/agentome)

## Agentome vs Helix Context

| | Agentome | Helix Context |
|---|---------|---------------|
| **What** | The concept/framework | The implementation |
| **Analogy** | "Genome" | "Human Genome Project" |
| **Package** | `pip install agentome` | `pip install helix-context` |
| **API** | Re-exports Helix Context | The actual engine |

## Full Documentation

See the [Helix Context README](https://github.com/SwiftWing21/helix-context) for complete documentation including:

- 6-step expression pipeline
- Delta-epsilon health monitoring
- Horizontal Gene Transfer (genome export/import)
- Claude Code skill integration
- Continue IDE integration
- ScoreRift divergence detection bridge

## License

Apache 2.0
