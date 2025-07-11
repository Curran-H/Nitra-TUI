from textual.widgets import Static


class DeploymentsPanel(Static):
    """Panel displaying fake deployment status."""

    def __init__(self) -> None:
        content = (
            "[b]\u2593\u2593 DEPLOYMENTS \u2593\u2593[/b]\n\n"
            "Momentum: \u2714 BTC \u2714 ETH \u2716 LTC\n"
            "Scalper:  \u2714 SOL \u2716 DOGE \u2716 XRP\n\n"
            "[Group \u25BE]  or  [Matrix View]"
        )
        super().__init__(content, classes="panel")
        self.id = "deployments"

