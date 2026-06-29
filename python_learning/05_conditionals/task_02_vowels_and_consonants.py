"""Task 2: Count vowels and consonants in a lowercase latin word."""

word = input("Введите слово из маленьких латинских букв: ").strip()
vowels = "aeiou"

vowel_total = 0
for letter in vowels:
    vowel_total += word.count(letter)

print(f"Количество согласных: {len(word) - vowel_total}")
print(f"Количество гласных: {vowel_total}")

for letter in vowels:
    count = word.count(letter)
    if count > 0:
        print(f"{letter}: {count}")
    else:
        print(f"{letter}: False")
