
tasks = [] 


class Task: 
  def __init__(self, name, priority): 
    self.name = name
    self.priority = priority
    self.completed = False 

  def markAsCompleted(self): 
    self.completed = True 

while True: 
  # ask the user for name of the task 
  name = input("Enter task name: ")
  # ask the user for the priority of the task 
  priority = input("Enter priority: ")

  task = Task(name, priority)

  tasks.append(task)

  print(tasks)

  choice = input("Enter q to quit or any key to continue!")
  if choice == "q": 
    break 
