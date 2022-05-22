"""
COMP.CS.100 Programming 1
Assignment "Improved Box Printing" code template
"""


def print_box(width, height, border_mark="#", inner_mark=" "):
    """
    Tulostaa halutun kokoisen ja näköisen neliön

    :param width: int, laatikon leveys
    :param height: int, laatikon korkeus
    :param border_mark: str, merkki, jolla laatikon reunat piirretään
    :param inner_mark: str, merkki, jolla laatikon sisäosa piirretään
    """

    for h in range(1, height+1):
        for w in range(1, width+1):
            if h == 1 or h == height or w == 1 or w == width:
                print(border_mark, end="")
            else:
                print(inner_mark, end="")
        print()
    print()


def main():
    print_box(5, 4)
    print_box(3, 8, "*")
    print_box(5, 4, "O", "o")
    print_box(inner_mark=".", border_mark="O", height=4, width=6)


if __name__ == "__main__":
    main()
