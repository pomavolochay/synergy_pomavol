from __future__ import annotations

import pytest

from _loader import load_module


task_01 = load_module("task_01_factorial_chain.py", "task_01_factorial_chain")


def test_factorial() -> None:
    assert task_01.factorial(1) == 1
    assert task_01.factorial(3) == 6
    assert task_01.factorial(6) == 720


def test_factorial_rejects_non_natural_number() -> None:
    with pytest.raises(ValueError):
        task_01.factorial(0)


def test_descending_factorials() -> None:
    assert task_01.descending_factorials(6) == [720, 120, 24, 6, 2, 1]


def test_factorial_chain_from_input() -> None:
    assert task_01.factorial_chain_from_input(3) == [720, 120, 24, 6, 2, 1]


def test_read_natural_number_retries(monkeypatch, capsys) -> None:
    inputs = iter(["abc", "0", "-5", "4"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    value = task_01.read_natural_number("Введите число: ")

    captured = capsys.readouterr()
    assert value == 4
    assert "Введите корректное целое число." in captured.out
    assert captured.out.count("Число должно быть натуральным.") == 2


def test_main_prints_factorial_chain(monkeypatch, capsys) -> None:
    monkeypatch.setattr("builtins.input", lambda _: "3")

    task_01.main()

    captured = capsys.readouterr()
    assert captured.out.strip() == "[720, 120, 24, 6, 2, 1]"
