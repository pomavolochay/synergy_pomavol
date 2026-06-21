"""Task 1: Generate and add matrices."""

import random


Matrix = list[list[int]]


def read_positive_int(prompt: str) -> int:
    """Read a positive integer from user input."""
    while True:
        raw_value = input(prompt).strip()
        try:
            value = int(raw_value)
        except ValueError:
            print("Введите корректное целое число.")
            continue

        if value <= 0:
            print("Число должно быть положительным.")
            continue

        return value


def read_int(prompt: str) -> int:
    """Read an integer from user input."""
    while True:
        raw_value = input(prompt).strip()
        try:
            return int(raw_value)
        except ValueError:
            print("Введите корректное целое число.")


def get_matrix_shape(matrix: Matrix) -> tuple[int, int]:
    """Return matrix shape as (rows, columns)."""
    if not matrix:
        return 0, 0

    rows = len(matrix)
    columns = len(matrix[0])

    for row in matrix:
        if len(row) != columns:
            raise ValueError("Матрица должна быть прямоугольной.")

    return rows, columns


def generate_matrix(
    rows: int,
    columns: int,
    min_value: int = -100,
    max_value: int = 100,
) -> Matrix:
    """Generate matrix with random integer values."""
    if rows <= 0 or columns <= 0:
        raise ValueError("Размеры матрицы должны быть положительными.")
    if min_value > max_value:
        raise ValueError("Минимальное значение не может быть больше максимального.")

    return [
        [random.randint(min_value, max_value) for _ in range(columns)]
        for _ in range(rows)
    ]


def add_matrices(first: Matrix, second: Matrix) -> Matrix:
    """Return sum of two matrices with the same shape."""
    first_shape = get_matrix_shape(first)
    second_shape = get_matrix_shape(second)

    if first_shape != second_shape:
        raise ValueError("Матрицы должны быть одинаковой размерности.")

    return [
        [
            first[row_index][column_index] + second[row_index][column_index]
            for column_index in range(first_shape[1])
        ]
        for row_index in range(first_shape[0])
    ]


def print_matrix(matrix: Matrix) -> None:
    """Print matrix row by row."""
    for row in matrix:
        print(row)


def main() -> None:
    rows = read_positive_int("Введите количество строк: ")
    columns = read_positive_int("Введите количество столбцов: ")
    min_value = read_int("Введите минимальное значение элемента: ")
    max_value = read_int("Введите максимальное значение элемента: ")

    matrix_1 = generate_matrix(rows, columns, min_value, max_value)
    matrix_2 = generate_matrix(rows, columns, min_value, max_value)
    matrix_3 = add_matrices(matrix_1, matrix_2)

    print("Матрица 1:")
    print_matrix(matrix_1)
    print("Матрица 2:")
    print_matrix(matrix_2)
    print("Сумма матриц:")
    print_matrix(matrix_3)


if __name__ == "__main__":
    main()
