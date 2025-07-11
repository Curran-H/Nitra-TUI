from textual.widgets import Static

class StrategyPanel(Static):
    def compose(self):
        yield Static("Strategy Panel")
