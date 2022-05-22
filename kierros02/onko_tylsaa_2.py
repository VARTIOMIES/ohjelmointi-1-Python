def main():
    answer = input("Answer Y or N: ")
    while answer != "y" and answer != "Y" and answer != "n" and answer != "N":
        print("Incorrect entry.")
        answer = input("Please retry: ")
    print("You answered", answer)

if __name__ == "__main__":
    main()