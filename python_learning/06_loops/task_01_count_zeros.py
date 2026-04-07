"""Task 1: Count zeros among N input integers."""


def read_int(prompt: str) -> int:
    """Read integer from user input."""
    while True:
        raw_value = input(prompt).strip()
        try:
            return int(raw_value)
        except ValueError:
            print("Введите корректное целое число.")


def count_zeros(numbers: list[int]) -> int:
    """Return amount of zeros in a list of integers."""
    return sum(1 for number in numbers if number == 0)


def main() -> None:
    while True:
        count = read_int("Введите количество чисел N: ")
        if count >= 0:
            break
        print("N должно быть неотрицательным.")

    values: list[int] = []
    for index in range(1, count + 1):
        values.append(read_int(f"Введите число #{index}: "))

    print(count_zeros(values))


if __name__ == "__main__":
    main()
