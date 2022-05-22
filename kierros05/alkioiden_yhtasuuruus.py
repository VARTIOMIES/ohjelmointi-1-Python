"""
COMP.CS.1 Programming 1
Tekijä: Onni Merilä
Opiskelijanumero: H299725
"""


def are_all_members_same(ls):
    """Checks if all members are same

    :param ls: list,
    :return: bool,
    """
    if len(ls) > 1:
        for memb in ls:
            if memb != ls[1]:
                return False
    return True
