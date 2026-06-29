from __future__ import annotations

from _loader import load_module


def run_script(monkeypatch, value: str) -> None:
    monkeypatch.setattr("builtins.input", lambda *args: value)
    load_module("task_01_number_description.py", "task_01_number_description")


def test_zero(monkeypatch, capsys) -> None:
    run_script(monkeypatch, "0")

    assert capsys.readouterr().out.strip() == "нулевое число"


def test_positive_even(monkeypatch, capsys) -> None:
    run_script(monkeypatch, "190")

    assert capsys.readouterr().out.strip() == "положительное четное число"


def test_negative_even(monkeypatch, capsys) -> None:
    run_script(monkeypatch, "-8")

    assert capsys.readouterr().out.strip() == "отрицательное четное число"


def test_odd(monkeypatch, capsys) -> None:
    run_script(monkeypatch, "7")

    assert capsys.readouterr().out.strip() == "число не является четным"
