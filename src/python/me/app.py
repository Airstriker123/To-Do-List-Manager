#modules preinstalled up here
import os

try:
   # from backend.main import *
    from colorama import Fore, Back, Style
    from client.ui.ui import UserInterface
    from backend.commands import *
    import fade
    #list modules here
except:
    #include their install command here e.g os.system('pip install <module>')
    dependencies = [
        #list your module in string 🥷 -_-
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
             elif choice == "2":
                 Commands().del_task()
             elif choice == "3":
                 Commands().check_task()
             elif choice == "4":
                 Commands().print_task()
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
             print(f"{red}in: app.py (main method)")
             print(f"{blue}{e}{reset}")

#only exec if opened as script and not module (why would it be opened as a module idfk)
if __name__ == "__main__":
    ToDoList()
    ToDoList.main()

