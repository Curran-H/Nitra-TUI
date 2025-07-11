"""Panel streaming log output."""

from __future__ import annotations

from datetime import datetime

from textual.app import ComposeResult
from textual.widgets import Log
from textual.widget import Widget

from ..data.mock_dashboard import LOGS


class LogOutputPanel(Widget):
    """Display a scrollable list of log entries."""

    def compose(self) -> ComposeResult:
        yield Log(id="log_output", highlight=False)

    async def on_mount(self) -> None:
        log = self.query_one(Log)
        for line in LOGS:
            log.write(self._format_line(line))
        log.auto_scroll = True

    def _format_line(self, line: str) -> str:
        timestamp = datetime.now().strftime("%H:%M:%S")
        return f"{timestamp} {line}"

