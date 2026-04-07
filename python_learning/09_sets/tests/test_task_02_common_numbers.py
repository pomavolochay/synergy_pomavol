from __future__ import annotations

from _loader import load_module


task_02 = load_module("task_02_common_numbers.py", "task_02_common_numbers")


def test_count_common_numbers() -> None:
    assert task_02.count_common_numbers([1, 2, 2, 3], [2, 3, 4, 4]) == 2


def test_parse_int_list_empty() -> None:
    assert task_02.parse_int_list("") == []


def test_main_prints_common_count(monkeypatch, capsys) -> None:
    inputs = iter(["1 2 2 3", "2 3 4"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    task_02.main()

    captured = capsys.readouterr()
    assert captured.out.strip().endswith("2")
