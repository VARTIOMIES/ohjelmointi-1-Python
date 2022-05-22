def main():
    string = input("How do you feel? (1-10) ")
    feel = int(string)
    if feel >= 1 and feel <= 10:
        if feel == 10:
            face = ":-D"
        elif feel == 1:
            face = ":'("
        elif feel > 7:
            face = ":-)"
        elif feel >= 4:
            face = ":-|"
        else:
            face = ":-("
        print("A suitable smiley would be",face)
    else:
        print("Bad input!")

if __name__ == "__main__":
    main()