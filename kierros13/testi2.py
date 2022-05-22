from tkinter import *

class Käyttöliittymä:

  def __init__(self):
    self.__pääikkuna = Tk()

    self.__lähtöarvo = Entry()
    self.__lähtöarvo.pack()

    self.__muunnosnappi = Button(self.__pääikkuna, text="muunna",
                                 command=self.muunna)
    self.__muunnosnappi.pack()

    self.__tulosarvo = Entry()
    self.__tulosarvo.pack()

    self.__lopetusnappi = Button(self.__pääikkuna, text="lopeta",
                                 command=self.lopeta)
    self.__lopetusnappi.pack()

    self.__pääikkuna.mainloop()

  def muunna(self):
    aika_mantereella = self.__lähtöarvo.get()

    # Tilan säästämiseksi kellonajalle tehtävävät
    # virhetarkistukset poistettu tästä kohdasta.

    (tunnit, minuutit) = aika_mantereella.split(".")
    tunnit = int(tunnit)

    if tunnit < 1:           # 00.00-00.59 -> 12.00 AM-12.59 AM
        tunnit += 12
        pääte = "AM"

    elif tunnit < 12:        # 01.00-11.59 ->  1.00 AM-11.59 AM
        pääte = "AM"

    elif 12 <= tunnit < 13:  # 12.00-12.59 -> 12.00 PM-12.59 PM
        pääte = "PM"

    else:                    # 13.00-23.59 ->  1.00 PM-11.59 PM
        tunnit -= 12
        pääte = "PM"

    tulos = f"{tunnit}:{minuutit} {pääte}"

    self.__tulosarvo.delete(0, END)
    self.__tulosarvo.insert(0, tulos)

  def lopeta(self):
    self.__pääikkuna.destroy()


def main():
    Käyttöliittymä()


if __name__ == "__main__":
    main()