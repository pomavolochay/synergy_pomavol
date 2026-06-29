# 03_io_and_variables

Решения двух задач на ввод/вывод и переменные: прямой ввод и вывод данных, с тестами.

## Выполненные задания

### Задание 1: карточка питомца

Файл: `task_01_pet_profile.py`

Что делает:
- Запрашивает вид питомца, возраст и кличку.
- Не принимает пустые значения для строковых полей.
- Проверяет, что возраст: положительное целое число.
- Выводит итоговую фразу с корректным склонением: `год/года/лет`.

Пример вывода:

```text
Это желторотый питон по кличке "Каа". Возраст: 34 года.
```

### Задание 2: стадии развития человека

Файл: `task_02_human_stages.py`

Что делает:
- Запрашивает 6 стадий развития человека.
- Не принимает пустые значения.
- Выводит все стадии в одной строке, разделяя через `=>`.

Пример вывода:

```text
Australopithecus => Homo habilis => Homo erectus => Homo neanderthalensis => Homo sapiens => Homo sapiens sapiens
```

## Структура

```text
03_io_and_variables/
  task_01_pet_profile.py
  task_02_human_stages.py
  tests/
    _loader.py
    test_task_01_pet_profile.py
    test_task_02_human_stages.py
```

## Запуск

Из директории `03_io_and_variables`:

```bash
python task_01_pet_profile.py
python task_02_human_stages.py
```

## Проверка (тесты)

Установить `pytest` (если не установлен):

```bash
python -m pip install pytest
```

Запустить тесты:

```bash
python -m pytest -q
```

Ожидаемый результат:
- Все тесты проходят успешно.
