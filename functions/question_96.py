# Find all words with the highest frequency

def high_frequency(sentence):
    words = sentence.split()
    count = {}

    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1

    # return count
    max_count = 0
    # find highest count of words in dictionary
    for key, value in count.items():
        if value > max_count:
            max_count = value  

    high_frequency_word = []
    for key, value in count.items():
        if value == max_count:
            high_frequency_word.append(key)
        
    return high_frequency_word
 

sentence = "python is easy and python is powerful and java is popular"
print(high_frequency(sentence))