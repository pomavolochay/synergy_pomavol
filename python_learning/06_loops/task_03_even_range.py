"""Task 3: Print all even numbers in [A, B]."""

a = int(input("Введите A: "))
b = int(input("Введите B: "))
evens = []
for number in range(a, b + 1):
    if number % 2 == 0:
        evens.append(number)
print(*evens)
