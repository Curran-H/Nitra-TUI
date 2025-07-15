# panels/logs.py
"""
logs.py – streaming log viewer with pause / clear / auto-scroll
Uses Button.Pressed for click handling and supports scrollable multiline logs.
"""

from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.widgets import Static, Log, Button

__all__ = ["LogsPanel"]


class LogsPanel(Static):
    """Real-time log viewer with user controls."""

    DEFAULT_CSS = """
    LogsPanel {
        border: round #5a5a7a;
        padding: 1;
        background: #2e2e3f;
    }
    LogsPanel > .panel-header {
        background: #444464;
        color: #ffffff;
        padding: 0 1;
        dock: top;
        height: 1;
    }
    LogsPanel .log-area {
        max-height: 6;
        padding: 1 0 0 2;
        background: #1e1e2e;
        overflow-y: scroll;
    }
    LogsPanel .log-controls {
        padding: 1 0 0 2;
    }
    LogsPanel Button {
        margin-right: 2;
        background: #3b3b5f;
        color: #ffffff;
    }
    """

    def __init__(self) -> None:
        super().__init__(classes="panel", id="logs")
        self._log: Log | None = None
        self.paused: bool = False
        self.auto_scroll: bool = True

    def write_log(self, message: str) -> None:
        """Append to log respecting pause / auto-scroll."""
        if self._log and not self.paused:
            self._log.write(message)
            if self.auto_scroll:
                self._log.scroll_end(animate=False)

    def compose(self) -> ComposeResult:
        # Header
        yield Static(" LOGS", classes="panel-header")

        # The scrollable Log widget
        self._log = Log(highlight=False, classes="log-area")
        self._log.markup = False
        yield self._log

        # Seed some demo entries
        for entry in [
            "[INFO] 14:21:34 BUY BTC",
            "[ERROR] 14:21:36 API Timeout",
            "[DEBUG] Polling…",
            "[INFO] 14:22:10 SELL BTC",
            "[INFO] 14:22:55 BUY ETH",
        ]:
            self.write_log(entry)

        # Control buttons
        yield Horizontal(
            Button("Pause", id="pause-button"),
            Button("Clear", id="clear-button"),
            Button("Auto-Scroll ON", id="autoscroll-button"),
            classes="log-controls",
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle Pause / Clear / Auto-Scroll toggles."""
        btn = event.button
        if btn.id == "pause-button":
            self.paused = not self.paused
            btn.label = "Resume" if self.paused else "Pause"
        elif btn.id == "clear-button" and self._log:
            self._log.clear()
        elif btn.id == "autoscroll-button":
            self.auto_scroll = not self.auto_scroll
            state = "ON" if self.auto_scroll else "OFF"
            btn.label = f"Auto-Scroll {state}"
