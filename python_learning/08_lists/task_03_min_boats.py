"""Task 3: Compute minimum boats to move all fishermen."""


def read_int(prompt: str) -> int:
    """Read integer from user input."""
    while True:
        raw_value = input(prompt).strip()
        try:
            return int(raw_value)
        except ValueError:
            print("Введите корректное целое число.")


def min_boats(limit: int, weights: list[int]) -> int:
    """Return minimal number of boats using two-pointer greedy approach."""
    sorted_weights = sorted(weights)
    left = 0
    right = len(sorted_weights) - 1
    boats = 0

    while left <= right:
        if left == right:
            boats += 1
            break

        if sorted_weights[left] + sorted_weights[right] <= limit:
            left += 1

        right -= 1
        boats += 1

    return boats


def main() -> None:
    while True:
        limit = read_int("Введите максимальную массу лодки m: ")
        if 1 <= limit <= 10_000_000:
            break
        print("m должно быть в диапазоне [1, 10000000].")

    while True:
        count = read_int("Введите количество рыбаков n: ")
        if 1 <= count <= 100:
            break
        print("n должно быть в диапазоне [1, 100].")

    weights: list[int] = []
    for index in range(1, count + 1):
        while True:
            weight = read_int(f"Введите вес рыбака #{index}: ")
            if 1 <= weight <= limit:
                weights.append(weight)
                break
            print(f"Вес должен быть в диапазоне [1, {limit}].")

    print(min_boats(limit, weights))


if __name__ == "__main__":
    main()
