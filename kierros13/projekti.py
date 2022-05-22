"""
COMP.CS.100 Ohjelmointi 1 Projekti

Tekijä: Onni Merilä
Opiskelijanumero: H299725
Sähköposti: onni.merila@tuni.fi

Dokumentaatio:
Tämä ohjelma on matopeli, joka toimii Tkinterillä ja hyödyntää vain Pythonin
peruskirjastoja. Ohjelma aukaisee ensin valikon, jossa on ylhäällä hieno itse
tehty kuva. Sen alapuolella on useita eri nappeja, joista päästään esimerkiksi
muuttamaan asetuksia ja näkemään pelissä saadut Top 5 pisteet. Pelin voi käyn-
nistää painamalla "Aloitus"-nappia. Tällöin valikko sulkeutuu ja peli alkaa.

Pelissä ideana on liikuttaa matoa ympäri pelikenttää keräten marjoja. Matoa
ohjataan ikkunan alaosassa olevilla neljällä napilla, jota painamalla päätetään
madon suunta. Mato ei saa osua itseensä, tai peli on hävitty. Kun mato osuu
marjaan, se syö sen ja pelaaja saa pisteen. Sitten uusi marja ilmestyy
pelikentälle. Peli jatkuu niin pitkään, kunnen mato osuu itseensä, jolloin peli
päättyy. Jos pelaajan saamat pisteet ovat parhaiden 5 pisteiden joukossa,
pisteet tallennetaan. Peli ikkuna sammuu ja palataan menuun.

Tällä hetkellä pelissä on ainoastaan yksi asetus, jolla voidaan muuttaa madon
nopeutta, jolloin pelistä tulee vaikeampi tai helpompi. Tein ohjelman kuitenkin
niin, että kun tulee uusia ideoita, mitä asetuksia voitaisiin lisätä, niin ne
on helpompi lisätä ohjelmaan, kun asetukset on sanakirjassa.

Pelin toimiminen vaatii sitä, että tämän koodin kansio sisältää seuraavat:
10x10 pikselin kokoiset "tyhja.png", "taysi.png" ja "herkku.png" kuvat.
Otsikkokuvan "banner.png"
tekstitiedoston "top_scores.txt"

Nämä tarvittavat tiedostot on lähetetty samassa zip. paketissa tämän ohjelman
kanssa.

Tähtäsin tällä työlläni kehittyneeseen ohjelmaan ja mielestäni täytin kaikki
vaatimukset. Työhön kului aika paljon aikaa, ja aluksi oli vaikeata miettiä
toteutustapaa. Sen ratkaistuani minulla oli ongelmia suorituskyvyn kanssa, mut-
ta ongelmana oli liiallinen Label olioiden luominen. Ongelma ratkesi, kun muok-
kasin ohjelmani toimintaa niin, että en aina luo uutta Labelia, vaan muokaan
jo olemassa olevaa oliota, joka on tietyssä kohdassa matriisia
"""

from tkinter import *
from random import *
from time import *

# Tässä määritellään pelikentän koko.
# Suorituskyvyn kannalta ei kannata tehdä liian suurta pelikenttää!!!
KENTÄN_KOKO_X = 30
KENTÄN_KOKO_Y = 20


