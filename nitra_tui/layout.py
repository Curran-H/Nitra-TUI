from textual.app import ComposeResult
from textual.containers import Grid

from .panels.deployments_panel import DeploymentsPanel
from .panels.logs_panel import LogsPanel
from .panels.portfolio_panel import PortfolioPanel
from .panels.strategy_detail_panel import StrategyDetailPanel


class NitraLayout(Grid):
    """Grid layout with four panels."""

    def compose(self) -> ComposeResult:
        grid = Grid()
        grid.set_columns("1fr 1fr")
        grid.set_rows("1fr 1fr")
        grid.place(
            deployments=DeploymentsPanel(id="deployments"),
            logs=LogsPanel(id="logs"),
            portfolio=PortfolioPanel(id="portfolio"),
            intel=StrategyDetailPanel(id="intel"),
        )
        yield grid
