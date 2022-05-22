"""
COMP.CS.100 Programming 1
Tekijä: Onni Merilä
Opiskelijanumero: H299725

Ohjelma laskee yhteispistemäärän tiedostossa olevista arvoista. Tiedoston tulee
olla muotoa 'nimi pisteet'. Eli tiedostonrivien pitää olla kaksiosaisia erotet-
tuna välilyönnillä. Ohjelma hyödyntää sanakirja-tiedostontalletusta(dictionary)
Ohjelma tulostaa nimen ja pisteet nimien perusteella aakkosjärjestyksessä.
"""


def main():

    error = False
    # Avataan haluttu tiedosto
    filename = input("Enter the name of the score file: ")

    try:
        file = open(filename, mode="r")

    except OSError:
        print("There was an error in reading the file.")
        return
    # Luodaan sanakirja
    pisteet = {}

    # Käydään tiedosto läpi riveittäin

    for line in file:
        try:
            line_list = line.split()

            name = line_list[0]
            points = line_list[1]

        except IndexError:
            print("There was an erroneous line in the file:")
            print(line)
            error = True
            break

        try:
            points = int(points)

        except ValueError:
            print("There was an erroneous score in the file:")
            print(points)
            error = True
            break

        # Lisätään listan indeksissä 0 (name) ja listan indeksissä 1 (points)
        # sanakirjaan "pisteet".
        if name not in pisteet:
            pisteet[name] = points
        else:
            pisteet[name] += points

    # Suljetaan tiedosto
    file.close()

    # Pysäytetään ohjelma, jos on ilmennyt virheitä
    if error:
        return

    # Nyt on täytetty tiedoston tiedoista sanakirja, jossa key pitäisi ollanimi
    # Ja value numero (int) joka kuvaa pelaajan yhteispisteitä

    # Tulostetaan yhteen lasketut pisteet
    print("Contestant score:")

    for player in sorted(pisteet):
        print(player, pisteet[player])


if __name__ == "__main__":
    main()
