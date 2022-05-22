"""
COMP.CS.1 Programming 1
Tekijä: Onni Merilä
Opiskelijanumero: H299725
"""


def input_to_list(amount):
    """Creates and return a list, which's length is given as parameter

    :param amount: int, how many numbers wanted to the list
    :return: list, list with wanted amount of numbers
    """
    print(f"Enter {amount} numbers:")
    list = []
    for _ in range(0, amount):
        num = int(input())
        list.append(num)

    return list


def main():
    amount = int(input("How many numbers do you want to process: "))
    list_of_nums = input_to_list(amount)

    searched = int(input("Enter the number to be searched: "))
    found = 0
    for step in list_of_nums:
        if step == searched:
            found += 1

    if found > 0:
        print(f"{searched} shows up {found} times among the numbers \
you have entered.")
    else:
        print(searched, "is not among the numbers you have entered.")


if __name__ == "__main__":
    main()
