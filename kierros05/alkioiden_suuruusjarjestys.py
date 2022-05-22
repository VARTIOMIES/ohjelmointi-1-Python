"""
COMP.CS.1 Programming 1
Tekijä: Onni Merilä
Opiskelijanumero: H299725
"""


def is_the_list_in_order(ls):
    """Checks if the list is in order or not

    :param ls: list,
    :return: bool,
    """
    if len(ls) > 0:
        last = ls[0]
    else:
        return True

    for memb in ls:
        if memb < last:
            return False
        last = memb
    return True
