from __future__ import annotations

from _loader import load_module


task_03 = load_module("task_03_even_range.py", "task_03_even_range")


def test_even_numbers_in_range_mixed() -> None:
    assert task_03.even_numbers_in_range(3, 11) == [4, 6, 8, 10]


def test_even_numbers_in_range_single_even() -> None:
    assert task_03.even_numbers_in_range(8, 8) == [8]


def test_even_numbers_in_range_none() -> None:
    assert task_03.even_numbers_in_range(5, 5) == []


def test_main_retries_when_invalid_range(monkeypatch, capsys) -> None:
    inputs = iter(["10", "5", "2", "8"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    task_03.main()

    captured = capsys.readouterr()
    output_lines = [line.strip() for line in captured.out.strip().splitlines() if line.strip()]
    assert any("A <= B" in line for line in output_lines)
    assert output_lines[-1] == "2 4 6 8"
