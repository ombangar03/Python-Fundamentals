# ind the most frequent element


def most_frequent(numbers):
    most_frequent_count = {}

    for num in numbers:
        if num in most_frequent_count:
            most_frequent_count[num] += 1
        else:
            most_frequent_count[num] = 1

    max_count = 0
    max_freq_count = None

    for key, value in most_frequent_count.items():
        if value > max_count:
            max_count = value
            max_freq_count = key 

    
    return max_freq_count

numbers = [1, 2, 3, 2, 4, 2, 5, 3, 3, 3]
print(most_frequent(numbers))


# My assessment
# You've demonstrated that you can independently work with:
# 1. Dictionaries and frequency counting.
# 2. Conditional initialization and updating values.
# 3. Multiple loops for processing data.
# 4. Lists inside dictionaries and grouping.
# 5. Accumulators and comparisons.
# 6. Functions with meaningful return values.
# One area to keep practising is combining multiple loops and accessing the correct dictionary key inside each loop.