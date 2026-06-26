"""The game world: a grid of terrain cells with forests, rivers and fires."""

from __future__ import annotations

from random import Random

from forest_guard.config import (
    FOREST_DENSITY,
    MAX_SIZE,
    MIN_SIZE,
    RIVER_COUNT,
    RIVER_LENGTH,
    Terrain,
)
from forest_guard.geometry import Position, random_position


class World:
    """Rectangular map storing terrain and the rules that change it."""

    def __init__(self, width: int, height: int, rng: Random | None = None) -> None:
        if not (MIN_SIZE <= width <= MAX_SIZE and MIN_SIZE <= height <= MAX_SIZE):
            raise ValueError(
                f"Размеры поля должны быть в диапазоне {MIN_SIZE}..{MAX_SIZE}."
            )
        self.width = width
        self.height = height
        self._rng = rng or Random()
        self.grid: list[list[Terrain]] = [
            [Terrain.EMPTY for _ in range(width)] for _ in range(height)
        ]

    @classmethod
    def generated(cls, width: int, height: int, rng: Random | None = None) -> "World":
        """Build a world and populate it with forest, rivers and buildings."""
        world = cls(width, height, rng)
        world._grow_initial_forest()
        for _ in range(RIVER_COUNT):
            world._carve_river(RIVER_LENGTH)
        world._place_feature(Terrain.HOSPITAL)
        world._place_feature(Terrain.SHOP)
        return world

    def in_bounds(self, position: Position) -> bool:
        """Return True if the position lies inside the map."""
        return 0 <= position.row < self.height and 0 <= position.col < self.width

    def terrain_at(self, position: Position) -> Terrain:
        """Return the terrain type at the given position."""
        return self.grid[position.row][position.col]

    def grow_tree(self) -> bool:
        """Grow a tree on a random empty or scorched cell. Return True on success."""
        position = self._random_position()
        if self.terrain_at(position) in (Terrain.EMPTY, Terrain.SCORCHED):
            self._set(position, Terrain.TREE)
            return True
        return False

    def ignite(self, count: int) -> int:
        """Set fire to up to `count` random trees. Return how many ignited."""
        ignited = 0
        for _ in range(count):
            position = self._random_position()
            if self.terrain_at(position) is Terrain.TREE:
                self._set(position, Terrain.FIRE)
                ignited += 1
        return ignited

    def extinguish(self, position: Position) -> bool:
        """Put out a fire, restoring the tree. Return True if there was a fire."""
        if self.terrain_at(position) is Terrain.FIRE:
            self._set(position, Terrain.TREE)
            return True
        return False

    def spread_fires(self) -> int:
        """Spread every active fire to adjacent trees; burnt cells become scorched.

        Returns the number of trees that burned down this step so the caller can
        apply the score penalty.
        """
        burning = [
            Position(r, c)
            for r in range(self.height)
            for c in range(self.width)
            if self.grid[r][c] is Terrain.FIRE
        ]
        to_ignite: set[Position] = set()
        for fire in burning:
            for neighbour in fire.neighbours():
                if self.in_bounds(neighbour) and self.terrain_at(neighbour) is Terrain.TREE:
                    to_ignite.add(neighbour)
            self._set(fire, Terrain.SCORCHED)
        for position in to_ignite:
            self._set(position, Terrain.FIRE)
        return len(burning)

    def _grow_initial_forest(self) -> None:
        for row in range(self.height):
            for col in range(self.width):
                if self._rng.random() < FOREST_DENSITY:
                    self.grid[row][col] = Terrain.TREE

    def _carve_river(self, length: int) -> None:
        position = self._random_position()
        self._set(position, Terrain.RIVER)
        steps_left = length
        while steps_left > 0:
            d_row, d_col = self._rng.choice(
                ((-1, 0), (1, 0), (0, -1), (0, 1))
            )
            candidate = position.shifted(d_row, d_col)
            if self.in_bounds(candidate):
                self._set(candidate, Terrain.RIVER)
                position = candidate
                steps_left -= 1

    def _place_feature(self, terrain: Terrain) -> None:
        """Place a unique building on a random empty cell."""
        position = self._random_empty_cell()
        self._set(position, terrain)

    def _random_empty_cell(self, attempts: int = 100) -> Position:
        for _ in range(attempts):
            position = self._random_position()
            if self.terrain_at(position) is Terrain.EMPTY:
                return position
        for row in range(self.height):
            for col in range(self.width):
                if self.grid[row][col] is Terrain.EMPTY:
                    return Position(row, col)
        raise RuntimeError("На карте не осталось свободных клеток.")

    def _random_position(self) -> Position:
        return random_position(self._rng, self.width, self.height)

    def _set(self, position: Position, terrain: Terrain) -> None:
        self.grid[position.row][position.col] = terrain

    def to_dict(self) -> dict:
        """Serialize the world into a plain JSON-friendly dictionary."""
        return {
            "width": self.width,
            "height": self.height,
            "grid": [[int(cell) for cell in row] for row in self.grid],
        }

    @classmethod
    def from_dict(cls, data: dict, rng: Random | None = None) -> "World":
        """Rebuild a world from a dictionary produced by :meth:`to_dict`."""
        world = cls(data["width"], data["height"], rng)
        world.grid = [[Terrain(cell) for cell in row] for row in data["grid"]]
        return world
