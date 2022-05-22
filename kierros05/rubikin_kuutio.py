"""
COMP.CS.1 Programming 1
Tekijä: Onni Merilä
Opiskelijanumero: H299725
"""


def fill_list():
    """Fills the list

    :return: list,
    """
    ls = []
    for n in range(1, 6):
        ls.append(float(input(f"Enter the time for performance {n}: ")))
    return ls


def delete_max_min(ls):
    """Deletes max and min

    :param ls: list,
    :return: list,
    """
    # First let's find the max time
    maximum = max(ls)
    ls.remove(maximum)

    # Then min time
    minimum = min(ls)
    ls.remove(minimum)

    return ls


def ka(ls):
    """Calculates keskiarvo

    :param ls: list,
    :return: float,
    """
    cumulativ = 0.0
    amount = 0.0
    for time in ls:
        cumulativ += time
        amount += 1.0
    return cumulativ/amount


def main():
    lista = fill_list()
    lista = delete_max_min(lista)
    print(f"The official competition score is {ka(lista):.2f} seconds.")


if __name__ == "__main__":
    main()
