from textual.widgets import Static


class LogsPanel(Static):
    """Panel showing logs."""

    def __init__(self) -> None:
        super().__init__("Logs Panel", classes="panel logs")
