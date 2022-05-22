"""
COMP.CS.100 Programming 1
Tekijä: Onni Merilä
Opiskelijanumero: H299725
Laskee parasetamolin annostelun
"""

AMOUNT_OF_MED_PER_KG = 15
MAX_MED_PER_24 = 4000


def calculate_dose(paino, aika, kokonais_24):
    """Laskee sopivan lääkeannoksen

    :param paino: int, potilaan paino kg
    :param aika: int, milloin annettiin viimeksi lääkettä h
    :param kokonais_24: int, yhteensä annettu lääkkeen määrä 24h
    :return: int, annettava lääkemäärä mg
    """
    # Tarkistetaan ensin, että lääkeen otosta on enemmän kuin 6 tuntia aikaa
    if aika < 6:
        return 0

    # Seuraavaksi lasketaan suurin mahd. annos määrä henkilön painoon nähden
    annos = paino * AMOUNT_OF_MED_PER_KG

    # Tarkistetaan, että potilaan kokonaisannostus viim. 24 tunnin aikana
    # ei mene yli sallitun rajan.
    # Muuten annetaan annokseksi juuri sen verran, että päivän raja ei ylity
    if annos + kokonais_24 > MAX_MED_PER_24:
        annos = MAX_MED_PER_24 - kokonais_24

    # Palautetaan annoksen suuruus (mg)
    return annos


def main():

    patient_weight = int(input("Patient's weight (kg): "))
    from_previous_dose = int(input("How much time has passed from the"
                                   " previous dose (full hours): "))
    total_dose = int(input("The total dose for the last 24 hours (mg): "))

    print("The amount of Parasetamol to give to the patient: "
          f"{calculate_dose(patient_weight, from_previous_dose, total_dose)}")

    # calculate_dose assumes parameters to be of type int
    # and they should be passed in the order: weight, time, total_doze_24
    # (or more like the automated tests assume this)


if __name__ == "__main__":
  main()