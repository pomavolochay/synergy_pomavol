from __future__ import annotations

from _loader import load_module


def run_script(monkeypatch, values: list[str]) -> None:
    inputs = iter(values)
    monkeypatch.setattr("builtins.input", lambda *args: next(inputs))
    load_module("task_03_investors.py", "task_03_investors")


def test_both_can(monkeypatch, capsys) -> None:
    run_script(monkeypatch, ["50", "100", "120"])

    assert capsys.readouterr().out.strip() == "2"


def test_only_mike(monkeypatch, capsys) -> None:
    run_script(monkeypatch, ["50", "100", "40"])

    assert capsys.readouterr().out.strip() == "Mike"


def test_only_ivan(monkeypatch, capsys) -> None:
    run_script(monkeypatch, ["50", "30", "60"])

    assert capsys.readouterr().out.strip() == "Ivan"


def test_only_together(monkeypatch, capsys) -> None:
    run_script(monkeypatch, ["50", "30", "25"])

    assert capsys.readouterr().out.strip() == "1"


def test_none(monkeypatch, capsys) -> None:
    run_script(monkeypatch, ["50", "10", "20"])

    assert capsys.readouterr().out.strip() == "0"
