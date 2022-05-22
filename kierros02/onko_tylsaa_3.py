def main():
    not_bored = True
    while not_bored:
        answer = input("Bored? (y/n) ")
        while answer != "y" and answer != "Y" and answer != "n" and answer != "N":
            print("Incorrect entry.")
            answer = input("Please retry: ")
        if answer == "y" or answer == "Y":
            not_bored = False
    print("Well, let's stop this, then.")
if __name__ == "__main__":
    main()