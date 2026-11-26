numbers = [10, 25, 30, 45, 50, 65, 70, 85]

# Task: Calculate the sum of numbers greater than 40.

total = 0

for num in numbers:
    if num > 40:
        total += num
        
print(total)