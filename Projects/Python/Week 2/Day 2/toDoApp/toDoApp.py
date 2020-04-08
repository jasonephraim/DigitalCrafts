
all_tasks = [] 


class Task: 
  def __init__(self, name, priority): 
    self.name = name
    self.priority = priority
    self.completed = False 

  def markAsCompleted(self): 
    self.completed = True 

while True:

  print("Enter 1 to add new task")
  print("Enter 2 to delete the task")
  print("Enter 3 to view all tasks")
  
  choice = input("enter choice: ")

  if choice == "1":
    name = input("Enter task name: ")
    # ask the user for the priority of the task 
    priority = input("Enter priority: ")

    task = Task(name, priority)
    all_tasks.append(task)

    with open("Python/Week 2/Day 2/toDoApp/todos.txt","a") as file:
      for index in range(0, len(all_tasks)):
        t = all_tasks[index]
        data =  f"{index + 1} - {t.name} - {t.priority}"
        file.write(data)
        file.write("\n")
  
  elif choice == "2":
    with open("Python/Week 2/Day 2/toDoApp/todos.txt","a") as file:  
      tasklist = file.read()
    print(tasklist)
    completed = int(input("Enter the number for the completed task: ") + 1)
    all_tasks.pop(completed) #removed from array but not marked complete?


  elif choice == "3":
    with open("Python/Week 2/Day 2/toDoApp/todos.txt","r") as file:  
      tasklist = file.read()
    print(tasklist)

  elif choice == "q":
    file.close()
    break
