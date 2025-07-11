from textual.widgets import Static


class DeploymentsPanel(Static):
    """Panel displaying deployments."""

    def __init__(self) -> None:
        super().__init__("Deployments Panel", classes="panel deployments")
