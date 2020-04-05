import data

def divider():
    print('- - - - - - - - - - - - - - - - - - - - - - - - -')

def priority_with_wording(priority):
    if priority == 1:
        return "low"
    elif priority == 2:
        return "med"
    elif priority == 3:
        return "high"
    else:
        return "none"

def show_menu():
    divider()
    print("Press '1' to add task")
    print("Press '2' to delete task")
    print("Press '3' to view all tasks")
    print("Press '4' to change priority of an existing task")
    print("Press '5' to sort the tasks by priority")
    print("Press 'q' to quit")

def show_tasks():
    if data.tasks:
        print('All Tasks:')
        for index, task in enumerate(data.tasks):
            print(
                f'{index} - {task["description"]} - {priority_with_wording(task["priority"])}'
            )
    else:
        print('No tasks found')


def select_task(action):
    show_tasks()
    return int(input(f"Choose the task by number to '{action}': "))