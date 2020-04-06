def toDoData(toDoData):
    for index, toDo in enumerate(toDoData):
        print(
            f'{toDo["title"]} {toDo["priority"]}'
        )