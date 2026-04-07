from __future__ import annotations

from _loader import load_module


task_01 = load_module("task_01_number_description.py", "task_01_number_description")


def test_describe_number_zero() -> None:
    assert task_01.describe_number(0) == "нулевое число"


def test_describe_number_even_numbers() -> None:
    assert task_01.describe_number(190) == "положительное четное число"
    assert task_01.describe_number(-8) == "отрицательное четное число"


def test_describe_number_odd_number() -> None:
    assert task_01.describe_number(7) == "число не является четным"


def test_read_int_retries(monkeypatch, capsys) -> None:
    inputs = iter(["abc", "12"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    value = task_01.read_int("Введите число: ")

    captured = capsys.readouterr()
    assert value == 12
    assert "Введите корректное целое число." in captured.out


def test_main_prints_description(monkeypatch, capsys) -> None:
    monkeypatch.setattr("builtins.input", lambda _: "190")

    task_01.main()

    captured = capsys.readouterr()
    assert captured.out.strip() == "положительное четное число"
