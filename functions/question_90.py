"""Challenge 4: Find duplicate elements in a list
Write a function called find_duplicates(numbers)."""

def find_duplicates(numbers):
    seen = []
    duplicate = []
    for num in numbers:
        if num not in seen:
           seen.append(num)
        else:
            if num not in duplicate:
                duplicate.append(num)
        
    return duplicate

            

numbers = [1, 2, 2, 2, 3, 3]
print(find_duplicates(numbers))