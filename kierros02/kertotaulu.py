def main():
    number = int(input("Choose a number: "))
    i = 1
    while i <= 10:
        print(i , "*" , number, "=" , i * number)
        i += 1

if __name__ == "__main__":
    main()