# 07_strings

Решения задач по строкам: прямая работа со строками без функций, отдельные файлы и тесты.

## Задание 1: палиндром

Файл: `task_01_palindrome.py`

Логика:
- На вход подается одна строка без пробелов.
- Если строка равна своей перевернутой версии, выводится `yes`.
- Иначе выводится `no`.

## Задание 2: нормализация пробелов

Файл: `task_02_normalize_spaces.py`

Логика:
- На вход подается строка длиной до 1000 символов.
- Все группы подряд идущих пробелов заменяются на один пробел.
- Результат выводится одной строкой.

## Структура

```text
07_strings/
  task_01_palindrome.py
  task_02_normalize_spaces.py
  tests/
    _loader.py
    test_task_01_palindrome.py
    test_task_02_normalize_spaces.py
```

## Запуск

Из директории `07_strings`:

```bash
python task_01_palindrome.py
python task_02_normalize_spaces.py
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
