"""Task 2: Override seating capacity for Autobus."""


class Transport:
    """Base transport model."""

    def __init__(self, name: str, max_speed: int, mileage: int) -> None:
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity: int) -> str:
        return f"Вместимость одного автобуса {self.name}: {capacity} пассажиров"


class Autobus(Transport):
    """Autobus with default seating capacity."""

    def seating_capacity(self, capacity: int = 50) -> str:
        return super().seating_capacity(capacity)


def main() -> None:
    autobus = Autobus("Renaul Logan", 180, 12)
    print(autobus.seating_capacity())


if __name__ == "__main__":
    main()
