from __future__ import annotations

from _loader import load_module


def run_script(monkeypatch, value: str) -> None:
    monkeypatch.setattr("builtins.input", lambda *args: value)
    load_module("task_01_palindrome.py", "task_01_palindrome")


def test_palindrome_yes(monkeypatch, capsys) -> None:
    run_script(monkeypatch, "level")

    assert capsys.readouterr().out.strip() == "yes"


def test_not_palindrome_no(monkeypatch, capsys) -> None:
    run_script(monkeypatch, "python")

    assert capsys.readouterr().out.strip() == "no"
