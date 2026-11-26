numbers = [10, 20, 10, 30, 20, 40, 50, 30]

# Task: Find the frequency of each number.

count = {}

for num in numbers:
    if num not in count:
        count[num] = 1
    else:    
        count[num] += 1

print(count)
    
    