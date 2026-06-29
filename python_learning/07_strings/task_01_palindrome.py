"""Task 1: Check whether an input string is a palindrome."""

text = input("Введите строку: ").strip()
print("yes" if text == text[::-1] else "no")
