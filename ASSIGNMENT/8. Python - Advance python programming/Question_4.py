# 4. Write a Python program to read first n lines of a file

# To read first n lines of a file

file = open('file_name.txt', 'r')
print(file.readlines(1))
file.close()
 
