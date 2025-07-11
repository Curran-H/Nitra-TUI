from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.widgets import Static, Label


class StrategyPanel(Static):
    """Panel with mock strategy configuration."""

    def __init__(self) -> None:
        super().__init__(classes="panel", id="strategy")

    def compose(self) -> ComposeResult:
        yield Static("STRATEGY", classes="panel-header")
        yield Static("Strategy: Scalper-V2")
        yield Static("Pair: ETH/USDT")
        yield Horizontal(
            Static("TP", classes="metric"),
            Static("5.0%", classes="metric-value"),
        )
        yield Horizontal(
            Static("SL", classes="metric"),
            Static("2.0%", classes="metric-value"),
        )
        yield Static("Cooldown: 2m")
        yield Static("Recent Trades: BUY @ 13:55, SELL @ 14:05")
        yield Label("[ Full Screen ]")

