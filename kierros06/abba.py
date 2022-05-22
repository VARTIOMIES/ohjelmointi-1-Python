"""
Progrmaming 1
Tekijä: Onni Merilä
Opiskelijanumero: H299725
"""


def count_abbas(text):
    """Laskee syötteessä olevien kirjainyhdistelmien "abba" määrän
    (eri kuin .count())
    :param text: str,
    :return: int,
    """
    abba_counter = 0
    for char_index in range(len(text)):
        char = text[char_index]

        if char_index + 3 >= len(text):
            break

        if char.lower() == "a":
            pass
        else:
            continue

        if text[char_index:(char_index+4)].lower() == "abba":
            abba_counter += 1

    return abba_counter
