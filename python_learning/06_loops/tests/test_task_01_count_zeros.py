from __future__ import annotations

from _loader import load_module


task_01 = load_module("task_01_count_zeros.py", "task_01_count_zeros")


def test_count_zeros() -> None:
    assert task_01.count_zeros([0, 1, 0, -5, 7, 0]) == 3


def test_read_int_retries(monkeypatch, capsys) -> None:
    inputs = iter(["abc", "12"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    value = task_01.read_int("Введите число: ")

    captured = capsys.readouterr()
    assert value == 12
    assert "Введите корректное целое число." in captured.out


def test_main_prints_zero_count(monkeypatch, capsys) -> None:
    inputs = iter(["5", "0", "1", "0", "2", "3"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    task_01.main()

    captured = capsys.readouterr()
    assert captured.out.strip().endswith("2")
