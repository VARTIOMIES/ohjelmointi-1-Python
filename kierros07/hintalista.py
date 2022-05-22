"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: H299725
Name: Onni Merilä
Email:

Template for pricelist assignment.
"""

PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.70, "grasshopper": 13.25,
    "sushi": 19.90, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}


def main():
    while True:
        syöte = input("Enter product name: ").strip()

        if syöte == "":
            print("Bye!")
            break

        if syöte in PRICES:
            print(f"The price of {syöte} is {PRICES[syöte]:.2f} e")
        else:
            print(f"Error: {syöte} is unknown.")


if __name__ == "__main__":
    main()
