"""Task 3: Print whether each number appeared earlier in sequence."""


def parse_int_list(raw_line: str) -> list[int]:
    """Parse space-separated integers from input line."""
    parts = raw_line.split()
    if not parts:
        return []
    return [int(value) for value in parts]


def seen_before_flags(numbers: list[int]) -> list[str]:
    """Return YES/NO flags for each number based on previous occurrences."""
    seen: set[int] = set()
    flags: list[str] = []

    for number in numbers:
        if number in seen:
            flags.append("YES")
        else:
            flags.append("NO")
            seen.add(number)

    return flags


def main() -> None:
    while True:
        try:
            numbers = parse_int_list(input("Введите последовательность чисел через пробел: "))
        except ValueError:
            print("Последовательность должна содержать только целые числа. Попробуйте еще раз.")
            continue

        for flag in seen_before_flags(numbers):
            print(flag)
        break


if __name__ == "__main__":
    main()
