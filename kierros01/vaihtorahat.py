def main():
    price = int(input("Purchase price: "))
    money = int(input("Paid amount of money: "))
    # Lasketaan palautettavan rahan määrä
    change = money - price
    if change > 0:
        print("Offer change: ")
        ten_euro = change // 10  # Amount of 10 euro notes
        if ten_euro > 0:
            print(ten_euro, "ten-euro notes")
        remain = change - ten_euro * 10
        if remain != 0:
            five_euro = remain // 5   # Amount of 5 euro notes
            if five_euro > 0:
                print(five_euro, "five-euro notes")
            remain = remain - five_euro * 5
            if remain != 0:
                two_euro = remain // 2    # Amount of 2 euro coins
                if two_euro > 0:
                    print(two_euro, "two-euro coins")
                remain = remain - two_euro * 2
                if remain != 0:
                    print("1 one-euro coins")
    else:
        print("No change")

if __name__ == "__main__":
    main()