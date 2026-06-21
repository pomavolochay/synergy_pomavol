"""Task 1: Cash register class."""


class NotEnoughMoneyError(ValueError):
    """Raised when cash register does not have enough money."""


class CashRegister:
    """Store and manage current cash amount."""

    def __init__(self, balance: int = 0) -> None:
        if balance < 0:
            raise ValueError("Начальный баланс не может быть отрицательным.")
        self.balance = balance

    def top_up(self, amount: int) -> None:
        """Top up cash register by amount."""
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной.")
        self.balance += amount

    def count_1000(self) -> int:
        """Return how many full thousands are in cash register."""
        return self.balance // 1000

    def take_away(self, amount: int) -> None:
        """Withdraw amount or raise an error if balance is not enough."""
        if amount <= 0:
            raise ValueError("Сумма списания должна быть положительной.")
        if amount > self.balance:
            raise NotEnoughMoneyError("Недостаточно денег в кассе.")
        self.balance -= amount


def main() -> None:
    cash_register = CashRegister(2500)
    cash_register.top_up(1500)
    print(f"Баланс: {cash_register.balance}")
    print(f"Целых тысяч: {cash_register.count_1000()}")
    cash_register.take_away(1200)
    print(f"Баланс после списания: {cash_register.balance}")


if __name__ == "__main__":
    main()
