from textual.app import ComposeResult
from textual.containers import Grid

from panels.deployments import DeploymentsPanel
from panels.logs import LogsPanel
from panels.portfolio import PortfolioPanel
from panels.strategy import StrategyPanel


class NitraLayout(Grid):
    """Grid layout containing the main dashboard panels."""

    def compose(self) -> ComposeResult:
        yield DeploymentsPanel()
        yield LogsPanel()
        yield PortfolioPanel()
        yield StrategyPanel()
