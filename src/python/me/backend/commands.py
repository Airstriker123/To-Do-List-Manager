import time
import sys
import os
from colorama import Fore, Back, Style

reset = Fore.RESET
red = Fore.RED
blue = Fore.BLUE
lred = Fore.LIGHTRED_EX
lblue = Fore.LIGHTBLUE_EX
lc = Fore.LIGHTCYAN_EX
green = Fore.GREEN
yellow = Fore.YELLOW
orange = '\033[38;5;208m'

class Commands:
    def __init__(self):
            pass

    def __str__(self):
        return "invalid use of class!"

    def option_1(self):
        """Method to add a new task use this to modify backend"""
        pass

    def option_2(self):
        """Method to remove a task"""
        pass

    def option_3(self):
        """Method to check off a task"""
        pass

    @staticmethod
    def option_4():
        """Method to exit app"""
        print(f"{lc}exiting app!{reset}")
        sys.exit()
