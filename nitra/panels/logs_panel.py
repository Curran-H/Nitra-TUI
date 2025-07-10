"""Panel showing debug logs."""

from __future__ import annotations

from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import TextLog

from ..bot_manager import manager


class LogsPanel(Widget):
    """Scrollable panel that displays log entries."""

    _last_len: int = 0

    def compose(self) -> ComposeResult:
        yield TextLog(id="logs_log", highlight=False)

    async def on_mount(self) -> None:
        log = self.query_one("#logs_log", TextLog)
        for entry in manager.logs:
            log.write_line(entry)
        self._last_len = len(manager.logs)
        log.auto_scroll_bottom = True
        self.set_interval(5.0, self.refresh_logs)

    def refresh_logs(self) -> None:
        log = self.query_one("#logs_log", TextLog)
        for entry in manager.logs[self._last_len :]:
            log.write_line(entry)
        self._last_len = len(manager.logs)