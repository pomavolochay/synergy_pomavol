from __future__ import annotations

from _loader import load_module


task_02 = load_module("task_02_normalize_spaces.py", "task_02_normalize_spaces")


def test_normalize_spaces_basic() -> None:
    assert task_02.normalize_spaces("a   b    c") == "a b c"


def test_normalize_spaces_keeps_single_spaces() -> None:
    assert task_02.normalize_spaces("one two three") == "one two three"


def test_normalize_spaces_with_edges() -> None:
    assert task_02.normalize_spaces("   hello   world   ") == "hello world"


def test_main_prints_normalized_string(monkeypatch, capsys) -> None:
    monkeypatch.setattr("builtins.input", lambda: "a    b  c")

    task_02.main()

    captured = capsys.readouterr()
    assert captured.out.strip() == "a b c"
