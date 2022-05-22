"""
COMP.CS.100 Programming 1
Tekijä: Onni Merilä
Opiskelijanumero: H299725
Funktio, joka avaa .csv tiedoston ja tallentaa tiedot sanakirjaan,jonka sisällä
on lisää sanakirjoja ja sitten tulostaa halutun tiedon. Toimii konsolissa
"""


def read_file(filename):
    """

    :param filename: str,
    :return: dict, information in dictionary
    """

    # Avataan tiedosto
    try:
        file = open(filename, mode="r")

    except OSError:
        print("Tiedoston lukeminen ei onnistunut")
        return None
    # Käsitellään tiedosto riveittäin ja tallennetaan tiedot tietorakenteeseen
    keys = {}

    try:
        x = 1
        for line in file:
            # Skipataan ensimmäinen rivi

            if x == 1:
                x = 0
                continue
            
            line_ls = line.rstrip().split(";")
            if len(line_ls) != 5:
                raise ValueError("Tiedoston rivin tietojen määrä ei ole 5")

            # Luodaan info sanakirja johon tallennetaan keywordien kohdalle
            # tiedot

            info = {"name": line_ls[1], "phone": line_ls[2],
                    "email": line_ls[3], "skype": line_ls[4]}

            # Talletetaan nämä tiedot key sanakirjaan
            keys[line_ls[0]] = info

            # Siirrytään seuraavaan riviin
    except ValueError as virheilmoitus:
        print("Virhe:", virheilmoitus)
        return None
    file.close()
    # Nyt kaikki tiedot on tallennettu sanakirjaan 'keys'
    # Palautetaan tämä sanakirja, jotta sitä voidaan käyttää konsolissa yms
    return keys
