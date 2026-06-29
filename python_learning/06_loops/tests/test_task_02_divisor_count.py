from __future__ import annotations

from _loader import load_module


def run_script(monkeypatch, value: str) -> None:
    monkeypatch.setattr("builtins.input", lambda *args: value)
    load_module("task_02_divisor_count.py", "task_02_divisor_count")


def test_divisors_of_12(monkeypatch, capsys) -> None:
    run_script(monkeypatch, "12")

    assert capsys.readouterr().out.strip() == "6"


def test_divisors_of_36(monkeypatch, capsys) -> None:
    run_script(monkeypatch, "36")

    assert capsys.readouterr().out.strip() == "9"
