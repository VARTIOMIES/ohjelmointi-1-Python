"""
Programming 1
Tekijä: Onni Merilä
Opiskelijanumero: H299725
"""


def longest_substring_in_order(text):
    """ Etsii annetusta merkkijonosta pisimmän aakkosjärjestyksessä olevan
    osamerkkijonon (Optimoitu)

    :param text: str, Annettu merkkijono
    :return: str, pisin löydetty aakkosjärjestyksessä oleva merkkijonon osa
    """
    last_index = 0
    pisin = ""
    skip_amount = 0
    for char_index in range(len(text)):

        char = text[char_index]

        # Seuraava ehtolause optimoi koodia, ei välitetä siitä vielä
        if skip_amount > 0:
            skip_amount -= 1
            continue

        # Käydään läpi seuraavia alkioita
        for index in range(char_index, len(text)):

            # varmistus, että ei tule stackoverflow
            if index == len(text)-1:
                last_index = index
                break

            if text[index+1] >= text[index]:
                continue
            else:
                last_index = index
                break

        # Nyt meillä on x:pituisen aakkosjärjestyksessä olevan substringin
        # ensimmäisen ja viimeisen kirjaimen indeksit.
        # Koska halutaan tietää pisin aakkosjärjestyksessä oleva jono, niin
        # verrataan sitä edelliseen pisimpään jonoon. Jos vertailtavana oleva
        # substring on pidempi mitä edellinen "pisin", niin tallennetaan
        # se "pisin":mmän paikalle.
        # (1. kierroksella vertailtavana on tyhjä string, jolloin pisimpään
        # tallentuu lyhimmillään yksi kirjain)

        if len(text[char_index:last_index+1]) > len(pisin):
            pisin = text[char_index:last_index+1]

        # Tällöin muuttujassa "pisin" on kaikista pisin aakkosjärjestyksessä
        # oleva merkkijono.
        # Siirrytään seuraavaan kirjaimeen

        # Koska last_index:iin asti olevat merkit ovat jo otettu huomioon
        # vertailtessa "pisin"mpään, niin voidaan hypätä niiden yli, jolloin
        # jatketaan kirjaimien tutkimista last_index:in jälkeen

        skip_amount = last_index - char_index

    # Nyt ollaan käyty kaikki kirjaimet läpi. Tällöin voidaan palauttaa
    # muuttujassa "pisin" oleva arvo, joka on siis pisin, aakkosjärjestyksessä
    # oleva merkkijono annetun merkkijonon sisällä
    return pisin
