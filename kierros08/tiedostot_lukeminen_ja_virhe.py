"""
COMP.CS.100 Programming 1
Tekijä: Onni Merilä
Opiskelijanumero: H299725
Ohjelma lukee tiedoston, ja tulostaa tiedoston tekstin rivinumeroiden kanssa
"""


def main():

    filename = input("Enter the name of the file: ")

    try:
        file = open(filename, mode="r")

    except OSError:
        print("There was an error in reading the file.")
        return

    line_number = 1

    for file_line in file:

        file_line = file_line.rstrip()

        print(line_number, file_line)
        line_number += 1

    file.close()


if __name__ == "__main__":
    main()
