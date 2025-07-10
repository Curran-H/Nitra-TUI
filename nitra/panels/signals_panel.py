"""Panel displaying mock trading signals."""

from __future__ import annotations

from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import Log

from ..bot_manager import manager


class SignalsPanel(Widget):
    """Show incoming BUY/SELL/HOLD signals."""

    _last_len: int = 0

    def compose(self) -> ComposeResult:
        yield Log(id="signals_log", highlight=False)

    async def on_mount(self) -> None:
        log = self.query_one("#signals_log", Log)
        for signal in manager.signals:
            log.write(signal)
        log.auto_scroll = True
        self._last_len = len(manager.signals)
        self.set_interval(5.0, self.refresh_signals)

    def refresh_signals(self) -> None:
        log = self.query_one("#signals_log", Log)
        new_signals = manager.signals[self._last_len :]
        for signal in new_signals:
            log.write(signal)
        self._last_len = len(manager.signals)
