def main():
    print("Moi ammuli!")
    print()
    print("Tämä on ammulin 'feeling to emoji' -kone")
    print()
    olo = int(input("Mikä fiilis asteikolla [huono] 1 - 10 [mahtava!!]?"))
    print()
    if olo <= 10 and olo >= 1:

        if olo == 10:
            emoji = ":D"
        elif olo > 6:
            emoji = ":)"
        elif olo > 1:
            emoji = ":("
        else:
            emoji = ":<<"
        print("Sopiva emoji olisi:", emoji)
    else:
        print("Eläs yritä huijata! :<<")

if __name__ == "__main__":
    main()