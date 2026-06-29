from __future__ import annotations

from _loader import load_module


def run_script(monkeypatch, value: str) -> list[str]:
    monkeypatch.setattr("builtins.input", lambda *args: value)
    load_module("task_02_vowels_and_consonants.py", "task_02_vowels_and_consonants")


def test_hello(monkeypatch, capsys) -> None:
    run_script(monkeypatch, "hello")

    lines = capsys.readouterr().out.strip().splitlines()
    assert lines == [
        "Количество согласных: 3",
        "Количество гласных: 2",
        "a: False",
        "e: 1",
        "i: False",
        "o: 1",
        "u: False",
    ]


def test_banana(monkeypatch, capsys) -> None:
    run_script(monkeypatch, "banana")

    lines = capsys.readouterr().out.strip().splitlines()
    assert lines[0] == "Количество согласных: 3"
    assert lines[1] == "Количество гласных: 3"
    assert "a: 3" in lines
