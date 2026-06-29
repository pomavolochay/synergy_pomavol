from __future__ import annotations

from _loader import load_module


def run_script(monkeypatch, values: list[str]) -> None:
    inputs = iter(values)
    monkeypatch.setattr("builtins.input", lambda *args: next(inputs))
    load_module("task_01_count_zeros.py", "task_01_count_zeros")


def test_counts_zeros(monkeypatch, capsys) -> None:
    run_script(monkeypatch, ["5", "0", "1", "0", "2", "3"])

    assert capsys.readouterr().out.strip() == "2"


def test_no_zeros(monkeypatch, capsys) -> None:
    run_script(monkeypatch, ["3", "1", "2", "3"])

    assert capsys.readouterr().out.strip() == "0"
