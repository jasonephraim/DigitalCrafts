import data
import view

is_running = True

while is_running:
    view.show_menu()
    user_input = input('Choose an option: ')
    view.divider()

    if user_input == '1':
        print('Add Task')
        new_task_description = input("What is the description? ")
        new_task_priority = input("What is the priority (low, med, high)? ")
        data.tasks.append({
            "description": new_task_description,
            "priority": data.convert_wording_to_priority_int(new_task_priority)
        })
        print("Task was added successfully")
    elif user_input == '2':
        index_of_task_to_delete = view.select_task('remove')
        data.tasks.pop(index_of_task_to_delete)
        print('Task removed successfully')
    elif user_input == '3':
        view.show_tasks()
    elif user_input == '4':
        index_of_task_to_update_priority = view.select_task('update priority')
        new_priority = input("What is the new priority (low,med,high)? ")
        data.tasks[index_of_task_to_update_priority][
            "priority"] = data.convert_wording_to_priority_int(new_priority)
        print("The task's priority successfully")
    elif user_input == 'q':
        is_running = False
