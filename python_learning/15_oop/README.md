# 15_oop

Решения задач по наследованию и переопределению методов в ООП.

## Задание 1: наследование от `Transport`

Файл: `task_01_transport_inheritance.py`

Логика:
- Создан родительский класс `Transport`.
- Создан дочерний класс `Autobus`.
- `Autobus` наследует поля `name`, `max_speed`, `mileage`.
- Для красивого вывода реализован метод `__str__()`.

Ожидаемый вывод:

```text
Название автомобиля: Renaul Logan Скорость: 180 Пробег: 12
```

## Задание 2: переопределение метода

Файл: `task_02_autobus_capacity.py`

Логика:
- `Autobus` наследуется от `Transport`.
- Метод `seating_capacity()` переопределен.
- Значение вместимости по умолчанию равно `50`.
- Внутри переопределенного метода используется `super()`.

Ожидаемый вывод:

```text
Вместимость одного автобуса Renaul Logan: 50 пассажиров
```

## Структура

```text
15_oop/
  task_01_transport_inheritance.py
  task_02_autobus_capacity.py
  tests/
    _loader.py
    test_task_01_transport_inheritance.py
    test_task_02_autobus_capacity.py
```

## Запуск

Из директории `15_oop`:

```bash
python task_01_transport_inheritance.py
python task_02_autobus_capacity.py
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
