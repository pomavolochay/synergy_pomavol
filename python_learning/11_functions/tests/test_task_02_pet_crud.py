from __future__ import annotations

from _loader import load_module


task_02 = load_module("task_02_pet_crud.py", "task_02_pet_crud")


def make_database() -> dict[int, dict[str, dict[str, str | int]]]:
    return {
        1: {
            "Мухтар": {
                "Вид питомца": "Собака",
                "Возраст питомца": 9,
                "Имя владельца": "Павел",
            },
        },
        2: {
            "Каа": {
                "Вид питомца": "желторотый питон",
                "Возраст питомца": 19,
                "Имя владельца": "Саша",
            },
        },
    }


def test_get_suffix() -> None:
    assert task_02.get_suffix(1) == "год"
    assert task_02.get_suffix(2) == "года"
    assert task_02.get_suffix(5) == "лет"
    assert task_02.get_suffix(11) == "лет"
    assert task_02.get_suffix(21) == "год"
    assert task_02.get_suffix(24) == "года"


def test_get_pet_returns_record_or_false() -> None:
    database = make_database()

    assert task_02.get_pet(2, database) == database[2]
    assert task_02.get_pet(999, database) is False


def test_create_adds_record_with_next_id() -> None:
    database = make_database()

    pet_id = task_02.create(database, "Барсик", "Кот", 3, "Ирина")

    assert pet_id == 3
    assert database[3] == {
        "Барсик": {
            "Вид питомца": "Кот",
            "Возраст питомца": 3,
            "Имя владельца": "Ирина",
        }
    }


def test_create_starts_from_one_for_empty_database() -> None:
    database = {}

    pet_id = task_02.create(database, "Кеша", "Попугай", 2, "Анна")

    assert pet_id == 1
    assert 1 in database


def test_read_formats_pet_info() -> None:
    database = make_database()

    assert (
        task_02.read(2, database)
        == 'Это желторотый питон по кличке "Каа". Возраст питомца: 19 лет. Имя владельца: Саша'
    )


def test_read_returns_false_for_missing_pet() -> None:
    assert task_02.read(999, make_database()) is False


def test_update_changes_record() -> None:
    database = make_database()

    result = task_02.update(2, database, "Каа", "питон", 21, "Сергей")

    assert result is True
    assert (
        task_02.read(2, database)
        == 'Это питон по кличке "Каа". Возраст питомца: 21 год. Имя владельца: Сергей'
    )


def test_update_returns_false_for_missing_pet() -> None:
    assert task_02.update(999, make_database(), "Каа", "питон", 21, "Сергей") is False


def test_delete_removes_record() -> None:
    database = make_database()

    result = task_02.delete(2, database)

    assert result is True
    assert 2 not in database


def test_delete_returns_false_for_missing_pet() -> None:
    assert task_02.delete(999, make_database()) is False


def test_pets_list() -> None:
    pet_infos = task_02.pets_list(make_database())

    assert len(pet_infos) == 2
    assert pet_infos[0] == 'Это Собака по кличке "Мухтар". Возраст питомца: 9 лет. Имя владельца: Павел'
