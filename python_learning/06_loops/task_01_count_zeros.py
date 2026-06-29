"""Task 1: Count zeros among N input integers."""

n = int(input("Введите количество чисел N: "))
count = 0
for _ in range(n):
    number = int(input("Введите число: "))
    if number == 0:
        count += 1
print(count)
