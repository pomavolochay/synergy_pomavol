"""Task 2: Simple CRUD database for veterinary clinic pets."""

import collections
from typing import Literal


PetInfo = dict[str, str | int]
PetRecord = dict[str, PetInfo]
PetsDatabase = dict[int, PetRecord]

pets: PetsDatabase = {
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


def read_non_empty(prompt: str) -> str:
    """Read a non-empty string from user input."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Поле не должно быть пустым. Попробуйте еще раз.")


def read_positive_int(prompt: str) -> int:
    """Read a positive integer from user input."""
    while True:
        raw_value = input(prompt).strip()
        try:
            value = int(raw_value)
        except ValueError:
            print("Введите корректное целое число.")
            continue

        if value <= 0:
            print("Число должно быть положительным.")
            continue

        return value


def get_pet(pet_id: int, database: PetsDatabase | None = None) -> PetRecord | Literal[False]:
    """Return pet record by ID or False if record does not exist."""
    source = pets if database is None else database
    return source[pet_id] if pet_id in source.keys() else False


def get_suffix(age: int) -> str:
    """Return correct Russian suffix for pet age."""
    if 11 <= age % 100 <= 14:
        return "лет"

    last_digit = age % 10
    if last_digit == 1:
        return "год"
    if 2 <= last_digit <= 4:
        return "года"
    return "лет"


def _next_pet_id(database: PetsDatabase) -> int:
    if not database:
        return 1

    last = collections.deque(database, maxlen=1)[0]
    return last + 1


def _build_pet_record(pet_name: str, pet_type: str, pet_age: int, owner_name: str) -> PetRecord:
    return {
        pet_name: {
            "Вид питомца": pet_type,
            "Возраст питомца": pet_age,
            "Имя владельца": owner_name,
        }
    }


def create(
    database: PetsDatabase | None = None,
    pet_name: str | None = None,
    pet_type: str | None = None,
    pet_age: int | None = None,
    owner_name: str | None = None,
) -> int:
    """Create a pet record and return its new ID."""
    target = pets if database is None else database

    pet_name = pet_name if pet_name is not None else read_non_empty("Введите кличку питомца: ")
    pet_type = pet_type if pet_type is not None else read_non_empty("Введите вид питомца: ")
    pet_age = pet_age if pet_age is not None else read_positive_int("Введите возраст питомца: ")
    owner_name = owner_name if owner_name is not None else read_non_empty("Введите имя владельца: ")

    pet_id = _next_pet_id(target)
    target[pet_id] = _build_pet_record(pet_name, pet_type, pet_age, owner_name)
    return pet_id


def format_pet_record(record: PetRecord) -> str:
    """Format one pet record as a human-readable string."""
    pet_name = next(iter(record.keys()))
    pet_data = next(iter(record.values()))

    pet_type = pet_data["Вид питомца"]
    pet_age = pet_data["Возраст питомца"]
    owner_name = pet_data["Имя владельца"]

    if not isinstance(pet_age, int):
        raise TypeError("Возраст питомца должен быть целым числом.")

    return (
        f'Это {pet_type} по кличке "{pet_name}". '
        f"Возраст питомца: {pet_age} {get_suffix(pet_age)}. "
        f"Имя владельца: {owner_name}"
    )


def read(pet_id: int | None = None, database: PetsDatabase | None = None) -> str | Literal[False]:
    """Return formatted pet info or False if pet does not exist."""
    source = pets if database is None else database
    pet_id = pet_id if pet_id is not None else read_positive_int("Введите ID питомца: ")

    pet = get_pet(pet_id, source)
    if pet is False:
        return False

    return format_pet_record(pet)


def update(
    pet_id: int | None = None,
    database: PetsDatabase | None = None,
    pet_name: str | None = None,
    pet_type: str | None = None,
    pet_age: int | None = None,
    owner_name: str | None = None,
) -> bool:
    """Update pet record by ID."""
    target = pets if database is None else database
    pet_id = pet_id if pet_id is not None else read_positive_int("Введите ID питомца: ")

    if get_pet(pet_id, target) is False:
        return False

    pet_name = pet_name if pet_name is not None else read_non_empty("Введите новую кличку питомца: ")
    pet_type = pet_type if pet_type is not None else read_non_empty("Введите новый вид питомца: ")
    pet_age = pet_age if pet_age is not None else read_positive_int("Введите новый возраст питомца: ")
    owner_name = owner_name if owner_name is not None else read_non_empty("Введите новое имя владельца: ")

    target[pet_id] = _build_pet_record(pet_name, pet_type, pet_age, owner_name)
    return True


def delete(pet_id: int | None = None, database: PetsDatabase | None = None) -> bool:
    """Delete pet record by ID."""
    target = pets if database is None else database
    pet_id = pet_id if pet_id is not None else read_positive_int("Введите ID питомца: ")

    if get_pet(pet_id, target) is False:
        return False

    del target[pet_id]
    return True


def pets_list(database: PetsDatabase | None = None) -> list[str]:
    """Return formatted info for every pet in database."""
    source = pets if database is None else database
    return [format_pet_record(record) for record in source.values()]


def main() -> None:
    command = ""
    while command != "stop":
        command = input("Введите команду (create/read/update/delete/list/stop): ").strip().lower()

        if command == "create":
            pet_id = create()
            print(f"Запись создана. ID: {pet_id}")
        elif command == "read":
            result = read()
            print(result if result else "Питомец с таким ID не найден.")
        elif command == "update":
            result = update()
            print("Запись обновлена." if result else "Питомец с таким ID не найден.")
        elif command == "delete":
            result = delete()
            print("Запись удалена." if result else "Питомец с таким ID не найден.")
        elif command == "list":
            for pet_info in pets_list():
                print(pet_info)
        elif command == "stop":
            print("Работа завершена.")
        else:
            print("Неизвестная команда.")


if __name__ == "__main__":
    main()
