count = {"Python": 5, "Java": 3, "SQL": 7, "C++": 2}

max_count = 0
most_frequent = None

for key, value in count.items():
    if value > max_count:
        max_count = value
        most_frequent = key

print(most_frequent)

