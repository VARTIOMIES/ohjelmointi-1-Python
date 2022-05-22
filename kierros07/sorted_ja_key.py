"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Tekijä: Onni Merilä
Opiskelijanumero: H299725

Template for sorting by price assignment.
"""

PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.70, "grasshopper": 13.25,
    "sushi": 19.90, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}


def main():
    def payload(key):
        return PRICES[key]

    for tuote in sorted(PRICES, key=payload):
        print(f"{tuote} {PRICES[tuote]:.2f}")


if __name__ == "__main__":
    main()
