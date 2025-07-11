from textual.widgets import Static

class LogsPanel(Static):
    def compose(self):
        yield Static("Logs Panel")
