# panels/portfolio.py
"""
portfolio.py – concise value overview + tiny ASCII trend graph (refined styling)
"""

from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.widgets import Static

__all__ = ["PortfolioPanel"]


class PortfolioPanel(Static):
    """Displays high-level portfolio metrics."""

    DEFAULT_CSS = """
    PortfolioPanel {
        border: round #5b5b7a;
        padding: 1;
        background: #2e2e3f;
    }
    PortfolioPanel > .panel-header {
        background: #444464;
        color: #ffffff;
        padding: 0 1;
        dock: top;
        height: 1;
    }
    PortfolioPanel .toggle {
        padding: 0 1 1 2;
    }
    PortfolioPanel .metric {
        padding: 0 2;
    }
    PortfolioPanel .metric-value {
        text-align: right;
    }
    """

    def __init__(self) -> None:
        super().__init__(classes="panel", id="portfolio")
        self._metrics = [
            ("Total (USD)", "$14,203.78"),
            ("Total (ETH)", "4.02"),
            ("PNL (7d)", "▲ +4.72%"),
            ("Exposure", "84.5%"),
        ]
        self._trend = "▁▂▃▄▅▆▇█▇▆▄▃▂▁"  # ASCII sparkline

    def compose(self) -> ComposeResult:
        yield Static(" PORTFOLIO", classes="panel-header")
        yield Static("[ETH ▼]   [USD ▼]", classes="toggle")

        for label, value in self._metrics:
            yield Horizontal(
                Static(label, classes="metric"),
                Static(value, classes="metric-value"),
            )

        yield Static(f"Trend (7d): {self._trend}", classes="metric")
