# panels/deployments.py
"""
deployments.py – DeploymentsPanel with expanded coin/strategy matrix,
dynamic summary, sparkline, and bottom controls.
"""

from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.widgets import Static, Button, DataTable

__all__ = ["DeploymentsPanel"]

CELL_ON  = "✅"
CELL_OFF = "❌"


class DeploymentsPanel(Static):
    DEFAULT_CSS = """
    DeploymentsPanel {
        border: round #5b5b7a;
        background: #2e2e3f;
        padding: 1;
    }
    DeploymentsPanel > .panel-header {
        height: 1;
        padding: 0 1;
        background: #444464;
        color: #ffffff;
    }
    DeploymentsPanel .summary {
        height: 1;
        padding: 0 1;
        color: #cccccc;
    }
    DeploymentsPanel DataTable {
        height: auto;
        background: #1e1e2e;
        padding: 0 1;
    }
    DeploymentsPanel .sparkline {
        height: 1;
        padding: 0 1;
        color: #8ab8ff;
    }
    DeploymentsPanel .controls {
        dock: bottom;
        height: 3;
        padding: 0 1;
    }
    DeploymentsPanel .controls Button {
        margin-right: 1;
        background: #444464;
        color: #ffffff;
    }
    """

    def __init__(self) -> None:
        super().__init__(classes="panel", id="deployments")

        # 7 strategies
        self._strategies = [
            "Momentum",
            "Scalper",
            "MeanRev",
            "Breako",
            "TrendF",
            "GridT",
            "MktMk",
        ]

        # 10 coins
        self._assets = [
            "BTC", "ETH", "DOGE",
            "XRP", "XLM", "SOL",
            "ADA", "SUI", "LINK", "LTC",
        ]

        # deployment on/off map
        self._matrix = {
            (s, a): False
            for s in self._strategies
            for a in self._assets
        }

        # pre-activate a couple
        self._matrix[("Momentum", "BTC")] = True
        self._matrix[("Momentum", "ETH")] = True

        # advanced vs minimized
        self._mode_advanced = False

        # history for sparkline
        self._history = []

        # widget placeholders
        self._header  = None  # Static
        self._summary = None  # Static
        self._table   = None  # DataTable
        self._spark   = None  # Static
        self._ctrls   = None  # Horizontal

    def compose(self) -> ComposeResult:
        # Title bar
        self._header = Static(" DEPLOYMENTS", classes="panel-header")
        yield self._header

        # Summary line
        self._summary = Static("", classes="summary")
        yield self._summary

        # Deployment table
        self._table = DataTable(id="deployments-table")
        yield self._table

        # Sparkline filler
        self._spark = Static("", classes="sparkline")
        yield self._spark

        # Bottom controls
        self._ctrls = Horizontal(
            Button("Panic Off All",   id="panic-button"),
            Button("Activate All",    id="activate-all-button"),
            Button("Advanced View",   id="toggle-adv-button"),
            classes="controls",
        )
        yield self._ctrls

    def on_mount(self) -> None:
        # Initial render
        self._refresh_table()

    def _refresh_table(self) -> None:
        if not self._table:
            return

        # clear old
        self._table.clear(columns=True)

        if self._mode_advanced:
            # full breakdown
            self._table.add_columns("Strategy", "Asset", "PnL", "Trades", "Status")
            for (s, a), active in self._matrix.items():
                pnl    = "0.0%"                  
                trades = "0"                    
                status = "Active" if active else "Paused"
                self._table.add_row(s, a, pnl, trades, status)

            # clear summary & spark
            self._summary.update("")
            self._spark.update("")
        else:
            # minimized matrix
            self._table.add_columns("Strat", *self._assets, "PnL", "TR")
            for s in self._strategies:
                pnl    = "+1.2%" if s == "Momentum" else "+0.8%"
                trades = "24"    if s == "Momentum" else "30"
                row    = [s[:5]] + [
                    CELL_ON if self._matrix[(s, a)] else CELL_OFF
                    for a in self._assets
                ] + [pnl, trades]
                self._table.add_row(*row, key=s)

            # update summary
            total  = len(self._matrix)
            active = sum(self._matrix.values())
            top    = next((s for (s,a),v in self._matrix.items() if v), "None")
            self._summary.update(
                f"Active Deploys: {active} of {total}   Top Strat: {top}"
            )

            # update sparkline
            self._history.append(active)
            self._history = self._history[-20:]
            bars = "▁▂▃▄▅▆▇"
            mx   = max(self._history) or 1
            chart = "".join(
                bars[int((val / mx) * (len(bars) - 1))]
                for val in self._history
            )
            self._spark.update(chart)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        btn = event.button.id

        if btn == "panic-button":
            for k in self._matrix:
                self._matrix[k] = False

        elif btn == "activate-all-button":
            for k in self._matrix:
                self._matrix[k] = True

        elif btn == "toggle-adv-button":
            self._mode_advanced = not self._mode_advanced
            event.button.label = (
                "Minimized View" if self._mode_advanced else "Advanced View"
            )

        self._refresh_table()

    def on_data_table_cell_selected(self, event) -> None:
        if self._mode_advanced:
            return

        col = event.coordinate.column
        # only asset columns (1..len(self._assets))
        if not (1 <= col <= len(self._assets)):
            return

        strat = event.key
        asset = self._assets[col - 1]
        new   = not self._matrix[(strat, asset)]
        self._matrix[(strat, asset)] = new
        self._table.update_cell(event.coordinate, CELL_ON if new else CELL_OFF)
