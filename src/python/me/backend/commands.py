import time
import sys
import os
from colorama import Fore, Back, Style
from backend.main import ToDoBackend

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
    backend = ToDoBackend()
    backend.deserialise()
    def __init__(self):
        pass

    def __str__(self):
        return "invalid use of class!"

    def add_task(self):
        """Method to add a new task use this to modify backend"""
        todo = input("What todo would you like to add: ")
        self.backend.add_todo(todo)

    def del_task(self):
        """Method to remove a task"""
        todo_id = ""
        while True:
            todo_id = input("What todo ID do you want to remove (Type: help to print tasks): ")
            if todo_id.lower() == "help":
               self.print_task()
            else:
               break

        todo = self.backend.find_todo(int(todo_id))
        self.backend.remove_todo(todo)

    def check_task(self):
        """Method to check off a task"""
        self.del_task()
        pass

    def print_task(self):
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
