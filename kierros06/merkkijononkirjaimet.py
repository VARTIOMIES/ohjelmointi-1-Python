"""
Ohjelmointi 1
Tekijä: Onni Merilä
Opiskeijanumero: H299725
Tulostaa syötetyn sanan vokaalien ja konsonanttien määrän
"""


def main():
    vokaalit = ("a", "e", "i", "o", "u", "y", "ä", "ö")
    vokaali_määrä = 0
    konsonantti_määrä = 0
    text = input("Enter a word: ")
    for char in text:
        if char in vokaalit:
            vokaali_määrä += 1
        else:
            konsonantti_määrä += 1
    print(f"The word {text} contains {vokaali_määrä} vowels and"
          f" {konsonantti_määrä} consonants")


if __name__ == "__main__":
    main()