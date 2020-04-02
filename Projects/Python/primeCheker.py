num = int(input("Please enter a whole number: "))

if num > 1:
   for n in range(2,num):
       if (num % n) == 0:
           print(num,"is not a prime number")
           break
   else:
       print(num,"is a prime number")
else:
    print(num,"is not a prime number")