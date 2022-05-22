"""
Programming 1 Spesiaali tehtävä
Tekijä: Onni Merilä
Opiskelijanumero: H299725
"""




def row_list_to_word_list(list1):
    """MAkes the row list into a list with every word in their own index

    :param list1: list, list of rows
    :return: list, list of independent words from every index in list1
    """
    word_list = []
    for index in range(len(list1)):
        word_list += list1[index].split()

    #print(word_list)#--------------------------------------
    return word_list


def rows_of_words(words, char_per_line):
    """ Determines the rows for words according to how many characters are
    wanted per line

    :param words: list, list of words
    :param char_per_line: int, number of characters wanted in one row
    :return:
    """
    # Let's start with checking how many full words is fitted in row
    space_left = char_per_line
    index = 0
    row = 0
    row_index = []

    # Gives row indexes for all given words
    while True:
        if index >= len(words):
            break
        if len(words[index]) <= space_left:
            row_index.append(row)

            space_left -= len(words[index]) + 1
            index += 1
            continue
        else:
            row += 1
            space_left = char_per_line
            continue
    #print(row_index)#----------------------------------
    return row_index


def fill_the_gaps(words, rows, char_per_line):
    """sitä että

    :param words: list, näin
    :param rows: list, noin
    :param char_per_line: int, ei nööin
    :return:
    """
    # Let's go through each row and see, how many spaces needs to be filled in
    missing = 0
    row = 0
    while_loop_break = False
    while row <= max(rows):

        line_list = []
        for row_index in range(len(rows)):
            row_num = rows[row_index]
            if row_num == row:
                line_list.append(words[row_index])

        if row >= max(rows):
            print(" ".join(line_list))
            row += 1
            break
        """
        Following codes are modified versions of Otto Tjukanoff's codes, who 
        helped
        me make my code work, because i had problems with adding the spaces
        
        I made sure, that I understand every step of it, before including
        it in my code
        """
        length = len(line_list)
        if length == 1:
            line = "".join(line_list)
            print(line)
            row += 1
            continue

        missing = char_per_line - len("".join(line_list)) - length + 1

        last_word = line_list.pop()
        length = len(line_list)
        for x in range(missing):
            line_list[x % length] += " "

        """
        Here ends those codes
        """

        # Now we have added spaces in to the list. Lets squeeze the list to a
        # string
        line = " ".join(line_list) + " " + last_word

        print(line)

        row += 1


def main():
    print("Enter text rows. Quit by entering an empty row.")
    text_list = read_rows()
    words = row_list_to_word_list(text_list)
    char_per_line = int(input("Enter the number of characters per line: "))
    rows = rows_of_words(words, char_per_line)
    fill_the_gaps(words, rows, char_per_line)


if __name__ == "__main__":
    main()


