"""Task 1: Check whether an input string is a palindrome."""


def is_palindrome(text: str) -> bool:
    """Return True if text is palindrome, False otherwise."""
    return text == text[::-1]


def main() -> None:
    text = input().strip()
    print("yes" if is_palindrome(text) else "no")


if __name__ == "__main__":
    main()
