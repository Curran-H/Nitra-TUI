from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import Static


class LogsPanel(Widget):
    """Placeholder logs panel."""

    def __init__(self, *, id: str | None = None, classes: str | None = None) -> None:
        super().__init__(id=id, classes=classes)

    def compose(self) -> ComposeResult:
        yield Static("Logs")
