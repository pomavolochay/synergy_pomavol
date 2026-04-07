"""Task 2: Count common numbers in two lists."""


def parse_int_list(raw_line: str) -> list[int]:
    """Parse space-separated integers from input line."""
    parts = raw_line.split()
    if not parts:
        return []
    return [int(value) for value in parts]


def count_common_numbers(first: list[int], second: list[int]) -> int:
    """Return count of unique numbers present in both lists."""
    return len(set(first) & set(second))


def main() -> None:
    while True:
        try:
            first = parse_int_list(input("Введите первый список чисел через пробел: "))
            second = parse_int_list(input("Введите второй список чисел через пробел: "))
        except ValueError:
            print("Списки должны содержать только целые числа. Попробуйте еще раз.")
            continue

        print(count_common_numbers(first, second))
        break


if __name__ == "__main__":
    main()
