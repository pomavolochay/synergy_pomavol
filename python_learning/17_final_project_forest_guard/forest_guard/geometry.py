"""Geometry primitives and random helpers shared across the game."""

from __future__ import annotations

from dataclasses import dataclass
from random import Random
from typing import Final

CARDINAL_OFFSETS: Final[tuple[tuple[int, int], ...]] = (
    (-1, 0),  # up
    (1, 0),  # down
    (0, -1),  # left
    (0, 1),  # right
)


@dataclass(frozen=True, slots=True)
class Position:
    """Immutable cell coordinate (row, col) used as a value object."""

    row: int
    col: int

    def shifted(self, d_row: int, d_col: int) -> "Position":
        """Return a new position moved by the given row/column delta."""
        return Position(self.row + d_row, self.col + d_col)

    def neighbours(self) -> tuple["Position", ...]:
        """Return the four orthogonal neighbours of this position."""
        return tuple(self.shifted(dr, dc) for dr, dc in CARDINAL_OFFSETS)


def random_position(rng: Random, width: int, height: int) -> Position:
    """Return a uniformly random position inside a width x height grid."""
    return Position(rng.randrange(height), rng.randrange(width))
