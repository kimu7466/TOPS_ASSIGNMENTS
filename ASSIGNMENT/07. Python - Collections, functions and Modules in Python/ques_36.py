# Q.36 How Do You Check The Presence Of A Key In A Dictionary?
""" The get() method allows you to retrieve the value for a specified key. It returns None if the key is not found (or you can specify a default value).
"""
'''Example:'''

my_dict = {'apple': 5, 'banana': 10, 'orange': 7}
given_key = 'banana'

if my_dict.get(given_key) is not None:
    print(f"The key '{given_key}' exists in the dictionary.")
else:
    print(f"The key '{given_key}' does not exist in the dictionary.")
    
