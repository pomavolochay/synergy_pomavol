"""Task 2: Compute a formula based on digits of a five-digit integer."""

number = abs(int(input("Введите пятизначное целое число: ")))
ten_thousands = number // 10000
thousands = (number // 1000) % 10
hundreds = (number // 100) % 10
tens = (number // 10) % 10
ones = number % 10
result = (tens ** ones) * hundreds / (ten_thousands - thousands)
print(f"Результат: {result}")
