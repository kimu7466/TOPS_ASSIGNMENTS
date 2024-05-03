# Q.32 Write a Python script to sort (ascending and descending) a dictionary by value.

my_dict = {'apple': 5, 'banana': 2, 'orange': 8, 'grape': 3, 'kiwi': 1}

# Sorting the dictionary keys in ascending order (A to Z)
sorted_keys = sorted(my_dict.keys())
print("Ascending order of keys (A to Z):", sorted_keys)

# Sorting the dictionary keys in descending order (Z to A)
sorted_keys_desc = sorted(my_dict.keys(), reverse=True)
print("Descending order of keys (Z to A):", sorted_keys_desc)
