# 9. Write a Python program to count the number of lines in a text file.

file = open('file_name.txt', 'r')

lines = len(file.readlines())

print("Total number of lines: ", lines)