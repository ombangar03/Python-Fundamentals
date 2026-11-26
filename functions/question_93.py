# Find duplicate elements in a list
# Write a function called find_duplicates(numbers).


def find_duplicates(numbers):
    seen = []
    duplicates= []

    for num in numbers:
        if num not in seen:
            seen.append(num)
        else:
            if num not in duplicates:
                duplicates.append(num)
    
    return duplicates

# numbers =  [1, 2, 3, 2, 4, 5, 1, 6, 3]
numbers = [1, 2, 2, 2, 3, 3]
print(find_duplicates(numbers))