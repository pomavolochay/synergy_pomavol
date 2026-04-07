"""Task 2: Rearrange list as last, first, second, ..."""


def read_int(prompt: str) -> int:
    """Read integer from user input."""
    while True:
        raw_value = input(prompt).strip()
        try:
            return int(raw_value)
        except ValueError:
            print("Введите корректное целое число.")


def rearrange_last_first(numbers: list[int]) -> list[int]:
    """Rearrange [a1, a2, ..., an] into [an, a1, a2, ..., a(n-1)]."""
    if not numbers:
        return []
    return [numbers[-1], *numbers[:-1]]


def read_n_numbers(count: int) -> list[int]:
    """Read exactly count integers from one input line."""
    while True:
        raw_values = input("Введите N чисел через пробел: ").split()
        if len(raw_values) != count:
            print(f"Нужно ввести ровно {count} чисел.")
            continue

        try:
            return [int(value) for value in raw_values]
        except ValueError:
            print("Все значения должны быть целыми числами.")


def main() -> None:
    while True:
        count = read_int("Введите N: ")
        if 1 <= count <= 100_000:
            break
        print("N должно быть в диапазоне [1, 100000].")

    numbers = read_n_numbers(count)
    print(*rearrange_last_first(numbers))


if __name__ == "__main__":
    main()
