"""Panel displaying mock trading signals."""

from __future__ import annotations

from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import TextLog

from ..bot_manager import manager


class SignalsPanel(Widget):
    """Show incoming BUY/SELL/HOLD signals."""

    _last_len: int = 0

    def compose(self) -> ComposeResult:
        yield TextLog(id="signals_log", highlight=False)

    async def on_mount(self) -> None:
        log = self.query_one("#signals_log", TextLog)
        for s in manager.signals:
            log.write_line(s)
        self._last_len = len(manager.signals)
        log.auto_scroll_bottom = True
        self.set_interval(5.0, self.refresh_signals)

    def refresh_signals(self) -> None:
        log = self.query_one("#signals_log", TextLog)
        for s in manager.signals[self._last_len :]:
            log.write_line(s)
        self._last_len = len(manager.signals)