from __future__ import annotations

from _loader import load_module


def test_stages_joined_with_arrows(monkeypatch, capsys) -> None:
    stages = [
        "Australopithecus",
        "Homo habilis",
        "Homo erectus",
        "Homo neanderthalensis",
        "Homo sapiens",
        "Homo sapiens sapiens",
    ]
    inputs = iter(stages)
    monkeypatch.setattr("builtins.input", lambda *args: next(inputs))

    load_module("task_02_human_stages.py", "task_02_human_stages")

    assert (
        capsys.readouterr().out.strip()
        == "Australopithecus => Homo habilis => Homo erectus => Homo neanderthalensis => Homo sapiens => Homo sapiens sapiens"
    )
