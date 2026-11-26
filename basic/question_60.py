# First non-repeating character


# text = "programming"

# count = {}

# for char in text:
#     if char in count:
#         count[char] += 1
#     else:
#         count[char] = 1

# print(count)

# freq_char = []

# for key, value in count.items():
#     if value == 1:
#         freq_char.append(key)

# print(freq_char[:1])


text = "swiss"

count = {}

for char in text:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

print(count)


for char in text:
    if count[char] == 1:
        print(char)
        break
# print(count)


"""We iterate over the original string because:
1. We need to preserve the original character order.
2. We check each character's frequency using the dictionary.
3. As soon as we find a character with frequency 1, we use break to stop the loop."""