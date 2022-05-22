def main():
    amount = int(input("How many numbers would you like to have? "))
    for i in range(1, amount+1):
        if i % 3 == 0:
            if i % 7 == 0:
                print("zip boing")
            else:
                print("zip")
        elif i % 7 == 0:
            print("boing")
        else:
            print(i)
if __name__ == "__main__":
    main()