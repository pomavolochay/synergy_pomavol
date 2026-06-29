from __future__ import annotations

from _loader import load_module


def run_script(monkeypatch, values: list[str]) -> None:
    inputs = iter(values)
    monkeypatch.setattr("builtins.input", lambda *args: next(inputs))
    load_module("task_01_rectangle_metrics.py", "task_01_rectangle_metrics")


def test_integer_sides(monkeypatch, capsys) -> None:
    run_script(monkeypatch, ["3", "4"])

    assert capsys.readouterr().out.strip().splitlines() == ["Площадь: 12.0", "Периметр: 14.0"]


def test_decimal_side_with_comma(monkeypatch, capsys) -> None:
    run_script(monkeypatch, ["3,5", "2"])

    assert capsys.readouterr().out.strip().splitlines() == ["Площадь: 7.0", "Периметр: 11.0"]
