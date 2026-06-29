from __future__ import annotations

from _loader import load_module


task_01 = load_module("task_01_count_distinct.py", "task_01_count_distinct")


def test_count_distinct() -> None:
    assert task_01.count_distinct([1, 2, 2, 3, 1]) == 3


def test_main_prints_distinct_count(monkeypatch, capsys) -> None:
    inputs = iter(["5", "1 2 2 3 1"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    task_01.main()

    captured = capsys.readouterr()
    assert captured.out.strip().endswith("3")
