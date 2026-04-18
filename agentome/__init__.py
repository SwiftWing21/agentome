"""
Agentome — Coordinate index layer for agent context, powered by Helix Context.

Agentome is the concept / framework; Helix Context is the engine.

    pip install agentome

is equivalent to:

    pip install helix-context

All public APIs are re-exported from helix_context, including the
packet-mode schemas introduced in 0.4.0b1 (agent-safe context
labeling per the agent-context-index build spec).
"""

from helix_context import (
    # Config
    HelixConfig,
    load_config,
    # Schemas
    Gene,
    ContextWindow,
    ContextHealth,
    ChromatinState,
    PromoterTags,
    EpigeneticMarkers,
    # Core
    Genome,
    Ribosome,
    OllamaBackend,
    CodonChunker,
    CodonEncoder,
    RawStrand,
    Codon,
    HelixContextManager,
    create_app,
    # Exceptions
    HelixError,
    CodonAlignmentError,
    PromoterMismatch,
    FoldingError,
    TranscriptionError,
    GenomeFullError,
)

# Packet-mode schemas (shipped in helix-context 0.4.0b1 — see the
# agent-context-index build spec). Re-exported at top-level so
# consumers can `from agentome import ContextPacket`.
from helix_context.schemas import (
    ContextItem,
    ContextPacket,
    RefreshTarget,
)

# Aliases for the Agentome vocabulary
AgentomeConfig = HelixConfig
AgentomeManager = HelixContextManager

__all__ = [
    # Helix Context re-exports
    "HelixConfig",
    "load_config",
    "Gene",
    "ContextWindow",
    "ContextHealth",
    "ChromatinState",
    "PromoterTags",
    "EpigeneticMarkers",
    "Genome",
    "Ribosome",
    "OllamaBackend",
    "CodonChunker",
    "CodonEncoder",
    "RawStrand",
    "Codon",
    "HelixContextManager",
    "create_app",
    "HelixError",
    "CodonAlignmentError",
    "PromoterMismatch",
    "FoldingError",
    "TranscriptionError",
    "GenomeFullError",
    # Packet-mode schemas
    "ContextItem",
    "ContextPacket",
    "RefreshTarget",
    # Agentome aliases
    "AgentomeConfig",
    "AgentomeManager",
]
