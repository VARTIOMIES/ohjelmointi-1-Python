"""
COMP.CS.100 Programming 1
Tekijä: Onni Merilä
Opiskelijanumero: H299725
Ohjelma tulostaa Yogi Bear -laulun
"""


def verse(sanat, nimi):
    """Tulostaa säkeistön annetuilla sanoilla ja karhun ninmellä

    :param sanat: str,
    :param nimi: str,
    """
    print(sanat)
    print(f"{nimi}, {nimi}")
    print(sanat)
    repeat_name(nimi, 3)
    print(sanat)
    repeat_name(nimi,1)
    print()

def repeat_name(toistettava, määrä):
    """Toistaa karhun nimen ja tulostaa sen halutun verran kertoja

    :param toistettava: int,
    :param määrä: int,
    :return:
    """
    for _ in range(0, määrä):
        print(f"{toistettava}, {toistettava} Bear")


def main():
    verse("I know someone you don't know", "Yogi")
    verse("Yogi has a best friend too", "Boo Boo")
    verse("Yogi has a sweet girlfriend", "Cindy")


if __name__ == "__main__":
    main()


