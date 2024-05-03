# Q.39 Write a Python program to map two lists into a dictionary.

keys = ['red', 'green', 'blue']

values = ['#FF0000', '#008000', '#0000FF']

# Use the 'zip' function to pair each color name with its corresponding color code and create a list of tuples.
# Then, use the 'dict' constructor to convert this list of tuples into a dictionary 'color_dictionary'.

color_dictionary = dict(zip(keys, values))

print(color_dictionary)
