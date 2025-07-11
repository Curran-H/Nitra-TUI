from textual.app import App, ComposeResult

from .layout import NitraLayout


class NitraApp(App):
    """Main application class."""

    def compose(self) -> ComposeResult:
        yield NitraLayout()


if __name__ == "__main__":
    app = NitraApp()
    app.run()
