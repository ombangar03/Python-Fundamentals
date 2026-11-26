numbers = [4, 5, 4, 6, 5, 4, 7, 6]

seen = []
duplicates = []

for num in numbers:
    if num in seen and num not in duplicates:
        duplicates.append(num)
    elif num not in seen:
        seen.append(num)

print(duplicates)