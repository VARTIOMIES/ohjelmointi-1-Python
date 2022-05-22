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


def main():
    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message()

    print("The same, shouting:")
    for rows in msg:
        print(rows.upper())


if __name__ == "__main__":
    main()