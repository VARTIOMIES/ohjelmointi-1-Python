"""
Funktio, joka kääntää väärin annetun nimen oikein ja poistaa esimerkiksi
turhat välilyönnit
"""


def reverse_name(line):
    """ Puts name right

    :param line: str,
    :return: str,
    """

    if "," not in line:
        parts = line.split()
        if len(parts) == 2:
            line = parts[0] + " " + parts[-1]
        elif len(parts) == 0:
            line = ""
        else:
            line = parts[0]
    else:
        line = line.strip()
        parts = line.split(",")
        if "" in parts:
            line = parts[-1].strip() + parts[0].strip()
        else:
            line = parts[-1].strip() + " " + parts[0].strip()

    return line


def main():
    print(reverse_name(input()))


if __name__ == "__main__":
    main()