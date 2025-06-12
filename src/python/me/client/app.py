#modules preinstalled up here
import os
import logging
import time

try:
   # from backend.main import *
    from colorama import Fore, Back, Style
    from ui.ui import UserInterface
    import fade
    #list modules here
except:
    #include their install command here e.g os.system('pip install <module>')
    dependencies = [
        #list your module in string 🥷 -_-
        "colorama>=0.4.6",
        "fade",
    ]
    #install custom py modules using pip
    for module in dependencies:
        print(f"Installing module: {module}")
        os.system(f"pip install {module}")
        import fade
    from colorama import Fore, Back, Style
logging.basicConfig(level=logging.INFO)
reset = Fore.RESET
red = Fore.RED
blue = Fore.BLUE
lred = Fore.LIGHTRED_EX
lblue = Fore.LIGHTBLUE_EX
green = Fore.GREEN
yellow = Fore.YELLOW
orange = '\033[38;5;208m'

class ToDoList:
    #class static variables here most likely will have them
    # variables for colour printing
    def __init__(self
                 ):
        pass
    #construct app here

    def __str__(self):
        return ""

    @staticmethod
    def main() -> None:
     while True:
         try:
             # app code to be called from classes/functions
             banner = UserInterface().banner
             gradient_banner = fade.fire(banner)
             print(f"{green}{gradient_banner}\n{yellow}{UserInterface().task_menu}{reset}")
             choice = input\
(f"""
{orange}[Enter your choice]:->{reset}\
""")
             if choice == "1":
                 pass
             elif choice == "2":
                 pass
             elif choice == "3":
                 pass
             elif choice == "4":
                 pass
             else:
                 print(f'{red}"{choice}" is not in options!{reset}')
                 print(f"{red}[!] Invalid choice!{reset}")
                 time.sleep(1)

         except Exception as e:
             # catch any error
             print(f"{red}Something went wrong.{reset}")
             print(f"{red}in: app.py (main method)")
             print(f"{blue}{e}{reset}")

#only exec if opened as script and not module (why would it be opened as a module idfk)
if __name__ == "__main__":
    ToDoList()
    ToDoList.main()
input()
