# 6. Write a Python program to read a file line by line and store it into a list.

file = open('output1.txt', 'r')
print(file.readlines())
file.close()