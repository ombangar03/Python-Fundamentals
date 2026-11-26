# Find unique elements

# numbers = [10, 20, 30, 10, 40, 20, 50]
numbers = [10, 20, 10, 30, 20, 40, 50, 30]



count = {}

for num in numbers:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

print(count)

unique_numbers = []

for key, value in count.items():
    if value == 1:
        unique_numbers.append(key) 

print(unique_numbers)






