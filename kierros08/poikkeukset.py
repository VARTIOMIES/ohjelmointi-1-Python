"""
COMP.CS.100 Programming 1
Tekijä: Onni Merilä
Opiskelijanumero: H299725
Print a box with input error checking
"""


def read_input(text):
    """Pyytää käyttäjältä lukua niin kauan, kunnes saa positiivisen luvun

    :param text: str, kysymys jonka käyttäjä näkee
    :return: float, palauttaa positiivisen luvun
    """
    annettu = 0

    while annettu <= 0:
        try:
            annettu = int(input(text))
        except ValueError:
            pass

    return annettu


def print_box(leveys, korkeus, merkki):
    """Tulostaa halutun kokoisen ja näköisen neliön

    :param leveys: int, laatikon leveys
    :param korkeus: int, laatikon korkeus
    :param merkki: str, merkki, jolla laatikko piirretään
    """
    for _ in range(0, korkeus):
        print(merkki*leveys)


def main():
    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")

    print_box(width, height, mark)


if __name__ == "__main__":
    main()
