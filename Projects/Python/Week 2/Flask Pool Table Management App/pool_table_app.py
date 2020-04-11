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

# write to table
def update_table_status(table_list, file_name):
    with open(file_name,"w") as file_object:
        json.dump(table_list, file_object, indent=2)

# update table history file when ending

def update_pool_table_history_json_file(table_object_as_dictionary, file_name):
    new_table_object_as_dictionary = table_object_as_dictionary

    table_list = []
    
    try:
        # If exists capture full list and append
        table_list = read_from_file(file_name)

        table_list.append(new_table_object_as_dictionary)

        # Dump new list
        update_table_status(table_list, file_name)

        print("Message: History table updated")
    
    except FileNotFoundError:
        table_list.append(new_table_object_as_dictionary)

        update_table_status(table_list, file_name)

        print("Message: New history file {} created and table added".format(file_name))

# define table view
def table_view():
    tables_file = "tables.json"
    table_list = read_from_file(tables_file)
    print (color.UNDERLINE + "Table Number","Status","\tStart Date and Time","\t\tTotal Playtime" + color.END)
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

def table_rent():
    table_status_file = "tables.json"
    table_history_file = "tables-history.json"

    # Rent table
    rent_table_number = input("Select table to rent out or 'x' to cancel: ")

    if rent_table_number == "x":
        return

    # Find specific table number in table list
    table_dictionary = {}
    tables_file = "tables.json"
    table_list = read_from_file(tables_file)
    for table in table_list:
        if table["table_number"] == rent_table_number:
            table_dictionary = table

    # If table number not found return to options menu
    if table_dictionary == {}:
        print('Message: Table number does not exists.')
        

    # If table number found rent out the table if available
    if table_dictionary["start_date_time"] == "":
        table_dictionary["start_date_time"] = datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S")
        print("Pool table {0} rented out".format(table_dictionary["table_number"]))
    else:
        print("Pool table {0} is currently occupied".format(table_dictionary["table_number"]))

    update_table_status(table_list, table_status_file)

def table_end_rent():

    while True:
        end_rent_table_number = input("Enter table number to end rental")

        
        table_dictionary = {}
        tables_file = "tables.json"
        table_list = read_from_file(tables_file)
        for table in table_list:
            if table["table_number"] == end_rent_table_number:
                table_dictionary = table

        # If table number not found return to options menu
        if table_dictionary == {}:
            print('Message: Table number does not exists.')
            break

        # If table number found document the end of the table rental, track the table rental info into separate file and reset the table rental state.
        if table_dictionary["start_date_time"] != "":       # ie Table is occupied

            end_date_time = datetime.datetime.now()

            # Calculate total minutes
            number_of_minutes_played = 0
            time_difference = ""
            time_in_date_time = ""

            table_status = "TABLE RENTAL ENDED"
            table_start_datetime = table_dictionary["start_date_time"]

            # Number of minutes played
            time_in_date_time = datetime.datetime.strptime(table_start_datetime,"%m/%d/%y %H:%M:%S")
            time_difference = datetime.datetime.now() - time_in_date_time
            number_of_minutes_played = math.floor(time_difference.total_seconds() / 60)

            # Temporarily prep table dictionary object with calculated values to save to history file
            table_dictionary["end_date_time"] = end_date_time.strftime("%m/%d/%y %H:%M:%S")
            table_dictionary["total_time_played"] = number_of_minutes_played

            # Save to daily history file.  Create one if it does not exist for the day.
            string_file_name = "./"
            date_today = datetime.datetime.now().date().strftime("%m-%d-%Y")
            string_file_name = string_file_name + date_today + ".json"
            table_history_file_string = string_file_name

            update_pool_table_history_json_file(table_dictionary,table_history_file_string)

            # Reset pool table states file for the specific table
            table_dictionary["start_date_time"] = ""
            table_dictionary["end_date_time"] = ""
            table_dictionary["total_time_played"] = ""

            # Update the pool table states file
            update_table_status(table_list, tables_file)

            # Info on update
            table_view()

            break

        else:
            print("Pool table {0} is not currently occupied".format(table_dictionary["table_number"]))

            

# define user options logic function
def user_options():

    while True:

        choice = input(color.UNDERLINE + "Pool Table Management App:\n" + color.END + "v - View current table status\nr - Start new table rental\ne - End current table rental\nq - Quit application\n" + color.BOLD + "Please enter your choice: " + color.END)

        if choice == "q":
            break

        elif choice =="v":
            table_view()

        elif choice =="r":
            table_view()
            table_rent()

        elif choice =="e":
            table_view()
            table_end_rent()
            
# Initiate application with options
while True:
    option = user_options()
