"""Task 2: Collect and print the stages of human evolution."""

STAGE_COUNT = 6


def read_non_empty(prompt: str) -> str:
    """Read a non-empty user input."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Стадия не должна быть пустой. Попробуйте еще раз.")


def collect_stages(count: int) -> list[str]:
    """Collect human evolution stages from user input."""
    stages: list[str] = []
    for index in range(1, count + 1):
        prompt = f"Введите {index}-ю стадию развития человека: "
        stages.append(read_non_empty(prompt))
    return stages


def main() -> None:
    stages = collect_stages(STAGE_COUNT)
    print(*stages, sep=" => ")


if __name__ == "__main__":
    main()
