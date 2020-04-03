# FizzBuzz Exercise: Print out 1-100 and replace numbers divisible by 3 with “Fizz”, numbers divisible by 5 with “Buzz”, and numbers divisible by 3 and 5 print “FizzBuzz”.
def fizzBuzzApp():
    #Set range with "i" as start count and "max" as max
    #i = 1
    #max = 100
    #prompt user for count
    i = int(input("Please enter the starting number: "))
    max = int(input("Please enter the ending number: "))
    #loop through all numbers i to 100
    while i <= max:
        #print Fizz if divisible by 3 and 5
        if i % 3 == 0 and i % 5 == 0:
            print(i, "FizzBuzz")
        #print Fizz if divisible by 3
        elif i % 3 == 0:
            print(i, "Fizz")
        #print Fizz if divisible by 5
        elif i % 5 == 0:
            print(i, "Buzz")
        #print number if not divisible by 3, 5 or both
        else:
            print(i)
        #print for each number
        print()
        #iterate to next number
        i += 1
fizzBuzzApp()