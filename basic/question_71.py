
numbers = [5, 10, 5, 20, 10, 5, 30, 20, 40, 10]

"""Write Python code to:
1. Build a frequency dictionary.
2. Find the maximum frequency.
3. Store all numbers having that maximum frequency in a result list.
4. Print both the frequency dictionary and result list.
Important: Don't hardcode the maximum frequency. Calculate"""


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

print(max_frequency)


result = []

for key, value in count.items():
    if value == max_frequency:
        result.append(key)


print(result)
