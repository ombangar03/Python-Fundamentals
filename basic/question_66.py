# First repeating word

words = ["python", "java", "sql", "python", "django", "java"]

seen = set()

for word in words:
    if word in seen:
        print(word)
        break
    else:
        seen.add(word)



# Find ALL repeating words

words = ["python", "java", "sql", "python", "django", "java", "python"]


seen = set()
duplicates = []

for word in words:
    if word in seen:
        if word not in duplicates:
            duplicates.append(word)
            
            
    else:
        seen.add(word)
        # print(word)

print(duplicates)
        