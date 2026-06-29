from __future__ import annotations

from _loader import load_module


def run_script(monkeypatch, values: list[str]) -> None:
    inputs = iter(values)
    monkeypatch.setattr("builtins.input", lambda *args: next(inputs))
    load_module("task_01_pet_profile.py", "task_01_pet_profile")


def test_profile_line(monkeypatch, capsys) -> None:
    run_script(monkeypatch, ["желторотый питон", "34", "Каа"])

    assert capsys.readouterr().out.strip() == 'Это желторотый питон по кличке "Каа". Возраст: 34 года.'


def test_year_singular(monkeypatch, capsys) -> None:
    run_script(monkeypatch, ["кот", "1", "Барсик"])

    assert capsys.readouterr().out.strip().endswith("Возраст: 1 год.")


def test_year_plural(monkeypatch, capsys) -> None:
    run_script(monkeypatch, ["кот", "11", "Барсик"])

    assert capsys.readouterr().out.strip().endswith("Возраст: 11 лет.")
