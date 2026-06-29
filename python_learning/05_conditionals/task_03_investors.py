"""Task 3: Determine startup investment scenario."""

minimum = int(input("Введите минимальную сумму инвестиций X: "))
mike = int(input("Введите сумму Майкла A: "))
ivan = int(input("Введите сумму Ивана B: "))

if mike >= minimum and ivan >= minimum:
    print("2")
elif mike >= minimum:
    print("Mike")
elif ivan >= minimum:
    print("Ivan")
elif mike + ivan >= minimum:
    print("1")
else:
    print("0")
