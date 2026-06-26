"""Game orchestration: world state, the tick loop, commands and rendering."""

from __future__ import annotations

from random import Random

from forest_guard.config import (
    BORDER_GLYPH,
    BURN_PENALTY,
    CLOUD_GLYPH,
    DEFAULT_HEIGHT,
    DEFAULT_WIDTH,
    FIRE_IGNITE_EVERY,
    FIRE_SPREAD_EVERY,
    FIRES_PER_IGNITION,
    HELICOPTER_GLYPH,
    LIFE_PACK_AMOUNT,
    LIFE_PACK_COST,
    SAVE_FILE,
    STORM_DAMAGE,
    STORM_GLYPH,
    TERRAIN_GLYPHS,
    TREE_GROW_EVERY,
    TREE_REWARD,
    UPGRADE_TANK_COST,
    WEATHER_CHANGE_EVERY,
    Terrain,
    Weather,
)
from forest_guard.geometry import Position, random_position
from forest_guard.helicopter import Helicopter
from forest_guard.persistence import load_snapshot, save_snapshot
from forest_guard.weather import Sky

SNAPSHOT_VERSION = 1

_MOVES: dict[str, tuple[int, int]] = {
    "w": (-1, 0),
    "s": (1, 0),
    "a": (0, -1),
    "d": (0, 1),
}


class Game:
    """Holds the whole game state and advances it one tick at a time."""

    def __init__(
        self,
        width: int = DEFAULT_WIDTH,
        height: int = DEFAULT_HEIGHT,
        rng: Random | None = None,
        save_file: str = SAVE_FILE,
    ) -> None:
        self._rng = rng or Random()
        self.save_file = save_file
        from forest_guard.world import World

        self.world = World.generated(width, height, self._rng)
        self.sky = Sky(width, height, self._rng)
        self.helicopter = Helicopter(
            random_position(self._rng, width, height)
        )
        self.tick = 0
        self.running = True
        self.message = "Туши пожары вертолётом! [WASD] двигаться, [E] взаимодействовать."

    def update(self) -> None:
        """Advance the simulation by a single tick."""
        self._apply_cell_effects()
        self._apply_weather()
        self.tick += 1
        if self.tick % TREE_GROW_EVERY == 0:
            self.world.grow_tree()
        if self.tick % FIRE_IGNITE_EVERY == 0:
            self.world.ignite(FIRES_PER_IGNITION)
        if self.tick % FIRE_SPREAD_EVERY == 0:
            self._spread_fires()
        if self.tick % WEATHER_CHANGE_EVERY == 0:
            self.sky.advance()

    def handle_command(self, command: str) -> None:
        """Apply a single player command character."""
        if command in _MOVES:
            d_row, d_col = _MOVES[command]
            self.helicopter.move(d_row, d_col, self.world.in_bounds)
        elif command == "e":
            self._interact()
        elif command == "z":
            self.save()
        elif command == "x":
            self.load()
        elif command == "q":
            self.running = False

    @property
    def is_over(self) -> bool:
        """Return True once the game should stop."""
        return not self.running or not self.helicopter.is_alive

    def _apply_cell_effects(self) -> None:
        terrain = self.world.terrain_at(self.helicopter.position)
        if terrain is Terrain.RIVER:
            self.helicopter.refill()
        elif terrain is Terrain.FIRE and self.helicopter.use_water():
            self.world.extinguish(self.helicopter.position)
            self.helicopter.reward(TREE_REWARD)
            self.message = f"Пожар потушен! +{TREE_REWARD} очков."

    def _apply_weather(self) -> None:
        if self.sky.is_storm(self.helicopter.position):
            self.helicopter.damage(STORM_DAMAGE)
            self.message = f"Удар молнии! -{STORM_DAMAGE} жизни."

    def _spread_fires(self) -> None:
        burned = self.world.spread_fires()
        if burned:
            penalty = burned * BURN_PENALTY
            self.helicopter.penalize(penalty)
            self.message = f"Сгорело деревьев: {burned}. -{penalty} очков."

    def _interact(self) -> None:
        terrain = self.world.terrain_at(self.helicopter.position)
        if terrain is Terrain.SHOP:
            if self.helicopter.buy_tank_upgrade(UPGRADE_TANK_COST):
                self.message = "Резервуар улучшен! +1 к объёму."
            else:
                self.message = f"Не хватает очков (нужно {UPGRADE_TANK_COST})."
        elif terrain is Terrain.HOSPITAL:
            if self.helicopter.buy_lives(LIFE_PACK_COST, LIFE_PACK_AMOUNT):
                self.message = f"Госпиталь: +{LIFE_PACK_AMOUNT} жизней."
            else:
                self.message = f"Не хватает очков (нужно {LIFE_PACK_COST})."
        else:
            self.message = "Здесь не с чем взаимодействовать."

    def snapshot(self) -> dict:
        """Capture the full game state as a serializable dictionary."""
        return {
            "version": SNAPSHOT_VERSION,
            "tick": self.tick,
            "world": self.world.to_dict(),
            "sky": self.sky.to_dict(),
            "helicopter": self.helicopter.to_dict(),
        }

    def restore(self, data: dict) -> None:
        """Replace the current state with a previously captured snapshot."""
        from forest_guard.world import World

        self.tick = data["tick"]
        self.world = World.from_dict(data["world"], self._rng)
        self.sky = Sky.from_dict(data["sky"], self._rng)
        self.helicopter = Helicopter.from_dict(data["helicopter"])

    def save(self) -> None:
        """Persist the current game to the configured save file."""
        save_snapshot(self.save_file, self.snapshot())
        self.message = "Игра сохранена."

    def load(self) -> None:
        """Restore the game from the configured save file, if present."""
        try:
            self.restore(load_snapshot(self.save_file))
            self.message = "Игра загружена."
        except FileNotFoundError:
            self.message = "Сохранение не найдено."

    def render(self) -> str:
        """Return the full textual frame: HUD, map and status message."""
        return "\n".join((self._render_hud(), self._render_map(), self._render_footer()))

    def _render_hud(self) -> str:
        helicopter = self.helicopter
        return (
            f"🪣 {helicopter.tank}/{helicopter.max_tank}   "
            f"🏆 {helicopter.score}   "
            f"❤️ {helicopter.lives}   "
            f"⏱ {self.tick}"
        )

    def _render_map(self) -> str:
        top = BORDER_GLYPH * (self.world.width + 2)
        rows = [top]
        for row in range(self.world.height):
            cells = "".join(
                self._glyph(Position(row, col)) for col in range(self.world.width)
            )
            rows.append(f"{BORDER_GLYPH}{cells}{BORDER_GLYPH}")
        rows.append(top)
        return "\n".join(rows)

    def _render_footer(self) -> str:
        return (
            f"{self.message}\n"
            "[WASD] движение  [E] магазин/госпиталь  "
            "[Z] сохранить  [X] загрузить  [Q] выход"
        )

    def _glyph(self, position: Position) -> str:
        """Pick the glyph for a cell, layering helicopter and weather on top."""
        if self.helicopter.position == position:
            return HELICOPTER_GLYPH
        terrain = self.world.terrain_at(position)
        if terrain is Terrain.FIRE:
            return TERRAIN_GLYPHS[Terrain.FIRE]
        weather = self.sky.weather_at(position)
        if weather is Weather.STORM:
            return STORM_GLYPH
        if weather is Weather.CLOUD:
            return CLOUD_GLYPH
        return TERRAIN_GLYPHS[terrain]
