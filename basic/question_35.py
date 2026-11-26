numbers = [10, 20, 10, 30, 20, 10, 40, 30]

#Task: Find the second most frequent number.
count = {}

for num in numbers:
    if num not in count:
        count[num] = 1
    else:
        count[num] += 1
print(count)

max_count = 0
second_max_count = 0
second_most_freq = []

for key, value in count.items():
    if value > max_count:
        max_count = value
        print("max_count", max_count)
        
    if value < max_count and value > second_max_count:
        second_max_count = value

    if value == second_max_count:
        second_most_freq.append(key)
        

print("second_max_count:",second_max_count)
print("second_most_freq:",second_most_freq)
        