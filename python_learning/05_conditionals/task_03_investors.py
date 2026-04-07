"""Task 3: Determine startup investment scenario."""


def investment_result(mike: int, ivan: int, minimum: int) -> str:
    """Return who can invest based on available money and minimum amount."""
    mike_can = mike >= minimum
    ivan_can = ivan >= minimum

    if mike_can and ivan_can:
        return "2"
    if mike_can:
        return "Mike"
    if ivan_can:
        return "Ivan"
    if mike + ivan >= minimum:
        return "1"
    return "0"


def read_non_negative_int(prompt: str) -> int:
    """Read a non-negative integer from input."""
    while True:
        raw_value = input(prompt).strip()
        try:
            value = int(raw_value)
        except ValueError:
            print("Введите корректное целое число.")
            continue

        if value < 0:
            print("Число не может быть отрицательным.")
            continue

        return value


def main() -> None:
    minimum = read_non_negative_int("Введите минимальную сумму инвестиций X: ")
    mike = read_non_negative_int("Введите сумму Майкла A: ")
    ivan = read_non_negative_int("Введите сумму Ивана B: ")

    print(investment_result(mike, ivan, minimum))


if __name__ == "__main__":
    main()
