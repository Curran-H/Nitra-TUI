from textual.widgets import Static

class PortfolioPanel(Static):
    def compose(self):
        yield Static("Portfolio Panel")
