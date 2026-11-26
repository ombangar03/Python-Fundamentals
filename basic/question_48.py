text = "programming"

# Write a Python program to count how many times each character appears.

count = {}

for char in text:
    if char not in count:
        count[char] = 1
    else:
        count[char] += 1

print(count)