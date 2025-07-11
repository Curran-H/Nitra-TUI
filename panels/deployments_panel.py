from textual.widgets import Static

class DeploymentsPanel(Static):
    def compose(self):
        yield Static("Deployments Panel")
