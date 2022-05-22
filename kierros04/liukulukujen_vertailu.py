"""
CS.100.1 Programming 1
Tekijä: Onni Merilä
Opiskelijanumero: H
"""


def compare_floats(a, b, epsilon):
    """
    This function compares 2 given floats and returns True or False depending
    on whether the given numbers are maximum of an epsilon apart from eachother

    :param a: float, number given by user
    :param b: float, number given by user
    :param epsilon: float, wanted
    :return: bool,
    """
    return abs(a-b) < epsilon

