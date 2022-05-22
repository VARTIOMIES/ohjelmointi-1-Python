"""
COMP.CS.100 Programming 1
Tekijä: Onni Merilä
Opiskelijanumero: H299725
Ohjelma tulostaa ruutuja
"""


def print_box(leveys, korkeus, merkki):
    """Tulostaa halutun kokoisen ja näköisen neliön

    :param leveys: int, laatikon leveys
    :param korkeus: int, laatikon korkeus
    :param merkki: str, merkki, jolla laatikko piirretään
    """
    for _ in range(0, korkeus):
        print(merkki*leveys)


def main():
    width = input("Enter the width of a frame: ")
    height = input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")

    print()
    print_box(int(width), int(height), mark)


if __name__ == "__main__":
    main()