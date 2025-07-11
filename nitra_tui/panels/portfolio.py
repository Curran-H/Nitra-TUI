from textual.widgets import Static


class PortfolioPanel(Static):
    """Panel displaying mock portfolio metrics."""

    def __init__(self) -> None:
        content = (
            "[b]\u2593\u2593 PORTFOLIO \u2593\u2593[/b]\n\n"
            "Primary Coin: [ ETH \u25BE ]\n"
            "PNL (7d): \u25B2 +4.72%\n"
            "Exposure: 84.5%\n"
            "Total (USD): $14,203.78\n"
            "Total (ETH): 4.02\n"
            "Net Deposits: $2,000\n"
            "Allocation: BTC 30%, ETH 40%, DOGE 20%, LTC 10%"
        )
        super().__init__(content, classes="panel")
        self.id = "portfolio"

