"""Task 3: Print all even numbers in [A, B]."""


def read_int(prompt: str) -> int:
    """Read integer from user input."""
    while True:
        raw_value = input(prompt).strip()
        try:
            return int(raw_value)
        except ValueError:
            print("Введите корректное целое число.")


def even_numbers_in_range(start: int, end: int) -> list[int]:
    """Return all even numbers from inclusive range [start, end]."""
    first_even = start if start % 2 == 0 else start + 1
    return list(range(first_even, end + 1, 2))


def main() -> None:
    while True:
        start = read_int("Введите A: ")
        end = read_int("Введите B: ")
        if start <= end:
            break
        print("Должно выполняться условие A <= B. Попробуйте еще раз.")

    even_numbers = even_numbers_in_range(start, end)
    print(*even_numbers)


if __name__ == "__main__":
    main()
