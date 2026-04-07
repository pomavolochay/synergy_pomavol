"""Task 1: Describe an integer by sign and parity."""


def describe_number(value: int) -> str:
    """Return textual description for an integer."""
    if value == 0:
        return "нулевое число"

    if value % 2 != 0:
        return "число не является четным"

    sign = "положительное" if value > 0 else "отрицательное"
    return f"{sign} четное число"


def read_int(prompt: str) -> int:
    """Read integer from user input."""
    while True:
        raw_value = input(prompt).strip()
        try:
            return int(raw_value)
        except ValueError:
            print("Введите корректное целое число.")


def main() -> None:
    number = read_int("Введите целое число: ")
    print(describe_number(number))


if __name__ == "__main__":
    main()
