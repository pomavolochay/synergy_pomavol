# 14_recursion

Решение задачи по рекурсии: вывод элементов списка без циклов.

## Задание 1: рекурсивный вывод списка

Файл: `task_01_recursive_list_print.py`

Логика:
- Есть список `MY_LIST` со значениями от `0` до `16`.
- Функция `print_list_recursive()` выводит элементы от первого до последнего.
- После последнего элемента выводится сообщение `Конец списка`.
- Циклы в рабочей функции не используются.

Базовый случай рекурсии:

```python
if index >= len(values):
    print(END_MESSAGE)
    return
```

## Структура

```text
14_recursion/
  task_01_recursive_list_print.py
  tests/
    _loader.py
    test_task_01_recursive_list_print.py
```

## Запуск

Из директории `14_recursion`:

```bash
python task_01_recursive_list_print.py
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
