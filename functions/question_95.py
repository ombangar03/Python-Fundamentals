# Word Frequency Counter
# Write a function called word_frequency(sentence) that:
# 1. Accepts a sentence as input.
# 2. Counts how many times each word appears.
# 3. Stores the result in a dictionary.
# 4. Returns the dictionary.


def word_frequency(sentence):
    words = sentence.split()
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    
    # return frequency

# Find the most frequent word
# Now reuse your previous logic.

    max_count = 0
    high_frequency = None

    for key, value in frequency.items():
        if value > max_count:
            max_count = value
            high_frequency = key
    
    return high_frequency, max_count

# sentence = "python is easy and python is powerful"
sentence = "python is easy and python is powerful and python is popular"
print(word_frequency(sentence))