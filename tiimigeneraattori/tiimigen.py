
from random import *

TYYPIT = {"Otto", "Petteri", "Onni V.", "Viivi O.", "Matias", "Aaron",
          "Viivi M.", "Jesse", "Ronja", "Sami", "Kaarle", "Kasperi", "Ville",
          "Niina", "Aapo", "Miro", "Onni M."}
MAKSIMI_KOKO = 6
RYHMIEN_MAARA = 3


def tiimijako(tyypit, num_of_groups):
    group = []
    for _ in range(num_of_groups):
        group.append([])
    for tyyppi in tyypit:

        rng_group = randint(0, num_of_groups-1)
        # Jos ryhmä on täynnä, arvotaan uusi
        while len(group[rng_group]) >= MAKSIMI_KOKO:
            rng_group = randint(0, num_of_groups-1)

        group[rng_group].append(tyyppi)

    return group


def preferred(groups, lempi):
    for pari in lempi:
        on_pari = False
        for group in groups:
            if pari[0] in group and pari[1] in group:
                on_pari = True
                break
        if on_pari:
            continue
        else:
            return False
    return True


def omistajat_eri_paikoissa(paikat, omistajat):

    for paikka in paikat:
        onko_omistaja = False
        for omistaja in omistajat:
            if omistaja in paikka and not onko_omistaja:
                onko_omistaja = True
                continue
            elif omistaja in paikka and onko_omistaja:
                return False
    return True


def main():
    # Mahdolliset parit
    pref = [["Onni M.", "Otto"], ["Niina", "Sami"]]
    # Talojen omistajat
    omistajat = ["Kasperi", "Niina", "Matias"]

    # Arvotaan ryhmät
    paikat = tiimijako(TYYPIT, RYHMIEN_MAARA)
    while not preferred(paikat, pref) or not omistajat_eri_paikoissa(paikat, omistajat):
        paikat = tiimijako(TYYPIT, RYHMIEN_MAARA)

    # Tulostus
    for paikka in paikat:
        print(paikka)


if __name__ == "__main__":
    main()
