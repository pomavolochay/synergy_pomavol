"""Reading and writing game snapshots as JSON files."""

from __future__ import annotations

import json
from pathlib import Path


def save_snapshot(path: str | Path, snapshot: dict) -> None:
    """Write a snapshot dictionary to disk as formatted JSON."""
    Path(path).write_text(
        json.dumps(snapshot, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def load_snapshot(path: str | Path) -> dict:
    """Read a snapshot dictionary from a JSON file.

    Raises FileNotFoundError if the save file does not exist.
    """
    return json.loads(Path(path).read_text(encoding="utf-8"))
