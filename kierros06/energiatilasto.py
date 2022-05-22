"""
COMP.CS.100 Ohjelmointi 1 Projekti: Energiatilasto
Tekijä: Onni Merilä
Opiskelijanumero: H299725
Ohjelma kysyy energiankulutuksen arvoja, ja kun sille syötetään tyhjä rivi,
tulostaa se histogrammin eri energiakulutksen luokista.
"""


def alku_tulostus():
    """Tulostaa ensimmäiset tulostukset.
    """
    print("Enter energy consumption data.")
    print("End by entering an empty line.")
    print()


def syötekehoite():
    """Pyytää käyttäjältä syötteitä niin pitkään, kunnes käyttäjä syöttää
    tyhjän merkkijonon.

    :return: list, palautetaan käyttäjän syötteet listana
    """
    syöte_lista = []
    while True:
        # Kysytään käyttäjältä syöte
        syöte = input("Enter energy consumption (kWh): ")

        # Tarkistetaan, että syöte ei ole tyhjä rivi. Jos on, poistutaan toisto
        # rakenteesta
        if syöte == "":
            break

        # Nyt kun syöte ei ole tyhjä rivi, voidaan muuttaa se kokonaisluvuksi
        syöte = int(syöte)

        # Tarkistetaan, että syöte ei ole negatiivinen
        if negatiivinen(syöte):
            virhe_tulostus(syöte)
            continue

        # Talletetaan syöte listaan
        syöte_lista.append(syöte)

    return syöte_lista


def negatiivinen(numero):
    """Tarkistaa onko numero negatiivien, palauttaa True, jos on negatiivinen.

    :param numero: int, Syötetty numero.
    :return: bool, Palauttaa True, jos on negatiivinen.
    """
    if numero >= 0:
        return False
    else:
        return True


def virhe_tulostus(numero):
    """Tulostaa virhetulostuksen.

    :param numero: int, Virheellisen syötteen arvo.
    """
    print(f"You entered: {numero}. Enter non-negative numbers only!")


def luokittelu(arvo):
    """ Funktio selvittää sille syötetyn arvon energialuokan ja palauttaa
    luokan numeron.

    :param arvo: int, annettu energia-arvo
    :return: int, luokan numero, johon annettu arvo kuuluu
    """
    # Esimerkissä annettu algoritmi luokan löytämiselle hieman muokattuna
    luokka = 1
    while True:
        luokan_pienin_arvo = 10 ** luokka // 100 * 10
        luokan_suurin_arvo = 10 ** luokka - 1
        if luokan_pienin_arvo <= arvo <= luokan_suurin_arvo:
            break
        luokka += 1

    return luokka


def listan_luokittelu(lista):
    """Luokittelee annetun listan luokkiin ja palauttaa listan jossa on
    syötteiden luokat syöttöjärjestyksessä

    :param lista: list, Syötteiden lista, jossa energiaarvoja
    :return: list, Lista, jossa on annettujen arvojen luokat
    """
    # Alustetaan lista
    luokiteltu_lista = []
    # Täytetään lista ja hyödynnetään luotua luokittelu() funktiota
    for indeksi in range(len(lista)):
        luokka = luokittelu(lista[indeksi])
        luokiteltu_lista.append(luokka)

    return luokiteltu_lista


def histogrammi(luokka_lista):
    """
    Täyttää histogrammin tulostamiseen tarvittavan listan. Listassa on joko
    "Nothing to ... " tai tulostettavien tähtien määrä
    Sen jälkeen tulostaa histogrammin

    :param luokka_lista: list, Syötettyjen energia-arvojen luokat listassa
    syöttöjärjestyksessä
    """
    # Tarkistetaan, että lista ei ole tyhjä. Jos on, niin tulostetaan ... ja
    # funktio päättyy.
    if not len(luokka_lista) > 0:
        print("Nothing to print. Done.")
    else:
        # Tarkistetaan montako luokkaa on ja tehdään histogrammi_lista:sta sen
        # pituinen.
        # histogrammi_lista on siis lista, johon ensin talletetaan luokka-
        # listasta saatavat eri luokkien lukumäärät.

        # Alustetaan ensin tämä lista sopivasti
        suurin_luokka = max(luokka_lista)
        histogrammi_lista = [0] * suurin_luokka

        # Käydään luokka_lista läpi ja lasketaan histogrammi_lista:an eri
        # luokkien lukumäärät ( esimerkiksi jos luokka_lista on [2,2,3],
        # histogrammi_lista olisi: [0,2,1] )
        for luokka in luokka_lista:
            histogrammi_lista[luokka-1] += 1

        # Tallennetaan histogrammiin tulostettavat asiat listaan
        # Muutetaan siis histogrammi_lista:ssa olevat lukumäärät niin, että
        # alkiona oleva numero vastaa tähtien lukumäärää. Tämä helpottaa
        # tulostusta rivillä 160 kun määritetään tulostettavan palkin pituus
        for määrä in histogrammi_lista:
            indeksi = histogrammi_lista.index(määrä)
            histogrammi_lista[indeksi] = "*" * määrä

        # Oma kommentti: Äskeisen operaation olisi voinut jättää tekemättä
        # ja tehdä saman operaation vähän eri tavalla sitten tulostettaessa

        # ----------------
        # Tulostetaan sitten histogrammi.
        # Aikaisemmin saatiin listan suurimmaksi luokaksi suurin_luokka.
        # Lasketaan tämän mukaan, kuinka paljon tilaa tulostukseen tarvitaan
        # jokaiselle luokalle.

        leveys = suurin_luokka * 2 + 1

        # Aletaan tulostamaan
        for luokka in range(1, suurin_luokka + 1):
            # Määritetään tulostettavat luokan suurin ja pienin arvo
            luokan_pienin = 10 ** luokka // 100 * 10
            luokan_suurin = 10 ** luokka - 1

            # Tähtien määrä aiemmin täytetyssä histogrammin listassa
            # luokka-1 on siis luokan indeksi histogrammilistassa
            palkki = histogrammi_lista[luokka-1]

            # Tulosteen alkuosa, eli luokkien pienin ja suurin luku
            luokan_min_max_tuloste = f"{luokan_pienin}-{luokan_suurin}"
            # Tulostetaan rivi
            print(f"{luokan_min_max_tuloste:>{leveys}}: {palkki}")


def main():
    alku_tulostus()
    syötteet = syötekehoite()

    luokat = listan_luokittelu(syötteet)

    histogrammi(luokat)


if __name__ == "__main__":
    main()