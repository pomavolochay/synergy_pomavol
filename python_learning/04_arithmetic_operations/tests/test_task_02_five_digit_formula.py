from __future__ import annotations

from _loader import load_module


def run_script(monkeypatch, value: str) -> None:
    monkeypatch.setattr("builtins.input", lambda *args: value)
    load_module("task_02_five_digit_formula.py", "task_02_five_digit_formula")


def test_example_from_statement(monkeypatch, capsys) -> None:
    run_script(monkeypatch, "46275")

    assert capsys.readouterr().out.strip() == "Результат: -16807.0"


def test_another_number(monkeypatch, capsys) -> None:
    run_script(monkeypatch, "12345")

    assert capsys.readouterr().out.strip() == "Результат: -3072.0"
