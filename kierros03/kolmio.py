"""
COMP.CS.100 Programming 1
Tekijä: Onni Merilä
Opiskelijanumero: H299725
"""

from math import sqrt


def area(a, b, c):
    """Laskee kolmion, jonka sivujen pituudet annetaan, pinta-alan

    :param a: float, 1. kolmion sivu
    :param b: float, 2. kolmion sivu
    :param c: float, 3. kolmion sivu
    :return: float, kolmion pinta-ala
    """
    s = (a+b+c) / 2
    return sqrt(s * (s-a) * (s-b) * (s-c))


def main():
    line1 = float(input("Enter the length of the first side: "))
    line2 = float(input("Enter the length of the second side: "))
    line3 = float(input("Enter the length of the third side: "))

    print(f"The triangle's area is {area(line1, line2, line3):.1f}")


if __name__ == "__main__":
    main()