from textual.app import ComposeResult
from textual.widgets import Static
from textual.widgets import Log



class LogsPanel(Static):
    """Panel showing placeholder logs."""

    def __init__(self) -> None:
        super().__init__(classes="panel")
        self.id = "logs"

    def compose(self) -> ComposeResult:
        yield Static("[b]\u2593\u2593 LOGS \u2593\u2593[/b]", classes="header")
        log = Log(highlight=False)
        for line in [
            "[INFO] 14:21:34 BUY BTC",
            "[ERROR] 14:21:36 API Timeout",
            "[DEBUG] Polling…",
            "[INFO] 14:22:10 SELL BTC",
            "[INFO] 14:22:55 BUY ETH",
        ]:
            log.write(line)
        yield log
        yield Static("[Filter \u25BE] [Pause] [Clear] [Auto-Scroll: ON]", classes="footer")

