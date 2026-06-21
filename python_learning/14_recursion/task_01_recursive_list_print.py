"""Task 1: Print list values recursively without loops."""

MY_LIST = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
END_MESSAGE = "Конец списка"


def print_list_recursive(values: list[int], index: int = 0) -> None:
    """Print all list values recursively and then print the end message."""
    if index >= len(values):
        print(END_MESSAGE)
        return

    print(values[index])
    print_list_recursive(values, index + 1)


def main() -> None:
    print_list_recursive(MY_LIST)


if __name__ == "__main__":
    main()
