#modules preinstalled up here
import os

try:
    #list modules here
    pass
except:
    #include their install command here e.g os.system('pip install <module>')
    dependencies = [
        #list your module in string 🥷 -_-
        "module_here",
        "",
    ]
    os.system(f"pip install {dependencies}")

class ToDOList:
    #class static variables here most likely will have them
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
    ToDOList()
    ToDOList.main()

