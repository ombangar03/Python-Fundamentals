# numbers = [10, 20, 10, 30, 20, 40, 50, 30, 60, 10]

numbers = [10, 20, 10, 20, 30, 40 , 30, 10, 30]

# Find the number that appears the maximum number of times.

count = {}

for num in numbers:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

print(count)

max_frequency = 0


for key, value in count.items():
    if value > max_frequency:
        max_frequency = value
        

result = []

for key, value in count.items():
    if value == max_frequency:
        result.append(key)
        
print(max_frequency)
print(result)