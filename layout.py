from textual.containers import Grid
from textual.app import ComposeResult
from panels.deployments_panel import DeploymentsPanel
from panels.logs_panel import LogsPanel
from panels.portfolio_panel import PortfolioPanel
from panels.strategy_panel import StrategyPanel

class NitraLayout(Grid):
    def compose(self) -> ComposeResult:
        yield DeploymentsPanel()
        yield LogsPanel()
        yield PortfolioPanel()
        yield StrategyPanel()
