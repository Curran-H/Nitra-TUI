from textual.app import App, ComposeResult

from nitra.layout import NitraLayout


class NitraApp(App):
    """Main application class."""

    CSS_PATH = "nitra.css"

    def compose(self) -> ComposeResult:
        yield NitraLayout()


if __name__ == "__main__":
    app = NitraApp()
    app.run()
