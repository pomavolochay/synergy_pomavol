"""Task 2: Count natural divisors of X."""

x = int(input("Введите натуральное число X: "))
count = 0
for divisor in range(1, x + 1):
    if x % divisor == 0:
        count += 1
print(count)
