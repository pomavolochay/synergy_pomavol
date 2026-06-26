from __future__ import annotations

from random import Random

import _loader
from forest_guard.config import Terrain
from forest_guard.geometry import Position
from forest_guard.world import World


def empty_world(width: int = 5, height: int = 5) -> World:
    """A bare world with all cells empty (no random generation)."""
    return World(width, height, Random(0))


def test_in_bounds() -> None:
    world = empty_world(6, 5)

    assert world.in_bounds(Position(0, 0))
    assert world.in_bounds(Position(4, 5))
    assert not world.in_bounds(Position(-1, 0))
    assert not world.in_bounds(Position(5, 0))  # row == height
    assert not world.in_bounds(Position(0, 6))  # col == width


def test_generated_world_has_buildings() -> None:
    world = World.generated(20, 10, Random(1))
    terrains = {cell for row in world.grid for cell in row}

    assert Terrain.HOSPITAL in terrains
    assert Terrain.SHOP in terrains
    assert Terrain.RIVER in terrains


def test_grow_tree_only_fills_empty_or_scorched() -> None:
    world = empty_world()

    assert world.grow_tree() is True
    trees = sum(cell is Terrain.TREE for row in world.grid for cell in row)
    assert trees == 1


def test_extinguish_restores_tree() -> None:
    world = empty_world()
    world.grid[2][2] = Terrain.FIRE

    assert world.extinguish(Position(2, 2)) is True
    assert world.terrain_at(Position(2, 2)) is Terrain.TREE
    assert world.extinguish(Position(2, 2)) is False  # no fire anymore


def test_spread_fires_scorches_source_and_ignites_neighbours() -> None:
    world = empty_world()
    world.grid[2][2] = Terrain.FIRE
    world.grid[2][1] = Terrain.TREE
    world.grid[1][2] = Terrain.TREE

    burned = world.spread_fires()

    assert burned == 1
    assert world.terrain_at(Position(2, 2)) is Terrain.SCORCHED
    assert world.terrain_at(Position(2, 1)) is Terrain.FIRE
    assert world.terrain_at(Position(1, 2)) is Terrain.FIRE


def test_invalid_size_is_rejected() -> None:
    import pytest

    with pytest.raises(ValueError):
        World(2, 2)
