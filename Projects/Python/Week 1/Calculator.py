firstNumber = float(input("Enter first number > "))
operator = input("Please enter an operator > ")
secondNumber = float(input("Enter second number > "))
if operator == "+":
    print(firstNumber + secondNumber)
elif operator == "-":
    print(firstNumber - secondNumber)
elif operator == "*":
    print(firstNumber * secondNumber)
elif operator =="/":
    print(firstNumber / secondNumber)
else:
    print("Invalid operator. Please use '+,-,* or /'")
