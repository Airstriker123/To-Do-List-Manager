# Back end for ToDo app
# SHOULD NOT UNDER ANY CIRCUMSTANCES BE CREATED BY MIDDLE OR FRONT END
class ToDoBackend:
    def __init__(self):
        """
        Initalises all data for the back end
        DO NOT CALL
        """

        self.db_name = "tododata.txt"
        self.todos = []

    def deserialise(self):
        """
        Deserialises text data into python data
        """

        # Opens a file in read mode, splits the fil by newlines and appends them as todo's
        with open(self.db_name, 'r+') as db:
            self.todos = [line.strip() for line in db.readlines()]

    def serialise(self):
        """
        Serialise you todo data to the db file
        """

        # Opens file in write mode and serialises all todos
        with open(self.db_name, 'w') as db:
            for todo in self.todos:
                db.write(f"{todo}\n")

    def add_todo(self, todo):
        """
        Adds a todo (String) to the array
        """

        # Appends todo to the list
        todo.append(todo)

    def remove_todo(self, todo):
        """
        Removes todo from list, if no todo found then nothing happens
        """

        self.todos.remove(todo)

    def find_todo(self, todo_id):
        """
        Returns todo string based on index
        """

        return self.todos[todo_id]
