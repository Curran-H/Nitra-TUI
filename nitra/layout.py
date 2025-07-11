from textual.app import ComposeResult
from textual.containers import Container

from nitra.panels import (
    DeploymentsPanel,
    LogsPanel,
    PortfolioPanel,
    StrategyPanel,
)


class NitraLayout(Container):
    """Primary layout container for the application."""

    def compose(self) -> ComposeResult:
        yield DeploymentsPanel()
        yield LogsPanel()
        yield PortfolioPanel()
        yield StrategyPanel()
