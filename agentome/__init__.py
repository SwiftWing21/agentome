"""
Agentome — Genome-based context compression for AI agents.

This is the reference implementation, powered by Helix Context.
Agentome is the concept; Helix Context is the engine.

    pip install agentome

is equivalent to:

    pip install helix-context

All public APIs are re-exported from helix_context.
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
    # Agentome aliases
    "AgentomeConfig",
    "AgentomeManager",
]
