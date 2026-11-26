# Separate even and odd numbers using a function
# numbers = [10, 15, 20, 25, 30, 35, 40]

def separate_numbers(numbers):
    even_number = []
    odd_number = []

    for num in numbers:
        if num % 2 == 0:
            even_number.append(num)
        else:
            odd_number.append(num)
    
    return {
        "even_number": even_number, 
        "odd_number": odd_number
    }
    

numbers = [10, 15, 20, 25, 30, 35, 40]
print(separate_numbers(numbers))
