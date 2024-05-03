# Q.43 Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.

# sample data: {'1': ['a','b'], '2': ['c','d']}
# Expected Output:
# ac ad bc bd

from itertools import product

data = {'1': ['a', 'b'], '2': ['c', 'd']}

combinations = list(product(*(data[key] for key in data)))
for combination in combinations:
       print(''.join(combination))

