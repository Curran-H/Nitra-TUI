"""Panel providing strategy details."""

from __future__ import annotations

from textual.app import ComposeResult
from textual.widgets import Static

from ..data.mock_dashboard import STRATEGY_INTEL


class StrategyDetailPanel(Static):
    """Display information about the selected strategy."""

    def __init__(self, strategy: str = "mean_rev") -> None:
        super().__init__(id="strategy_detail")
        self.strategy = strategy

    def compose(self) -> ComposeResult:
        yield Static(id="detail_content")

    async def on_mount(self) -> None:
        self.update_details(self.strategy)

    def update_details(self, name: str) -> None:
        """Update the panel with details for ``name``."""
        data = STRATEGY_INTEL.get(name, {})
        text = (
            f"[b]{name}[/b]\n"
            f"Active deployments: {data.get('active', 0)}\n"
            f"Max drawdown: {data.get('max_drawdown', 'N/A')}\n"
            f"24h ROI: {data.get('roi_24h', '0%')}\n"
            f"Avg signal latency: {data.get('latency', '-')}"
        )
        self.query_one("#detail_content", Static).update(text)

