"""Task 2: Create dictionary with numbers and their own powers."""


def create_powers_dict(start: int = 10, end: int = -5) -> dict[int, float | int]:
    """Create dictionary {number: number ** number} for descending range."""
    step = -1 if start >= end else 1
    return {
        number: number**number
        for number in range(start, end + step, step)
    }


def main() -> None:
    powers = create_powers_dict()
    print(powers)


if __name__ == "__main__":
    main()
