"""The player-controlled helicopter: position, water tank, score and lives."""

from __future__ import annotations

from collections.abc import Callable

from forest_guard.config import START_LIVES, START_MAX_TANK
from forest_guard.geometry import Position


class Helicopter:
    """Player avatar carrying water, money (score) and a pool of lives."""

    def __init__(
        self,
        position: Position,
        max_tank: int = START_MAX_TANK,
        lives: int = START_LIVES,
    ) -> None:
        if max_tank <= 0:
            raise ValueError("Объём резервуара должен быть положительным.")
        if lives < 0:
            raise ValueError("Количество жизней не может быть отрицательным.")
        self.position = position
        self.max_tank = max_tank
        self.tank = 0
        self.score = 0
        self.lives = lives

    @property
    def has_water(self) -> bool:
        """Return True if the tank holds at least one unit of water."""
        return self.tank > 0

    @property
    def is_alive(self) -> bool:
        """Return True while the helicopter still has lives left."""
        return self.lives > 0

    def move(self, d_row: int, d_col: int, can_enter: Callable[[Position], bool]) -> None:
        """Move by a delta if the target cell is allowed by `can_enter`."""
        target = self.position.shifted(d_row, d_col)
        if can_enter(target):
            self.position = target

    def refill(self) -> None:
        """Fill the water tank to its current maximum."""
        self.tank = self.max_tank

    def use_water(self) -> bool:
        """Spend one unit of water. Return False if the tank was empty."""
        if not self.has_water:
            return False
        self.tank -= 1
        return True

    def reward(self, points: int) -> None:
        """Add points to the score."""
        self.score += points

    def penalize(self, points: int) -> None:
        """Subtract points from the score, never dropping below zero."""
        self.score = max(0, self.score - points)

    def damage(self, amount: int) -> None:
        """Lose `amount` lives, never dropping below zero."""
        self.lives = max(0, self.lives - amount)

    def buy_tank_upgrade(self, cost: int) -> bool:
        """Spend score to enlarge the tank. Return False if it is unaffordable."""
        if self.score < cost:
            return False
        self.score -= cost
        self.max_tank += 1
        return True

    def buy_lives(self, cost: int, amount: int) -> bool:
        """Spend score to gain lives. Return False if it is unaffordable."""
        if self.score < cost:
            return False
        self.score -= cost
        self.lives += amount
        return True

    def to_dict(self) -> dict:
        """Serialize the helicopter into a plain dictionary."""
        return {
            "row": self.position.row,
            "col": self.position.col,
            "tank": self.tank,
            "max_tank": self.max_tank,
            "score": self.score,
            "lives": self.lives,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Helicopter":
        """Rebuild a helicopter from a dictionary produced by :meth:`to_dict`."""
        helicopter = cls(
            position=Position(data["row"], data["col"]),
            max_tank=data["max_tank"],
            lives=data["lives"],
        )
        helicopter.tank = data["tank"]
        helicopter.score = data["score"]
        return helicopter
