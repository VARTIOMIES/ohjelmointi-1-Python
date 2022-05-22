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
