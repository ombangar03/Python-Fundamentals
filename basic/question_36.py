numbers = [5, 10, 5, 20, 10, 5, 30, 20, 10]
# Find all numbers that appear exactly twice.
count = {}

for num in numbers:
    if num not in count :
        count[num] = 1
    else:
        count[num] += 1
print(count)

number_appear_twice = []

for key, value in count.items():
    # if value == 2,  second condition is same as this 2:   
    if value > 1 and value < 3:
        # print(value)
        count = number_appear_twice.append(key)

print(number_appear_twice)
