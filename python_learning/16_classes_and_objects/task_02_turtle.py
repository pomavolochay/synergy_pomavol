"""Task 2: Turtle movement class."""

import math


class TurtleStepError(ValueError):
    """Raised when turtle step would become invalid."""


class Turtle:
    """Store turtle position and movement step."""

    def __init__(self, x: int = 0, y: int = 0, step: int = 1) -> None:
        if step <= 0:
            raise ValueError("Шаг должен быть положительным.")
        self.x = x
        self.y = y
        self.s = step

    def go_up(self) -> None:
        """Move turtle up by current step."""
        self.y += self.s

    def go_down(self) -> None:
        """Move turtle down by current step."""
        self.y -= self.s

    def go_left(self) -> None:
        """Move turtle left by current step."""
        self.x -= self.s

    def go_right(self) -> None:
        """Move turtle right by current step."""
        self.x += self.s

    def evolve(self) -> None:
        """Increase turtle step by one."""
        self.s += 1

    def degrade(self) -> None:
        """Decrease turtle step by one or raise error if step becomes invalid."""
        if self.s - 1 <= 0:
            raise TurtleStepError("Шаг не может стать меньше или равен нулю.")
        self.s -= 1

    def count_moves(self, x2: int, y2: int) -> int:
        """Return minimum number of moves to reach target coordinates."""
        x_distance = abs(x2 - self.x)
        y_distance = abs(y2 - self.y)
        return math.ceil(x_distance / self.s) + math.ceil(y_distance / self.s)


def main() -> None:
    turtle = Turtle(0, 0, 2)
    turtle.go_right()
    turtle.go_up()
    print(f"Позиция: x={turtle.x}, y={turtle.y}, шаг={turtle.s}")
    print(f"Минимум ходов до (10, 6): {turtle.count_moves(10, 6)}")


if __name__ == "__main__":
    main()
