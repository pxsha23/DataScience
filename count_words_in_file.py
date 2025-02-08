# 2
# Write a Python program to read a text file and count the 
# number of words in it.

def count_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            words = text.split()
            num_words = len(words)
            return num_words
    except FileNotFoundError:
        return "File not found."

# Example usage
filename = r'C:\Users\Piyusha\OneDrive\Desktop\Spiderman.txt'
word_count = count_words_in_file(filename)
print(f"Number of words in '{filename}': {word_count}")
