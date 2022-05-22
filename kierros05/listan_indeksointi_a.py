"""
COMP.CS.1 Programming 1
Tekijä: Onni Merilä
Opiskelijanumero: H299725
"""


def main():
    num_list = []

    print("Give 5 numbers:")
    for _ in range(0, 5):
        num = int(input("Next number: "))
        num_list.append(num)

    print("The numbers you entered that were greater than zero were:")
    for num_in_list in num_list:
        if num_in_list > 0:
            print(num_in_list)


if __name__ == "__main__":
    main()