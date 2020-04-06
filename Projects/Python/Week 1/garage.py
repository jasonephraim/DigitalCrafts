# Create a garage with multiple cars inside (array of cars)
cars = ["Toyota", "Ford", "Honda", "Subaru"]
# print how many cars are in the garage "there are # cars"
print(len(cars))
# Add a car to the garage
cars.append("Volvo")
print(cars)
# Remove the last car in the garage
cars.pop(4)
print(cars)
# Remove a specific car from the garage (ex: "Ford")
cars.remove("Honda")
print(cars)
# Print all of the cars
print(cars[0::1]) #Using step to account for variable list length