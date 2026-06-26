"""Entry point: wires keyboard input to the game and runs the tick loop."""

from __future__ import annotations

import os
import queue
import time

from pynput import keyboard

from forest_guard.config import (
    DEFAULT_HEIGHT,
    DEFAULT_WIDTH,
    MAX_SIZE,
    MIN_SIZE,
    TICK_SECONDS,
)
from forest_guard.game import Game


def clear_screen() -> None:
    """Clear the terminal on both POSIX and Windows."""
    os.system("cls" if os.name == "nt" else "clear")


def ask_size(prompt: str, default: int) -> int:
    """Ask the player for a map dimension, clamped to the allowed range."""
    raw = input(f"{prompt} [{MIN_SIZE}..{MAX_SIZE}, по умолчанию {default}]: ").strip()
    if not raw:
        return default
    try:
        value = int(raw)
    except ValueError:
        return default
    return max(MIN_SIZE, min(MAX_SIZE, value))


def run() -> None:
    """Create a game, start the keyboard listener and run until game over."""
    width = ask_size("Ширина поля", DEFAULT_WIDTH)
    height = ask_size("Высота поля", DEFAULT_HEIGHT)
    game = Game(width=width, height=height)

    commands: "queue.Queue[str]" = queue.Queue()

    def on_release(key: keyboard.Key | keyboard.KeyCode) -> None:
        char = getattr(key, "char", None)
        if char:
            commands.put(char.lower())

    listener = keyboard.Listener(on_release=on_release)
    listener.start()
    try:
        _loop(game, commands)
    finally:
        listener.stop()

    clear_screen()
    print(f"💀 Игра окончена! Итоговый счёт: {game.helicopter.score}")


def _loop(game: Game, commands: "queue.Queue[str]") -> None:
    while not game.is_over:
        _drain_commands(game, commands)
        game.update()
        clear_screen()
        print(game.render())
        time.sleep(TICK_SECONDS)


def _drain_commands(game: Game, commands: "queue.Queue[str]") -> None:
    """Apply every command queued since the previous tick."""
    while True:
        try:
            command = commands.get_nowait()
        except queue.Empty:
            return
        game.handle_command(command)


if __name__ == "__main__":
    run()
