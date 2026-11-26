# find the numbers that appear more than once. 
numbers = [10, 20, 10, 30, 20, 40, 50, 30, 60]

count = {}

for num in numbers:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

print(count)

number_appear_more_than_once = []

for key, value in count.items():
    if value > 1:
        number_appear_more_than_once.append(key)

print(number_appear_more_than_once)