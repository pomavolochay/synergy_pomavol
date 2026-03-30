from __future__ import annotations

from _loader import load_module


task_02 = load_module("task_02_human_stages.py", "task_02_human_stages")


def test_collect_stages_returns_expected_values(monkeypatch) -> None:
    inputs = iter([
        "Australopithecus",
        "Homo habilis",
        "Homo erectus",
        "Homo neanderthalensis",
        "Homo sapiens",
        "Homo sapiens sapiens",
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    stages = task_02.collect_stages(6)

    assert stages == [
        "Australopithecus",
        "Homo habilis",
        "Homo erectus",
        "Homo neanderthalensis",
        "Homo sapiens",
        "Homo sapiens sapiens",
    ]


def test_collect_stages_retries_when_stage_is_blank(monkeypatch, capsys) -> None:
    inputs = iter(["", "Australopithecus"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    stages = task_02.collect_stages(1)

    captured = capsys.readouterr()
    assert stages == ["Australopithecus"]
    assert "Стадия не должна быть пустой" in captured.out


def test_main_prints_stages_with_arrow_separator(monkeypatch, capsys) -> None:
    inputs = iter([
        "Australopithecus",
        "Homo habilis",
        "Homo erectus",
        "Homo neanderthalensis",
        "Homo sapiens",
        "Homo sapiens sapiens",
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    task_02.main()

    captured = capsys.readouterr()
    assert (
        captured.out.strip()
        == "Australopithecus => Homo habilis => Homo erectus => Homo neanderthalensis => Homo sapiens => Homo sapiens sapiens"
    )
