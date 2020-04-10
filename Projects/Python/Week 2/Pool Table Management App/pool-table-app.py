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
# colors for text prettiness
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

# define data tables return function based on source
def read_from_file(file_name):
    with open(file_name,"r") as file_object:
        tables = json.load(file_object)
        return tables

# define table view
def table_view():
    tables_file = "Python/Week 2/Pool Table Management App/tables.json"
    table_list = read_from_file(tables_file)
    print (color.BOLD + "Table Number","Status","\tStart Date and Time","\t\tTotal Playtime" + color.END)
    for table in table_list:
        # format JSON data in terminal
        table_status = ""
        table_start_datetime = ""
        # If there is no start time, set to not occupied
        if table["start_date_time"] == "":
            table_status = " - NOT OCCUPIED"
            print("Table {0} {1}".format(table["table_number"], " - ", table_status))
        # If there is a start time, set to occupied
        else:
            # set counter to 0 and use datetime function to cal
            minutes_played = 0
            time_difference = ""
            time_in_date_time = ""

            table_status = " - OCCUPIED"
            table_start_datetime = table["start_date_time"]

            # Number of minutes played
            time_in_date_time = datetime.datetime.strptime(table_start_datetime,"%m/%d/%y %H:%M:%S")
            time_difference = datetime.datetime.now() - time_in_date_time
            minutes_played = math.floor(time_difference.total_seconds() / 60)
            print (color.RED + "Table {0} {1}\t Start: {2}\t Minutes Played: {3}".format(table["table_number"], table_status, table_start_datetime, minutes_played) + color.END) #find way to make JSON display prettier data

# define user options logic
def user_options():
    
    while True:

        choice = input("Pool Table Management App:\n v-view tables\n r-rent\n e-end rental\n q-exit app\n Please enter your choice: ")

        if choice == "q":
            return choice

        elif choice =="v":
            table_view()
            

while True:
    print("** POOL TABLE MANAGEMENT APP STARTED **")
    option = user_options()

    if (choice == "q"):
        break
