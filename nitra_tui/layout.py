from textual.app import ComposeResult
from textual.containers import Grid

from nitra_tui.panels.deployments import DeploymentsPanel
from nitra_tui.panels.logs import LogsPanel
from nitra_tui.panels.portfolio import PortfolioPanel
from nitra_tui.panels.strategy import StrategyPanel


class NitraLayout(Grid):
    """Grid layout containing the main dashboard panels."""

    def compose(self) -> ComposeResult:
        yield DeploymentsPanel()
        yield LogsPanel()
        yield PortfolioPanel()
        yield StrategyPanel()
