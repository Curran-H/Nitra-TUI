"""Mock data for the Nitra dashboard panels."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Deployment:
    """Represents a strategy deployment on a particular asset."""

    asset: str
    pnl: float
    status: str
    signal: str


DEPLOYMENTS: Dict[str, List[Deployment]] = {
    "mean_rev": [
        Deployment(asset="ETH", pnl=1.5, status="RUNNING", signal="BUY"),
        Deployment(asset="BTC", pnl=-0.4, status="PAUSED", signal="HOLD"),
    ],
    "scalper": [
        Deployment(asset="ETH", pnl=0.3, status="RUNNING", signal="SELL"),
    ],
}

PORTFOLIO: List[dict[str, float | str]] = [
    {"token": "ETH", "holdings": 2.0, "entry": 1800.0, "pnl": 5.2, "status": "LONG"},
    {"token": "BTC", "holdings": 0.5, "entry": 30000.0, "pnl": -2.1, "status": "SHORT"},
]

STRATEGY_INTEL: Dict[str, dict[str, str | int]] = {
    "mean_rev": {
        "active": 2,
        "max_drawdown": "3%",
        "roi_24h": "1.2%",
        "latency": "120ms",
    },
    "scalper": {
        "active": 1,
        "max_drawdown": "1.5%",
        "roi_24h": "0.8%",
        "latency": "80ms",
    },
}

LOGS: List[str] = [
    "[ETH] initialized",
    "[BTC] price spike detected",
]

