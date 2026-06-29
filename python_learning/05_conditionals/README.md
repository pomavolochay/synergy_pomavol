# 05_conditionals

Решения задач по условным операторам: прямые решения через if/else без функций и тесты.

## Задание 1: описание целого числа

Файл: `task_01_number_description.py`

Логика:
- `0` -> `нулевое число`
- четное положительное -> `положительное четное число`
- четное отрицательное -> `отрицательное четное число`
- нечетное -> `число не является четным`

## Задание 2: гласные и согласные

Файл: `task_02_vowels_and_consonants.py`

Логика:
- Вводится слово из маленьких латинских букв.
- Считается количество согласных и гласных.
- Для каждой гласной из `a, e, i, o, u` выводится ее количество.
- Если конкретной гласной нет, выводится `False`.

## Задание 3: инвесторы

Файл: `task_03_investors.py`

Логика:
- Если оба могут вложить минимум `X` -> `2`
- Если только Майкл -> `Mike`
- Если только Иван -> `Ivan`
- Если отдельно не могут, но вместе хватает -> `1`
- Иначе -> `0`

## Структура

```text
05_conditionals/
  task_01_number_description.py
  task_02_vowels_and_consonants.py
  task_03_investors.py
  tests/
    _loader.py
    test_task_01_number_description.py
    test_task_02_vowels_and_consonants.py
    test_task_03_investors.py
```

## Запуск

Из директории `05_conditionals`:

```bash
python task_01_number_description.py
python task_02_vowels_and_consonants.py
python task_03_investors.py
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
