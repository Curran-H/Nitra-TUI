"""Panel showing mock bot metrics."""

from __future__ import annotations

from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import Static

from ..bot_manager import manager


class MetricsPanel(Widget):
    """Display metrics that update periodically."""

    def compose(self) -> ComposeResult:
        yield Static(id="metrics_text")

    async def on_mount(self) -> None:
        self.refresh_metrics()
        self.set_interval(5.0, self.refresh_metrics)

    def refresh_metrics(self) -> None:
        metrics = manager.metrics
        text = (
            f"PnL: {metrics.pnl:.2f}\n"
            f"Trades: {metrics.trades}\n"
            f"Uptime: {metrics.uptime}s"
        )
        self.query_one("#metrics_text", Static).update(text)
