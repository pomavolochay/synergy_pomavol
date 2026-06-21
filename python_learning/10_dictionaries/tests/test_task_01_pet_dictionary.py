from __future__ import annotations

import pytest

from _loader import load_module


task_01 = load_module("task_01_pet_dictionary.py", "task_01_pet_dictionary")


def test_format_years_declension() -> None:
    assert task_01.format_years(1) == "1 год"
    assert task_01.format_years(2) == "2 года"
    assert task_01.format_years(5) == "5 лет"
    assert task_01.format_years(11) == "11 лет"
    assert task_01.format_years(21) == "21 год"
    assert task_01.format_years(24) == "24 года"


def test_create_pet_record() -> None:
    assert task_01.create_pet_record("Каа", "желторотый питон", 19, "Саша") == {
        "Каа": {
            "Вид питомца": "желторотый питон",
            "Возраст питомца": 19,
            "Имя владельца": "Саша",
        }
    }


def test_format_pet_info() -> None:
    pets = task_01.create_pet_record("Каа", "желторотый питон", 19, "Саша")

    assert (
        task_01.format_pet_info(pets)
        == 'Это желторотый питон по кличке "Каа". Возраст питомца: 19 лет. Имя владельца: Саша'
    )


def test_format_pet_info_rejects_non_integer_age() -> None:
    pets = {
        "Каа": {
            "Вид питомца": "желторотый питон",
            "Возраст питомца": "19",
            "Имя владельца": "Саша",
        }
    }

    with pytest.raises(TypeError):
        task_01.format_pet_info(pets)


def test_read_positive_int_retries(monkeypatch, capsys) -> None:
    inputs = iter(["abc", "0", "-1", "7"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    value = task_01.read_positive_int("Введите возраст: ")

    captured = capsys.readouterr()
    assert value == 7
    assert "Введите корректное целое число." in captured.out
    assert captured.out.count("Возраст должен быть положительным числом.") == 2


def test_main_prints_pet_info(monkeypatch, capsys) -> None:
    inputs = iter(["Каа", "желторотый питон", "19", "Саша"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    task_01.main()

    captured = capsys.readouterr()
    assert (
        captured.out.strip()
        == 'Это желторотый питон по кличке "Каа". Возраст питомца: 19 лет. Имя владельца: Саша'
    )
