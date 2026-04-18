"""Submodule re-export for agentome consumers who prefer the path form.

    from agentome.context_packet import build_context_packet, get_refresh_targets

is equivalent to:

    from helix_context.context_packet import build_context_packet, get_refresh_targets

The packet builder + refresh-plan helper shipped in helix-context
0.4.0b1. See the agent-context-index build spec at
docs/specs/2026-04-17-agent-context-index-build-spec.md in the
helix-context repo for the authoritative design.
"""

from helix_context.context_packet import (  # noqa: F401
    build_context_packet,
    get_refresh_targets,
)

__all__ = ["build_context_packet", "get_refresh_targets"]
