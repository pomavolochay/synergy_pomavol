from __future__ import annotations

from _loader import load_module


task_02 = load_module("task_02_vowels_and_consonants.py", "task_02_vowels_and_consonants")


def test_analyze_word_counts_and_missing_vowels() -> None:
    consonants, vowels, vowel_counts = task_02.analyze_word("banana")

    assert consonants == 3
    assert vowels == 3
    assert vowel_counts == {
        "a": 3,
        "e": False,
        "i": False,
        "o": False,
        "u": False,
    }


def test_analyze_word_all_vowels() -> None:
    consonants, vowels, vowel_counts = task_02.analyze_word("aeiou")

    assert consonants == 0
    assert vowels == 5
    assert vowel_counts == {
        "a": 1,
        "e": 1,
        "i": 1,
        "o": 1,
        "u": 1,
    }


def test_main_prints_analysis(monkeypatch, capsys) -> None:
    monkeypatch.setattr("builtins.input", lambda _: "hello")

    task_02.main()

    captured = capsys.readouterr()
    output_lines = captured.out.strip().splitlines()

    assert output_lines[0] == "Количество согласных: 3"
    assert output_lines[1] == "Количество гласных: 2"
    assert output_lines[2:] == [
        "a: False",
        "e: 1",
        "i: False",
        "o: 1",
        "u: False",
    ]
