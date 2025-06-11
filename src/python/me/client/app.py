#modules preinstalled up here
import os
import sys
import time
try:
    import logging
   # from backend.main import *
    from colorama import Fore, Back, Style
    #list modules here
except:
    #include their install command here e.g os.system('pip install <module>')
    dependencies = [
        #list your module in string 🥷 -_-
        "colorama>=0.4.6",
        "",
    ]
    #install custom py modules using pip
    os.system(f"pip install {dependencies}")
    import logging
   # from backend.main import *
    from colorama import Fore, Back, Style
logging.basicConfig(level=logging.INFO)
reset = Fore.RESET
red = Fore.RED
blue = Fore.BLUE
lred = Fore.LIGHTRED_EX
lblue = Fore.LIGHTBLUE_EX
green = Fore.GREEN

class ToDoList:
    #class static variables here most likely will have them
    # variables for colour printing
    def __init__(self
                 ):
        pass
    #construct app here

    @staticmethod
    def main() -> None:
        #public static void main ahh method -_-
        pass

#only exec if opened as script and not module (why would it be opened as a module idfk)
if __name__ == "__main__":
    ToDoList()
    ToDoList.main()

logging.debug(f"{green}Hello world!")
