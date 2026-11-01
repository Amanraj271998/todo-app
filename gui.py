import functions

import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter To-do", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 20])
edit_button = sg.Button("Edit")
complete_button = sg.Button('Complete')
exit_button = sg.Button('exit')

window = sg.Window('My To-Do App', layout=[[label],
                                           [input_box, add_button],
                                           [list_box, edit_button, complete_button]
                                           [exit_button]],
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
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = value["todos"][0]
            new_todo = value["todo"]

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "todos":
            window['todo'].update(value=value['todos'][0])
        case "Complete":
            todo_to_complete = value['todos'][0]
            todos = functions.get_todos()

            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case 'exit':
            break
        case sg.WINDOW_CLOSED:
            break

window.close()