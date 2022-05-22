def main():
    f_1 = 1
    f_2 = 1
    amount = int(input("How many Fibonacci numbers do you want? "))
    i = 1
    while i <= amount:
        print(f"{i}. {f_1}")
        fn = f_1 + f_2
        f_1 = f_2
        f_2 = fn
        i += 1


if __name__ == "__main__":
    main()