from __future__ import annotations

import pytest

from _loader import load_module


task_01 = load_module("task_01_cash_register.py", "task_01_cash_register")


def test_cash_register_top_up() -> None:
    cash_register = task_01.CashRegister(1000)

    cash_register.top_up(2500)

    assert cash_register.balance == 3500


def test_cash_register_count_1000() -> None:
    assert task_01.CashRegister(4500).count_1000() == 4


def test_cash_register_take_away() -> None:
    cash_register = task_01.CashRegister(3000)

    cash_register.take_away(1200)

    assert cash_register.balance == 1800


def test_cash_register_take_away_rejects_too_large_amount() -> None:
    cash_register = task_01.CashRegister(500)

    with pytest.raises(ValueError):
        cash_register.take_away(600)


def test_cash_register_rejects_negative_initial_balance() -> None:
    with pytest.raises(ValueError):
        task_01.CashRegister(-1)


def test_cash_register_rejects_non_positive_amounts() -> None:
    cash_register = task_01.CashRegister()

    with pytest.raises(ValueError):
        cash_register.top_up(0)

    with pytest.raises(ValueError):
        cash_register.take_away(-1)
