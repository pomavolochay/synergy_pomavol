from __future__ import annotations

import pytest

from _loader import load_module


task_01 = load_module("task_01_matrix_addition.py", "task_01_matrix_addition")


def test_get_matrix_shape() -> None:
    assert task_01.get_matrix_shape([[1, 2], [3, 4], [5, 6]]) == (3, 2)


def test_get_matrix_shape_rejects_ragged_matrix() -> None:
    with pytest.raises(ValueError):
        task_01.get_matrix_shape([[1, 2], [3]])


def test_generate_matrix_shape_and_bounds() -> None:
    matrix = task_01.generate_matrix(4, 3, -5, 5)

    assert task_01.get_matrix_shape(matrix) == (4, 3)
    assert all(-5 <= value <= 5 for row in matrix for value in row)


def test_generate_matrix_rejects_invalid_size() -> None:
    with pytest.raises(ValueError):
        task_01.generate_matrix(0, 3)


def test_generate_matrix_rejects_invalid_bounds() -> None:
    with pytest.raises(ValueError):
        task_01.generate_matrix(3, 3, 10, -10)


def test_add_matrices_10_by_10_example() -> None:
    matrix_1 = [
        [0, -2, -1, -6, -6, 0, -9, -8, -30, -9],
        [5, 12, 4, -16, -4, -9, -16, -15, 1, -26],
        [13, 39, 14, 23, -4, 40, 32, 6, -8, 23],
        [13, -8, 34, 49, 30, 18, 47, 11, -24, 11],
        [21, 73, 71, 61, -1, 79, -34, 22, 69, 67],
        [75, 25, 25, 39, 100, -12, -21, 81, -10, 87],
        [81, 63, 102, 104, 53, -44, 71, -36, -36, -9],
        [7, 98, 26, -3, 128, 94, 18, -26, 14, 21],
        [65, 128, 80, 124, 27, -32, 73, 59, 19, 34],
        [43, 111, 38, 149, 5, 112, 79, 53, 15, 92],
    ]
    matrix_2 = [
        [0, 4, 6, 11, 15, 6, 9, 26, 15, 21],
        [-5, 4, -15, -9, -4, 2, -8, 19, -4, -1],
        [-2, -39, -19, 14, 22, 5, -34, 15, 16, -9],
        [-22, -52, 11, -11, -3, 16, -11, -6, -32, -2],
        [-61, -47, -5, -58, 16, -13, 28, -36, -64, 2],
        [-29, 23, 19, 2, -14, -87, 7, -88, 39, 7],
        [-6, 18, -97, 26, -64, 0, -72, -34, -68, -92],
        [-120, -117, -72, -129, -139, 16, -61, 36, -137, -29],
        [-112, -83, 7, -119, -132, -129, -143, -154, -23, -34],
        [32, -67, -75, -92, 15, -163, 18, 31, -162, -16],
    ]

    assert task_01.add_matrices(matrix_1, matrix_2) == [
        [0, 2, 5, 5, 9, 6, 0, 18, -15, 12],
        [0, 16, -11, -25, -8, -7, -24, 4, -3, -27],
        [11, 0, -5, 37, 18, 45, -2, 21, 8, 14],
        [-9, -60, 45, 38, 27, 34, 36, 5, -56, 9],
        [-40, 26, 66, 3, 15, 66, -6, -14, 5, 69],
        [46, 48, 44, 41, 86, -99, -14, -7, 29, 94],
        [75, 81, 5, 130, -11, -44, -1, -70, -104, -101],
        [-113, -19, -46, -132, -11, 110, -43, 10, -123, -8],
        [-47, 45, 87, 5, -105, -161, -70, -95, -4, 0],
        [75, 44, -37, 57, 20, -51, 97, 84, -147, 76],
    ]


def test_add_matrices_4_by_3() -> None:
    assert task_01.add_matrices(
        [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],
        [[10, 20, 30], [40, 50, 60], [70, 80, 90], [100, 110, 120]],
    ) == [[11, 22, 33], [44, 55, 66], [77, 88, 99], [110, 121, 132]]


def test_add_matrices_rejects_different_shapes() -> None:
    with pytest.raises(ValueError):
        task_01.add_matrices([[1, 2]], [[1], [2]])
