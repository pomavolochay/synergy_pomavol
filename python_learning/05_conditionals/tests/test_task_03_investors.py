from __future__ import annotations

from _loader import load_module


task_03 = load_module("task_03_investors.py", "task_03_investors")


def test_investment_result_both_can() -> None:
    assert task_03.investment_result(100, 120, 50) == "2"


def test_investment_result_only_mike() -> None:
    assert task_03.investment_result(100, 40, 50) == "Mike"


def test_investment_result_only_ivan() -> None:
    assert task_03.investment_result(30, 60, 50) == "Ivan"


def test_investment_result_only_together() -> None:
    assert task_03.investment_result(30, 25, 50) == "1"


def test_investment_result_none() -> None:
    assert task_03.investment_result(10, 20, 50) == "0"


def test_read_non_negative_int_retries(monkeypatch, capsys) -> None:
    inputs = iter(["abc", "-5", "12"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    value = task_03.read_non_negative_int("Введите число: ")

    captured = capsys.readouterr()
    assert value == 12
    assert "Введите корректное целое число." in captured.out
    assert "Число не может быть отрицательным." in captured.out


def test_main_prints_result(monkeypatch, capsys) -> None:
    inputs = iter(["50", "30", "25"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    task_03.main()

    captured = capsys.readouterr()
    assert captured.out.strip() == "1"
