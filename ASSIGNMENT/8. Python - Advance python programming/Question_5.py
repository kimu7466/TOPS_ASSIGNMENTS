# 5. Write a Python program to read last n lines of a file.

# To read last n lines of a file

file = open('file_name.txt', 'r')
print(file.readlines([-1]))
file.close()