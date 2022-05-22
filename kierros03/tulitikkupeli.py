"""
COMP.CS.100 Ensimmäinen projekti: Tulitikkupeli
Tekijä: Onni Merilä
Opiskelijanumero: H299725
"""

"""
Ohjelma tulostaa tulitikkupelin, jonka voittaa,
kun vastustaja nostaa viimeisen tulitikun
"""


def main():
    print("Game of sticks")

    # Määritellään aluksi tulitikkujen aloitusmäärä ja pelaaja, joka aloittaa.
    tulitikkujen_maara = 21
    pelaaja = 1

    while True:
        # Kysytään pelaajalta, kuinka monta tikkua hän haluaa poistaa
        poistettava_maara = int(
            input(f"Player {pelaaja} enter how many sticks to remove: "))

        # Tarkistetaan, että poistetaan vain 1-3 tikkua.
        # Muuten palataan takaisin alkuun.
        if poistettava_maara != 1 and poistettava_maara != 2 and \
                poistettava_maara != 3:
            print("Must remove between 1-3 sticks!")
            continue

        # Poistetaan tikut.
        tulitikkujen_maara = tulitikkujen_maara - poistettava_maara

        # Tarkistetaan, että tulitikkuja on vielä jäljellä.
        # Jos tulitikut on loppu, poistutaan silmukasta ja peli on päättynyt.
        if tulitikkujen_maara <= 0:
            break

        # Tulostetaan tulitikkujen määrä
        print(f"There are {tulitikkujen_maara} sticks left")

        # Siirrytään seuraavan pelaajan vuoroon
        if pelaaja == 1:
            pelaaja = 2
        else:
            pelaaja = 1

    # Pelin päättyminen.
    print(f"Player {pelaaja} lost the game!")


if __name__ == "__main__":
    main()
