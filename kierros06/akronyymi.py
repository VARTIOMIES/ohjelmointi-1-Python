"""
Tekijä: Onni Merilä
Opiskelijanumero: H299725
Funktio, joka luo annetusta stringistä akronyymin
"""


def create_an_acronym(line):
    """Luo akronyymin

    :param line: str
    :return: str
    """
    new_line = ""
    osat = line.split()
    for osa in osat:
        new_line += osa[0].upper()

    return new_line


def main():
    print(create_an_acronym(input()))


if __name__ == "__main__":
    main()
