# Agentome

**Coordinate index layer for agent context — Agentome weighs, doesn't retrieve.**

Agentome is a framework for treating AI agent context like a
biological genome: compress, store, and emit a *verdict* on what to
trust versus what to reread — instead of stuffing raw text into
context windows.

This package is a thin identity wrapper around
[Helix Context](https://github.com/SwiftWing21/helix-context), the
reference implementation. `pip install agentome` pulls
`helix-context` and re-exports the full public API.

## Install

```bash
# Core (server + packet mode, no optional backends)
pip install agentome

# Recommended for daily use — launcher + tray + OTel + MCP + codec
pip install agentome[all]
```

Both commands install the engine under the hood. If you want the full
deps list resolved, see the **Full dependency matrix** section below.

## Quick Start

```python
from agentome import (
    HelixContextManager, load_config,
    ContextItem, ContextPacket, RefreshTarget,
)
from agentome.context_packet import build_context_packet

config = load_config()
manager = HelixContextManager(config)

# Ingest — provenance (source_kind, volatility, last_verified_at)
# auto-populated from the file extension.
manager.ingest(open("src/main.py").read(),
               content_type="code",
               metadata={"path": "/repo/src/main.py"})

# Decoder path — full assembled context for a downstream LLM
window = manager.build_context("How does auth work?")
print(window.expressed_context)
print(window.context_health.resolution_confidence)  # 0.0-1.0

# Index path — agent-safe packet with verdict + refresh plan
packet = build_context_packet("How does auth work?",
                              task_type="edit",
                              genome=manager.genome)
for item in packet.verified:
    print(f"[{item.status}] {item.source_id}  truth={item.live_truth_score:.2f}")
for target in packet.refresh_targets:
    print(f"reread: {target.source_id}  reason={target.reason}")
```

## What is an Agentome?

An **Agentome** is the complete set of compressed, structured
knowledge that an AI agent carries as persistent memory, plus the
*pathway layer* that tells the agent which parts of that memory it
should trust versus go re-verify. The weighing is as load-bearing as
the storage.

- **Genes** store compressed knowledge units (code, docs,
  conversations)
- **Promoter tags** enable fast retrieval by topic
- **Provenance fields** (source_kind, volatility_class,
  last_verified_at) drive task-sensitive freshness labeling
- **Coordinate confidence** measures whether retrieval landed in the
  right region, not just whether the words overlap
- **Co-activation** (`harmonic_links`) builds associative memory
  over time
- **Replication** grows the genome from every conversation

The concept is described in the research paper:
[The Agentome](https://mbachaud.substack.com/p/agentome)

## Agentome vs Helix Context

| | Agentome | Helix Context |
|---|---|---|
| **What** | The concept / framework | The implementation |
| **Analogy** | "Genome" | "Human Genome Project" |
| **Package** | `pip install agentome` | `pip install helix-context` |
| **API** | Re-exports Helix Context | The actual engine |
| **Extras** | Mirror helix-context's | `[launcher]`, `[codec]`, `[mcp]`, etc. |
| **Version policy** | Locked to helix-context | Semver, beta-track |

Use **agentome** in application code for the framework framing
(`from agentome import ...`). Use **helix-context** in infrastructure
code that you want to make obvious is wired to the engine. Both
imports resolve to the same Python objects.

## Full dependency matrix

Core `pip install agentome` installs:

| Package | Version | Source | Why |
|---|---|---|---|
| **helix-context** | `>=0.4.0b1` | [SwiftWing21/helix-context](https://github.com/SwiftWing21/helix-context) | The engine |
| fastapi | `>=0.110` | via helix-context | HTTP server |
| uvicorn | `>=0.29` | via helix-context | ASGI runtime |
| httpx | `>=0.27` | via helix-context | HTTP client (proxy + probes) |
| pydantic | `>=2.6` | via helix-context | Schema models |

That's enough to run `agentome` (alias for `helix`), the HTTP
server, and `/context` / `/context/packet` with a SQLite genome.

### Optional extras

Every extra mirrors the corresponding `helix-context` extra.
`pip install agentome[X]` == `pip install helix-context[X]` in
dep resolution.

| Extra | Pulls | Enables |
|---|---|---|
| `accel` | orjson | Faster JSON encode/decode |
| `embeddings` | numpy, sentence-transformers, torch (transitive) | SEMA 20D cold-tier retrieval |
| `cpu` | spacy | CpuTagger for entities (NER) |
| `mcp` | mcp>=1.0 | Run `python -m helix_context.mcp_server` for Claude Code / Cursor / Claude Desktop integration |
| `nli` | torch, transformers | DeBERTa relation-graph NLI backend (standalone; `embeddings` pulls these transitively) |
| `otel` | opentelemetry-sdk + exporter + instrumentation | Metrics + traces to Grafana/Prometheus when `HELIX_OTEL_ENABLED=1` |
| `launcher` | jinja2, psutil | Supervisor launcher (`helix-launcher` CLI, `:11438` dashboard) |
| `launcher-native` | jinja2, psutil, pywebview | Launcher with native window wrapper |
| `launcher-tray` | jinja2, psutil, pystray (**LGPL-3**), Pillow | Launcher with system tray icon |
| `ast` | tree-sitter + 4 language grammars | AST-aware code chunking |
| `scorerift` | scorerift | Divergence monitoring bridge |
| `codec` | **headroom-ai**[proxy,code]>=0.5.21 | **Recommended** — CPU-resident semantic compression (Headroom by Tejas Chopra, Apache-2.0). Replaces character-level truncation in the expression pipeline. See [NOTICE](https://github.com/SwiftWing21/helix-context/blob/main/NOTICE). |
| `dev` | pytest, pytest-asyncio | Contributor test suite |
| `all` | Every extra except `dev`, `launcher-tray`, `launcher-native` | The full feature surface |

### Non-pip runtime deps

Some features need infrastructure outside the Python dep graph. None
of these are required to start the server.

| Dependency | When | Install |
|---|---|---|
| **Python 3.11+** | always | [python.org](https://python.org) or your OS package manager |
| **SQLite FTS5** | retrieval (Tier 3) | Bundled with Python's sqlite3 on all mainstream builds. Verify with `python -c "import sqlite3; sqlite3.connect(':memory:').execute('CREATE VIRTUAL TABLE t USING fts5(x)')"` |
| **Ollama** | default `[ribosome] backend = "ollama"` + `/v1/chat/completions` answer generation | [ollama.com](https://ollama.com) — ships a local `ollama serve` on `:11434` |
| **spaCy model** | `[cpu]` extra for NER | `python -m spacy download en_core_web_sm` (after installing the `cpu` extra) |
| **OTel collector** | `[otel]` extra + `HELIX_OTEL_ENABLED=1` | Any OTLP/gRPC collector on `HELIX_OTEL_ENDPOINT` (default `localhost:4317`). Typically paired with Prometheus + Grafana. |

### Recommended install profiles

For different use cases, here's what to pull:

```bash
# Minimal — just serve /context and /context/packet with SQLite
pip install agentome

# Agent host (Claude Code, Cursor, MCP-aware tool)
pip install agentome[mcp,codec]

# Daily developer — everything you'd realistically use
pip install agentome[all,launcher]

# Observability stack
pip install agentome[all,otel,launcher]

# CI / bench / tests
pip install agentome[all,dev]
```

## Headroom composition (the compression path)

Agentome's default install uses character-level truncation for gene
content — works but leaves compression quality on the table. With
`pip install agentome[codec]`, the expression pipeline routes through
**Headroom** (Tejas Chopra, [chopratejas/headroom](https://github.com/chopratejas/headroom))
instead:

- **Kompress** — ModernBERT ONNX-based semantic compression (fast CPU)
- **CodeAwareCompressor** — language-aware for code content
- **LogCompressor / DiffCompressor** — contextual compressors for
  structured text

Headroom is opt-in to keep the core Agentome install small. When
installed, Agentome activates it transparently — no code changes.
Composition rule: *prefer Headroom when it's available, fall back to
char truncation when not.*

## Full Documentation

See the [Helix Context README](https://github.com/SwiftWing21/helix-context)
for complete documentation including:

- Two product surfaces (`/context` decoder path + `/context/packet`
  agent-safe index path)
- Weighing layer (freshness × authority × specificity × coord
  confidence)
- Pipeline lane reference
- Delta-epsilon health monitoring
- Horizontal Gene Transfer (genome export / import)
- Continue IDE integration
- MCP tool surface
- ScoreRift divergence detection bridge

## License

Apache 2.0
