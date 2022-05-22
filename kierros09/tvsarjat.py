"""
COMP.CS.100 Programming 1
Tekijä: Onni Merilä
Read genres and tv-series from a file into a dict.
Print a list of the genres in alphabetical order
and list tv-series by given genre on user's command.
"""


def read_file(filename):
    """
    Reads and saves the series and their genres from the file.

    :param filename: str, name of th efile where the data is
    :return: dict, dictionary where key is genre and value is show(s)
    TODO: comment the parameter and the return value.
    """

    #
    genre_dict = {}

    # TODO initialize a new data structure


    try:
        file = open(filename, mode="r")

        for row in file:

            # If the input row was correct, it contained two parts:
            # · the show name before semicolon (;) and
            # · comma separated list of genres after the semicolon.
            # If we know that a function (method split in this case)
            # returns a list containing two elements, we can assign
            # names for those elements as follows:
            name, genres = row.rstrip().split(";")

            genres = genres.split(",")
            #
            for genre in genres:
                if genre not in genre_dict:
                    genre_dict[genre] = []
                genre_dict[genre].append(name)

            # TODO add the name and genres data to the data structure

        file.close()
        return genre_dict # TODO return the data structure

    except ValueError:
        print("Error: rows were not in the format name;genres.")
        return None

    except IOError:
        print("Error: the file could not be read.")
        return None


def main():
    filename = input("Enter the name of the file: ")

    genre_data = read_file(filename)

    list_of_genres = sorted(genre_data)

    print("Available genres are:", ", ".join(list_of_genres))

    # TODO print the genres

    while True:
        genre = input("> ")

        if genre == "exit":
            return

        elif genre in genre_data:
            for name in sorted(genre_data[genre]):
                print(name)


    # TODO print the series belonging to a genre.


if __name__ == "__main__":
    main()
