import functions

import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter To-do", key="todo")
add_button = sg.Button("Add")

window = sg.Window('My To-Do App', layout=[[label], [input_box, add_button]],
                   font=('Georgia', 10))

while True:
    event, value = window.read()
    print(event)
    print(value)

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = value["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WINDOW_CLOSED:
            break

window.close()