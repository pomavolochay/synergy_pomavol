from __future__ import annotations

from _loader import load_module


task_02 = load_module("task_02_autobus_capacity.py", "task_02_autobus_capacity")


def test_autobus_default_capacity() -> None:
    autobus = task_02.Autobus("Renaul Logan", 180, 12)

    assert autobus.seating_capacity() == "Вместимость одного автобуса Renaul Logan: 50 пассажиров"


def test_autobus_custom_capacity() -> None:
    autobus = task_02.Autobus("Renaul Logan", 180, 12)

    assert autobus.seating_capacity(30) == "Вместимость одного автобуса Renaul Logan: 30 пассажиров"


def test_autobus_inherits_transport() -> None:
    autobus = task_02.Autobus("Renaul Logan", 180, 12)

    assert isinstance(autobus, task_02.Transport)


def test_main_prints_expected_output(capsys) -> None:
    task_02.main()

    captured = capsys.readouterr()
    assert captured.out.strip() == "Вместимость одного автобуса Renaul Logan: 50 пассажиров"
