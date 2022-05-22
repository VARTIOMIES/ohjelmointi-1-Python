"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: H299725
Name:       Onni Merilä
Email:      onni.merila@tuni.fi

Counter program, that works in a window.
"""

from tkinter import *


class Counter:
    def __init__(self):

        # Stores the value in it's own attribute
        self.__value = 60

        self.__main_window = Tk()

        self.__current_value = Label(self.__main_window, text=self.__value)
        self.__current_value.pack(side=TOP)

        self.__reset_button = Button(self.__main_window, text="Reset",
                                     command=self.reset, fg="red")
        self.__reset_button.pack(side=LEFT)

        self.__increase_button = Button(self.__main_window, text="Increase",
                                        command=self.increase, fg="green")
        self.__increase_button.pack(side=LEFT)

        self.__decrease_button = Button(self.__main_window, text="Decrease",
                                        command=self.decrease, fg="blue")
        self.__decrease_button.pack(side=LEFT)

        self.__quit_button = Button(self.__main_window, text="Quit",
                                    command=self.quit, fg="red")
        self.__quit_button.pack(side=LEFT)

        self.__main_window.mainloop()

    def reset(self):
        """
        Resets the value to zero.
        """

        self.__value = 0
        self.__current_value.configure(text=self.__value)

    def increase(self):
        """
        Increseases the value by one.
        """
        self.__value += 1
        if self.__value == 69:
            self.__current_value.configure(text="nice")
        else:
            self.__current_value.configure(text=self.__value)

    def decrease(self):
        """
        Decresases the value by one.
        """
        self.__value -= 1
        if self.__value == 69:
            self.__current_value.configure(text="nice")
        else:
            self.__current_value.configure(text=self.__value)

    def quit(self):
        """
        Closes the programs window.
        """
        self.__main_window.destroy()


def main():
    # There is no need to modify the main function.
    # As a matter of fact, automated tests ignore main
    # once again.

    Counter()


if __name__ == "__main__":
    main()
