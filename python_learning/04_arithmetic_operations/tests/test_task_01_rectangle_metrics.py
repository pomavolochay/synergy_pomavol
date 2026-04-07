from __future__ import annotations

from _loader import load_module


task_01 = load_module("task_01_rectangle_metrics.py", "task_01_rectangle_metrics")


def test_calculate_rectangle_metrics() -> None:
    area, perimeter = task_01.calculate_rectangle_metrics(3.5, 2)
    assert area == 7.0
    assert perimeter == 11.0


def test_read_positive_float_retries(monkeypatch, capsys) -> None:
    inputs = iter(["abc", "0", "-2", "2,5"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    value = task_01.read_positive_float("Введите сторону: ")

    captured = capsys.readouterr()
    assert value == 2.5
    assert "Введите корректное число" in captured.out
    assert captured.out.count("Значение должно быть больше нуля") == 2


def test_main_prints_metrics(monkeypatch, capsys) -> None:
    inputs = iter(["3", "4"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    task_01.main()

    captured = capsys.readouterr()
    lines = captured.out.strip().splitlines()
    assert lines == ["Площадь: 12.0", "Периметр: 14.0"]
