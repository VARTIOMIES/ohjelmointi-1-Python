"""
COMP.CS.100 Programming 1
Tekijä: Onni Merilä
Opiskelijanumero: H299725
"""


def read_message():
    """ Lukee käyttäjän syötteen ueammalta riviltä ja palauttaa listan, jonka
    alkioita ovat eri riveillä oleva tekstit

    :return: list,
    """
    text_list = []
    while True:
        text = input()
        if text == "":
            break
        text_list.append(text)
    return text_list


def encrypt(text):
    """
    Encrypts its parameter using ROT13 encryption technology.

    :param text: str,  string to be encrypted
    :return: str, <text> parameter encrypted using ROT13
    """

    regular_chars   = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                       "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                       "w", "x", "y", "z"]

    encrypted_chars = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                       "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                       "j", "k", "l", "m"]

    encrypted_text = ""
    for char in text:

        if char in regular_chars:
            index_of_char = regular_chars.index(char)
            encrypted_char = encrypted_chars[index_of_char]

        elif char.lower() in regular_chars:
            index_of_char = regular_chars.index(char.lower())
            encrypted_char = encrypted_chars[index_of_char].upper()

        else:
            encrypted_char = char
        encrypted_text += encrypted_char

    return encrypted_text


def row_encryption(text):
    """

    :param text: str
    :return: str
    """
    new_text = ""
    for char in text:
        new_text += encrypt(char)

    return new_text


def main():
    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message()

    print("ROT13:")
    for rows in msg:
        print(row_encryption(rows))


if __name__ == "__main__":
    main()
