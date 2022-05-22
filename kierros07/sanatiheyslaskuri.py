"""
COMP.CS.100 Programming 1
Tekijä: Onni Merilä
Opiskelijanumero: H299725

Laskee annetun tekstin sanojen määrän hyödyntäen dictionareja
"""


def read_input():
    """ Reads many lines of input and returns a list of every word separated by
    space

    :return: list, words , list of words individually
    """
    words = []
    invalid_input = False
    print("Enter rows of text for word counting. Empty row to quit.")
    while not invalid_input:
        line = input()
        if line.strip() == "":
            invalid_input = True
        else:
            line_ls = line.split()
            for word_index in range(len(line_ls)):
                word = line_ls[word_index].lower()
                words.append(word)

    return words


def main():
    words = read_input()

    counting = {}
    for word_index in range(len(words)):
        word = words[word_index]
        if word not in counting:
            counting[word] = 1
        else:
            counting[word] += 1

    for key in sorted(counting):
        print(key, ":", counting[key], "times")


if __name__ == "__main__":
    main()
