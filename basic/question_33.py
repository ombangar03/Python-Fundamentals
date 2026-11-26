numbers = [10, 20, 30, 10, 40, 20, 10, 50]

#Task: Find the number that appears most frequently.

count = {}

for num in numbers:
    if num not in count:
        count[num] = 1
    else:
        count[num] += 1

print(count)

max_count = 0
most_frequent = None

for key, value in count.items():
    # print(key, value)
    if value > max_count:
        max_count = value
        most_frequent = key

print(most_frequent)

