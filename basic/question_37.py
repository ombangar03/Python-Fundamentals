numbers = [10, 20, 10, 30, 20, 40, 10, 30, 50, 20]

# Your task: Find all numbers that appear more than once and their frequencies.

count = {}

for num in numbers:
    if num not in count:
        count[num] = 1
    else:
        count[num] += 1

print(count)

num_more_than_once = {}

for key, value in count.items():
    if value > 1:
        # print(key, value)
       num_more_than_once[key] = value

print(num_more_than_once)