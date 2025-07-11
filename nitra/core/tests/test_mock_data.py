"""Tests for mock dashboard data."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[3]))

from nitra.data import mock_dashboard


def test_deployments_present() -> None:
    assert "mean_rev" in mock_dashboard.DEPLOYMENTS
    assert mock_dashboard.DEPLOYMENTS["mean_rev"]

