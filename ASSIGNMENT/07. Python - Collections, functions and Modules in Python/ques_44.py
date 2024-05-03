# Q.44 Write a Python program to find the highest 3 values in a dictionary.

sample_dict = {'a': 10, 'b': 30, 'c': 20, 'd': 50, 'e': 40}

highest_values = sorted(sample_dict.values(), reverse=True)[:3]

print("The highest 3 values in the dictionary are:", highest_values)
