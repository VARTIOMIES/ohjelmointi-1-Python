def main():
    for month in range(1,13):
        # Checks how many days are in the specific month
        if month == 2:
            last_day = 28
        elif month == 4 or month == 6 or month == 9 or month == 11:
            last_day = 30
        else:
            last_day = 31
        # Prints the dates
        for day in range(1,last_day+1):
            print(f"{day}.{month}.")

if __name__ == "__main__":
    main()