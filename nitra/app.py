"""Main application entry for Nitra-TUI."""

from __future__ import annotations

from textual.app import App, ComposeResult

from .bot_manager import manager
from .layout import NitraLayout


class NitraApp(App):
    """Textual application that mounts the main layout."""

    TITLE = "Nitra-TUI"
    CSS_PATH = "styles/base.tcss"
    BINDINGS = [("q", "quit", "Quit")]

    def compose(self) -> ComposeResult:
        yield NitraLayout()

    async def on_mount(self) -> None:
        """Start background updates."""
        self.set_interval(5.0, manager.tick)