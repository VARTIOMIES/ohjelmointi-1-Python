"""
Tekijä: Onni Merilä
Opiskelijanumero: H299725
Funktio muuttaa annettuja sanoja niin, että jokaisen sanan alkukirjian on iso
"""


def capitalize_initial_letters(line):
    """ Täähän se ois se funktio

    :param line: str,
    :return: str,
    """
    hell = ""
    paskat = line.split()
    for vittu in paskat:
        hell += vittu.capitalize()
        if not vittu == paskat[-1]:
            hell += " "
    return hell


def main():
    print(capitalize_initial_letters(input()))


if __name__ == "__main__":
    main()