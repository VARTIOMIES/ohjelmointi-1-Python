"""
COMP.CS.100 Programming 1
Tekijä: Onni Merilä
Opiskelijanumero: H299725
Ohjelma kirjoittaa syötteistä tiedoston, jonka nimen käyttäjä antaa.
Ohjelma lisää tiedostoon myös tekstirivien numerot.
"""


def read_message():
    """ Lukee käyttäjän syötteen ueammalta riviltä ja palauttaa listan, jonka
    alkioita ovat eri riveillä oleva tekstit

    :return: list,
    """
    text_list = []
    while True:
        text = input()
        if text.strip() == "":
            break
        text_list.append(text)
    return text_list


def main():

    filename = input("Enter the name of the file: ")

    try:
        write_file = open(filename, mode="w")

    except OSError:
        print(f"Writing the file {filename} was not successful.")
        return

    print("Enter rows of text. Quit by entering an empty row.")
    lines = read_message()
    # Nyt meillä on tekstirivit listassa. Tallennetaan ne tiedostoon write_file

    line_number = 1
    for line in lines:

        print(line_number, line, file=write_file)

        line_number += 1

    write_file.close()

    print(f"File {filename} has been written.")





if __name__ == "__main__":
    main()