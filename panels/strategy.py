from textual.widgets import Static


class StrategyPanel(Static):
    """Panel with mock strategy configuration."""

    def __init__(self) -> None:
        content = (
            "[b]\u2593\u2593 STRATEGY \u2593\u2593[/b]\n\n"
            "Strategy: Scalper-V2\n"
            "Pair: ETH/USDT\n"
            "TP: 5.0%, SL: 2.0%\n"
            "Cooldown: 2m\n"
            "Recent Trades: BUY @ 13:55, SELL @ 14:05\n\n"
            "[ Full-Screen ]"
        )
        super().__init__(content, classes="panel")
        self.id = "strategy"

