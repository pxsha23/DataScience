# 1
# Write a Python program to count the frequency of each word in
# a given string using a dictionary.

def count_word_frequency(text):
    text = text.lower()
    words = text.split()
    word_freq = {}
    
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    
    return word_freq


text = "RED ROSES FOR RUBY RED RUBIES FOR ROSIE"
word_frequencies = count_word_frequency(text)

# Display the word frequencies
for word, frequency in word_frequencies.items():
    print(f"'{word}': {frequency}")
