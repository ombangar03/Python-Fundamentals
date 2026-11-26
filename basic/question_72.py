numbers = [5, 10, 5, 20, 10, 5, 30, 20, 40, 10]

frequency = {5: 3, 10: 3, 20: 2, 30: 1, 40: 1}

"""
You can also remember these three dictionary methods:
Method	Returns
count.keys()	All keys
count.values()	All values
count.items()	Key-value pairs
"""


count = {"Python": 3, "Java": 2, "SQL": 4}

for key in count:
    print(key, count[key])