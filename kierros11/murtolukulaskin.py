"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Fractions code template
Tekijä: Onni Merilä
Opiskelijanumero: H299725
"""


class Fraction:
    """
    This class represents one single fraction that consists of
    numerator (osoittaja) and denominator (nimittäjä).
    """

    def __init__(self, numerator, denominator):
        """
        Constructor. Checks that the numerator and denominator are of
        correct type and initializes them.

        :param numerator: int, fraction's numerator
        :param denominator: int, fraction's denominator
        """

        # isinstance is a standard function which can be used to check if
        # a value is an object of a certain class.  Remember, in Python
        # all the data types are implemented as classes.
        # ``isinstance(a, b´´) means more or less the same as ``type(a) is b´´
        # So, the following test checks that both parameters are ints as
        # they should be in a valid fraction.
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError

        # Denominator can't be zero, not in mathematics, and not here either.
        elif denominator == 0:
            raise ValueError

        self.__numerator = numerator
        self.__denominator = denominator

    def __lt__(self, fraction_object):
        """

        :param fraction_object:
        :return:
        """
        numerator1 = self.__numerator * fraction_object.__denominator
        numerator2 = fraction_object.__numerator * self.__denominator

        return numerator1 < numerator2

    def __gt__(self, fraction_object):
        """

        :param fraction_object:
        :return:
        """
        numerator1 = self.__numerator * fraction_object.__denominator
        numerator2 = fraction_object.__numerator * self.__denominator

        return numerator1 > numerator2

    def __str__(self):
        """

        :return:
        """
        if self.__numerator * self.__denominator < 0:
            sign = "-"

        else:
            sign = ""

        return f"{sign}{abs(self.__numerator)}/{abs(self.__denominator)}"

    def return_string(self):
        """
        :returns: str, a string-presentation of the fraction in the format
                       numerator/denominator.
        """

        if self.__numerator * self.__denominator < 0:
            sign = "-"

        else:
            sign = ""

        return f"{sign}{abs(self.__numerator)}/{abs(self.__denominator)}"

    def simplify(self):
        """
        Simplifys the fraction
        :return:
        """
        syt = greatest_common_divisor(self.__numerator, self.__denominator)

        self.__numerator = int(self.__numerator / syt)

        self.__denominator = int(self.__denominator / syt)

    def complement(self):
        """
        :returns: obj,
        """
        new_numerator = (-1) * self.__numerator
        vastaluku = Fraction(new_numerator, self.__denominator)

        return vastaluku

    def reciprocal(self):
        """
        :returns: obj,
        """
        käänteisluku = Fraction(self.__denominator, self.__numerator)

        return käänteisluku

    def multiply(self, fraction_object):
        """
        Multiplys two Fraction objects and returns new Fraction object
        :param fraction_object: obj,
        :return: obj,
        """
        numerator = self.__numerator * fraction_object.__numerator
        denominator = self.__denominator * fraction_object.__denominator

        result_object = Fraction(numerator, denominator)

        return result_object

    def divide(self, fraction_object):
        """
        Divides two Fraction objects
        :param fraction_object:
        :return:
        """
        # Kerrotaan jakajan (fraction_object) käänteisluvulla
        jakajan_käänteis = fraction_object.reciprocal()

        result_object = self.multiply(jakajan_käänteis)

        return result_object

    def add(self, fraction_object):
        """
        Sums two Fraction objects
        :param fraction_object: obj,
        :return: obj,
        """

        numerator1 = self.__numerator * fraction_object.__denominator
        denominator = self.__denominator * fraction_object.__denominator
        numerator2 = fraction_object.__numerator * self.__denominator

        numerator_sum = numerator1 + numerator2

        sum_fraction = Fraction(numerator_sum, denominator)

        return sum_fraction

    def deduct(self, fraction_object):
        """

        :param fraction_object:
        :return:
        """
        numerator1 = self.__numerator * fraction_object.__denominator
        denominator = self.__denominator * fraction_object.__denominator
        numerator2 = fraction_object.__numerator * self.__denominator

        numerator_deduction = numerator1 - numerator2

        deduct_fraction = Fraction(numerator_deduction, denominator)

        return deduct_fraction


def greatest_common_divisor(a, b):
    """
    Euclidean algorithm. Returns the greatest common
    divisor (suurin yhteinen tekijä).  When both the numerator
    and the denominator is divided by their greatest common divisor,
    the result will be the most reduced version of the fraction in question.
    """

    while b != 0:
        a, b = b, a % b

    return a


def main():
    fractions = {}
    while True:
        command = input("> ")
        if command == "add":
            msg = input("Enter a fraction in the form integer/integer: ")
            msg_list = msg.split("/")
            # Luodaan murtolukuolio
            fraction = Fraction(int(msg_list[0]), int(msg_list[1]))

            # Kysytään nimi tälle oliolle
            name_fraction = input("Enter a name: ")

            # Lisätään olio sanakirjaan, jota voidaan hakea nimen perusteella
            fractions[name_fraction] = fraction

        elif command == "print":
            name_fraction = input("Enter a name: ")
            if name_fraction in fractions:
                fraction = fractions[name_fraction]
                print(name_fraction, "=", fraction)
            else:
                print(f"Name {name_fraction} was not found")

        elif command == "list":
            for fraction_key in sorted(fractions):
                print(fraction_key, "=", fractions[fraction_key])

        elif command == "*":
            first = input("1st operand: ")
            if first not in fractions:
                print(f"Name {first} was not found")
                continue
            second = input("2nd operand: ")
            if second not in fractions:
                print(f"Name {second} was not found")
                continue

            fraction1 = fractions[first]
            fraction2 = fractions[second]

            fraction3 = fraction1.multiply(fraction2)

            print(f"{fraction1} * {fraction2} = {fraction3}")

            fraction3.simplify()
            print("simplified", fraction3)

        elif command == "file":
            filename = input("Enter the name of the file: ")
            try:
                file = open(filename, mode="r")

            except OSError:
                print("Error: the file cannot be read.")
                continue

            try:
                for line in file:
                    # Luetaan tiedot tiedostosta
                    line_ls = line.split("=")
                    name = line_ls[0]
                    fraction_part_ls = line_ls[1].split("/")
                    fraction = Fraction(int(fraction_part_ls[0]),
                                        int(fraction_part_ls[1]))

                    # Lisätään sanakirjaan
                    fractions[name] = fraction

            except IndexError:
                print("Error: the file cannot be read.")
                continue

        elif command == "quit":
            print("Bye bye!")
            break

        else:
            print("Unknown command!")
            continue


if __name__ == "__main__":
    main()
