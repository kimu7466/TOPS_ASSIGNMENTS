# 22. How to Define a Class in Python? What Is Self? Give An Example Of A Python Class.

'''
Syntax of class : 

class class_name:
    Data memebers

    Member functions

Syntax of object:
instance_name = class_name([paras])

--> What Is Self?
    Self represents the instance of the class. By using the “self” we can access the attributes and methods of the class in Python.
    It binds the attributes with the given arguments
    
--> Example Of A Python Class: 
'''

class demo:
    name = input("Enter a name: ")
    age = int(input("Enter an age: "))


    def student(self):
        print("I am a student")

s = demo()
print(s.name)
print(s.age)
s.student()    
       
