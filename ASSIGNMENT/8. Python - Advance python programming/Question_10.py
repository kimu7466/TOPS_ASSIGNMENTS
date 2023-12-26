# 10. Write a Python program to count the frequency of words in a file. 


def word_count(file_name):
    word_freq = {}  # Create an empty dictionary to store word frequencies

    with open(file_name, 'r') as file:
        words = file.read().split()  # Read the file and split it into words

        for word in words:
            if word in word_freq:
                word_freq[word] += 1  # Increment the count if the word is already in the dictionary
            else:
                word_freq[word] = 1  # Initialize the count if it's a new word

    return word_freq

file_name = "file_name.txt"
word_frequencies = word_count(file_name)

# Display word frequencies
for word, frequency in word_frequencies.items():
    print(f"Word: {word}, Frequency: {frequency}")


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# from collections import Counter

# def word_count(file_name):
#     open("file_name.txt")

#     return Counter(file_name.read().split())

# print("Number of words in the file: ", word_count("file_name.txt")) 

