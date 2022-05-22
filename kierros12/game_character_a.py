"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Tekijä: Onni Merilä
Opiskelijatunnus: H299725
This program models a character adventuring in a video game,
or more like, the stuff that the character carries around.
"""


class Character:
    """
    Tämä luokka esittää pelihahmoa, joka voi pitää erilaisia esineitä hallussa
    """

    def __init__(self, name):

        self.__name = name
        self.__inventory = []

    def give_item(self, item):
        """
        Adds <item> into the given characters inventory

        :param item: str, name of the item
        :return:
        """

        self.__inventory.append(item)

    def remove_item(self, item):
        """
        Removes <item> from inventory of the character

        :param item: str, name of the item
        :return:
        """
        try:
            self.__inventory.remove(item)

        except ValueError:
            return

    def printout(self):
        """
        Prints what <self> has in it's inventory
        :return:
        """
        # Counting the items
        count_dict = {}
        for item in self.__inventory:
            if item not in count_dict:
                count_dict[item] = 1
            else:
                count_dict[item] += 1

        # Items are now counted and stored in <count_dict>

        # Prints out the results
        print("Name:", self.__name)

        for item in sorted(count_dict):
            print(f"  {count_dict[item]} {item}")

        if len(count_dict) == 0:
            print("  --nothing--")

    def get_name(self):
        """
        :returns: str, name of Character object
        """
        return self.__name

    def has_item(self, item):
        """
        Checks, if item is in characters inventory

        :param item: str, name of item to be checked if in inventory
        :return: bool, True, if Character has <item> in it's __inventory
        """
        if item in self.__inventory:
            return True
        else:
            return False

    def how_many(self, item):
        """

        :param item:
        :return:
        """
        return self.__inventory.count(item)


def main():
    character1 = Character("Conan the Barbarian")
    character2 = Character("Deadpool")

    for test_item in ["sword", "sausage", "plate armor", "sausage", "sausage"]:
        character1.give_item(test_item)

    for test_item in ["gun", "sword", "gun", "sword", "hero outfit"]:
        character2.give_item(test_item)

    character1.remove_item("sausage")
    character2.remove_item("hero outfit")

    character1.printout()
    character2.printout()

    for hero in [character1, character2]:
        print(f"{hero.get_name()}:")

        for test_item in ["sausage", "sword", "plate armor", "gun", "hero outfit"]:
            if hero.has_item(test_item):
                print(f"  {test_item}: {hero.how_many(test_item)} found.")
            else:
                print(f"  {test_item}: none found.")


if __name__ == "__main__":
    main()
