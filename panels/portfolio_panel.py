from textual.widgets import Static


class PortfolioPanel(Static):
    """Panel for portfolio information."""

    def __init__(self) -> None:
        super().__init__("Portfolio Panel", classes="panel portfolio")
