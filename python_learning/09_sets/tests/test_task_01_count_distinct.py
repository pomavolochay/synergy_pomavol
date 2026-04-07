from __future__ import annotations

from _loader import load_module


task_01 = load_module("task_01_count_distinct.py", "task_01_count_distinct")


def test_count_distinct() -> None:
    assert task_01.count_distinct([1, 2, 2, 3, 1]) == 3


def test_read_n_numbers_retries(monkeypatch, capsys) -> None:
    inputs = iter(["1 2", "1 a 3", "1 2 3"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    values = task_01.read_n_numbers(3)

    captured = capsys.readouterr()
    assert values == [1, 2, 3]
    assert "Нужно ввести ровно 3 чисел." in captured.out
    assert "Все значения должны быть целыми числами." in captured.out


def test_main_prints_distinct_count(monkeypatch, capsys) -> None:
    inputs = iter(["5", "1 2 2 3 1"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    task_01.main()

    captured = capsys.readouterr()
    assert captured.out.strip().endswith("3")
