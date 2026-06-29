"""Task 2: Collect and print the stages of human evolution."""

stages = []
for index in range(1, 7):
    stages.append(input(f"Введите {index}-ю стадию развития человека: "))

print(*stages, sep=" => ")
