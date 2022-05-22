def main():
    number = int(input("Choose a number: "))
    i = 1
    while (i-1) * number <= 100:
        print(i , "*" , number, "=" , i * number)
        i += 1

if __name__ == "__main__":
    main()