"""
COMP.CS.100 Programming 1
Code template for "replacing grades" program
Tekijä: Onni Merilä
Opiskleijanumero: H299725
"""


def convert_grades(grades):
    """Converts grades

    :param grades: list,
    """
    for grade in grades:
        if grade != 0:
            grades[grades.index(grade)] = 6


def main():
    grades = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0]
    convert_grades(grades)
    print(grades)  # Should print [0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0]


if __name__ == "__main__":
    main()
