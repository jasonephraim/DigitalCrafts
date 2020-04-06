# Tip Calculator

bill = input("What is the total bill amount? > $")
bill = float(bill)
tipPercentage = input("What is the tip percentage amount? > ")
tipPercentage = float(tipPercentage)

finalTotal = (bill * tipPercentage) + bill

print(finalTotal)