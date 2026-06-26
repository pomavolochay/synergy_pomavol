"""Sky model: drifting clouds that can escalate into damaging storms."""

from __future__ import annotations

from random import Random

from forest_guard.config import CLOUD_CHANCE, STORM_CHANCE, Weather
from forest_guard.geometry import Position


class Sky:
    """Weather layer rendered on top of the world and regenerated each cycle."""

    def __init__(self, width: int, height: int, rng: Random | None = None) -> None:
        self.width = width
        self.height = height
        self._rng = rng or Random()
        self.grid: list[list[Weather]] = [
            [Weather.CLEAR for _ in range(width)] for _ in range(height)
        ]

    def weather_at(self, position: Position) -> Weather:
        """Return the weather state at the given position."""
        return self.grid[position.row][position.col]

    def is_storm(self, position: Position) -> bool:
        """Return True if a thunderstorm currently covers the position."""
        return self.weather_at(position) is Weather.STORM

    def advance(self) -> None:
        """Regenerate the weather: scatter clouds, some of which become storms."""
        for row in range(self.height):
            for col in range(self.width):
                self.grid[row][col] = self._roll_cell()

    def _roll_cell(self) -> Weather:
        if self._rng.random() >= CLOUD_CHANCE:
            return Weather.CLEAR
        if self._rng.random() < STORM_CHANCE:
            return Weather.STORM
        return Weather.CLOUD

    def to_dict(self) -> dict:
        """Serialize the sky into a plain dictionary."""
        return {
            "width": self.width,
            "height": self.height,
            "grid": [[int(cell) for cell in row] for row in self.grid],
        }

    @classmethod
    def from_dict(cls, data: dict, rng: Random | None = None) -> "Sky":
        """Rebuild a sky from a dictionary produced by :meth:`to_dict`."""
        sky = cls(data["width"], data["height"], rng)
        sky.grid = [[Weather(cell) for cell in row] for row in data["grid"]]
        return sky
