"""Next challenge: Second-largest unique number
Write a function called second_largest(numbers)"""

def second_largest(numbers):
    # frequency_count = {}
    
    # for num in numbers:
    #     if num in frequency_count:
    #         frequency_count[num] += 1
    #     else:
    #         frequency_count[num] = 1

    large_number =  float('-inf')
    second_largest_number = float('-inf')
    
    for num in numbers:
        if num >= large_number:
            second_largest_number = large_number
            large_number = num
        elif num < large_number and num > second_largest_number:
            second_largest_number = num
    
    return second_largest_number
        

numbers = [10, 25, 45, 25, 60, 45, 30]
print(second_largest(numbers))