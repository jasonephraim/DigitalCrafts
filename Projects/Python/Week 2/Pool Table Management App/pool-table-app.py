import json
import datetime
import math

# define pool table class

class Table:
    def __init__(self, table_number):
        self.table_number = table_number
        self.table_status = "NOT OCCUPIED"
        self.table_use_start = ""
        self.table_use_end = ""
        self.table_use_total = 0

def read_from_file(file_name):
    with open(file_name,"r") as file_object:
        tables = json.load(file_object)
        return tables

def user_options():
    table_state_file_string = "./tables.json"
    
    while True:

        choice = input("Pool Table Management App:\n v-view tables\n r-rent\n e-end rental\n q-exit app\n Please enter your choice: ")

        if choice == "q":
            return choice

        elif choice =="v":
            table_list = read_from_file(table_state_file_string)
            print(table_list) # printing to check we are getting data
            

while True:
    print("** POOL TABLE MANAGEMENT APP STARTED **")
    option = user_options()

    if (choice == "q"):
        break
