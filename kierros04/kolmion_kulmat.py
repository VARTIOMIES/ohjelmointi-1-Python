"""
Tekijä Onni Merilä
Funktio, joka laskee kolmion kolmannen kulman
"""


def calculate_angle(a, b=90):
    """
    Calculates the angle of triangle, when 1 or 2 angles are given.

    :param a: int, given angle
    :param b: int, given angle, if left empty, the angle is 90
    :return: int, the last angle of the triangle
    """
    return 180 - a - b
