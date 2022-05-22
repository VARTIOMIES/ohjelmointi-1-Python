"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Project: accesscontrol, program template

Tekijä: Onni Merilä
Opiskelijanumero: H299725

Ohjelma toimii kulunvalvonta järjestelmänä, jossa tekstitiedostosta luettuja
kulkukorttien tietoja voidaan tarkastella ja muokata. Kulkukortit mallinnetaan
olioina <Accesscard> ja ne tallennetaan dict tietorakenteeseen <Cards>, josta
niitä pystytään kutsumaan kulkukortin id:n avulla. Käyttäjällä on useita eri
komentoja, joilla hän hallitsee ohjelman suoritusta.
"""

DOORCODES = {'TC114': ['TIE'], 'TC203': ['TIE'], 'TC210': ['TIE', 'TST'],
             'TD201': ['TST'], 'TE111': [], 'TE113': [], 'TE115': [],
             'TE117': [], 'TE102': ['TIE'], 'TD203': ['TST'], 'TA666': ['X'],
             'TC103': ['TIE', 'OPET', 'SGN'], 'TC205': ['TIE', 'OPET', 'ELT'],
             'TB109': ['OPET', 'TST'], 'TB111': ['OPET', 'TST'],
             'TB103': ['OPET'], 'TB104': ['OPET'], 'TB205': ['G'],
             'SM111': [], 'SM112': [], 'SM113': [], 'SM114': [],
             'S1': ['OPET'], 'S2': ['OPET'], 'S3': ['OPET'], 'S4': ['OPET'],
             'K1705': ['OPET'], 'SB100': ['G'], 'SB202': ['G'],
             'SM220': ['ELT'], 'SM221': ['ELT'], 'SM222': ['ELT'],
             'secret_corridor_from_building_T_to_building_F': ['X', 'Y', 'Z'],
             'TA': ['G'], 'TB': ['G'], 'SA': ['G'], 'KA': ['G']}

# Tietorakenne, jota käytän, on sanakirja, johon tallennetaan korttiolioita.
CARDS = {}


class Accesscard:
    """
    This class models an access card which can be used to check
    whether a card should open a particular door or not.
    """

    def __init__(self, id, name):
        """
        Constructor, creates a new object that has no access rights.

        :param id: str, card holders personal id
        :param name: str, card holders name

        THIS METHOD IS AUTOMATICALLY TESTED, DON'T CHANGE THE NAME OR THE
        PARAMETERS!
        """
        self.__id = id
        self.__name = name
        self.__access_codes = []

    def info(self):
        """
        The method has no return value. It prints the information related to
        the access card in the format:
        id, name, access: a1,a2,...,aN
        for example:
        777, Thelma Teacher, access: OPET, TE113, TIE
        Note that the space characters after the commas and semicolon need to
        be as specified in the task description or the test fails.

        THIS METHOD IS AUTOMATICALLY TESTED, DON'T CHANGE THE NAME, THE
        PARAMETERS, OR THE PRINTOUT FORMAT!
        """
        # Tallennetaan muuttujiin kortin tiedot koodia selkeyttääksemmme.
        id = self.__id
        name = self.__name
        access = self.__access_codes
        access_str = ", ".join(sorted(access))

        print(f"{id}, {name}, access: {access_str}")

    def get_name(self):
        """
        :return: Returns the name of the accesscard holder.
        """
        return self.__name

    def add_access(self, new_access_code):
        """
        The method adds a new accesscode into the accesscard according to the
        rules defined in the task description.

        :param new_access_code: str, the accesscode to be added in the card.

        THIS METHOD IS AUTOMATICALLY TESTED, DON'T CHANGE THE NAME, THE
        PARAMETERS, OR THE RETURN VALUE! DON'T PRINT ANYTHING IN THE METHOD!
        """

        # Listataan kaikki huoneet, mihin tällä hetkellä päästään.
        old_access = []

        for old_access_code in self.__access_codes:

            # Jos koodi on vain yhden oven koodi, niin lisätään se listaan.
            if old_access_code in DOORCODES:
                old_access.append(old_access_code)

            # Muuten koodi on aluekoodi. Katsotaan kaikki ovet minne päästään.
            else:
                for key in DOORCODES:
                    if old_access_code in DOORCODES[key]:
                        old_access.append(key)

        # Tarkistetaan, onko uusi ovikoodi jo kortilla tai onko uuden koodin
        # oven avaamisen tarvittava aluekoodi jo kortilla. Jos näin on,
        # niin ei tarvitse lisätä mitään, ja voidaan lopettaa metodin suoritus.

        if new_access_code in old_access or \
                new_access_code in self.__access_codes:
            return

        # Jos tänne päästiin, niin:
        # Koodi on siis aivan uusi koodi, eli ovet jotka aukeavat tällä
        # koodilla ei ole ennen auennut aikaisemmin tällä kortilla.

        # Katsotaan, onko uusi koodi aluekoodi vai ei. Jos koodi ei ole
        # aluekoodi, niin se on ovikoodi. Lisätään vain ovikoodi ja poistutaan.

        if new_access_code in DOORCODES:
            self.__access_codes.append(new_access_code)
            return

        # Jos koodi on aluekoodi, niin poistetaan turhat yksittäisten ovien
        # koodit.
        else:
            # Käydään läpi vanhat koodit.
            for code in self.__access_codes:
                # Jos koodi on ovikoodi...
                if code in DOORCODES:
                    # ...ja jos uusi aluekoodi sisältää tämän oven...
                    if new_access_code in DOORCODES[code]:
                        # ...niin poistetaan ovikoodi kortin pääsykoodeista.
                        self.__access_codes.remove(code)

        # Lisätään lopuksi uusi aluekoodi kortille.
        self.__access_codes.append(new_access_code)

    def check_access(self, door):
        """
        Checks if the accesscard allows access to a certain door.

        :param door: str, the doorcode of the door that is being accessed.
        :return: True: The door opens for this accesscard.
                 False: The door does not open for this accesscard.

        THIS METHOD IS AUTOMATICALLY TESTED, DON'T CHANGE THE NAME, THE
        PARAMETERS, OR THE RETURN VALUE! DON'T PRINT ANYTHING IN THE METHOD!
        """
        # Listataan kaikki koodit, jotka voivat avata oven.
        access_codes_needed = [door]
        for area_code in DOORCODES[door]:
            access_codes_needed.append(area_code)

        # Nyt on listattu ne aluekoodit, joilla on kulkulupa ovesta.
        # Tarkistetaan nyt, onko self:illä joitakin näistä koodeista.
        for code in self.__access_codes:
            if code in access_codes_needed:
                return True

        # Jos tänne asti päästään, niin kortilla ei ole oven avaavaa koodia.
        return False

    def merge(self, card):
        """
        Merges the accesscodes from another accesscard to this accesscard.

        :param card: Accesscard, the accesscard whose access rights are added to this card.

        THIS METHOD IS AUTOMATICALLY TESTED, DON'T CHANGE THE NAME, THE
        PARAMETERS, OR THE RETURN VALUE! DON'T PRINT ANYTHING IN THE METHOD!
        """
        for access_code in card.__access_codes:
            self.add_access(access_code)


def invalid_id(id, mode):
    """
    Checks if id is a known, valid id. This function has different modes to
    check id from different places and to print different error messages.

    :param id: str, id of card or door
    :param mode: str, Options: card, door, access
    :return: True if id is invalid
             False if id is valid and exists
    """
    if mode == "card":
        if id not in CARDS:
            print("Error: unknown id.")
            return True

    elif mode == "door":
        if id not in DOORCODES:
            print("Error: unknown doorcode.")
            return True

    elif mode == "access":
        # Käydään ovet läpi. Jos id on joku ovi tai joku oven aluekoodeista,
        # niin id on 'valid' eli palautetaan False.
        for door in DOORCODES:

            if door == id or id in DOORCODES[door]:
                return False

        # Jos päästään tähän, niin id ei ole minkään oven tai alueen id, joten:
        print("Error: unknown accesscode.")
        return True

    return False


def read_file(file):
    """
    Reads file line by line. Saves data from the file to different Accesscard
    objects, and saves the objects to CARDS dictionary.

    :param file: file, The file to be read.
    """
    for line in file:
        line_list = line.rstrip().split(";")

        # Tallennetaan tunniste ja nimi, ja poistetaan ne listasta popilla.
        id = line_list.pop(0)
        name = line_list.pop(0)

        # Listassa on nyt vain pääsykoodeja. Erotellaan ne toisistaan ja
        # tallennetaan ne <access_codes> listaan.
        if len(line_list) > 0:
            access_codes = line_list[0].split(",")

        else:
            access_codes = []

        # Luodaan olio, joka tallennetaan sanakirjaan.
        CARDS[id] = Accesscard(id, name)

        # Lisätään pääsykoodit tälle oliolle.
        for access_code in access_codes:
            CARDS[id].add_access(access_code)

    # Funktio tallentaa siis dictiin <cards> olioita, joiden 'key' on kortin id
    # Olioita voidaan sis käsitellä, kun tiedetään id.


def main():

    # Avataan tiedosto, jos mahdollista.
    try:
        file = open("accessinfo.txt", mode="r")

    except OSError:
        print("Error: file cannot be read")
        return

    read_file(file)

    while True:
        line = input("command> ")

        if line == "":
            break

        strings = line.split()
        command = strings[0]

        if command == "list" and len(strings) == 1:
            # Käydään korttioliosanakirja CARDS läpi ja käytetään .info metodia
            for card in sorted(CARDS):
                CARDS[card].info()

        elif command == "info" and len(strings) == 2:
            card_id = strings[1]

            # Tarkistetaan, onko id olemassa.
            if invalid_id(card_id, "card"):
                continue

            CARDS[card_id].info()

        elif command == "access" and len(strings) == 3:
            card_id = strings[1]
            door_id = strings[2]

            # Tarkistetaan onko idt olemassa.
            if invalid_id(card_id, "card") or invalid_id(door_id, "door"):
                continue

            card = CARDS[card_id]
            # Katsotaan, onko kortilla pääsyä huoneeseen. Tulostetaan se tieto.
            if card.check_access(door_id):
                print(f"Card {card_id} ( {card.get_name()} ) has access to "
                      f"door {door_id}")
            else:
                print(f"Card {card_id} ( {card.get_name()} ) has no access to "
                      f"door {door_id}")

        elif command == "add" and len(strings) == 3:
            card_id = strings[1]
            access_code = strings[2]

            # Tarkistetaan onko idt olemassa.
            if invalid_id(card_id, "card") or\
                    invalid_id(access_code, "access"):
                continue
            # Lisätään pääsykoodi kortille.
            CARDS[card_id].add_access(access_code)

        elif command == "merge" and len(strings) == 3:
            card_id_to = strings[1]
            card_id_from = strings[2]

            # Tarkistetaan onko idt olemassa.
            if invalid_id(card_id_to, "card") or \
                    invalid_id(card_id_from, "card"):
                continue

            # Yhdistetään kortin vanhat tiedot toisen kortin tietojen kanssa.
            CARDS[card_id_to].merge(CARDS[card_id_from])

        elif command == "quit":
            print("Bye!")
            return
        else:
            print("Error: unknown command.")


if __name__ == "__main__":
    main()
