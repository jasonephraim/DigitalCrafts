num = int(input("Please enter a whole number: "))
fact = 1
for n in range(1,num + 1):
    fact = fact*n
print("The factorial of",num,"is",fact)