"""Task 1: Reverse an array of N integers."""


def read_int(prompt: str) -> int:
    """Read integer from user input."""
    while True:
        raw_value = input(prompt).strip()
        try:
            return int(raw_value)
        except ValueError:
            print("Введите корректное целое число.")


def reverse_array(numbers: list[int]) -> list[int]:
    """Return reversed copy of input list."""
    return numbers[::-1]


def main() -> None:
    while True:
        count = read_int("Введите N: ")
        if 1 <= count <= 10_000:
            break
        print("N должно быть в диапазоне [1, 10000].")

    values: list[int] = []
    for index in range(1, count + 1):
        values.append(read_int(f"Введите число #{index}: "))

    print(*reverse_array(values))


if __name__ == "__main__":
    main()
