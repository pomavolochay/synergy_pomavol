"""Task 2: Compute a formula based on digits of a five-digit integer."""


def parse_five_digit_number(raw_value: str) -> int:
    """Parse and validate a five-digit integer string."""
    value = raw_value.strip()
    signless_value = value.lstrip("-")

    if not signless_value.isdigit() or len(signless_value) != 5:
        raise ValueError("Нужно ввести пятизначное целое число.")

    return int(value)


def calculate_special_value(number: int) -> float:
    """Calculate the expression from task statement."""
    absolute_number = abs(number)

    ten_thousands = absolute_number // 10000
    thousands = (absolute_number // 1000) % 10
    hundreds = (absolute_number // 100) % 10
    tens = (absolute_number // 10) % 10
    ones = absolute_number % 10

    denominator = ten_thousands - thousands
    if denominator == 0:
        raise ZeroDivisionError("Разность десятков тысяч и тысяч равна нулю.")

    numerator = (tens**ones) * hundreds
    return float(numerator / denominator)


def main() -> None:
    while True:
        raw_value = input("Введите пятизначное целое число: ")
        try:
            number = parse_five_digit_number(raw_value)
            result = calculate_special_value(number)
        except ValueError as error:
            print(error)
            continue
        except ZeroDivisionError as error:
            print(error)
            continue

        print(f"Результат: {result}")
        break


if __name__ == "__main__":
    main()
