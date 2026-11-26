# numbers = [1, 2, 3, 2, 4, 5, 1, 6]
numbers = [1, 2, 2, 2, 3, 3, 4]

#Task: Find the duplicate numbers.

seen = []
duplicates = []

for num in numbers:
    if num in seen and num not in duplicates:
        duplicates.append(num)
    
    elif num not in seen:
        seen.append(num)

print(duplicates)
        



