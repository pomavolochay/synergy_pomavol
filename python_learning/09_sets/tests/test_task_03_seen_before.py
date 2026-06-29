from __future__ import annotations

from _loader import load_module


task_03 = load_module("task_03_seen_before.py", "task_03_seen_before")


def test_seen_before_flags() -> None:
    assert task_03.seen_before_flags([1, 2, 1, 3, 2]) == ["NO", "NO", "YES", "NO", "YES"]


def test_main_prints_flags(monkeypatch, capsys) -> None:
    monkeypatch.setattr("builtins.input", lambda _: "1 2 1 1")

    task_03.main()

    captured = capsys.readouterr()
    assert captured.out.strip().splitlines()[-4:] == ["NO", "NO", "YES", "YES"]
