# One common problem when prompting for numerical inut occurs when people provide text instead of numbers.
# When you try to convert the inout to an int, you'll get a ValueError. 
# Write a program that prompts for two numbers. Add them together and print the result. 
# Catch the ValueError if either input is not a number, and print a friendly error message. 
# Test your program by entering two numbers and then by enterting some text instead of a number.

try: 
    print("Enter two numbers to see their sum: ")
    value1 = int(input("Please enter a number: "))
    value2 = int(input("Please enter another number: "))
    total = value1 + value2
except ValueError:
    print("Please use only numbers")

print(total)