from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.widgets import Static


class PortfolioPanel(Static):
    """Panel displaying mock portfolio metrics."""

    def __init__(self) -> None:
        super().__init__(classes="panel", id="portfolio")

    def compose(self) -> ComposeResult:
        yield Static("PORTFOLIO", classes="panel-header")
        yield Static("[ETH \u25BE]   [USD \u25BE]", classes="toggle")
        metrics = [
            ("Total (USD)", "$14,203.78"),
            ("Total (ETH)", "4.02"),
            ("PNL (7d)", "\u25B2 +4.72%"),
            ("Exposure", "84.5%"),
        ]
        for label, value in metrics:
            yield Horizontal(
                Static(label, classes="metric"),
                Static(value, classes="metric-value"),
            )

