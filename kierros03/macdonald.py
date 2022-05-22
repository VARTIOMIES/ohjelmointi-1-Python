"""
COMP.CS.100 Programming 1
Tekijä: Onni Merilä
Opiskelijanumero: H299725
Template Song: Old MacDonald
"""


def print_verse(eläin, ääni):
    """Tulostaa säkeistön annetun eläimen ja sen äänen mukaan

    :param eläin: str, säkeistön haluttu eläin
    :param ääni: str, säkeitön eläimen äänähdys
    """
    print(f"""Old MACDONALD had a farm
E-I-E-I-O
And on his farm he had a {eläin}
E-I-E-I-O
With a {ääni} {ääni} here
And a {ääni} {ääni} there
Here a {ääni}, there a {ääni}
Everywhere a {ääni} {ääni}
Old MacDonald had a farm
E-I-E-I-O
""")


def main():
    print_verse("cow", "moo")
    print_verse("pig", "oink")
    print_verse("duck", "quack")
    print_verse("horse", "neigh")
    print_verse("lamb", "baa")


if __name__ == "__main__":
    main()
