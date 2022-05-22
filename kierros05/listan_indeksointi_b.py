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

    print("The numbers you entered, in reverse order:")
    for index in range(len(num_list), 0, -1):
        print(num_list[index-1])



if __name__ == "__main__":
    main()