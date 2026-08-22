"""Browser-side online/offline monitor for PeerNet AI."""

from pathlib import Path

import streamlit.components.v1 as components


_FRONTEND_PATH = Path(__file__).parent / "connectivity_frontend"
_connectivity_monitor = components.declare_component(
    "peernet_connectivity_monitor",
    path=str(_FRONTEND_PATH),
)


def render_connectivity_monitor() -> None:
    """Mount a zero-height monitor that expands when the browser goes offline."""
    _connectivity_monitor(key="peernet_browser_connectivity")
