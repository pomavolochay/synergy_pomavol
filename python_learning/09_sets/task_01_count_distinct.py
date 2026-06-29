"""Task 1: Count distinct numbers in a list."""


def count_distinct(numbers: list[int]) -> int:
    """Return number of distinct values."""
    return len(set(numbers))


def main() -> None:
    input("Введите N: ")
    numbers = list(map(int, input("Введите числа через пробел: ").split()))
    print(count_distinct(numbers))


if __name__ == "__main__":
    main()
