def main():
    not_bored = True
    while not_bored:
        answer = input("Bored? (y/n) ")
        if answer == "y":
            not_bored = False
    print("Well, let's stop this, then.")



if __name__ == "__main__":
    main()