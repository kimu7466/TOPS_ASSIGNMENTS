# 6. Write a Python program to read a file line by line and store it into a list.

file = open('file_name.txt', 'r')
print(file.readlines())
file.close()