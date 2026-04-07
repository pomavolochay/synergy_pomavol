from __future__ import annotations

from _loader import load_module


task_02 = load_module("task_02_last_first_rearrange.py", "task_02_last_first_rearrange")


def test_rearrange_last_first() -> None:
    assert task_02.rearrange_last_first([1, 2, 3, 4]) == [4, 1, 2, 3]
    assert task_02.rearrange_last_first([7]) == [7]


def test_read_n_numbers_retries(monkeypatch, capsys) -> None:
    inputs = iter(["1 2", "1 two 3", "1 2 3"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    values = task_02.read_n_numbers(3)

    captured = capsys.readouterr()
    assert values == [1, 2, 3]
    assert "Нужно ввести ровно 3 чисел." in captured.out
    assert "Все значения должны быть целыми числами." in captured.out


def test_main_prints_rearranged(monkeypatch, capsys) -> None:
    inputs = iter(["5", "10 20 30 40 50"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    task_02.main()

    captured = capsys.readouterr()
    assert captured.out.strip().endswith("50 10 20 30 40")
