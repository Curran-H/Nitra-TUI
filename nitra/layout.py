"""Application layout container."""

from __future__ import annotations

from textual.app import ComposeResult
from textual.containers import Grid

from .panels.deployments_panel import DeploymentsPanel
from .panels.detail_panel import StrategyDetailPanel
from .panels.log_output_panel import LogOutputPanel
from .panels.portfolio_panel import PortfolioPanel


class NitraLayout(Grid):
    """Defines the 2x2 grid layout for the dashboard."""

    def compose(self) -> ComposeResult:
        yield DeploymentsPanel(id="deployments", classes="panel deployments")
        yield LogOutputPanel(id="logs", classes="panel logs")
        yield PortfolioPanel(id="portfolio", classes="panel portfolio")
        yield StrategyDetailPanel(id="intel", classes="panel intel")

