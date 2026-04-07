"""Task 2: Replace consecutive spaces with a single space."""


def normalize_spaces(text: str) -> str:
    """Collapse sequences of spaces into one space."""
    return " ".join(text.split())


def main() -> None:
    text = input()
    print(normalize_spaces(text))


if __name__ == "__main__":
    main()
