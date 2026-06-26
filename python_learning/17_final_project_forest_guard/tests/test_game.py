from __future__ import annotations

from random import Random

import _loader
from forest_guard.config import (
    STORM_DAMAGE,
    TREE_REWARD,
    UPGRADE_TANK_COST,
    Terrain,
    Weather,
)
from forest_guard.game import Game
from forest_guard.geometry import Position


def new_game() -> Game:
    return Game(width=10, height=8, rng=Random(0))


def test_snapshot_round_trip() -> None:
    game = new_game()
    game.helicopter.reward(300)
    game.tick = 7

    restored = new_game()
    restored.restore(game.snapshot())

    assert restored.tick == 7
    assert restored.world.to_dict() == game.world.to_dict()
    assert restored.helicopter.to_dict() == game.helicopter.to_dict()


def test_save_and_load_file(tmp_path) -> None:
    save_file = tmp_path / "savegame.json"
    game = Game(width=10, height=8, rng=Random(0), save_file=str(save_file))
    game.helicopter.reward(123)
    game.save()

    loaded = Game(width=10, height=8, rng=Random(0), save_file=str(save_file))
    loaded.load()

    assert save_file.exists()
    assert loaded.helicopter.score == 123


def test_flying_over_fire_with_water_extinguishes_and_rewards() -> None:
    game = new_game()
    game.helicopter.position = Position(3, 3)
    game.world.grid[3][3] = Terrain.FIRE
    game.helicopter.refill()
    score_before = game.helicopter.score

    game.update()

    assert game.world.terrain_at(Position(3, 3)) is Terrain.TREE
    assert game.helicopter.score == score_before + TREE_REWARD


def test_interact_with_shop_upgrades_tank() -> None:
    game = new_game()
    game.helicopter.position = Position(2, 2)
    game.world.grid[2][2] = Terrain.SHOP
    game.helicopter.reward(UPGRADE_TANK_COST)
    max_tank_before = game.helicopter.max_tank

    game.handle_command("e")

    assert game.helicopter.max_tank == max_tank_before + 1


def test_storm_cell_damages_helicopter() -> None:
    game = new_game()
    game.helicopter.position = Position(1, 1)
    game.sky.grid[1][1] = Weather.STORM
    lives_before = game.helicopter.lives

    game.update()

    assert game.helicopter.lives == lives_before - STORM_DAMAGE


def test_quit_command_ends_game() -> None:
    game = new_game()

    game.handle_command("q")

    assert game.is_over is True
