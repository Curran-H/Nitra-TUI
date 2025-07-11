"""Panel listing active strategy deployments."""

from __future__ import annotations

from typing import Iterable

from textual.app import ComposeResult
from textual.widgets import DataTable
from textual.widget import Widget

from ..data.mock_dashboard import DEPLOYMENTS


class DeploymentsPanel(Widget):
    """Display deployments grouped by strategy name."""

    def compose(self) -> ComposeResult:
        table = DataTable(zebra_stripes=True, id="deployments_table")
        table.add_columns("Asset", "PnL %", "Status", "Signal")
        yield table

    async def on_mount(self) -> None:
        self.load_data()
        self.query_one(DataTable).focus()

    def load_data(self) -> None:
        """Populate the deployments table with mock data."""
        table = self.query_one(DataTable)
        table.clear()
        for strategy, deployments in DEPLOYMENTS.items():
            table.add_row(f"[b]{strategy}[/b]", "", "", "", style="bold")
            for dep in deployments:
                pnl_style = "green" if dep.pnl >= 0 else "red"
                signal_style = {
                    "BUY": "green",
                    "SELL": "red",
                    "HOLD": "yellow",
                }[dep.signal]
                table.add_row(
                    f"  {dep.asset}",
                    f"[{pnl_style}]{dep.pnl:.2f}%[/]",
                    dep.status,
                    f"[{signal_style}][{dep.signal}][/]",
                )

