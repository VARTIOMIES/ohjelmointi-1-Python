"""
COMP.CS.100 Programming 1
Tekijä: Onni Merilä
Opsikelijanumero: H299725
Ohjelma tulostaa todennäköisyyden voittaa lotossa, jonka arvottujen numeroiden
lukumäärän käyttäjä syöttää.
"""


def positiivinen(arvo, arvo2):
    """
    Tarkistaa, ovatko annetut luvut positiivisia kokonaislukuja

    :param arvo: int, annettu arvo 1
    :param arvo2: int, annettu arvo 2
    :return: bool, Palauttaa True, jos molemmat arvot ovat suurempaa kuin 0
    """
    return arvo > 0 and arvo2 > 0


def liian_paljon(arvo, arvo2):
    """
    Tarkistaa, että palloja ei yritetä ottaa liikaa

    :param arvo: int, kaikkien pallojen määrä
    :param arvo2: int, otettavien pallojen määrä
    :return: bool, palauttaa False, jos palloja otetaan liikaa
    """
    return arvo < arvo2


def lottorivien_määrä(n, p):
    """
    Laskee lottorivien määrän

    :param n: int, kaikki pallot
    :param p: int, nostetut pallot
    :return: int, lottorivien määrä
    """
    k = n - p

    # Lasketaan kertomat

    # n
    a = 1
    for index in range(1, n+1):
        a = index * a

    # k
    b = 1
    for index in range(1, k+1):
        b = index * b

    # p
    c = 1
    for index in range(1, p+1):
        c = index * c

    # Lasketaan lottorivien määrä
    lottorivejä = a / (b * c)
    return int(lottorivejä)


def main():
    kaikki_pallot = int(input("Enter the total number of lottery balls: "))
    otetut_pallot = int(input("Enter the number of the drawn balls: "))

    # Tarkistetaan että arvot ovat positiivisia ja palloja ei yritetä ottaa
    # liikaa
    if positiivinen(kaikki_pallot, otetut_pallot):
        if not liian_paljon(kaikki_pallot, otetut_pallot):
            # Lasketaan lottorivien lukumäärä
            lottorivit = lottorivien_määrä(kaikki_pallot, otetut_pallot)

            # Tulostetaan todennäköisyys
            print(f"The probability of guessing all {otetut_pallot} balls "
                  f"correctly is 1/{lottorivit}")
        else:
            print("At most the total number of balls can be drawn.")
    else:
        print("The number of balls must be a positive number.")


if __name__ == "__main__":
    main()
