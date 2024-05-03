# Q.11 Write a Python function that takes a list and returns a new list with unique elements of the first list. 

list1 = [10, 20, 10, 30, 40, 40]

unique_list_1 = list(dict.fromkeys(list1))

print(unique_list_1)
