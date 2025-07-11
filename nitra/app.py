"""Main application entry for Nitra-TUI."""

from __future__ import annotations

from textual.app import App, ComposeResult
from textual.widgets import Footer

from .bot_manager import manager
from .layout import NitraLayout


class NitraApp(App):
    """Textual application that mounts the main layout."""

    TITLE = "Nitra-TUI"
    CSS_PATH = "styles/base.tcss"
    BINDINGS = [
        ("q", "quit", "Quit"),
        ("tab", "focus_next", "Next Panel"),
        ("enter", "toggle_fullscreen", "Toggle Panel"),
        ("right", "intel_fullscreen", "Intel Full"),
        ("p", "pause", "Pause"),
        ("r", "resume", "Resume"),
    ]

    def compose(self) -> ComposeResult:
        yield NitraLayout()
        yield Footer()

    async def on_mount(self) -> None:
        """Start background updates."""
        self.set_interval(5.0, manager.tick)

    def action_toggle_fullscreen(self) -> None:
        """Toggle focused panel between normal and full-screen."""
        focused = self.focused
        if not focused:
            return
        panels = list(self.query(".panel"))
        others_hidden = any(not p.display for p in panels if p is not focused)
        if others_hidden:
            for panel in panels:
                panel.display = True
        else:
            for panel in panels:
                panel.display = panel is focused

    def action_intel_fullscreen(self) -> None:
        """Show the strategy intel panel full-screen."""
        intel = self.query_one("#intel")
        self.set_focus(intel)
        self.action_toggle_fullscreen()

    def action_pause(self) -> None:  # pragma: no cover - placeholder
        pass

    def action_resume(self) -> None:  # pragma: no cover - placeholder
        pass

