"""User command input panel."""

from __future__ import annotations

from textual.app import ComposeResult
from textual.containers import Vertical
from textual.widgets import Input, Log
from textual.widget import Widget

from ..bot_manager import manager


class CommandPanel(Widget):
    """Panel for entering commands and viewing command history."""

    def compose(self) -> ComposeResult:
        with Vertical():
            yield Log(id="command_log", highlight=False)
            yield Input(placeholder="Enter command...", id="command_input")

    async def on_mount(self) -> None:
        """Populate initial command history."""
        log = self.query_one("#command_log", Log)
        for cmd in manager.commands:
            log.write(cmd)
        log.auto_scroll = True

    async def on_input_submitted(self, event: Input.Submitted) -> None:
        """Handle user command submission."""
        command = event.value.strip()
        if command:
            manager.add_command(command)
            log = self.query_one("#command_log", Log)
            log.write(command)
        event.input.value = ""
