"""Application layout container."""

from textual.containers import Grid
from textual.app import ComposeResult

from .panels.metrics_panel import MetricsPanel
from .panels.signals_panel import SignalsPanel
from .panels.command_panel import CommandPanel
from .panels.logs_panel import LogsPanel


class NitraLayout(Grid):
    """Defines the 2x2 grid layout for the application."""

    def compose(self) -> ComposeResult:
        yield MetricsPanel(id="metrics", classes="panel metrics")
        yield SignalsPanel(id="signals", classes="panel signals")
        yield CommandPanel(id="command", classes="panel command")
        yield LogsPanel(id="logs", classes="panel logs")
