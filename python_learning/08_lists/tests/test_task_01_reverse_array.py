from __future__ import annotations

from _loader import load_module


task_01 = load_module("task_01_reverse_array.py", "task_01_reverse_array")


def test_reverse_array() -> None:
    assert task_01.reverse_array([1, 2, 3, 4]) == [4, 3, 2, 1]


def test_main_prints_reversed(monkeypatch, capsys) -> None:
    inputs = iter(["4", "10", "20", "30", "40"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    task_01.main()

    captured = capsys.readouterr()
    assert captured.out.strip().endswith("40 30 20 10")
