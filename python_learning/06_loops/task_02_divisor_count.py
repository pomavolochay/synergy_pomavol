"""Task 2: Count natural divisors of X."""


def read_natural_number(prompt: str) -> int:
    """Read a natural number (> 0)."""
    while True:
        raw_value = input(prompt).strip()
        try:
            value = int(raw_value)
        except ValueError:
            print("Введите корректное целое число.")
            continue

        if value <= 0:
            print("Число должно быть натуральным (больше нуля).")
            continue

        return value


def count_divisors(value: int) -> int:
    """Count divisors in O(sqrt(n))."""
    divisors = 0
    candidate = 1

    while candidate * candidate <= value:
        if value % candidate == 0:
            pair = value // candidate
            divisors += 1 if pair == candidate else 2
        candidate += 1

    return divisors


def main() -> None:
    number = read_natural_number("Введите натуральное число X: ")
    print(count_divisors(number))


if __name__ == "__main__":
    main()
