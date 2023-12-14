# Q.46 Write a Python program to create a dictionary from a string.

input_string = "hello"
dict = {}

for char in input_string:
    if char in dict:
        dict[char] += 1
    else:
        dict[char] = 1

print(dict)
