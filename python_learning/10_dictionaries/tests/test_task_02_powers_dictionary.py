from __future__ import annotations

from _loader import load_module


task_02 = load_module("task_02_powers_dictionary.py", "task_02_powers_dictionary")


def test_create_powers_dict_default_range() -> None:
    powers = task_02.create_powers_dict()

    assert list(powers.keys()) == list(range(10, -6, -1))
    assert powers[10] == 10_000_000_000
    assert powers[9] == 387_420_489
    assert powers[1] == 1
    assert powers[0] == 1
    assert powers[-5] == -0.00032


def test_create_powers_dict_ascending_range() -> None:
    assert task_02.create_powers_dict(-2, 2) == {
        -2: 0.25,
        -1: -1.0,
        0: 1,
        1: 1,
        2: 4,
    }


def test_main_prints_dictionary(monkeypatch, capsys) -> None:
    task_02.main()

    captured = capsys.readouterr()
    assert "10: 10000000000" in captured.out
    assert "-5: -0.00032" in captured.out
