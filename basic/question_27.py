numbers = [12, 45, 7, 89, 23, 56]

# Task: Find the second largest number without using sort() or max().

large_number = numbers[0]
second_largest_number = numbers[0]

for num in numbers:
    if num > large_number:
        second_largest_number = large_number
        large_number = num
    
    elif num > second_largest_number:
        second_largest_number = num

print(second_largest_number)