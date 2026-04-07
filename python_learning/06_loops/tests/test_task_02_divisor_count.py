from __future__ import annotations

from _loader import load_module


task_02 = load_module("task_02_divisor_count.py", "task_02_divisor_count")


def test_count_divisors_small_values() -> None:
    assert task_02.count_divisors(1) == 1
    assert task_02.count_divisors(6) == 4
    assert task_02.count_divisors(36) == 9


def test_count_divisors_large_value() -> None:
    assert task_02.count_divisors(1_000_000_000) == 100


def test_read_natural_number_retries(monkeypatch, capsys) -> None:
    inputs = iter(["abc", "0", "-1", "17"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    value = task_02.read_natural_number("Введите X: ")

    captured = capsys.readouterr()
    assert value == 17
    assert "Введите корректное целое число." in captured.out
    assert "Число должно быть натуральным" in captured.out


def test_main_prints_divisor_count(monkeypatch, capsys) -> None:
    monkeypatch.setattr("builtins.input", lambda _: "12")

    task_02.main()

    captured = capsys.readouterr()
    assert captured.out.strip() == "6"
