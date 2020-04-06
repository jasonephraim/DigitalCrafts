example_task = {
    "description": "Buy milk at the store",
    "priority": 1
}

tasks = [example_task]

# priorities
# 0 = none
# 1 = low
# 2 = med
# 3 = high

def convert_wording_to_priority_int(word):
    if word.lower() == 'low':
        return 1
    elif word.lower() == 'med':
        return 2
    elif word.lower() == 'high':
        return 3
    else:
        print("Priority doesn't exist, set to none")
        return 0
