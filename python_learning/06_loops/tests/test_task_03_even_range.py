from __future__ import annotations

from _loader import load_module


def run_script(monkeypatch, values: list[str]) -> None:
    inputs = iter(values)
    monkeypatch.setattr("builtins.input", lambda *args: next(inputs))
    load_module("task_03_even_range.py", "task_03_even_range")


def test_even_numbers_from_even_start(monkeypatch, capsys) -> None:
    run_script(monkeypatch, ["2", "8"])

    assert capsys.readouterr().out.strip() == "2 4 6 8"


def test_even_numbers_from_odd_start(monkeypatch, capsys) -> None:
    run_script(monkeypatch, ["3", "11"])

    assert capsys.readouterr().out.strip() == "4 6 8 10"
