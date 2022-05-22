"""
COMP.CS.100 Programming 1
Tekijä: Onni Merilä
Opiskelijanumero: H299725
"""


class Player:
    """
    This class models a player in mölkky
    """
    def __init__(self, player_name):
        """
        Constructor, has 5 attributes

        :param player_name: str.
        """
        self.__name = player_name
        self.__score = 0
        self.__throws = 0
        self.__true_score = 0
        self.__missed = 0

    def get_name(self):
        """

        :return: str, Name of the wanted player.
        """
        return self.__name

    def add_points(self, points):
        """
        Adds given points to the Player's score. Warns if score is close to 50

        :param points: int, points of throw
        :return: None
        """
        # Add throw
        self.__throws += 1

        # Add points or if missed then adds one to missed count
        if points == 0:
            self.__missed += 1
        else:
            self.__score += points
            self.__true_score += points

        if self.__score in range(40, 49):
            remaining = 50 - self.__score
            print(f"{self.__name} needs only {remaining} points. It's better"
                  f" to avoid knocking down the pins with higher points.")

    def better_than_average(self, points):
        """
        Return true if points of throw is greater than the average
        of points per throw so far (of Player).

        :param points: int,
        :return:
        """

        if points > self.__true_score / self.__throws:
            return True

    def has_won(self):
        """
        Checks if the player has 50 points or if over, sets points back to
        25.
        :return: bool,
        """

        if self.__score == 50:
            return True

        elif self.__score > 50:
            print(self.__name, "gets penalty points!")
            self.__score = 25
            return False

        else:
            return False

    def get_points(self):
        """
        Return points of <self>
        :return: int
        """
        return self.__score

    def get_hit_percentage(self):
        """
        Returns hit percentage of <self>

        :return: float, hit percentage
        """
        if self.__throws != 0:
            miss_percentage = self.__missed / self.__throws * 100.0
        else:
            miss_percentage = 100.0

        hit_percentage = 100.0 - miss_percentage

        return hit_percentage


def main():
    # Here we define two variables which are the objects initiated from the
    # class Player. This is how the constructor of the class Player
    # (the method that is named __init__) is called!

    player1 = Player("Matti")
    player2 = Player("Teppo")

    throw = 1
    while True:

        # if throw is an even number
        if throw % 2 == 0:
            in_turn = player1

        # else throw is an odd number
        else:
            in_turn = player2

        pts = int(input("Enter the score of player " + in_turn.get_name() +
                        " of throw " + str(throw) + ": "))

        in_turn.add_points(pts)

        if in_turn.better_than_average(pts):
            print(f"Cheers {in_turn.get_name()}!")

        if in_turn.has_won():
            print("Game over! The winner is " + in_turn.get_name() + "!")
            return

        print("")
        print("Scoreboard after throw " + str(throw) + ":")
        print(f"{player1.get_name()}: {player1.get_points()} p, hit percentage"
              f" {player1.get_hit_percentage():.1f}")
        print(f"{player2.get_name()}: {player2.get_points()} p, hit percentage"
              f" {player2.get_hit_percentage():.1f}")
        print("")

        throw += 1


if __name__ == "__main__":
    main()
