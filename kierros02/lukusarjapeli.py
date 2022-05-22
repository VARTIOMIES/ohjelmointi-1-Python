def main():
    amount = int(input("How many numbers would you like to have? "))
    i = 1
    while i <= amount:
        if i % 3 == 0:
            if i % 7 == 0:
                print("zip boing")
            else:
                print("zip")
        elif i % 7 == 0:
            print("boing")
        else:
            print(i)
        i += 1



if __name__ == "__main__":
    main()