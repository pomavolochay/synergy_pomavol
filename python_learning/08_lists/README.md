# 08_lists

Решения задач по спискам: отдельные скрипты, тесты и инструкция по запуску.

## Задание 1: развернуть массив

Файл: `task_01_reverse_array.py`

Логика:
- Считывается `N`, затем ровно `N` целых чисел (по одному в строке).
- Выводится массив в обратном порядке.

## Задание 2: перестановка `последний, первый, второй...`

Файл: `task_02_last_first_rearrange.py`

Логика:
- Считывается `N`, затем `N` чисел через пробел.
- Массив преобразуется в вид: последний элемент, потом все элементы с начала до предпоследнего.

## Задание 3: минимальное число лодок

Файл: `task_03_min_boats.py`

Логика:
- В лодке максимум 2 человека и общий вес не более `m`.
- Используется жадный алгоритм после сортировки весов и 2 указателя (`left/right`).
- Возвращается минимальное число лодок.

## Структура

```text
08_lists/
  task_01_reverse_array.py
  task_02_last_first_rearrange.py
  task_03_min_boats.py
  tests/
    _loader.py
    test_task_01_reverse_array.py
    test_task_02_last_first_rearrange.py
    test_task_03_min_boats.py
```

## Запуск

Из директории `08_lists`:

```bash
python task_01_reverse_array.py
python task_02_last_first_rearrange.py
python task_03_min_boats.py
```

## Проверка тестами

Установить `pytest` (если нужно):

```bash
python -m pip install pytest
```

Запустить:

```bash
python -m pytest -q
```