class MatopeliGUI:
    """
    Tämä olio on matopelin oma peli-ikkuna, joka sisältää pelikentän ja napit
    sekä kaiken pelin toiminnallisuuden.
    """
    def __init__(self, asetukset):
        """
        Rakentaja metodi (Constructor). Sisältää ikkunan luomisen sekä pelin
        aloituksen.
        :param asetukset: dict, sanakirja menussa annetuista asetuksista.
                             Sanakirjassa on {nopeus:int}. Tämä on sanakirja
                             myöhempää asetusten mahdollista lisäystä varten.
        """
        self.__peli_ikkuna = Tk()
        self.__peli_ikkuna.title("Matopeli 2.0")

        # Ikkunan yläosaan tulee pisteet ja tulostuskenttä, sitten pelikenttä
        # ja alas 4 nappia
        self.__info_frame = Frame(self.__peli_ikkuna)
        self.__pelikenttä = Frame(self.__peli_ikkuna,
                                  bd=5,
                                  relief=GROOVE
                                  )
        self.__napit = Frame(self.__peli_ikkuna)

        # Alueiden sijoitus

        self.__info_frame.pack()
        self.__pelikenttä.pack()
        self.__napit.pack()

        # Ruudut ovat 10x10 px kokoisia kuvia, musta, valkoinen ja herkku
        self.__tyhjä_ruutu = PhotoImage(file="tyhja.png")
        self.__täysi_ruutu = PhotoImage(file="taysi.png")
        self.__herkku_ruutu = PhotoImage(file="herkku.png")

        # Info framen sisältö
        self.__piste_label = Label(self.__info_frame,
                                   text="Pisteet:")
        self.__info_label = Label(self.__info_frame,
                                  text="")
        self.__piste_label.grid(row=0, column=0)
        self.__info_label.grid(row=0, column=1)
        # Pelikentän luominen
        # Pelikenttä koostuu ruuduista, jotka ovat joko mustia tai valkoisia
        # Luodaan pelikentän matriisi ensin tietorakenteena. 0 tarkoittaa
        # tyhjää, 1 tarkoittaa matoa ja 2 herkkua.
        self.__peliruutu = []
        for x in range(KENTÄN_KOKO_X):
            self.__peliruutu.append([])
            for y in range(KENTÄN_KOKO_Y):
                self.__peliruutu[x].append(0)

        # Nyt miellä on siis matriisi, joka on halutun kokoinen

        # Nappien luominen. (Löysin netistä tavan komentojen attribuuttien
        # lisäämiselle Tkinterin buttonille (lambda:))
        self.__ylös_nappi = Button(self.__napit,
                                   command=lambda: self.suunnan_vaihto("ylös"),
                                   text="^"
                                   )
        self.__oikealle_nappi = Button(self.__napit,
                                       command=lambda: self.suunnan_vaihto("oikea"),
                                       text=">"
                                       )
        self.__alas_nappi = Button(self.__napit,
                                   command=lambda: self.suunnan_vaihto("alas"),
                                   text="v"
                                   )
        self.__vasemmalle_nappi = Button(self.__napit,
                                         command=lambda: self.suunnan_vaihto("vasen"),
                                         text="<"
                                         )

        # Nappien sijoittaminen
        self.__ylös_nappi.grid(row=0, column=1, ipadx=10, ipady=8)
        self.__oikealle_nappi.grid(row=1, column=2, ipadx=10, ipady=8)
        self.__alas_nappi.grid(row=2, column=1, ipadx=10, ipady=8)
        self.__vasemmalle_nappi.grid(row=1, column=0, ipadx=10, ipady=8)

        # Luodaan pelikentän labelit alustavasti ja talletetaan ne matriisiin
        self.__peliruutu_labels = []
        for x in range(len(self.__peliruutu)):
            self.__peliruutu_labels.append([""] * KENTÄN_KOKO_Y)
        # Luodaan labelit ja sijoitetaan alustettuun matriisiin
        for x in range(len(self.__peliruutu)):
            for y in range(len(self.__peliruutu[x])):
                pikseli_label = Label(self.__pelikenttä,
                                      bd=0)
                self.__peliruutu_labels[x][y] = pikseli_label
        #####
        # Nyt on luotu kaikki tkinteriin liittyvät asiat. Seuraavaksi muut
        # peli-ikkunan attribuutit

        # Madon pään sijainti
        self.__madon_pää = [0, 0]
        # Minne mato on seuraavaksi menossa
        self.__suunta = "oikea"
        # Madon vartalon sijainnit listassa (matriisi)
        self.__mato = [[0, 0]]
        # Madon koko
        self.__koko = 6
        # Madon nopeus
        self.__nopeus = asetukset["nopeus"] * 100
        # Pelin alussa on 0 pistettä
        self.__pisteet = 0
        # Onko mato elossa vai ei
        self.__elossa = True
        # Herkun sijainti
        self.__herkku = [0, 0]

        # Aloitetaan. Lisätään herkku ja käynnistetään peli.
        self.herkkujen_lisäys()
        self.tick()

        self.__peli_ikkuna.mainloop()

    def suunnan_vaihto(self, uusi_suunta):
        """
        Metodi vaihtaa madon suuntaa, kun nuolinappia painetaan.
        :param uusi_suunta: str, joko "oikea", "vasen", "alas" tai "ylös"
        """

        # Tarkistetaan, onko käännös mahdollinen. Eli katsotaan, onko annettu
        # suunta kiellettyjen suunnan muutosten listassa. Jos ei ole, niin
        # suuunta vaihtuu. Muuten ei.
        if uusi_suunta == self.__suunta:
            return
        elif self.__suunta == "vasen" and uusi_suunta == "oikea":
            return
        elif self.__suunta == "oikea" and uusi_suunta == "vasen":
            return
        elif self.__suunta == "ylös" and uusi_suunta == "alas":
            return
        elif self.__suunta == "alas" and uusi_suunta == "ylös":
            return

        # Suunnan vaihto on siis sallittua
        self.__suunta = uusi_suunta

    def tick(self):
        """
        Tässä metodissa tapahtuu suurin osa madon toiminnasta. Metodi hoitaa
        kaiken: kutsuu muita metodeita ja lopussa itseään tietyn ajan kuluttua.
        """
        # Ensin suoritetaan madon liikkuminen
        self.liikkuminen()

        # Itseensä osumisen tarkistus
        # Jos mato osuu itseensä, niin peli loppuu
        if self.__madon_pää in self.__mato:
            self.kuolema()

        # Tallennetaan madon pään sijainti matolistaan nyt, kun tämän liikkeen
        # mahdollisuus on varmistettu (mato ei osu itseensä yms)
        self.__mato.append([self.__madon_pää[0], self.__madon_pää[1]])

        # Syöminen ja mahdollinen uuden herkun lisäys
        if self.syöminen():
            self.herkkujen_lisäys()

        # Listassa on aina korkeintaan madon pituuden verran sijainteja
        # Tarkistetaan pituus ja poistetaan madon sijainneista vanhin, eli
        # poistetaan madon perä
        if len(self.__mato) > self.__koko:
            perä = self.__mato.pop(0)
            x_perä = perä[0]
            y_perä = perä[1]
            self.__peliruutu[x_perä][y_perä] = 0

        # Sijoitetaan madon ruudut peliruutuun
        for mato_ruutu in self.__mato:
            x = mato_ruutu[0]
            y = mato_ruutu[1]
            self.__peliruutu[x][y] = 1

        # Varmistetaan vielä, että jos mato on kuollut, niin mitään ei jää
        # päälle pyörimään
        if self.__elossa:

            # Päivitetään peliruutu, jolloin tapahtuneet muutokset tulevat
            # näkyviin
            self.päivitä_ruutu()

            # Tehdään kaikki uudelleen. Peli pyrii käytännöss niin pitkään,
            # kunnes mato kuolee. Uudelleenkutsumisen nopeutta voidaan säätää
            # muuttamalla madon nopeutta
            self.__peli_ikkuna.after(self.__nopeus, self.tick)

    def liikkuminen(self):
        """
        Tämä metodi siirtää matoa siihen suuntaan, minkä käyttäjä on määrännyt
        madolle suunta nappeja painamalla.
        """
        # Katsotaan madon tämän hetkinen sijainti
        x = self.__madon_pää[0]
        y = self.__madon_pää[1]

        # Mato likkuu yhden pykälän (pikselin) verran
        # Liikutetaan matoa tiettyyn suuntaan. Tässä tapahtuu myös kentän pää-
        # tyjen yli liikkuminen toiseen päätyyn.
        if self.__suunta == "ylös":
            if y == 0:
                y = KENTÄN_KOKO_Y-1
            else:
                y -= 1
        elif self.__suunta == "oikea":
            if x == KENTÄN_KOKO_X-1:
                x = 0
            else:
                x += 1
        elif self.__suunta == "alas":
            if y == KENTÄN_KOKO_Y-1:
                y = 0
            else:
                y += 1
        elif self.__suunta == "vasen":
            if x == 0:
                x = KENTÄN_KOKO_X-1
            else:
                x -= 1

        # Päivitetään pään sijainti
        self.__madon_pää[0] = x
        self.__madon_pää[1] = y

    def kuolema(self):
        """
        Tämä metodi hoitaa kaiken sen, mitä madon kuolemisen jälkeen tapahtuu.
        """
        self.__elossa = False

        # Tallennetaan pisteet
        top_pisteet = lue_piste_tiedosto()
        top_pisteet.append(self.__pisteet)
        top_pisteet.sort()
        top_pisteet.reverse()
        # Tallennetaan vain 5 parasta tulosta. Poistetaan ylimääräiset pisteet.
        while len(top_pisteet) > 5:
            top_pisteet.pop(len(top_pisteet)-1)
        # Tallennetaan tiedostoon
        tallenna_piste_tiedostoon(top_pisteet)

        # Poistetaan kääntymisnapit käytöstä
        self.__ylös_nappi.configure(state=DISABLED)
        self.__oikealle_nappi.configure(state=DISABLED)
        self.__alas_nappi.configure(state=DISABLED)
        self.__vasemmalle_nappi.configure(state=DISABLED)

        # Ilmoitetaan tapahtunut info_labeliin käyttäjän näkyville
        self.__info_label.configure(text="Kuolit!", fg="red")
        self.__info_label.update()

        sleep(5)
        # Poistutaan ruudusta
        self.__peli_ikkuna.destroy()
        # Avataan menu-ikkuna
        MatomenuGUI()

    def päivitä_ruutu(self):
        """
        Tämä metodi piirtää pelikentän joka tick ja päivittää pisteet.
        """
        # Päivitetään pisteet
        self.__piste_label.configure(text=f"Pisteet: {self.__pisteet}")

        for x in range(len(self.__peliruutu_labels)):
            for y in range(len(self.__peliruutu_labels[x])):
                # __peliruutu ja __peliruutu_labels ovat samankokoisia
                # matriiseja. Käydään __peliruutu matriisi läpi ja päivitetään
                # sen määrittämät tiedot näkyvissä olevaan __peliruutu_labels
                # matriisiin pelaajan näkyville.
                # Jos matriisissa on 0, se tarkoittaa että siinä on tyhjää.
                if self.__peliruutu[x][y] == 0:
                    self.__peliruutu_labels[x][y].configure(
                        image=self.__tyhjä_ruutu)

                # Jos matriisissa on 2, se tarkoittaa, että siinä on herkku.
                elif self.__peliruutu[x][y] == 2:
                    self.__peliruutu_labels[x][y].configure(
                        image=self.__herkku_ruutu)

                # Tällöin matriisissa on 1, jolloin siinä on mato.
                else:
                    self.__peliruutu_labels[x][y].configure(
                        image=self.__täysi_ruutu)

                # Sijoitetaan päivitetty label gridiin oikeaan kohtaan.
                self.__peliruutu_labels[x][y].grid(column=x, row=y)

    def syöminen(self):
        """
        Tämä metodi tarkistaa, jos mato syö tickissä herkun, eli madon pään
        sijainti on sama kuin herkun sijainti. Tällöin metodi poistaa herkun.
        :return: True, jos mato syö herkun
                 False, jos ei syö herkkua
        """
        if self.__madon_pää[0] == self.__herkku[0] and \
                self.__madon_pää[1] == self.__herkku[1]:

            # Lisätään piste
            self.__pisteet += 1

            # Lisätään madon pituutta
            self.__koko += 1

            # Poistetaan herkku
            self.__peliruutu[self.__herkku[0]][self.__herkku[1]] = 0
            return True
        else:
            return False

    def herkkujen_lisäys(self):
        """
        Metodi lisää herkun __peliruutu matriisiin. Herkku lisätään randomilla
        johonkin ruutuun, jossa mato ei tällä hetkellä ole.
        """
        herkku_madossa = True
        herkun_x = None
        herkun_y = None
        # Lisätään satunnaiseen ruutuun. Herkkua ei voida kuitenkaan lisätä
        # sellaiseen ruutuun, jossa mato on tällä hetkellä.
        while herkku_madossa:
            herkku_madossa = False
            herkun_x = randint(0, KENTÄN_KOKO_X-1)
            herkun_y = randint(0, KENTÄN_KOKO_Y-1)

            # Tarkistetaan, että herkku ei ole madossa
            for mato in self.__mato:
                # Jos herkku on madossa, arvotan uudet koordinaatit.
                if mato[0] == herkun_x and mato[1] == herkun_y:
                    herkku_madossa = True
            # Jos ei, niin herkku_madossa on False, jolloin poistutaan loopista

        # Päivitetään herkun sijainti
        self.__herkku[0] = herkun_x
        self.__herkku[1] = herkun_y

        # Lisätään herkku peliruutu matriisiin, eli muutetaan numeroksi 2
        self.__peliruutu[herkun_x][herkun_y] = 2


