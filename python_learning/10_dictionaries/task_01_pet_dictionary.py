"""Task 1: Create nested pet dictionary from user input."""


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
            print("Возраст должен быть положительным числом.")
            continue

        return value


def format_years(age: int) -> str:
    """Return age with the correct Russian word form."""
    if 11 <= age % 100 <= 14:
        suffix = "лет"
    else:
        last_digit = age % 10
        if last_digit == 1:
            suffix = "год"
        elif 2 <= last_digit <= 4:
            suffix = "года"
        else:
            suffix = "лет"

    return f"{age} {suffix}"


def create_pet_record(
    pet_name: str,
    pet_type: str,
    pet_age: int,
    owner_name: str,
) -> dict[str, dict[str, str | int]]:
    """Create nested pet dictionary."""
    return {
        pet_name: {
            "Вид питомца": pet_type,
            "Возраст питомца": pet_age,
            "Имя владельца": owner_name,
        }
    }


def format_pet_info(pets: dict[str, dict[str, str | int]]) -> str:
    """Return pet information string using dictionary keys() and values()."""
    pet_name = next(iter(pets.keys()))
    pet_values = next(iter(pets.values()))

    pet_type = pet_values["Вид питомца"]
    pet_age = pet_values["Возраст питомца"]
    owner_name = pet_values["Имя владельца"]

    if not isinstance(pet_age, int):
        raise TypeError("Возраст питомца должен быть целым числом.")

    return (
        f'Это {pet_type} по кличке "{pet_name}". '
        f"Возраст питомца: {format_years(pet_age)}. "
        f"Имя владельца: {owner_name}"
    )


def main() -> None:
    pet_name = read_non_empty("Введите кличку питомца: ")
    pet_type = read_non_empty("Введите вид питомца: ")
    pet_age = read_positive_int("Введите возраст питомца: ")
    owner_name = read_non_empty("Введите имя владельца: ")

    pets = create_pet_record(pet_name, pet_type, pet_age, owner_name)
    print(format_pet_info(pets))


if __name__ == "__main__":
    main()
