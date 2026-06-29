# 06_loops

Решения задач по циклам: прямые решения на циклах и тесты.

## Задание 1: количество нулей

Файл: `task_01_count_zeros.py`

Логика:
- Сначала вводится `N`.
- Затем считываются ровно `N` целых чисел.
- Выводится количество значений, равных нулю.

## Задание 2: количество делителей

Файл: `task_02_divisor_count.py`

Логика:
- Вводится натуральное число `X`.
- Подсчитывается число натуральных делителей (включая `1` и `X`).
- Используется алгоритм `O(sqrt(X))`, который подходит для больших значений.

## Задание 3: четные на отрезке

Файл: `task_03_even_range.py`

Логика:
- Вводятся `A` и `B`, где должно выполняться `A <= B`.
- Выводятся все четные числа на отрезке `[A, B]` через пробел.

## Структура

```text
06_loops/
  task_01_count_zeros.py
  task_02_divisor_count.py
  task_03_even_range.py
  tests/
    _loader.py
    test_task_01_count_zeros.py
    test_task_02_divisor_count.py
    test_task_03_even_range.py
```

## Запуск

Из директории `06_loops`:

```bash
python task_01_count_zeros.py
python task_02_divisor_count.py
python task_03_even_range.py
```

## Проверка тестами

Установка `pytest` (если нужно):

```bash
python -m pip install pytest
```

Запуск:

```bash
python -m pytest -q
```
