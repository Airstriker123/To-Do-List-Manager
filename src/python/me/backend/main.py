import csv

# Back end for ToDo app
# SHOULD NOT UNDER ANY CIRCUMSTANCES BE CREATED BY MIDDLE OR FRONT END
class ToDoBackend:
    def __init__(self):
        """
        Initalises all data for the back end
        DO NOT CALL
        """

        self.db_name = "tododata.csv"
        self.python_data = None

    def deserialise(self):
        """
        Deserialises CSV data into python data
        AGAIN DO NOT CALL
        """
        with open(self.db_name, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                print(', '.join(row))

class ToDoAPI:
    def __init__(self):
        self.backend = ToDoBackend()
        self.backend.deserialise()
