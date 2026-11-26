# Find the frequency of each word in a sentence using a function.
"""Write a function called word_frequency(sentence) that:
1. Accepts a sentence as input.
2. Counts how many times each word appears.
3. Stores the result in a dictionary.
4. Returns the dictionary."""

def word_frequency(sentence):
    
    words = sentence.split()
    count = {}
    
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1

    # return count
    max_count = 0
    most_frequent = None

    for key, value in count.items():
        # print(key, value)
        if value > max_count:
            max_count = value
            most_frequent = key
            # print(max_count)
            # print(most_frequent)
        
    return most_frequent, max_count

# sentence = "python is easy and python is powerful"

sentence = "python is easy and python is powerful and python is popular"
print(word_frequency(sentence))