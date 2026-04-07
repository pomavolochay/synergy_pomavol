"""Task 1: Count distinct numbers in a list."""


def read_int(prompt: str) -> int:
    """Read integer from user input."""
    while True:
        raw_value = input(prompt).strip()
        try:
            return int(raw_value)
        except ValueError:
            print("Введите корректное целое число.")


def read_n_numbers(count: int) -> list[int]:
    """Read exactly count integers from one line."""
    while True:
        raw_values = input("Введите N чисел через пробел: ").split()
        if len(raw_values) != count:
            print(f"Нужно ввести ровно {count} чисел.")
            continue

        try:
            return [int(value) for value in raw_values]
        except ValueError:
            print("Все значения должны быть целыми числами.")


def count_distinct(numbers: list[int]) -> int:
    """Return number of distinct values."""
    return len(set(numbers))


def main() -> None:
    while True:
        count = read_int("Введите N: ")
        if 1 <= count <= 100_000:
            break
        print("N должно быть в диапазоне [1, 100000].")

    numbers = read_n_numbers(count)
    print(count_distinct(numbers))


if __name__ == "__main__":
    main()
