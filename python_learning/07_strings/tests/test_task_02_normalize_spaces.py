from __future__ import annotations

from _loader import load_module


def run_script(monkeypatch, value: str) -> None:
    monkeypatch.setattr("builtins.input", lambda *args: value)
    load_module("task_02_normalize_spaces.py", "task_02_normalize_spaces")


def test_collapses_multiple_spaces(monkeypatch, capsys) -> None:
    run_script(monkeypatch, "a   b    c")

    assert capsys.readouterr().out.strip() == "a b c"


def test_trims_and_collapses_edges(monkeypatch, capsys) -> None:
    run_script(monkeypatch, "   hello   world   ")

    assert capsys.readouterr().out.strip() == "hello world"
