from textual.app import App
from layout import NitraLayout

class NitraApp(App):
    def compose(self):
        yield NitraLayout()

if __name__ == "__main__":
    app = NitraApp()
    app.run()
