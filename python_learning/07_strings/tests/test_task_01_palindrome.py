from __future__ import annotations

from _loader import load_module


task_01 = load_module("task_01_palindrome.py", "task_01_palindrome")


def test_is_palindrome_true() -> None:
    assert task_01.is_palindrome("шалаш") is True
    assert task_01.is_palindrome("level") is True


def test_is_palindrome_false() -> None:
    assert task_01.is_palindrome("python") is False


def test_main_prints_yes(monkeypatch, capsys) -> None:
    monkeypatch.setattr("builtins.input", lambda: "шалаш")

    task_01.main()

    captured = capsys.readouterr()
    assert captured.out.strip() == "yes"


def test_main_prints_no(monkeypatch, capsys) -> None:
    monkeypatch.setattr("builtins.input", lambda: "hello")

    task_01.main()

    captured = capsys.readouterr()
    assert captured.out.strip() == "no"
