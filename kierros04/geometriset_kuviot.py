"""
COMP.CS.100 Programming 1
Code template for geometric shapes.
"""
from math import pi


def print_circ(circ):
    """
    Prints circumference
    :param circ: float
    """
    print(f"The total circumference is {circ:.2f}")


def print_area(area):
    """
    Prints area
    :param area:
    """
    print(f"The surface area is {area:.2f}")


def positive(num):
    """
    Cheks if the given number is positive and returns boolean

    :param num: int, given input
    :return: bool, If positive, returns true
    """
    return num > 0


def square():
    """
    Asks for the length of the side and prints out circumference and area
    """
    while True:
        side = float(input("Enter the length of the square's side: "))
        if positive(side):
            break

    print_circ(4*side)
    print_area(side*side)


def rectangle():
    """
    Asks for the length of the sides and prints circumference and area
    """
    while True:
        side1 = float(input("Enter the length of the rectangle's side 1: "))
        if positive(side1):
            break

    while True:
        side2 = float(input("Enter the length of the rectangle's side 2: "))
        if positive(side2):
            break

    print_circ(2*side1 + 2*side2)
    print_area(side1*side2)


def circle():
    """
    Asks for the radius and prints circumference and area
    """
    while True:
        radius = float(input("Enter the circle's radius: "))
        if positive(radius):
            break
    print_circ(2*pi*radius)
    print_area(pi*radius*radius)


def menu():
    """
    This function prints a menu for user to select which
    geometric shape to use in calculations.
    """

    while True:
        answer = input("Enter the pattern's first letter, q stops this (s/r/q): ")
        if answer == "s":
            square()

        elif answer == "r":
            rectangle()

        elif answer == "c":
            circle()

        elif answer == "q":
            return

        else:
            print("Incorrect entry, try again!")

        print()  # Empty row for the sake of readability


def main():
    menu()
    print("Goodbye!")


if __name__ == "__main__":
    main()
