from __future__ import annotations

import pytest

from _loader import load_module


task_02 = load_module("task_02_turtle.py", "task_02_turtle")


def test_turtle_moves() -> None:
    turtle = task_02.Turtle(0, 0, 3)

    turtle.go_up()
    turtle.go_right()
    turtle.go_down()
    turtle.go_left()

    assert (turtle.x, turtle.y) == (0, 0)


def test_turtle_evolve_and_degrade() -> None:
    turtle = task_02.Turtle(step=2)

    turtle.evolve()
    turtle.degrade()

    assert turtle.s == 2


def test_turtle_degrade_rejects_zero_step() -> None:
    turtle = task_02.Turtle(step=1)

    with pytest.raises(ValueError):
        turtle.degrade()


def test_turtle_rejects_invalid_initial_step() -> None:
    with pytest.raises(ValueError):
        task_02.Turtle(step=0)


def test_count_moves() -> None:
    turtle = task_02.Turtle(0, 0, 3)

    assert turtle.count_moves(10, 7) == 7


def test_count_moves_from_shifted_position() -> None:
    turtle = task_02.Turtle(2, -1, 4)

    assert turtle.count_moves(10, 7) == 4
