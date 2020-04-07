# You are responsible for creating an app that manages groceries. Your groceries are characterized by Shopping Lists which can contain grocery items. Here are the features you need to implement: 

# * You need to ask the user for the input. 

# - A user should be able to create a shopping list. A shopping list consists of a title and address. Example = Fiesta, Walmart, Sams Club, Cosco, Randalls etc 

# - A user should be able to add multiple shoppings lists 

# - Give user an option to display the list 

# - A user should be able to add a grocery items to a particular shopping list. A grocery item consists of a title, price, quantity. Example Milk, Cookies, Paper, Napkins, Soda, Chips etc 

# Fiesta

# Milk, Soda, Fish 

# Walmart

# Paper, Napkins, Plate, Chips 

# Sams Club 

# Chicken, Beef, Eggs, Sugar, Salt, Pepper, Honey 



class Groceries:

    def __init__(self,store,item):
        self.store = store
        self.item = item

    def start(self):
        print("Starting Groceries")


Kroger = Groceries('Kroger','apples')
Kroger.item = 'bananas'


Fiesta = Groceries('Fiesta','beer')
Fiesta.store = "Fiesta"
Fiesta.item = "tortillas"

print(Kroger.item)