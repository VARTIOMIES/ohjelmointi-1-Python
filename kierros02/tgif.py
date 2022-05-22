"""
Tulostaa vuoden 2014 jokaisen perjantain päivämäärän
"""
def main():

    day_counter = 0
    """
    The program will go through every day in the year.
    For everyday (1-365) it checks the date (d.m.).
    Then, knowing that first friday is 3.1. it will print out the date (d.m.)
    for every seven days from the day 3.1., which means the program prints 
    the dates for every friday of the year 2014.
    """
    # Lets first go through every date

    for month in range(1, 13):

        if month == 2:
            last_day = 28
        elif month == 4 or month == 6 or month == 9 or month == 11:
            last_day = 30
        else:
            last_day = 31

        for day in range(1, last_day + 1):
            day_counter += 1

            # Next line will print the date every 7 days, knowing that first
            # friday was 3.1.
            if day_counter % 7 == 3:
                print(f"{day}.{month}.")

if __name__ == "__main__":
    main()