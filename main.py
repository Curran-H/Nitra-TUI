from textual.app import App, ComposeResult

from layout import NitraLayout


class NitraApp(App):
    """Main application entry point."""

    CSS_PATH = "styles.css"

    def compose(self) -> ComposeResult:
        yield NitraLayout()


if __name__ == "__main__":
    NitraApp().run()
