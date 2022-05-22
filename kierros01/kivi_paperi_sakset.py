def main():
    string1 = input("Player 1, enter your choice (R/P/S): ")
    string2 = input("Player 2, enter your choice (R/P/S): ")
    # Määritellään voittaja:
    if string1 == "R":
        if string2 == "P":
            winner = 2
        elif string2 == "S":
            winner = 1
        else:
            winner = 0
    elif string1 == "P":
        if string2 == "S":
            winner = 2
        elif string2 == "R":
            winner = 1
        else:
            winner = 0
    elif string1 == "S":
        if string2 == "R":
            winner = 2
        elif string2 == "P":
            winner = 1
        else:
            winner = 0

    # Tulostetaan voittaja
    if winner >= 1:
        print("Player",winner,"won!")
    elif winner == 0:
        print("It's a tie!")


if __name__ == "__main__":
    main()