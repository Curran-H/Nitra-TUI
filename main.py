# main.py
"""
Nitra-TUI Main Entry Point
──────────────────────────
• Implements a 2×2 grid for stable layout.
• Loads each panel into its designated cell by yield order.
• Provides a global fullscreen toggle (F) and escape to exit.
"""

from textual.app import App, ComposeResult
from textual.containers import Grid
from textual.widgets import Static
from textual.events import Key

from panels.deployments import DeploymentsPanel
from panels.logs        import LogsPanel
from panels.portfolio   import PortfolioPanel
from panels.strategy    import StrategyPanel

__all__ = ["NitraApp", "NitraLayout"]


class NitraLayout(Grid):
    """2×2 grid that hosts the four main panels."""

    DEFAULT_CSS = """
    NitraLayout {
        grid-size: 2 2;         /* two rows, two columns */
        grid-gutter: 1 1;       /* 1-char gap between panels */
        padding: 1;             /* outer padding around all panels */
        background: $background;/* from styles.css */
    }
    """

    def compose(self) -> ComposeResult:
        # Row-major placement:
        #   [ Deployments | Logs ]
        #   [ Portfolio   | Strategy ]
        yield DeploymentsPanel()
        yield LogsPanel()
        yield PortfolioPanel()
        yield StrategyPanel()


class NitraApp(App[None]):
    """Main application entry point for Nitra-TUI."""

    CSS_PATH = "styles.css"
    BINDINGS = [
        ("f",      "toggle_fullscreen", "Toggle Fullscreen"),
        ("escape","exit_fullscreen",    "Exit Fullscreen"),
    ]

    _fullscreen_widget: Static | None = None

    def compose(self) -> ComposeResult:
        yield NitraLayout()

    def action_toggle_fullscreen(self) -> None:
        focused = self.focused
        if not isinstance(focused, Static):
            return
        if self._fullscreen_widget is None:
            self._fullscreen_widget = focused
            focused.styles.dock = "full"
        elif self._fullscreen_widget is focused:
            focused.styles.dock = None
            self._fullscreen_widget = None

    def action_exit_fullscreen(self) -> None:
        if self._fullscreen_widget:
            self.action_toggle_fullscreen()


if __name__ == "__main__":
    NitraApp().run()
