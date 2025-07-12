from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.widgets import Static, Label, Log
from textual.events import Click
from textual.widget import Widget


class LogsPanel(Static):
    """Panel showing real-time logs with interactive controls."""

    def __init__(self) -> None:
        super().__init__(classes="panel", id="logs")
        self._log: Log | None = None
        self.paused: bool = False
        self.auto_scroll: bool = True

    def compose(self) -> ComposeResult:
        yield Static("LOGS", classes="panel-header")

        self._log = Log(highlight=False, classes="log-area")
        self._log.markup = False

        for line in [
            "[INFO] 14:21:34 BUY BTC",
            "[ERROR] 14:21:36 API Timeout",
            "[DEBUG] Polling…",
            "[INFO] 14:22:10 SELL BTC",
            "[INFO] 14:22:55 BUY ETH",
            "[INFO] 14:23:05 BUY DOGE",
        ]:
            self._log.write(line)

        yield self._log

        yield Horizontal(
            Label("[Pause]", id="pause-button"),
            Label("[Clear]", id="clear-button"),
            Label("[Auto-Scroll]", id="autoscroll-button"),
            classes="log-controls",
        )

    def on_click(self, event: Click) -> None:
        target: Widget = event.target

        if target.id == "pause-button":
            self.paused = not self.paused
            target.update("[Resume]" if self.paused else "[Pause]")

        elif target.id == "clear-button" and self._log:
            self._log.clear()

        elif target.id == "autoscroll-button":
            self.auto_scroll = not self.auto_scroll
            target.update("[Auto-Scroll: ON]" if self.auto_scroll else "[Auto-Scroll: OFF]")

    def write_log(self, message: str) -> None:
        """External method for writing new logs safely."""
        if self._log and not self.paused:
            self._log.write(message)
            if self.auto_scroll:
                self._log.scroll_end(animate=False)
