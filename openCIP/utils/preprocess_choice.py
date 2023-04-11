'''Util for cli to choose which method of preprocessing happens.'''

import sys
import os

from config import Config


def preprocess_choice() -> int:
    '''
    Manages choosing and previewing different preprocessing for the video.
    '''
    if Config.GUI:
        return preprocess_choice_GUI()
    else:
        return preprocess_choice_CLI()


def preprocess_choice_GUI() -> int:
    '''
    Provides an interface for choosing and previewing different preprocessing
    types in GUI mode.
    '''
    pass


def preprocess_choice_CLI() -> int:
    '''
    Provides an interface for choosing and previewing different preprocessing
    types in CLI mode.
    '''
    choice: float = -1.0
    optionheight = 12

    while not choice.is_integer() or not choice > 0 or not choice < 11:
        width = Config.terminal_width
        halfwidth = int(width / 2)

        title: str = ("||" + "CHOOSE A METHOD OF PREPROCESSING"
                      .center(width - 4, " ") + "||")

        l1: str = ("1) Sobel".ljust(halfwidth, " ") +
                   "2) Scharr".rjust(halfwidth, " "))

        l2: str = ("3) Laplacian".ljust(halfwidth, " ") +
                   "4) Gaussian".rjust(halfwidth, " "))

        l3: str = ("5) Canny".ljust(halfwidth, " ") +
                   "6) Increase Brightness".rjust(halfwidth, " "))

        l4: str = ("7) Decrease Brightness".ljust(halfwidth, " ") +
                   "8) Increase Contrast".rjust(halfwidth, " "))

        l5: str = ("9) Decrease Contrast".ljust(halfwidth, " ") +
                   "10) None".rjust(halfwidth, " "))

        sep: str = "="*width + "\n"

        choice: str = ("||" + "Enter the number of the process to apply"
                       .center(width - 4, " ") + "||" + "\n")

        output = (sep + title + "\n" + sep + l1 +
                  "\n" + l2 + "\n" + l3 + "\n" +
                  l4 + "\n" + l5 + "\n" + sep + choice + sep)
        try:
            choice = float(input(output))
        except Exception:
            print("Invalid choice. Try again.")
            choice = -1.0

        sys.stdout.write("\33[F"*optionheight)

    os.system('cls' if os.name == 'nt' else 'clear')
    return choice
