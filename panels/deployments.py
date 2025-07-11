from textual.app import ComposeResult
from textual.widgets import Static


class DeploymentsPanel(Static):
    """Panel displaying fake deployment status."""

    def __init__(self) -> None:
        super().__init__(classes="panel", id="deployments")

    def compose(self) -> ComposeResult:
        yield Static("DEPLOYMENTS", classes="panel-header")
        yield Static("[Group \u25BE]   [Matrix View]", classes="toggle")
        matrix = "\n".join(
            [
                "           BTC   ETH   DOGE",
                "Momentum   \u2714    \u2714    \u2716",
                "Scalper    \u2714    \u2716    \u2716",
            ]
        )
        yield Static(matrix)

