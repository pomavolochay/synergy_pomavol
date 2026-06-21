"""Task 1: Create Autobus object inherited from Transport."""


class Transport:
    """Base transport model."""

    def __init__(self, name: str, max_speed: int, mileage: int) -> None:
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def __str__(self) -> str:
        return (
            f"Название автомобиля: {self.name} "
            f"Скорость: {self.max_speed} "
            f"Пробег: {self.mileage}"
        )


class Autobus(Transport):
    """Autobus inherits all behavior from Transport."""


def main() -> None:
    autobus = Autobus("Renaul Logan", 180, 12)
    print(autobus)


if __name__ == "__main__":
    main()
