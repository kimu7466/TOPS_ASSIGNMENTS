# Q.56  Write a Python program to read a random line from a file. 


import random

try:
    with open('file.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        if lines:
            random_line = random.choice(lines)
            print("Random line from the file:", random_line)
        else:
            print("The file is empty")
except FileNotFoundError:
    print("File not found")
