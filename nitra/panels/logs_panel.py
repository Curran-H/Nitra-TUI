"""Panel showing debug logs."""

from __future__ import annotations

from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import Log

from ..bot_manager import manager


class LogsPanel(Widget):
    """Scrollable panel that displays log entries."""

    _last_len: int = 0

    def compose(self) -> ComposeResult:
        yield Log(id="logs_log", highlight=False)

    async def on_mount(self) -> None:
        log = self.query_one("#logs_log", Log)
        for entry in manager.logs:
            log.write(entry)
        log.auto_scroll = True
        self._last_len = len(manager.logs)
        self.set_interval(5.0, self.refresh_logs)

    def refresh_logs(self) -> None:
        log = self.query_one("#logs_log", Log)
        for entry in manager.logs[self._last_len:]:
            log.write(entry)
        self._last_len = len(manager.logs)
