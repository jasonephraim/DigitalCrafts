import json
data = {}
data['people'] = []
running = True

while running == True:

    print("Enter 1 to add person")
    print("Enter q to quit")
  
    choice = input("enter choice: ")

    if choice == "1":
        userName = input("Please enter your full name: ")
        userAge = input("Please enter your age: ")

        data['people'].append({
        'name': userName,
        'age': userAge
        })

        with open("Python/Week 2/Day 3/Writing JSON Files/nameAge.txt","w") as outfile:
            json.dump(data, outfile)

    elif choice == "q":
        outfile.close()
        running = False
        break
