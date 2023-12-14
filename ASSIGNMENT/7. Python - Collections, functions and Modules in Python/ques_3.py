# Q.3 Differentiate between append () and extend () methods?

'''
---Append method

It adds an element at the end of the list. The argument passed in the append function is added as a single element at end of the list and 
the length of the list is increased by 1.
The element can be a string, integer, tuple, or another list.

Syntax:
list_name.append(element)

''' 

# Example:

list_1 = [1, 2, 3]

list_1.append(4)

print(list_1)

''' 
---Extend method
This method appends each element of the iterable (tuple, string, or list) to the end of the list and increases the length of the list by 
the number of elements of the iterable passed as an argument.

Syntax:
list_name.extend(iterable)

''' 
# Example:


# print("\n >>>>>>>>>> \n\n")

# list_2 = [1, 2, 3]

# list_2.extend([4, 5, 6])

# print(list_2)

# print("\n >>>>>>>>>> \n\n")

