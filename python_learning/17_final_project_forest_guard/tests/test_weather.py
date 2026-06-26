from __future__ import annotations

from random import Random

import _loader
from forest_guard.config import Weather
from forest_guard.geometry import Position
from forest_guard.weather import Sky


def test_advance_produces_only_valid_states() -> None:
    sky = Sky(8, 6, Random(0))

    sky.advance()

    states = {cell for row in sky.grid for cell in row}
    assert states <= {Weather.CLEAR, Weather.CLOUD, Weather.STORM}


def test_is_storm_matches_grid() -> None:
    sky = Sky(4, 4, Random(0))
    sky.grid[1][2] = Weather.STORM

    assert sky.is_storm(Position(1, 2)) is True
    assert sky.is_storm(Position(0, 0)) is False


def test_advance_is_deterministic_for_a_fixed_seed() -> None:
    first = Sky(8, 6, Random(123))
    second = Sky(8, 6, Random(123))

    first.advance()
    second.advance()

    assert first.grid == second.grid
