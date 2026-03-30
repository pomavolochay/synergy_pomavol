from __future__ import annotations

from _loader import load_module


task_01 = load_module("task_01_pet_profile.py", "task_01_pet_profile")


def test_format_years_declension() -> None:
    assert task_01.format_years(1) == "1 год"
    assert task_01.format_years(2) == "2 года"
    assert task_01.format_years(5) == "5 лет"
    assert task_01.format_years(11) == "11 лет"
    assert task_01.format_years(21) == "21 год"
    assert task_01.format_years(24) == "24 года"


def test_read_non_empty_retries_on_blank(monkeypatch, capsys) -> None:
    inputs = iter(["   ", "Питон"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    value = task_01.read_non_empty("Введите вид питомца: ")

    captured = capsys.readouterr()
    assert value == "Питон"
    assert "Поле не должно быть пустым" in captured.out


def test_read_positive_int_retries_on_invalid(monkeypatch, capsys) -> None:
    inputs = iter(["-1", "abc", "0", "12"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    value = task_01.read_positive_int("Введите возраст питомца: ")

    captured = capsys.readouterr()
    assert value == 12
    assert captured.out.count("Возраст должен быть положительным целым числом") == 3


def test_main_prints_expected_line(monkeypatch, capsys) -> None:
    inputs = iter(["желторотый питон", "34", "Каа"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    task_01.main()

    captured = capsys.readouterr()
    assert captured.out.strip() == 'Это желторотый питон по кличке "Каа". Возраст: 34 года.'
