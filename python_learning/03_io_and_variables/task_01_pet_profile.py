"""Task 1: Collect and print basic pet information for a vet clinic form."""


def read_non_empty(prompt: str) -> str:
    """Read a non-empty user input."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Поле не должно быть пустым. Попробуйте еще раз.")


def read_positive_int(prompt: str) -> int:
    """Read a positive integer value."""
    while True:
        raw_value = input(prompt).strip()
        if raw_value.isdigit() and int(raw_value) > 0:
            return int(raw_value)
        print("Возраст должен быть положительным целым числом. Попробуйте еще раз.")


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


def main() -> None:
    pet_type = read_non_empty("Введите вид питомца: ")
    pet_age = read_positive_int("Введите возраст питомца: ")
    pet_name = read_non_empty("Введите кличку питомца: ")

    print(f'Это {pet_type} по кличке "{pet_name}". Возраст: {format_years(pet_age)}.')


if __name__ == "__main__":
    main()
