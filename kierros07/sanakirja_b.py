"""
COMP.CS.100 Programming 1
Tekijä: Onni Merilä
Opiskelijanumero: H299725

Code template for  tourist dictionary.
"""


def main():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}
    print("Dictionary contents:")
    lista = sorted(english_spanish)
    print(", ".join(lista))
    while True:

        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        if command == "W":

            word = input("Enter the word to be translated: ")
            if word in english_spanish:
                print(word, "in Spanish is", english_spanish[word])
            else:
                print("The word", word, "could not be found from the "
                                        "dictionary.")

        elif command == "A":
            word = input("Give the word to be added in English: ")
            word_translated = input("Give the word to be added in Spanish: ")
            english_spanish[word] = word_translated
            print("Dictionary contents:")
            lista = sorted(english_spanish)
            print(", ".join(lista))
        
        elif command == "R":
            word = input("Give the word to be removed: ")
            if word in english_spanish:
                del english_spanish[word]
            else:
                print("The word", word, "could not be found from the "
                                        "dictionary.")

        elif command == "P":
            for word in sorted(english_spanish):
                print(word, english_spanish[word])

        elif command == "T":
            line = input("Enter the text to be translated into Spanish: ")
            line_list = line.split()

            for word_index in range(len(line_list)):
                word = line_list[word_index]

                if word in english_spanish:
                    line_list[word_index] = english_spanish[word]

            line = " ".join(line_list)

            print("The text, translated by the dictionary:")
            print(line)

        elif command == "Q":
            print("Adios!")
            return

        else:
            print("Unknown command, enter W, A, R, P, T or Q!")


if __name__ == "__main__":
    main()
