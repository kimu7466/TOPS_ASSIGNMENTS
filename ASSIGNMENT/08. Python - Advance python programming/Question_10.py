# 10. Write a Python program to count the frequency of words in a file. 


def word_count(file_name):
    word_freq = {}  

    with open(file_name, 'r') as file:
        words = file.read().split()  

        for word in words:
            if word in word_freq:
                word_freq[word] += 1  
            else:
                word_freq[word] = 1  

    return word_freq

file_name = "file_name.txt"
word_frequencies = word_count(file_name)

for word, frequency in word_frequencies.items():
    print(f"Word: {word}, Frequency: {frequency}")


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# from collections import Counter

# def word_count(file_name):
#     open("file_name.txt")

#     return Counter(file_name.read().split())

# print("Number of words in the file: ", word_count("file_name.txt")) 

