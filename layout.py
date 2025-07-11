from textual.app import ComposeResult
from textual.containers import Container

from panels.deployments_panel import DeploymentsPanel
from panels.logs_panel import LogsPanel
from panels.portfolio_panel import PortfolioPanel
from panels.strategy_panel import StrategyPanel



class NitraLayout(Container):
    """Primary layout container for the application."""

    def compose(self) -> ComposeResult:
        yield DeploymentsPanel()
        yield LogsPanel()
        yield PortfolioPanel()
        yield StrategyPanel()
