from __future__ import annotations

import _loader
import pytest
from forest_guard.geometry import Position
from forest_guard.helicopter import Helicopter


def make_helicopter() -> Helicopter:
    return Helicopter(Position(1, 1), max_tank=2, lives=3)


def in_bounds(position: Position) -> bool:
    return 0 <= position.row < 5 and 0 <= position.col < 5


def test_move_inside_bounds() -> None:
    helicopter = make_helicopter()

    helicopter.move(1, 0, in_bounds)

    assert helicopter.position == Position(2, 1)


def test_move_blocked_outside_bounds() -> None:
    helicopter = Helicopter(Position(0, 0))

    helicopter.move(-1, 0, in_bounds)

    assert helicopter.position == Position(0, 0)


def test_refill_and_use_water() -> None:
    helicopter = make_helicopter()

    helicopter.refill()
    assert helicopter.tank == 2
    assert helicopter.use_water() is True
    assert helicopter.tank == 1


def test_use_water_on_empty_tank() -> None:
    helicopter = make_helicopter()

    assert helicopter.has_water is False
    assert helicopter.use_water() is False


def test_penalize_never_goes_below_zero() -> None:
    helicopter = make_helicopter()
    helicopter.reward(100)

    helicopter.penalize(250)

    assert helicopter.score == 0


def test_buy_tank_upgrade() -> None:
    helicopter = make_helicopter()
    helicopter.reward(500)

    assert helicopter.buy_tank_upgrade(500) is True
    assert helicopter.max_tank == 3
    assert helicopter.score == 0
    assert helicopter.buy_tank_upgrade(500) is False


def test_buy_lives() -> None:
    helicopter = make_helicopter()
    helicopter.reward(1000)

    assert helicopter.buy_lives(1000, 5) is True
    assert helicopter.lives == 8


def test_damage_and_game_over() -> None:
    helicopter = Helicopter(Position(0, 0), lives=2)

    helicopter.damage(1)
    assert helicopter.is_alive is True

    helicopter.damage(5)
    assert helicopter.lives == 0
    assert helicopter.is_alive is False


def test_invalid_initial_state_is_rejected() -> None:
    with pytest.raises(ValueError):
        Helicopter(Position(0, 0), max_tank=0)
    with pytest.raises(ValueError):
        Helicopter(Position(0, 0), lives=-1)


def test_zero_lives_is_a_valid_restorable_state() -> None:
    helicopter = Helicopter(Position(0, 0), lives=0)

    assert helicopter.is_alive is False
