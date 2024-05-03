# 25. Explain Inheritance in Python with an example? What is init? Or What Is A Constructor In Python?
'''
inheritance allows you to reuse code and create more complex and organized programs.

there are 4 types of inheritance in python.

(1) Single inheritance --> A childe class can inherit from only one parent class.
'''
class animal:
    def speak(self):
        print("Animal speaking")
        
class dog(animal):
    def bark(self):
        print("Dog is barking")
               
d = dog()
d.bark()
d.speak() 
'''
(2) Multiple inheritance --> A Child class can inherit from multiple parent classes.
'''
class animal:
    def speak(self):
        print("Animal speaking")
        
class dog:
    def bark(self):
        print("Dog is barking")
        
class eat(dog,animal) :
    def eat(self):
        print("Eating")              
d = eat()

d.bark()
d.speak()
d.eat()
'''
(3) Multi_level inheritance --> A child class can inherit from parent class that inherits from another parent class.
'''
class animal:

    def speak(self):
        print("Animal speaking")
        
class dog(animal):
    def bark(self):
        print("Dog is barking")
        
class eat(dog) :
    def eat(self):
        print("Eating")  
                    
d = eat()
d.bark()
d.speak()
d.eat()
'''
(4) Hierarchical inheritance --> Multiple child classes inherit from a single parent class.
'''
class animal:

    def speak(self):
        print("Animal speaking")
        
class dog(animal):
    def bark(self):
        print("Dog is barking")
        
class eat(animal):
    def eat(self):
        print("Eating")   
                   
d = eat()
d.bark()
d.speak()
d.eat()
'''
--> What is init?
   The __init__ method also known as Constructor.
   This method called when an object is created from the class and it allow the class to initialize the attribbutes of a class.
   The python __init__ method is declared within a class and is used to initialize the attributes of an object as soon as the object is formed.

--> What is Python Constructor
In Python, a constructor is a special method that is called when an object is created. The purpose of a python constructor is to assign values to 
the data members within the class when an object is initialized. The name of the constructor method is always __init__.
'''
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
person=person("Vishal", 21)
print(person.name)
print(person.age) 
   