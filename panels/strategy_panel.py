from textual.widgets import Static


class StrategyPanel(Static):
    """Panel displaying strategy information."""

    def __init__(self) -> None:
        super().__init__("Strategy Panel", classes="panel strategy")
