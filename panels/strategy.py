# panels/strategy.py
"""
strategy.py – active strategy snapshot + tiny price chart (refined styling)
"""

from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.widgets import Static

__all__ = ["StrategyPanel"]


class StrategyPanel(Static):
    """Shows key data for the strategy with highest attention value."""

    DEFAULT_CSS = """
    StrategyPanel {
        border: round #5a5a7a;
        padding: 1;
        background: #2e2e3f;
    }
    StrategyPanel > .panel-header {
        background: #444464;
        color: #ffffff;
        padding: 0 1;
        dock: top;
        height: 1;
    }
    StrategyPanel .metric {
        padding: 0 2;
    }
    StrategyPanel .metric-value {
        text-align: right;
    }
    StrategyPanel .hint {
        color: #8888aa;
        padding-top: 1;
    }
    """

    def __init__(self) -> None:
        super().__init__(classes="panel", id="strategy")
        self._name = "Scalper-V2"
        self._pair = "ETH/USDT"
        self._tp = "5.0%"
        self._sl = "2.0%"
        self._exposure = "60% / $600"
        self._trend = "▁▃▄▅▆▇█▇▅▄▃▂▁"

    def compose(self) -> ComposeResult:
        yield Static(" STRATEGY", classes="panel-header")
        yield Static(f"Strategy: {self._name}")
        yield Static(f"Pair:     {self._pair}")

        yield Horizontal(
            Static("TP", classes="metric"),
            Static(self._tp, classes="metric-value"),
        )
        yield Horizontal(
            Static("SL", classes="metric"),
            Static(self._sl, classes="metric-value"),
        )
        yield Horizontal(
            Static("Exposure", classes="metric"),
            Static(self._exposure, classes="metric-value"),
        )

        yield Static(f"Trend: {self._trend}", classes="metric")
        yield Static("Recent Trades: BUY @ 13:55, SELL @ 14:05", classes="metric")
        yield Static("[Press F to Fullscreen]", classes="hint")
