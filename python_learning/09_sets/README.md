# 09_sets

Решения задач по множествам: отдельные скрипты, тесты и инструкция по запуску.

## Задание 1: количество различных чисел

Файл: `task_01_count_distinct.py`

Логика:
- Считывается `N` и затем `N` чисел через пробел.
- Выводится количество различных чисел с помощью `set`.

## Задание 2: сколько чисел есть в обоих списках

Файл: `task_02_common_numbers.py`

Логика:
- Вводятся два списка чисел (каждый в отдельной строке).
- Выводится количество уникальных чисел, встречающихся и в первом, и во втором списке.

## Задание 3: встречалось ли число раньше

Файл: `task_03_seen_before.py`

Логика:
- Для каждого числа последовательности выводится:
  - `YES`, если число уже встречалось ранее,
  - `NO`, если это первое появление.

## Структура

```text
09_sets/
  task_01_count_distinct.py
  task_02_common_numbers.py
  task_03_seen_before.py
  tests/
    _loader.py
    test_task_01_count_distinct.py
    test_task_02_common_numbers.py
    test_task_03_seen_before.py
```

## Запуск

Из директории `09_sets`:

```bash
python task_01_count_distinct.py
python task_02_common_numbers.py
python task_03_seen_before.py
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
