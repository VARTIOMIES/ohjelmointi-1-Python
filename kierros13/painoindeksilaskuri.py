"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

Body Mass Index template
"""

from tkinter import *


class Userinterface:

    def __init__(self):
        self.__mainwindow = Tk()

        self.__weight_value_label = Label(self.__mainwindow, text="Weight kg:")

        self.__weight_value = Entry()

        self.__height_value_label = Label(self.__mainwindow, text="Height cm:")

        self.__height_value = Entry()

        self.__calculate_button = Button(self.__mainwindow, text="Calculate",
                                         command=self.calculate_BMI, fg="cyan")

        self.__result_label = Label(self.__mainwindow, text="Result:")

        self.__result_text = Label(self.__mainwindow, text="")

        self.__explanation_text = Label(self.__mainwindow, text="")

        self.__stop_button = Button(self.__mainwindow, text="STOP", fg="red",
                                    command=self.stop)

        # If you read the Gaddis book, you can use pack here instead of grid!
        self.__weight_value_label.grid(row=0, column=0, columnspan=2)
        self.__height_value_label.grid(row=0, column=2, columnspan=2)
        self.__weight_value.grid(row=1, column=0, columnspan=2)
        self.__height_value.grid(row=1, column=2, columnspan=2)
        self.__calculate_button.grid(row=4, column=0, columnspan=2, sticky=W+E)
        self.__stop_button.grid(row=4, column=3)
        self.__result_label.grid(row=3, column=0)
        self.__result_text.grid(row=3, column=1, columnspan=3, sticky=W)
        self.__explanation_text.grid(row=5, column=0, columnspan=4, sticky=W)

    def calculate_BMI(self):
        """
        Part b) This method calculates the BMI of the user and
        displays it. First the method will get the values of
        height and weight from the GUI components
        self.__height_value and self.__weight_value.  Then the
        method will calculate the value of the BMI and show it in
        the element self.__result_text.

        Part e) Last, the method will display a verbal
        description of the BMI in the element
        self.__explanation_text.
        """
        try:
            height = float(self.__height_value.get())
            weight = float(self.__weight_value.get())

        except ValueError:
            msg = "Error: height and weight must be numbers."
            self.__explanation_text.configure(text=msg)
            self.reset_fields()
            return

        if height < 0 or weight < 0:
            msg = "Error: height and weight must be positive."
            self.__explanation_text.configure(text=msg)
            self.reset_fields()
            return

        # from cm to m
        height = height / 100

        result = weight/(height*height)
        txt_result = f"{result:.2f}"
        self.__result_text.configure(text=txt_result)

        if result > 25.0:
            self.__explanation_text.configure(text="You are overweight.")

        elif result < 18.5:
            self.__explanation_text.configure(text="You are underweight.")

        else:
            self.__explanation_text.configure(text="Your weight is normal.")

    def reset_fields(self):
        """
        In error situations this method will zeroize the elements
        self.__result_text, self.__height_value, and self.__weight_value.
        """
        self.__result_text.configure(text="")
        self.__height_value.delete(0, END)
        self.__weight_value.delete(0, END)

    def stop(self):
        """
        Ends the execution of the program.
        """

        self.__mainwindow.destroy()

    def start(self):
        """
        Starts the mainloop.
        """
        self.__mainwindow.mainloop()


def main():
    # Notice how the user interface can be created and
    # started separately.  Don't change this arrangement,
    # or automatic tests will fail.
    ui = Userinterface()
    ui.start()


if __name__ == "__main__":
    main()
