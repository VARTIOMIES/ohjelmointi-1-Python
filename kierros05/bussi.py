"""
COMP.CS.100 Programming 1
Tekijä: Onni Merilä
Opiskelijanumero: H299725
"""


def seuraavat_kolme_bussia(aika, aikataulu):
    """Selvittää annetun lähtöajan mukaan seuraavat kolme lähtevää bussia

    :param aika: int, Haluttu lähtöaika
    :param aikataulu: list, bussiaikataulu
    """
    kolme_seuraavaa = []
    for bussin_lahtoaika in aikataulu:
        bussin_indeksi = aikataulu.index(bussin_lahtoaika)
        if aika > bussin_lahtoaika:
            bussin_indeksi = 0
            continue
        else:
            break

    # Ollaan siis saatu seuraavan bussin lähtöajan indeksi aikataululistasta

    # selvitetään bussin indeksi - muodossa (i)
    for indeksi_minus in range(0, -6, -1):
        if aikataulu[indeksi_minus] == aikataulu[bussin_indeksi]:
            i = indeksi_minus

    # Tällöin jos vuorokausi vaihtuu, niin se ei tuota indeksiongelmaa
    # Selvitetään seuraavien lähtöjen ajat ja tehdään niistä lista

    while len(kolme_seuraavaa) < 3:
        kolme_seuraavaa.append(aikataulu[i])
        i += 1

    # Tulostetaan seuraavat kolme aikaa halutulla tavalla
    print("The next buses leave:")
    for aika in kolme_seuraavaa:
        print(aika)


def main():
    bussiaikataulu = [630, 1015, 1415, 1620, 1720, 2000]
    lahtoaika = int(input("Enter the time (as an integer): "))
    seuraavat_kolme_bussia(lahtoaika, bussiaikataulu)


if __name__ == "__main__":
    main()
