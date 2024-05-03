# Q.34  Write a Python script to check if a given key already exists in a dictionary. 

my_dict = {'apple': 5, 'banana': 10, 'orange': 7}
given_key = 'banana'

if given_key in my_dict:
    print(f"The key '{given_key}' exists in the dictionary.")
else:
    print(f"The key '{given_key}' does not exist in the dictionary.")
