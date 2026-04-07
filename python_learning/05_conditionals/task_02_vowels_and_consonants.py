"""Task 2: Count vowels and consonants in a lowercase latin word."""

VOWELS = "aeiou"


def analyze_word(word: str) -> tuple[int, int, dict[str, int | bool]]:
    """Return consonant and vowel counts plus per-vowel stats."""
    vowel_counts: dict[str, int | bool] = {}
    total_vowels = 0

    for vowel in VOWELS:
        count = word.count(vowel)
        vowel_counts[vowel] = count if count > 0 else False
        total_vowels += count

    consonants = len(word) - total_vowels
    return consonants, total_vowels, vowel_counts


def main() -> None:
    word = input("Введите слово из маленьких латинских букв: ").strip()
    consonants, vowels, vowel_counts = analyze_word(word)

    print(f"Количество согласных: {consonants}")
    print(f"Количество гласных: {vowels}")

    for vowel in VOWELS:
        print(f"{vowel}: {vowel_counts[vowel]}")


if __name__ == "__main__":
    main()
