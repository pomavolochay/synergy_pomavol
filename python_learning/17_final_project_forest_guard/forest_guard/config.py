"""Central game configuration: terrain, weather, glyphs and tunable balance."""

from __future__ import annotations

from enum import IntEnum
from typing import Final


class Terrain(IntEnum):
    """Type of a single map cell. Stored as an int so it serializes cleanly."""

    EMPTY = 0
    TREE = 1
    RIVER = 2
    HOSPITAL = 3
    SHOP = 4
    FIRE = 5
    SCORCHED = 6


class Weather(IntEnum):
    """Weather state of a single sky cell."""

    CLEAR = 0
    CLOUD = 1
    STORM = 2


TERRAIN_GLYPHS: Final[dict[Terrain, str]] = {
    Terrain.EMPTY: "🟩",
    Terrain.TREE: "🌲",
    Terrain.RIVER: "🌊",
    Terrain.HOSPITAL: "🏥",
    Terrain.SHOP: "🏪",
    Terrain.FIRE: "🔥",
    Terrain.SCORCHED: "🟫",
}

HELICOPTER_GLYPH: Final[str] = "🚁"
BORDER_GLYPH: Final[str] = "⬛"
CLOUD_GLYPH: Final[str] = "⬜"
STORM_GLYPH: Final[str] = "🟥"

DEFAULT_WIDTH: Final[int] = 20
DEFAULT_HEIGHT: Final[int] = 10
MIN_SIZE: Final[int] = 5
MAX_SIZE: Final[int] = 60

FOREST_DENSITY: Final[float] = 0.25
RIVER_COUNT: Final[int] = 2
RIVER_LENGTH: Final[int] = 12

TICK_SECONDS: Final[float] = 0.12
TREE_GROW_EVERY: Final[int] = 15
FIRE_IGNITE_EVERY: Final[int] = 35
FIRE_SPREAD_EVERY: Final[int] = 20
WEATHER_CHANGE_EVERY: Final[int] = 25
FIRES_PER_IGNITION: Final[int] = 3

START_LIVES: Final[int] = 10
START_MAX_TANK: Final[int] = 1

TREE_REWARD: Final[int] = 100
BURN_PENALTY: Final[int] = 150
UPGRADE_TANK_COST: Final[int] = 500
LIFE_PACK_COST: Final[int] = 1000
LIFE_PACK_AMOUNT: Final[int] = 5
STORM_DAMAGE: Final[int] = 1

CLOUD_CHANCE: Final[float] = 0.12
STORM_CHANCE: Final[float] = 0.25

SAVE_FILE: Final[str] = "savegame.json"
