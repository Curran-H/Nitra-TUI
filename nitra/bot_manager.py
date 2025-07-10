"""Simple singleton-style bot manager with mock data updates."""

from __future__ import annotations

from dataclasses import dataclass, field
from random import choice, gauss, randint
from typing import ClassVar, List


@dataclass
class Metrics:
    """Represents mock bot metrics."""

    pnl: float = 0.0
    trades: int = 0
    uptime: int = 0  # seconds


@dataclass
class BotManager:
    """Central manager holding bot state and generating mock data."""

    _instance: ClassVar["BotManager" | None] = None

    metrics: Metrics = field(default_factory=Metrics)
    logs: List[str] = field(default_factory=list)
    signals: List[str] = field(default_factory=list)
    commands: List[str] = field(default_factory=list)

    def __new__(cls) -> "BotManager":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    # Update methods -----------------------------------------------------

    def tick(self) -> None:
        """Advance mock data for metrics, logs, and signals."""
        self.update_metrics()
        self.generate_signal()
        self.generate_log()

    def update_metrics(self) -> None:
        """Simulate changing metrics."""
        self.metrics.pnl += gauss(0, 1)
        self.metrics.trades += randint(0, 2)
        self.metrics.uptime += 5

    def generate_signal(self) -> None:
        """Append a random signal."""
        signal = choice(["BUY", "SELL", "HOLD"])
        self.signals.append(signal)
        if len(self.signals) > 50:
            self.signals.pop(0)

    def generate_log(self) -> None:
        """Append a random log entry."""
        entry = f"Log entry {len(self.logs) + 1}"
        self.logs.append(entry)
        if len(self.logs) > 100:
            self.logs.pop(0)

    def add_command(self, command: str) -> None:
        """Record a user command."""
        self.commands.append(command)
        if len(self.commands) > 50:
            self.commands.pop(0)
        self.logs.append(f"Command executed: {command}")


# Convenience accessor -----------------------------------------------------
manager = BotManager()
