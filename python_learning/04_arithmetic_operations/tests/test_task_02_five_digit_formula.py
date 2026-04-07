from __future__ import annotations

import pytest
from _loader import load_module


task_02 = load_module("task_02_five_digit_formula.py", "task_02_five_digit_formula")


def test_parse_five_digit_number_success() -> None:
    assert task_02.parse_five_digit_number("46275") == 46275
    assert task_02.parse_five_digit_number("-12345") == -12345


def test_parse_five_digit_number_invalid() -> None:
    with pytest.raises(ValueError):
        task_02.parse_five_digit_number("1234")
    with pytest.raises(ValueError):
        task_02.parse_five_digit_number("12a45")


def test_calculate_special_value_example() -> None:
    assert task_02.calculate_special_value(46275) == -16807.0


def test_calculate_special_value_zero_division() -> None:
    with pytest.raises(ZeroDivisionError):
        task_02.calculate_special_value(55421)


def test_main_retries_after_invalid_input(monkeypatch, capsys) -> None:
    inputs = iter(["1234", "46275"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    task_02.main()

    captured = capsys.readouterr()
    assert "Нужно ввести пятизначное целое число." in captured.out
    assert "Результат: -16807.0" in captured.out
