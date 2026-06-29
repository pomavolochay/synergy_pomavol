"""Task 2: Count common numbers in two lists."""


def count_common_numbers(first: list[int], second: list[int]) -> int:
    """Return count of unique numbers present in both lists."""
    return len(set(first) & set(second))


def main() -> None:
    first = list(map(int, input("Введите первый список чисел через пробел: ").split()))
    second = list(map(int, input("Введите второй список чисел через пробел: ").split()))
    print(count_common_numbers(first, second))


if __name__ == "__main__":
    main()
