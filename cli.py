#from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%M")
print("It is ", now)

while True:
    # User input and stripping the extra spaces
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos)
    elif user_action.startswith("show"):

        todos = functions.get_todos()

        for i, items in enumerate(todos):
            items = items.strip("\n")
            print(f"{i+1}-{items.capitalize()}")
    elif user_action.startswith("edit"):

        try:
            index = int(user_action[5:])
            index = index - 1

            todos = functions.get_todos()

            new_todo = input("Enter the new task: ")
            todos[index] = new_todo

            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith("complete"):

        try:
            num = int(user_action[8:])

            todos = functions.get_todos()
            todos_to_remove = todos[num - 1].strip("\n")
            todos.pop(num-1)

            functions.write_todos(todos)

            message = f"The completed task {todos_to_remove} has been removed from the list"
            print(message)
        except IndexError:
            print("There is no item with that number")
    elif user_action.startswith("exit"):
        break
    else:
        print("The input is invalid")
print("Bye!")