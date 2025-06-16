#modules preinstalled up here
import os
import sys

try:
    from colorama import Fore, Back, Style
    from client.ui.ui import UserInterface
    from backend.commands import *
    import fade
    #list modules here
except:
    #include their install command here e.g os.system('pip install <module>')
    dependencies = [
        #list your module in string  -_-
        "colorama>=0.4.6",
        "fade",
    ]
    #install custom py modules using pip if not installed
    for module in dependencies:
        print(f"Installing module: {module}")
        os.system(f"pip install {module}")
    import fade
    from backend.commands import *



class ToDoList:
    #class static variables (here most likely will have them)
    def __init__(self
                 ):
        #construct app here             
        pass
    

    def __str__(self):
        return ""
    @staticmethod
    def Clear():
        """Function to clear terminal for both linux and windows every loop in main method"""
        try:
            if sys.platform.startswith("win"):
                os_name = "Windows"
            elif sys.platform.startswith("linux"):
                os_name = "penguin_operating_system"
            else:
                os_name = "Unknown"

            if os_name == "Windows":
                os.system("cls")
            if os_name == "penguin_operating_system":
                os.system("clear")
        except Exception as e:
            print("Failed to get os....")

    @staticmethod
    def main() -> None:
        #Main method to be called with all core logic in here
     while True:
         try:
             # app code to be called from classes/functions
             ToDoList().Clear()
             banner = UserInterface().banner
             gradient_banner = fade.fire(banner)
             #print banner and menu
             print(f"{green}{gradient_banner}\n{yellow}{UserInterface().task_menu}{reset}")
             #print choice
             choice = input\
(f"""
{orange}[Enter your choice]:->{reset}\
""")
             #manage input from choice and call function based on selection.
             if choice == "1":
                 Commands().add_task()
                 input(f"{yellow}[!]press enter to continue[!]:>{reset}")
             elif choice == "2":
                 Commands().del_task()
                 input(f"{yellow}[!]press enter to continue[!]:>{reset}")
             elif choice == "3":
                 Commands().check_task()
                 input(f"{yellow}[!]press enter to continue[!]:>{reset}")
             elif choice == "4":
                 Commands().print_task()
                 input(f"{yellow}[!]press enter to continue[!]:>{reset}")
             elif choice == "5":
                 #exit app
                 Commands().exit()
             else:
                 print(f'{red}"{choice}" is not in options!{reset}')
                 print(f"{red}[!] Invalid choice!{reset}")
                 time.sleep(1)

         except Exception as e:
             # catch any error
             print(f"{red}Something went wrong.{reset}")
             print(f"{blue}{e}{reset}")
             input(f"{blue}Press enter to continue...{reset}")
             ToDoList().Clear()

#only exec if opened as script and not module (why would it be opened as a module idk)
if __name__ == "__main__":
    ToDoList()
    ToDoList.main()

