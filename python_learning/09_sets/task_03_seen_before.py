"""Task 3: Print whether each number appeared earlier in sequence."""


def seen_before_flags(numbers: list[int]) -> list[str]:
    """Return YES/NO flags for each number based on previous occurrences."""
    seen: set[int] = set()
    flags: list[str] = []
    for number in numbers:
        flags.append("YES" if number in seen else "NO")
        seen.add(number)
    return flags


def main() -> None:
    numbers = list(map(int, input("Введите последовательность чисел через пробел: ").split()))
    print("\n".join(seen_before_flags(numbers)))


if __name__ == "__main__":
    main()
