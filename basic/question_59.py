# Find duplicate characters in a string

text = "programming"

count = {}

for char in text:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

print(count)

duplicate = []

for key, value in count.items():
    if value > 1:
        # print(value)
        duplicate.append(key)

print(duplicate)

