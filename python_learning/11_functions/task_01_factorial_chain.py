"""Task 1: Build descending list of factorials from factorial(n) to 1."""


def read_natural_number(prompt: str) -> int:
    """Read a natural integer from user input."""
    while True:
        raw_value = input(prompt).strip()
        try:
            value = int(raw_value)
        except ValueError:
            print("Введите корректное целое число.")
            continue

        if value <= 0:
            print("Число должно быть натуральным.")
            continue

        return value


def factorial(number: int) -> int:
    """Return factorial of a natural integer."""
    if number <= 0:
        raise ValueError("Факториал определен для натуральных чисел.")

    result = 1
    for value in range(2, number + 1):
        result *= value

    return result


def descending_factorials(number: int) -> list[int]:
    """Return factorials from factorial(number) down to factorial(1)."""
    return [factorial(value) for value in range(number, 0, -1)]


def factorial_chain_from_input(value: int) -> list[int]:
    """Return descending factorial list starting from factorial(value)."""
    return descending_factorials(factorial(value))


def main() -> None:
    number = read_natural_number("Введите натуральное число: ")
    result = factorial_chain_from_input(number)
    print(result)


if __name__ == "__main__":
    main()
