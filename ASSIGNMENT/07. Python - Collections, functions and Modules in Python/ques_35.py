# Q.35 How Do You Traverse Through A Dictionary Object In Python?

my_dict = {
    "name": "John Doe",
    "age": 30,
    "occupation": "Software Engineer"
}

for key in my_dict.keys():
    print(key)

for value in my_dict.values():
    print(value)

for key, value in my_dict.items():
    print(key, value)    
