"""Task 1: Calculate rectangle area and perimeter from user input."""


def read_positive_float(prompt: str) -> float:
    """Read a positive float from user input."""
    while True:
        raw_value = input(prompt).strip().replace(",", ".")
        try:
            value = float(raw_value)
        except ValueError:
            print("Введите корректное число. Попробуйте еще раз.")
            continue

        if value <= 0:
            print("Значение должно быть больше нуля. Попробуйте еще раз.")
            continue

        return value


def calculate_rectangle_metrics(width: float, height: float) -> tuple[float, float]:
    """Return rectangle area and perimeter."""
    area = width * height
    perimeter = 2 * (width + height)
    return area, perimeter


def main() -> None:
    width = read_positive_float("Введите первую сторону прямоугольника: ")
    height = read_positive_float("Введите вторую сторону прямоугольника: ")

    area, perimeter = calculate_rectangle_metrics(width, height)
    print(f"Площадь: {area}")
    print(f"Периметр: {perimeter}")


if __name__ == "__main__":
    main()
