from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.widgets import Static, Label
try:
    from textual.widgets import TextLog
except ImportError:  # fallback for older Textual versions
    from textual.widgets import Log as TextLog


class LogsPanel(Static):
    """Panel showing placeholder logs."""

    def __init__(self) -> None:
        super().__init__(classes="panel", id="logs")

    def compose(self) -> ComposeResult:
        yield Static("LOGS", classes="panel-header")
        log = TextLog(highlight=False, markup=False, classes="log-area")
        for line in [
            "[INFO] 14:21:34 BUY BTC",
            "[ERROR] 14:21:36 API Timeout",
            "[DEBUG] Polling…",
            "[INFO] 14:22:10 SELL BTC",
            "[INFO] 14:22:55 BUY ETH",
            "[INFO] 14:23:05 BUY DOGE",
        ]:
            log.write(line)
        yield log
        yield Horizontal(
            Label("[Pause]"),
            Label("[Clear]"),
            Label("[Auto-Scroll]") ,
            classes="log-controls",
        )

