#import dependencies
import data
import view

print('Welcome to the TODO App')

is_running = True

while is_running:
    print('Press 1 to add a new TODO item')
    print('Press 2 to remove a TODO item')
    print('Press "q" to quit')
    menu_choice = input('Choose a menu item: ')
    if menu_choice == '1':
        view.toDoData(data.toDoData)
        toDoTitle = str(input('Enter a TODO: '))
        toDoPriority = str(input('Enter a priority ("high", "medium", "low"): '))
        data.toDoData.append({
            'title': toDoTitle,
            'priority': toDoPriority
        })
    elif menu_choice == '2':
        view.toDoData(data.toDoData)
        removeToDo = int(input('Which number would you like to delete?: '))
        data.toDoData.pop(removeToDo) #this seems to work in the terminal session but not seeing it effect the data.py file
    elif menu_choice == 'q':
        is_running = False
    else:
        print('Oops, please try again')

print('Exit Application')