from __future__ import annotations

from _loader import load_module


task_03 = load_module("task_03_min_boats.py", "task_03_min_boats")


def test_min_boats_basic_pairing() -> None:
    assert task_03.min_boats(100, [40, 50, 60, 90]) == 3


def test_min_boats_all_single() -> None:
    assert task_03.min_boats(100, [80, 80, 80]) == 3


def test_min_boats_all_pairs() -> None:
    assert task_03.min_boats(120, [40, 50, 60, 70]) == 2


def test_main_prints_min_boats(monkeypatch, capsys) -> None:
    inputs = iter(["100", "4", "40", "50", "60", "90"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    task_03.main()

    captured = capsys.readouterr()
    assert captured.out.strip().endswith("3")
