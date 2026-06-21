from __future__ import annotations

from _loader import load_module


task_01 = load_module("task_01_recursive_list_print.py", "task_01_recursive_list_print")


def test_print_list_recursive_prints_values_and_end_message(capsys) -> None:
    task_01.print_list_recursive([1, 2, 3])

    captured = capsys.readouterr()
    assert captured.out.strip().splitlines() == ["1", "2", "3", "Конец списка"]


def test_print_list_recursive_handles_empty_list(capsys) -> None:
    task_01.print_list_recursive([])

    captured = capsys.readouterr()
    assert captured.out.strip() == "Конец списка"


def test_main_prints_default_sequence(capsys) -> None:
    task_01.main()

    captured = capsys.readouterr()
    assert captured.out.strip().splitlines() == [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "11",
        "12",
        "13",
        "14",
        "15",
        "16",
        "Конец списка",
    ]
