from __future__ import annotations

from _loader import load_module


task_01 = load_module("task_01_transport_inheritance.py", "task_01_transport_inheritance")


def test_autobus_inherits_transport() -> None:
    autobus = task_01.Autobus("Renaul Logan", 180, 12)

    assert isinstance(autobus, task_01.Transport)
    assert autobus.name == "Renaul Logan"
    assert autobus.max_speed == 180
    assert autobus.mileage == 12


def test_autobus_string_representation() -> None:
    autobus = task_01.Autobus("Renaul Logan", 180, 12)

    assert str(autobus) == "Название автомобиля: Renaul Logan Скорость: 180 Пробег: 12"


def test_main_prints_expected_output(capsys) -> None:
    task_01.main()

    captured = capsys.readouterr()
    assert captured.out.strip() == "Название автомобиля: Renaul Logan Скорость: 180 Пробег: 12"
