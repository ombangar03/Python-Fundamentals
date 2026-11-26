# find the least frequent elements

count = {
    "Python": 2,
    "Java": 4,
    "SQL": 1,
    "Django": 1,
    "FastAPI": 3
}

for key, value in count.items():
    if value == 1:
        print(key)


