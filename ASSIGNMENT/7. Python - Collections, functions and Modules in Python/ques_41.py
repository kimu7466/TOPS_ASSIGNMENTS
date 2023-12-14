# Q.41 Write a Python program to print all unique values in a dictionary. 

dict = {
    'imroz': '25',
    'brijesh': '32',
    'imroz': '25',
    'brijesh': '32',
    'mehboob': '55',
    'mehboob': '55',
}

print("Original Dictionary: ", dict)

unique_values = set(dict.values())

print("Unique Values: ", unique_values)
