# 10. Write a Python program to count the frequency of words in a file. 


from collections import Counter

def word_count(file_name):
    open("file_name.txt")

    return Counter(file_name.read().split())

print("Number of words in the file: ", word_count("file_name.txt")) 