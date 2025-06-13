import time
import sys
import os
from colorama import Fore, Back, Style
import me.backend.main as backend

reset = Fore.RESET
red = Fore.RED
blue = Fore.BLUE
lred = Fore.LIGHTRED_EX
lblue = Fore.LIGHTBLUE_EX
lc = Fore.LIGHTCYAN_EX
green = Fore.GREEN
yellow = Fore.YELLOW
#ascii colour code for orange (fore does not have a default colour code for orange)
orange = '\033[38;5;208m'

class Commands:
    """Class stores option logic"""
    def __init__(self):
        self.backend = backend.ToDoBackend()
        self.backend.deserialise()

    def __str__(self):
        return "invalid use of class!"

    def option_1(self):
        """Method to add a new task use this to modify backend"""
        todo = input("What todo would you like to add: ")

    def del_task(self):
        """Method to remove a task"""
        todo_id = input("What todo ID do you want to remove: ")

    def check_task(self, todo_id):
        """Method to check off a task"""
        self.del_task()
        pass

    def option_4(self):
        """Prints all tasks, with ids"""

        i = 0
        for task in self.backend.todos:
            print(f"[{i}] {task}")

            i += 1

    
    def exit(self):
        """Method to exit app"""
        print(f"{lc}exiting app!{reset}")
        self.backend.serialise()
        sys.exit()
