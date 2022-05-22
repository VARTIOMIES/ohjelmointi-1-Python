"""
COMP.CS.100 Programming 1
ROT13 program code template
Muokkaaja: Onni Merilä
Opiskelijanumero: H299725
"""


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
