# Second-largest unique number
# Write a function called second_largest(numbers).


def second_largest(numbers):
    
    largest_number = float('-inf')
    second_largest_number = float('-inf')

    for num in numbers:
        if num > largest_number:
            second_largest_number = largest_number
            largest_number = num

        elif num < largest_number and num > second_largest_number:
            second_largest = num

    return second_largest_number

numbers = [10, 25, 45, 25, 60, 45, 30]
print(second_largest(numbers))