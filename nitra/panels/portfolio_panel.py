"""Panel showing portfolio holdings."""

from __future__ import annotations

from textual.app import ComposeResult
from textual.widgets import DataTable
from textual.widget import Widget

from ..data.mock_dashboard import PORTFOLIO


class PortfolioPanel(Widget):
    """Display a summary of portfolio positions."""

    def compose(self) -> ComposeResult:
        table = DataTable(zebra_stripes=True, id="portfolio_table")
        table.add_columns("Token", "Holdings", "Avg Entry", "PnL %", "Status")
        yield table

    async def on_mount(self) -> None:
        self.load_data()

    def load_data(self) -> None:
        """Populate portfolio table with mock data."""
        table = self.query_one(DataTable)
        table.clear()
        for row in PORTFOLIO:
            pnl_style = "green" if row["pnl"] >= 0 else "red"
            status_style = "green" if row["status"] == "LONG" else "red"
            table.add_row(
                row["token"],
                f"{row['holdings']}",
                f"{row['entry']}",
                f"[{pnl_style}]{row['pnl']:.2f}%[/]",
                f"[{status_style}]{row['status']}[/]",
            )
        table.cursor_type = "row"

