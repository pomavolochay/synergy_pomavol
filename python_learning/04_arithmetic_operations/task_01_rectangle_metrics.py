"""Task 1: Calculate rectangle area and perimeter from user input."""

width = float(input("Введите первую сторону прямоугольника: ").replace(",", "."))
height = float(input("Введите вторую сторону прямоугольника: ").replace(",", "."))
print(f"Площадь: {width * height}")
print(f"Периметр: {2 * (width + height)}")