class MatomenuGUI:
    """
    Tämä on matopelin menu olio. Se sisältää valikon ja sen toiminnallisuudet
    sekä huolehtii pelin käynnistymisen, eli kutsuu peli oliota. Pelin loputtua
    palataan takaisin tähän menu olioon.
    """
    def __init__(self):
        self.__menu_ikkuna = Tk()
        self.__menu_ikkuna.title("Matopeli 2.0")

        # Tallennetaan pelaajan parhaat pisteet olion omaan attribuuttiin
        top_pisteet = lue_piste_tiedosto()
        self.__parhaat_pisteet = top_pisteet

        # Tässä sanakirjassa on peliin vietävät asetukset, joita voi muokata
        self.__asetukset = {"nopeus": 5}

        self.__banner_kuva = PhotoImage(file="banner.png")

        # Luodaan main menu frame
        self.__main_menu_frame = Frame(self.__menu_ikkuna)
        # Luodaan main menun napit
        self.__otsikko_label = Label(self.__main_menu_frame,
                                     image=self.__banner_kuva
                                     )
        self.__aloitus_nappi = Button(self.__main_menu_frame,
                                      text="Aloita",
                                      command=self.aloitus)
        self.__asetukset_nappi = Button(self.__main_menu_frame,
                                        text="Asetukset",
                                        command=self.asetukset)
        self.__pisteet_nappi = Button(self.__main_menu_frame,
                                      text="Pisteet",
                                      command=self.pisteet)
        self.__lopeta_nappi = Button(self.__main_menu_frame,
                                     text="Lopeta",
                                     command=self.lopeta)
        # Sijoitetaan komponentit main menun frameen
        self.__otsikko_label.pack()
        self.__aloitus_nappi.pack()
        self.__asetukset_nappi.pack()
        self.__pisteet_nappi.pack()
        self.__lopeta_nappi.pack()

        # Luodaan asetukset frame, joka sisältää kaikki asetukset
        self.__asetus_frame = Frame(self.__menu_ikkuna)

        self.__asetukset_label = Label(self.__asetus_frame,
                                       text="Asetukset:"
                                       )
        # Luodaan nopeusasetuksen säädin. Valitsin scalen, jolla voi valita
        # madon nopeuden liukusäätimellä.
        self.__nopeus_asetus = Scale(self.__asetus_frame,
                                     showvalue=0,
                                     orient=HORIZONTAL,
                                     label="Nopeus:  <-hidas   nopea-> ",
                                     from_=10,
                                     to=1,
                                     length=200
                                     )
        # Asetetaan alkuarvoksi 5
        self.__nopeus_asetus.set(5)
        self.__takaisin_nappi = Button(self.__asetus_frame,
                                       text="Takaisin",
                                       command=self.takaisin
                                       )
        # Sijoitetaan framen sisältö frameen
        self.__asetukset_label.pack()
        self.__nopeus_asetus.pack()
        self.__takaisin_nappi.pack()

        # Luodaan pisteet frame, joka sisältää parhaiden pisteiden listan
        self.__pisteet_frame = Frame(self.__menu_ikkuna)
        # Luodaan framen sisältö
        self.__pisteet_label = Label(self.__pisteet_frame,
                                     text="Parhaat pisteet:"
                                     )
        self.__pisteet_lista = Listbox(self.__pisteet_frame,
                                       height=5)
        # Sijoitetaan parhaat pisteet näkyviin listaan.
        indeksi = 0
        for pisteet in self.__parhaat_pisteet:
            self.__pisteet_lista.insert(indeksi, f"{indeksi+1}. {pisteet}")
            indeksi += 1

        self.__takaisin_nappi2 = Button(self.__pisteet_frame,
                                        text="Takaisin",
                                        command=self.takaisin
                                        )
        # Sijoitetaan framen sisältö frameen
        self.__pisteet_label.pack()
        self.__pisteet_lista.pack()
        self.__takaisin_nappi2.pack()

        # Aloitetaan UI. Laitetaan main menu ensimmäiseksi näkyviin.
        self.__main_menu_frame.pack()
        self.__menu_ikkuna.mainloop()

    def aloitus(self):
        """
        Metodi aloittaa mato pelin, ja siirtää valitut asetukset peliolioon.
        """
        # Siirretään valitut asetukset sanakirjaan, joka viedään olioon
        self.__asetukset["nopeus"] = self.__nopeus_asetus.get()
        # Suljetaan menuikkuna
        self.__menu_ikkuna.destroy()
        # Aloitetaan peli
        MatopeliGUI(self.__asetukset)

    def asetukset(self):
        """
        Avaa asetukst framen näkyville ja piilottaa muut framet
        """

        self.__main_menu_frame.pack_forget()
        self.__pisteet_frame.pack_forget()
        self.__asetus_frame.pack()

    def pisteet(self):
        """
        Avaa pisteet framen ja piilottaa muut framet
        """
        self.__main_menu_frame.pack_forget()
        self.__asetus_frame.pack_forget()
        self.__pisteet_frame.pack()

    def takaisin(self):
        """
        Piilottaa muut framet ja palaa takaisin main menu frameen
        """
        self.__asetus_frame.pack_forget()
        self.__pisteet_frame.pack_forget()
        self.__main_menu_frame.pack()

    def lopeta(self):
        """
        Sammuttaa menuikkunan
        """
        self.__menu_ikkuna.destroy()


def lue_piste_tiedosto():
    """
    Lukee pistetiedoston ja palauttaa parhaat pisteet listana.
    :return: list, parhata pisteet top_scores.txt tiedostosta siirretty listaan
    """
    try:
        file = open("top_scores.txt", mode="r")

    except OSError:
        return

    pisteet = []
    for rivi in file:
        pisteet.append(int(rivi))

    return pisteet


def tallenna_piste_tiedostoon(lista):
    """
    Tallentaa annetun listan top_scores.txt tiedostoon.
    :param lista: list, parhaat pisteet, jotka halutaan tallentaa.
    """
    try:
        file = open("top_scores.txt", mode="w")

    except OSError:
        print("Error opening the file")
        return

    for pisteet in lista:
        print(pisteet, file=file)


def main():
    MatomenuGUI()


if __name__ == "__main__":
    main()
